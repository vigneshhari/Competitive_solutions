package brainfuckcompiler.compiler.program.structure;

public class Line extends Item
{

    private String line;

    public Line(int indentLevel, String line, Block parentBlock, int lineNumber)
    {
        super(indentLevel, parentBlock, lineNumber);
        this.line = line;
    }

    public String getLine()
    {
        return line;
    }
}