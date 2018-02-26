package brainfuckcompiler.compiler.expressions.nodetypes;

import brainfuckcompiler.compiler.expressions.Node;
import brainfuckcompiler.compiler.expressions.operators.Operators;
import brainfuckcompiler.compiler.program.structure.Block;

/**
 *
 * @author vrighter
 */
public abstract class BinaryOperator extends Node
{

    public BinaryOperator(int lineNumber, Block parentBlock)
    {
        super(lineNumber, parentBlock);
    }
    /**
     *
     */
    public Node left = null, right = null;

    /**
     *
     * @param tokens
     * @param index
     * @return
     */
    public int populate(String[] tokens, int index)
    {
        right = Operators.createNode(tokens[index--], lineNumber, parentBlock);
        right.setParentNode(this);
        index = right.populate(tokens, index);
        left = Operators.createNode(tokens[index--], lineNumber, parentBlock);
        left.setParentNode(this);
        index = left.populate(tokens, index);
        return index;
    }
}
