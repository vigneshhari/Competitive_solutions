package brainfuckcompiler.compiler.program.structure;

import java.util.ArrayList;

public abstract class Statement
{

    protected Block parentBlock;
    protected int lineNumber;

    public Statement(Block parentBlock, int lineNumber)
    {
        this.parentBlock = parentBlock;
        this.lineNumber = lineNumber;
    }

    public abstract int parseStatement(ArrayList<Item> items, int currentPosition);

    public abstract void generate();

    public static boolean isValidVariableName(String name)
    {
        return !name.matches("(dim)|(declare)|(if)|(while)|(dowhile)|(debug)|(else)|(sub)|(func)|(random)|(random)|(push)|(pop)|(in)|(out)|(outs)|(ref)|(elseif)");
    }
}