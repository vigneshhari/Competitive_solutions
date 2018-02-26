package brainfuckcompiler.compiler.expressions.nodetypes;

import brainfuckcompiler.compiler.expressions.Node;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.statics;

/**
 *
 * @author vrighter
 */
public class ConstantNode extends Node
{

	private int value = 0;

	public ConstantNode(int lineNumber, Block parentBlock)
	{
		super(lineNumber, parentBlock);
	}

	/**
	 *
	 * @param tokens
	 * @param index
	 * @return
	 */
	public int populate(String[] tokens, int index)
	{
		value = Integer.parseInt(tokens[index + 1]);
		return index;
	}

	/**
	 *
	 * @return
	 */
	public int generateBF()
	{
		int address = statics.t.alloc();
		if (value != 0)
		{
			statics.t.to(address);
			statics.t.plus(value);
		}
		return address;
	}

	public int getValue()
	{
		return value;
	}
}
