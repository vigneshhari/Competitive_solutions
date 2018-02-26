package brainfuckcompiler.compiler.program.statements;

import brainfuckcompiler.compiler.expressions.ExpressionGenerator;
import brainfuckcompiler.compiler.expressions.Node;
import brainfuckcompiler.compiler.expressions.nodes.AssignmentOperator;
import brainfuckcompiler.compiler.expressions.nodetypes.PopNode;
import brainfuckcompiler.compiler.expressions.nodetypes.SubNode;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.compiler.program.structure.Item;
import brainfuckcompiler.compiler.program.structure.Line;
import brainfuckcompiler.compiler.program.structure.Statement;
import brainfuckcompiler.statics;
import java.util.ArrayList;

public class ExpressionStatement extends Statement
{

    Node expression;

    public ExpressionStatement(Block parentBlock, int LineNumber)
    {
        super(parentBlock, LineNumber);
    }

    @Override
    public int parseStatement(ArrayList<Item> items, int currentPosition)
    {
        expression = ExpressionGenerator.generateExpression(((Line) items.get(currentPosition)).getLine(), lineNumber, parentBlock);
        if (!((expression instanceof AssignmentOperator) || (expression instanceof SubNode) || (expression instanceof PopNode)))
        {
            System.err.println("Expression on line " + lineNumber + " must be an assignment, a sub/function call or a pop");
            System.exit(1);
        }
        currentPosition++;
        return currentPosition;
    }

    @Override
    public void generate()
    {
        if (expression instanceof SubNode)
        {
            SubNode s = (SubNode) expression;
            if (s.getType() == SubNode.SUB)
            {
                s.generateBF();
                return;
            } else if (s.getType() == SubNode.FUNC)
            {
                int ret = s.generateBF();
                statics.t.clear(ret);
                statics.t.free(ret);
                return;
            } else if (s.getType() == SubNode.NOTFOUND)
            {
                System.err.println("\"" + s.getSubName() + "\" not found on line " + lineNumber);
            }
        } else if (expression instanceof PopNode)
        {
            statics.t.append("c" + statics.t.getPointer() + "e");
            return;
        }
        expression.generateBF();
    }
}
