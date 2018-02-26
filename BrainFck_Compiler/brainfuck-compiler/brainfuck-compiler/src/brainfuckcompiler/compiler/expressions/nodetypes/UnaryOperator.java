package brainfuckcompiler.compiler.expressions.nodetypes;

import brainfuckcompiler.compiler.expressions.Node;
import brainfuckcompiler.compiler.expressions.operators.Operators;
import brainfuckcompiler.compiler.program.structure.Block;

/**
 *
 * @author vrighter
 */
public abstract class UnaryOperator extends Node
{

    public UnaryOperator(int lineNumber, Block parentBlock)
    {
        super(lineNumber, parentBlock);
    }
    public Node operand;

    /**
     *
     * @param tokens
     * @param index
     * @return
     */
    public int populate(String[] tokens, int index)
    {
        operand = Operators.createNode(tokens[index--], lineNumber, parentBlock);
        operand.setParentNode(this);
        index = operand.populate(tokens, index);
        return index;
    }
}
