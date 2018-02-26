package brainfuckcompiler.compiler.expressions.nodes;

import brainfuckcompiler.compiler.expressions.nodetypes.UnaryOperator;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.statics;

/**
 *
 * @author vrighter
 */
public class NotOperator extends UnaryOperator
{

    /**
     *
     */
    public NotOperator(int lineNumber, Block parentBlock)
    {
        super(lineNumber, parentBlock);
        returnsBoolean = true;
    }

    /**
     *
     * @param t
     * @return
     */
    public int generateBF()
    {
        int x = operand.returnsBoolean ? operand.generateBF() : statics.t.toBoolean(operand.generateBF());
        return statics.t.not(x);
    }
}
