package brainfuckcompiler.compiler.expressions.nodes;

import brainfuckcompiler.compiler.expressions.nodetypes.BinaryOperator;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.statics;

/**
 *
 * @author vrighter
 */
public class LargerThanOrEqualOperator extends BinaryOperator
{

    /**
     *
     */
    public LargerThanOrEqualOperator(int lineNumber, Block parentBlock)
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
        int x = left.generateBF(), y = right.generateBF();
        int res = statics.t.smallerthan(x, y);
        statics.t.clear(y);
        statics.t.free(y);
        res = statics.t.not(res);
        return res;
    }
}
