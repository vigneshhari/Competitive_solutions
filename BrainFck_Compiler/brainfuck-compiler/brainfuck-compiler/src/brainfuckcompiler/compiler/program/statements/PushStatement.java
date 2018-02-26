package brainfuckcompiler.compiler.program.statements;

import brainfuckcompiler.compiler.expressions.ExpressionGenerator;
import brainfuckcompiler.compiler.expressions.Node;
import brainfuckcompiler.compiler.expressions.nodetypes.SubNode;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.compiler.program.structure.Item;
import brainfuckcompiler.compiler.program.structure.Line;
import brainfuckcompiler.compiler.program.structure.Statement;
import brainfuckcompiler.statics;
import java.util.ArrayList;

public class PushStatement extends Statement
{

    String variableName;
    Node expression;

    public PushStatement(Block parentBlock, int lineNumber)
    {
        super(parentBlock, lineNumber);
    }

    @Override
    public int parseStatement(ArrayList<Item> items, int currentPosition)
    {
        Line l = (Line) items.get(currentPosition);
        currentPosition++;
        expression = ExpressionGenerator.generateExpression(l.getLine().substring(5).trim(), lineNumber, parentBlock);
        return currentPosition;
    }

    @Override
    public void generate()
    {
        if ((expression instanceof SubNode) && (((SubNode) expression).getType() == SubNode.SUB))
        {
            System.err.println("Cannot use sub in a push statement on line " + lineNumber);
            System.exit(1);
        }
        int p = expression.generateBF();
        statics.t.to(p);
        statics.t.append("s" + statics.t.getPointer() + "e");
        statics.t.free(p);
    }
}
