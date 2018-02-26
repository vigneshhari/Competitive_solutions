package brainfuckcompiler.compiler.program.statements;

import brainfuckcompiler.compiler.expressions.Node;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.compiler.program.structure.Item;
import brainfuckcompiler.compiler.program.structure.Statement;
import brainfuckcompiler.statics;
import java.util.ArrayList;

public class DebugStatement extends Statement
{

    Node expression = null;
    String variableName;

    public DebugStatement(Block parentBlock, int lineNumber)
    {
        super(parentBlock, lineNumber);
    }

    public int parseStatement(ArrayList<Item> items, int currentPosition)
    {
        return currentPosition + 1;
    }

    @Override
    public void generate()
    {
        statics.t.append("#");
    }
}
