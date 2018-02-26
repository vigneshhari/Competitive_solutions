package brainfuckcompiler.compiler.expressions.nodes;

import brainfuckcompiler.compiler.expressions.nodetypes.BinaryOperator;
import brainfuckcompiler.compiler.expressions.nodetypes.ConstantNode;
import brainfuckcompiler.compiler.expressions.nodetypes.VariableNode;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.statics;

/**
 *
 * @author vrighter
 */
public class EqualityOperator extends BinaryOperator
{

	/**
	 *
	 */
	public EqualityOperator(int lineNumber, Block parentBlock)
	{
		super(lineNumber, parentBlock);
		returnsBoolean = true;
	}

	/**
	 *
	 * @param t
	 * @return
	 */
	public int generateBF()
	{
		int x = 0, y = 0;
		boolean rightIsConstant = false;
		boolean leftIsConstant = false;
		if ((left instanceof ConstantNode) && (right instanceof ConstantNode))
		{
			rightIsConstant = true;
		} else if (right instanceof ConstantNode)
		{
			rightIsConstant = true;
		} else if (left instanceof ConstantNode)
		{
			leftIsConstant = true;
		}

		if (!leftIsConstant && !rightIsConstant)
		{
			boolean yIsVariable = false;
			if (right instanceof VariableNode)
			{
				x = left.generateBF();
				y = ((VariableNode) right).getVariable().getMemoryPosition();
				yIsVariable = true;
			} else if (left instanceof VariableNode)
			{
				x = right.generateBF();
				y = ((VariableNode) left).getVariable().getMemoryPosition();
				yIsVariable = true;
			}
			int temp = statics.t.alloc();
			statics.t.loop(y);
			statics.t.dec(x);
			if (yIsVariable)
			{
				statics.t.inc(temp);
			}
			statics.t.deloop(y);
			if (yIsVariable)
			{
				statics.t.move(y, temp);
			}
			statics.t.inc(temp);
			statics.t.loop(x);
			statics.t.dec(temp);
			statics.t.celoop(x);
			statics.t.free(x);
			if (!yIsVariable)
			{
				statics.t.free(y);
			}
			return temp;
		} else if (leftIsConstant)
		{
			x = right.generateBF();
			y = statics.t.alloc();
			statics.t.minus(x, ((ConstantNode) left).getValue());
			statics.t.inc(y);
			statics.t.loop(x);
			statics.t.dec(y);
			statics.t.celoop(x);
			statics.t.clear(x);
			statics.t.free(x);
			return y;
		} else
		{
			x = left.generateBF();
			y = statics.t.alloc();
			statics.t.minus(x, ((ConstantNode) right).getValue());
			statics.t.inc(y);
			statics.t.loop(x);
			statics.t.dec(y);
			statics.t.celoop(x);
			statics.t.clear(x);
			statics.t.free(x);
			return y;
		}
	}
}
