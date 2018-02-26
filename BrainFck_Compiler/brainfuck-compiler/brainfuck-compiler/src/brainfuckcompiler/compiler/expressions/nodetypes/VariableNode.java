package brainfuckcompiler.compiler.expressions.nodetypes;

import brainfuckcompiler.compiler.expressions.Node;
import brainfuckcompiler.compiler.program.Array;
import brainfuckcompiler.compiler.program.Variable;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.statics;
import java.util.ArrayList;

public class VariableNode extends Node
{

    private String variableName;

    public VariableNode(int lineNumber, Block parentBlock)
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
        variableName = tokens[index + 1];
        return index;
    }

    /**
     *
     * @return
     */
    public int generateBF()
    {
        return statics.t.copy(getVariable().getMemoryPosition());
    }

    public Variable getVariable()
    {
        ArrayList<Array> arrays = parentBlock.getArrayScope();
        for (Array a : arrays)
        {
            if (a.getName().equals(variableName))
            {
                System.err.println("\"" + variableName + "\" refers to an array not a variable at line " + lineNumber);
                System.exit(1);
            }
        }
        Block b = parentBlock;
        while (b != null)
        {
            ArrayList<Variable> variables = b.getVariableScope();
            for (Variable v : variables)
            {
                if (v.getName().equals(variableName))
                {
                    return v;
                }
            }
            b = b.getParentBlock();
        }
        System.err.println("Variable not found: " + variableName + " at line " + lineNumber);
        System.exit(1);
        return null;
    }
}
