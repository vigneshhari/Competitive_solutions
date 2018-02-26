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

public class WhileStatement extends Statement
{

    Node expression;
    Block loopBlock;

    public WhileStatement(Block parentBlock, int lineNumber)
    {
        super(parentBlock, lineNumber);
    }

    public int parseStatement(ArrayList<Item> items, int currentPosition)
    {
        Line l = (Line) items.get(currentPosition);
        expression = ExpressionGenerator.generateExpression(l.getLine().substring(6), l.getLineNumber(), parentBlock);
        if (expression instanceof AssignmentOperator)
        {
            System.err.println("Cannot assign a value to a variable on line " + l.getLineNumber());
            System.exit(1);
        }
        if ((expression instanceof SubNode) && (((SubNode) expression).getType() == SubNode.SUB))
        {
            System.err.println("Cannot use a sub in a while statement on line " + l.getLineNumber());
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
                    loopBlock = (Block) i;
                    loopBlock.generateStatements();
                    currentPosition++;
                } else
                {
                    System.err.println("Invalid indent level at line " + (i.getIndentLevel() + 1));
                }
            } else
            {
                System.err.println("Expected code block at line " + (l.getLine() + 1));
                System.exit(1);
            }
        } else
        {
            System.err.println("Expected code block at line " + (l.getLine() + 1));
            System.exit(1);
        }
        return currentPosition;
    }

    @Override
    public void generate()
    {
        int address = expression.generateBF();
        statics.t.loop(address);
        statics.t.clear(address);
        loopBlock.generate();
        int address2 = expression.generateBF();
        statics.t.move(address, address2);
        statics.t.free(address2);
        statics.t.teloop(address);
        statics.t.free(address);
    }
}