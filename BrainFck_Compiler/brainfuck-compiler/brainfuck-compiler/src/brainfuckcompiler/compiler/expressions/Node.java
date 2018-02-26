package brainfuckcompiler.compiler.expressions;

import brainfuckcompiler.compiler.program.structure.Block;

public abstract class Node
{

    protected Node parentNode = null;
    protected Block parentBlock;
    public boolean returnsBoolean = false;
    protected boolean stored = false;
    protected int lineNumber;

    public Node(int lineNumber, Block parentBlock)
    {
        this.lineNumber = lineNumber;
        this.parentBlock = parentBlock;
    }

    public abstract int generateBF();

    public abstract int populate(String[] tokens, int index);

    public Node getParentNode()
    {
        return parentNode;
    }

    public void setParentNode(Node parentNode)
    {
        this.parentNode = parentNode;
    }
}