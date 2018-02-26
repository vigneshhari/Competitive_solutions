package brainfuckcompiler.compiler.program.statements;

import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.compiler.program.structure.Item;
import brainfuckcompiler.compiler.program.structure.Statement;
import java.util.ArrayList;

public class BlockStatement extends Statement
{

    private Block block;

    public BlockStatement(Block block, Block parentBlock, int lineNumber)
    {
        super(parentBlock, lineNumber);
        this.block = block;
        this.block.generateStatements();
    }

    public int parseStatement(ArrayList<Item> items, int currentPosition)
    {
        return currentPosition;
    }

    @Override
    public void generate()
    {
        block.generate();
    }
}
