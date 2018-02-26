package brainfuckcompiler.compiler.expressions.nodetypes;

import brainfuckcompiler.compiler.expressions.Node;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.statics;

public class InNode extends Node
{

    public InNode(int lineNumber, Block parentBlock)
    {
        super(lineNumber, parentBlock);
    }

    /**
     *
     * @param tokens
     * @param index
     * @return
     */
    public int populate(String[] tokens, int index)
    {
        return index;
    }

    /**
     *
     * @return
     */
    public int generateBF()
    {
        int ret = statics.t.alloc();
        statics.t.to(ret);
        statics.t.append(",");
        return ret;
    }
}
