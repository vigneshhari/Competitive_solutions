package brainfuckcompiler.compiler.expressions.nodetypes;

import brainfuckcompiler.compiler.expressions.ExpressionGenerator;
import brainfuckcompiler.compiler.expressions.Node;
import brainfuckcompiler.compiler.program.Array;
import brainfuckcompiler.compiler.program.Variable;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.statics;
import java.util.ArrayList;

public class ArrayNode extends Node
{

    private String arrayName;
    private Node expression;

    public ArrayNode(int lineNumber, Block parentBlock)
    {
        super(lineNumber, parentBlock);
    }

    @Override
    public int generateBF()
    {
        Array a = getArray();
        int pos = expression.generateBF();
        int ret = statics.t.alloc();
        a.get(pos, ret);
        return ret;
    }

    @Override
    public int populate(String[] tokens, int index)
    {
        String token = tokens[index + 1];
        int pos = token.indexOf('[');
        arrayName = token.substring(0, pos).trim();
        expression = ExpressionGenerator.generateExpression(token.substring(pos + 1, token.length() - 1), lineNumber, parentBlock);
        return index;
    }

    public Array getArray()
    {
        ArrayList<Variable> variables = parentBlock.getVariableScope();
        for (Variable v : variables)
        {
            if (v.getName().equals(arrayName))
            {
                System.err.println("\"" + arrayName + "\" refers to a variable not an array at line " + lineNumber);
                System.exit(1);
            }
        }
        Block b = parentBlock;
        while (b != null)
        {
            ArrayList<Array> arrays = b.getArrayScope();
            for (Array a : arrays)
            {
                if (a.getName().equals(arrayName))
                {
                    return a;
                }
            }
            b = b.getParentBlock();
        }
        System.err.println("Array not found: " + arrayName + " at line " + lineNumber);
        System.exit(1);
        return null;
    }

    public Node getExpression()
    {
        return expression;
    }
}
