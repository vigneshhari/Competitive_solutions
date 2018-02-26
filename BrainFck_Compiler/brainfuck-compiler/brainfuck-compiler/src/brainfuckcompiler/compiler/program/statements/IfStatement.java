package brainfuckcompiler.compiler.program.statements;

import brainfuckcompiler.compiler.expressions.ExpressionGenerator;
import brainfuckcompiler.compiler.expressions.Node;
import brainfuckcompiler.compiler.expressions.nodes.AssignmentOperator;
import brainfuckcompiler.compiler.expressions.nodetypes.SubNode;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.compiler.program.structure.Item;
import brainfuckcompiler.compiler.program.structure.Line;
import brainfuckcompiler.compiler.program.structure.Statement;
import brainfuckcompiler.statics;
import java.util.ArrayList;

public class IfStatement extends Statement
{

	Block ifBlock = null;
	Block elseBlock = null;
	Node expression;
	IfStatement ifStatement = null;

	public IfStatement(Block parentBlock, int lineNumber)
	{
		super(parentBlock, lineNumber);
	}

	public int parseStatement(ArrayList<Item> items, int currentPosition)
	{
		Line l = (Line) items.get(currentPosition);
		expression = ExpressionGenerator.generateExpression(l.getLine().substring(l.getLine().startsWith("if ") ? 3 : 7), l.getLineNumber(), parentBlock);
		if (expression instanceof AssignmentOperator)
		{
			System.err.println("Cannot assign a value to a variable on line " + l.getLineNumber());
			System.exit(1);
		}
		if ((expression instanceof SubNode) && (((SubNode) expression).getType() == SubNode.SUB))
		{
			System.err.println("Cannot use a sub in an if statement on line " + l.getLineNumber());
			System.exit(1);
		}
		currentPosition++;
		if (currentPosition < items.size())
		{
			Item i = items.get(currentPosition);
			if (i instanceof Block)
			{
				if (i.getIndentLevel() == (l.getIndentLevel() + 1))
				{
					ifBlock = (Block) i;
					ifBlock.generateStatements();
				} else
				{
					System.err.println("Invalid indent level at line " + i.getLineNumber());
					System.exit(1);
				}
			} else
			{
				System.err.println("Expected code block at line " + (l.getLineNumber() + 1));
				System.exit(1);
			}
		} else
		{
			System.err.println("Expected code block at line " + (l.getLineNumber() + 1));
			System.exit(1);
		}
		currentPosition++;
		if (currentPosition < items.size())
		{
			Item i = items.get(currentPosition);
			if (i instanceof Line)
			{
				Line elseLine = (Line) i;
				if (elseLine.getLine().equals("else") && (elseLine.getIndentLevel() == l.getIndentLevel()))
				{
					currentPosition++;
					if (currentPosition < items.size())
					{
						Item eb = items.get(currentPosition);
						if (eb instanceof Block)
						{
							if (eb.getIndentLevel() == (elseLine.getIndentLevel() + 1))
							{
								elseBlock = (Block) eb;
								elseBlock.generateStatements();
								currentPosition++;
							} else
							{
								System.err.println("Invalid indent level at line " + eb.getLineNumber());
							}
						} else
						{
							System.err.println("Expected code block at line " + (elseLine.getLineNumber() + 1));
						}
					} else
					{
						System.err.println("Expected code block at line " + (elseLine.getLineNumber() + 1));
					}
				} else if (elseLine.getLine().startsWith("elseif ") && (elseLine.getIndentLevel() == l.getIndentLevel()))
				{
					ifStatement = new IfStatement(parentBlock, lineNumber);
					currentPosition = ifStatement.parseStatement(items, currentPosition);
				}
			}
		}
		return currentPosition;
	}

	@Override
	public void generate()
	{
		if ((elseBlock == null) && (ifStatement == null))
		{
			generateIf();
		} else
		{
			generateIfElse();
		}
	}

	private void generateIf()
	{
		int address = expression.generateBF();
		statics.t.loop(address);
		ifBlock.generate();
		statics.t.celoop(address);
		statics.t.free(address);
	}

	private void generateIfElse()
	{
		int x = (expression.returnsBoolean ? expression.generateBF() : statics.t.toBoolean(expression.generateBF()));
		int elseAddress = statics.t.alloc();
		statics.t.plus(elseAddress, 1);
		statics.t.loop(x);
		statics.t.clear(elseAddress);
		ifBlock.generate();
		statics.t.celoop(x);
		statics.t.free(x);
		statics.t.loop(elseAddress);
		if (elseBlock != null)
		{
			elseBlock.generate();
		} else
		{
			ifStatement.generate();
		}
		statics.t.celoop(elseAddress);
		statics.t.free(elseAddress);
	}
}
