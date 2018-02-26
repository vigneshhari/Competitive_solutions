package brainfuckcompiler.compiler.expressions.nodes;

import brainfuckcompiler.compiler.expressions.nodetypes.BinaryOperator;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.statics;

/**
 *
 * @author vrighter
 */
public class MultiplyOperator extends BinaryOperator
{

    public MultiplyOperator(int lineNumber, Block parentBlock)
    {
        super(lineNumber, parentBlock);
    }

    /**
     *
     * @param t
     * @return
     */
    public int generateBF()
    {
        int x = this.left.generateBF(), y = this.right.generateBF();
        int res = statics.t.multiply(x, y);
        statics.t.clear(y);
        statics.t.free(y);
        return res;
    }
}
