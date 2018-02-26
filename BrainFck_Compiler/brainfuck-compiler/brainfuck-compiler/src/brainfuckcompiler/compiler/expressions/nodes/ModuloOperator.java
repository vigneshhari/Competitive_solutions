package brainfuckcompiler.compiler.expressions.nodes;

import brainfuckcompiler.compiler.expressions.nodetypes.BinaryOperator;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.statics;

/**
 *
 * @author vrighter
 */
public class ModuloOperator extends BinaryOperator
{

    public ModuloOperator(int lineNumber, Block parentBlock)
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
        int x = left.generateBF(), y = right.generateBF();
        int res = statics.t.mod(x, y);
        statics.t.clear(y);
        statics.t.free(y);
        return res;
    }
}
