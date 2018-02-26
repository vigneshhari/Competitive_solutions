package brainfuckcompiler.compiler.program.structure;

public abstract class Item
{

    protected int indentLevel;
    protected Block parentBlock;
    protected int lineNumber;

    public Item(int indentLevel, Block parentBlock, int lineNumber)
    {
        this.indentLevel = indentLevel;
        this.parentBlock = parentBlock;
        this.lineNumber = lineNumber;
    }

    public void setParentBlock(Block parentBlock)
    {
        this.parentBlock = parentBlock;
    }

    public Block getParentBlock()
    {
        return parentBlock;
    }

    public int getIndentLevel()
    {
        return indentLevel;
    }

    public int getLineNumber()
    {
        return lineNumber;
    }
}