package brainfuckcompiler.compiler.expressions.nodetypes;

import brainfuckcompiler.compiler.expressions.ExpressionGenerator;
import brainfuckcompiler.compiler.expressions.Node;
import brainfuckcompiler.compiler.expressions.nodes.AssignmentOperator;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.compiler.program.structure.Function;
import brainfuckcompiler.compiler.program.structure.Subroutine;
import brainfuckcompiler.statics;

public class SubNode extends Node
{

    public static final int SUB = 0;
    public static final int FUNC = 1;
    public static final int NOTFOUND = -1;
    private Node[] expressions;
    private String subName;
    private int type;

    public SubNode(int lineNumber, Block parentBlock)
    {
        super(lineNumber, parentBlock);
        type = -2;
    }

    @Override
    public int generateBF()
    {
        if (this.getType() == SUB)
        {
            generateSub();
            return -1;
        } else if (this.getType() == FUNC)
        {
            return generateFunc();
        } else
        {
            System.err.println("\"" + subName + "\" not found on line " + lineNumber);
            System.exit(1);
            return -1;
        }
    }

    private void generateSub()
    {
        if (parentNode != null)
        {
            System.err.println("A subroutine call cannot be used in an expression. Line " + lineNumber);
            System.exit(1);
        }
        Subroutine sub = getSubroutine();
        int[] memoryLocations = new int[expressions.length];
        for (int i = 0; i < expressions.length; i++)
        {
            if ((expressions[i] instanceof SubNode) && (((SubNode) expressions[i]).getType() == SUB))
            {
                System.err.println("Cannot use a subroutine as a parameter. Line " + lineNumber);
                System.exit(1);
            }
            memoryLocations[i] = expressions[i].generateBF();
        }
        sub.generate(lineNumber, memoryLocations);
    }

    private int generateFunc()
    {
        Function func = getFunction();
        int[] memoryLocations = new int[expressions.length];
        for (int i = 0; i < expressions.length; i++)
        {
            if ((expressions[i] instanceof SubNode) && (((SubNode) expressions[i]).getType() == SUB))
            {
                System.err.println("Cannot use a subroutine as a parameter. Line " + lineNumber);
                System.exit(1);
            }
            memoryLocations[i] = expressions[i].generateBF();
        }
        func.generate(lineNumber, memoryLocations);
        return func.getReturnMemoryPosition();
    }

    private Subroutine getSubroutine()
    {
        Block scopeBlock = getScopeBlock();
        for (Subroutine s : scopeBlock.getSubScope())
        {
            if (s.getName().equals(subName))
            {
                return s;
            }
        }
        return null;
    }

    private Function getFunction()
    {
        Block scopeBlock = getScopeBlock();
        for (Function f : scopeBlock.getFuncScope())
        {
            if (f.getName().equals(subName))
            {
                return f;
            }
        }
        return null;
    }

    private Block getScopeBlock()
    {
        Block scopeBlock = parentBlock;
        while (scopeBlock.getParentBlock() != null)
        {
            scopeBlock = scopeBlock.getParentBlock();
        }
        return scopeBlock;
    }

    public int getType()
    {
        if (type != -2)
        {
            return type;
        } else
        {
            if (getSubroutine() != null)
            {
                this.type = SUB;
                return this.type;
            }
            if (getFunction() != null)
            {
                this.type = FUNC;
                return this.type;
            }
            this.type = NOTFOUND;
            return type;
        }
    }

    @Override
    public int populate(String[] tokens, int index)
    {
        String token = tokens[index + 1];
        int leftParen = token.indexOf('(');
        subName = token.substring(0, leftParen);
        String expr = token.substring(leftParen + 1, token.length() - 1);
        String[] expressionStrings;
        if (expr.trim().equals(""))
        {
            expressionStrings = new String[0];
        } else
        {
            expressionStrings = statics.splitOnComma(expr, lineNumber);
        }
        expressions = new Node[expressionStrings.length];
        for (int i = 0; i < expressions.length; i++)
        {
            Node n = ExpressionGenerator.generateExpression(expressionStrings[i].trim(), lineNumber, parentBlock);
            if (n instanceof AssignmentOperator)
            {
                System.err.println("Cannot have an assignment operator as a parameter. Line " + lineNumber);
                System.exit(1);
            }
            expressions[i] = n;
        }
        return index;
    }

    public String getSubName()
    {
        return subName;
    }
}