package brainfuckcompiler.compiler.program.statements;

import brainfuckcompiler.code.strings.StringTools;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.compiler.program.structure.Item;
import brainfuckcompiler.compiler.program.structure.Line;
import brainfuckcompiler.compiler.program.structure.Statement;
import java.util.ArrayList;

public class OutsStatement extends Statement
{

    String string;

    public OutsStatement(Block parentBlock, int lineNumber)
    {
        super(parentBlock, lineNumber);
    }

    @Override
    public int parseStatement(ArrayList<Item> items, int currentPosition)
    {
        Line l = (Line) items.get(currentPosition);
        currentPosition++;
        String s = l.getLine().substring(5).trim();
        if (s.matches("\".*\""))
        {
            string = s.substring(1, s.length() - 1);
        } else
        {
            System.err.println("Invalid string on line " + l.getLineNumber());
            System.exit(1);
        }
        return currentPosition;
    }

    @Override
    public void generate()
    {
        StringTools.printString(string);
    }
}
