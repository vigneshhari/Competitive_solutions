package brainfuckcompiler.compiler.program.statements;

import brainfuckcompiler.compiler.program.structure.*;
import brainfuckcompiler.statics;
import java.util.ArrayList;

public class SubStatement extends Statement
{

    Subroutine sub;

    public SubStatement(Block parentBlock, int lineNumber)
    {
        super(parentBlock, lineNumber);
    }

    @Override
    public int parseStatement(ArrayList<Item> items, int currentPosition)
    {
        Line l = (Line) items.get(currentPosition);
        String line = l.getLine().substring(4).trim();
        int openParen = line.indexOf('(');
        if ((openParen == -1) && (line.indexOf(')') != (line.length() - 1)))
        {
            System.err.println("Invalid sub declaration at line " + l.getLineNumber());
            System.exit(1);
        }
        String name = line.substring(0, openParen);
        line = line.substring(openParen + 1, line.length() - 1);
        String[] variableNames = statics.splitOnComma(line, lineNumber);
        if ((variableNames.length == 1) && (variableNames[0].trim().equals("")))
        {
            variableNames = new String[0];
        }
        for (int i = 0; i < variableNames.length; i++)
        {
            variableNames[i] = variableNames[i].trim();
            if ((!Statement.isValidVariableName(variableNames[i])) || (!variableNames[i].matches("[_a-zA-Z][_0-9a-zA-Z]*")))
            {
                System.err.println("Invalid variable name \"" + variableNames[i] + "\" at line " + lineNumber);
                System.exit(1);
            }
        }
        currentPosition++;
        if (currentPosition >= items.size())
        {
            System.err.println("Expected code block at line " + (l.getLineNumber() + 1));
            System.exit(1);
        }
        Item item = items.get(currentPosition);
        currentPosition++;
        if (!(item instanceof Block))
        {
            System.err.println("Expected code block at line " + (l.getLineNumber() + 1));
            System.exit(1);
        }
        ((Block) item).generateStatements();
        sub = new Subroutine(name, variableNames, (Block) item);
        return currentPosition;
    }

    @Override
    public void generate()
    {
        if (subNameExists())
        {
            System.err.println("Double declaration of subroutine/function at line " + lineNumber);
            System.exit(1);
        }
        sub.setExternalAccessibleVariables(parentBlock.getVariableScope(), parentBlock.getArrayScope(), parentBlock.getSubScope(), parentBlock.getFuncScope());
        parentBlock.getSubScope().add(sub);
    }

    private boolean subNameExists()
    {
        for (Subroutine s : parentBlock.getSubScope())
        {
            if (s.getName().equals(sub.getName()))
            {
                return true;
            }
        }
        for (Function f : parentBlock.getFuncScope())
        {
            if (f.getName().equals(sub.getName()))
            {
                return true;
            }
        }
        return false;
    }
}