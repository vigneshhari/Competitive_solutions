package brainfuckcompiler.compiler.program.statements;

import brainfuckcompiler.compiler.program.Array;
import brainfuckcompiler.compiler.program.Variable;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.compiler.program.structure.Item;
import brainfuckcompiler.compiler.program.structure.Line;
import brainfuckcompiler.compiler.program.structure.Statement;
import brainfuckcompiler.statics;
import java.util.ArrayList;

public class DimStatement extends Statement
{

    String arrayName;
    int arraySize;

    public DimStatement(Block parentBlock, int LineNumber)
    {
        super(parentBlock, LineNumber);
    }

    @Override
    public int parseStatement(ArrayList<Item> items, int currentPosition)
    {
        Line l = (Line) items.get(currentPosition);
        currentPosition++;
        String[] parts = statics.splitOnComma(l.getLine().substring(4), l.getLineNumber());
        if (parts.length != 2)
        {
            System.err.println("Incomplete declare statement at line " + l.getLineNumber());
            System.exit(1);
        }
        if (!parts[0].trim().matches("[_a-zA-Z][_0-9a-zA-Z]*"))
        {
            System.err.println("Invalid array name at line " + l.getLineNumber());
            System.exit(1);
        }
        arrayName = parts[0].trim();
        if (!Statement.isValidVariableName(arrayName))
        {
            System.err.println("Invalid array name at line " + lineNumber);
            System.exit(1);
        }
        try
        {
            arraySize = Integer.parseInt(parts[1].trim());
        } catch (NumberFormatException ex)
        {
            System.err.println("Invalid array size at line " + lineNumber);
            System.exit(1);
        }
        return currentPosition;
    }

    @Override
    public void generate()
    {
        if (nameExists())
        {
            System.err.println("Double declaration of array " + arrayName + " at line " + lineNumber);
            System.exit(1);
        }
        parentBlock.getArrayScope().add(new Array(arrayName, arraySize));
    }

    private boolean nameExists()
    {
        ArrayList<Variable> variables = parentBlock.getVariableScope();
        for (Variable v : variables)
        {
            if (v.getName().equals(arrayName))
            {
                return true;
            }
        }
        ArrayList<Array> arrays = parentBlock.getArrayScope();
        for (Array a : arrays)
        {
            if (a.getName().equals(arrayName))
            {
                return true;
            }
        }
        return false;
    }
}