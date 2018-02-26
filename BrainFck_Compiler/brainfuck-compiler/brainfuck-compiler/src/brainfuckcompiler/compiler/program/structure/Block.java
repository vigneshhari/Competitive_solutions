package brainfuckcompiler.compiler.program.structure;

import brainfuckcompiler.compiler.program.Array;
import brainfuckcompiler.compiler.program.Variable;
import brainfuckcompiler.compiler.program.statements.*;
import java.util.ArrayList;

public class Block extends Item
{

    private ArrayList<Item> items;
    private ArrayList<Statement> statements;
    private ArrayList<Variable> variableScope;
    private ArrayList<Array> arrayScope;
    private ArrayList<Subroutine> subScope;
    private ArrayList<Function> funcScope;
    private boolean subLock;
    private ArrayList<String> variablesNotToFree;

    public Block(ArrayList<Item> items, int indentLevel, Block parentBlock, int lineNumber)
    {
        super(indentLevel, parentBlock, lineNumber);
        for (Item i : items)
        {
            i.setParentBlock(this);
        }
        for (int i = 0; i < items.size(); i++)
        {
            Item item = items.get(i);
            int currentIndentLevel = item.getIndentLevel();
            int blockLineNumber = item.getLineNumber();
            if (currentIndentLevel > this.getIndentLevel())
            {
                if (currentIndentLevel == (this.getIndentLevel() + 1))
                {
                    int amtitems = 1;
                    for (int j = i + 1; j < items.size(); j++)
                    {
                        if (items.get(j).getIndentLevel() >= currentIndentLevel)
                        {
                            amtitems++;
                        } else
                        {
                            break;
                        }
                    }
                    ArrayList<Item> newBlockItems = new ArrayList<Item>();
                    for (int j = 0; j < amtitems; j++)
                    {
                        newBlockItems.add(items.remove(i));
                    }
                    items.add(i, new Block(newBlockItems, currentIndentLevel, this, blockLineNumber));
                } else
                {
                    System.err.println("Invalid indent level at line " + blockLineNumber);
                    System.exit(1);
                }
            }
        }
        this.items = items;
        this.items.trimToSize();
        variableScope = new ArrayList<Variable>();
        arrayScope = new ArrayList<Array>();
        subScope = new ArrayList<Subroutine>();
        funcScope = new ArrayList<Function>();
        subLock = false;
        variablesNotToFree = new ArrayList<String>();
    }

    public void setVariablesNotToFree(ArrayList<String> variablesNotToFree)
    {
        this.variablesNotToFree = variablesNotToFree;
        this.variablesNotToFree.trimToSize();
    }

    public void generateStatements()
    {
        statements = new ArrayList<Statement>();
        int pos = 0;
        while (pos < items.size())
        {
            Item i = items.get(pos);
            if (i instanceof Block)
            {
                Statement s = new BlockStatement((Block) i, this, i.getLineNumber());
                statements.add(s);
                pos++;
                continue;
            }
            Line l = (Line) i;
            if (l.getLine().equals("else"))
            {
                System.err.println("else without an if found at line " + l.getLineNumber());
                System.exit(1);
            }
            if (l.getLine().startsWith("elseif "))
            {
                System.err.println("elseif without an if found at line " + l.getLineNumber());
                System.exit(1);
            }
            if (l.getLine().startsWith("declare "))
            {
                Statement s = new DeclareStatement(this, l.getLineNumber());
                pos = s.parseStatement(items, pos);
                statements.add(s);
                continue;
            }
            if (l.getLine().equals("debug"))
            {
                Statement s = new DebugStatement(this, l.getLineNumber());
                pos = s.parseStatement(items, pos);
                statements.add(s);
                continue;
            }
            if (l.getLine().startsWith("dim "))
            {
                Statement s = new DimStatement(this, l.getLineNumber());
                pos = s.parseStatement(items, pos);
                statements.add(s);
                continue;
            }
            if (l.getLine().startsWith("sub "))
            {
                if (indentLevel != 0)
                {
                    System.err.println("Subroutines must be declared at indent level 0. Line " + l.getLineNumber());
                    System.exit(1);
                }
                if (subLock)
                {
                    System.err.println("Only declare, dim and debug statements are allowed before function or subroutine declarations. Line " + l.getLineNumber());
                    System.exit(1);
                }
                Statement s = new SubStatement(this, l.getLineNumber());
                pos = s.parseStatement(items, pos);
                statements.add(s);
                continue;
            }
            if (l.getLine().startsWith("func "))
            {
                if (indentLevel != 0)
                {
                    System.err.println("Functions must be declared at indent level 0. Line " + l.getLineNumber());
                    System.exit(1);
                }
                if (subLock)
                {
                    System.err.println("Only declare, dim and debug statements are allowed before function or subroutine declarations. Line " + l.getLineNumber());
                    System.exit(1);
                }
                Statement s = new FuncStatement(this, l.getLineNumber());
                pos = s.parseStatement(items, pos);
                statements.add(s);
                continue;
            }
            subLock = true;
            if (l.getLine().startsWith("out "))
            {
                Statement s = new OutStatement(this, l.getLineNumber());
                pos = s.parseStatement(items, pos);
                statements.add(s);
                continue;
            }
            if (l.getLine().startsWith("outs "))
            {
                Statement s = new OutsStatement(this, l.getLineNumber());
                pos = s.parseStatement(items, pos);
                statements.add(s);
                continue;
            }
            if (l.getLine().startsWith("push "))
            {
                Statement s = new PushStatement(this, l.getLineNumber());
                pos = s.parseStatement(items, pos);
                statements.add(s);
                continue;
            }
            if (l.getLine().startsWith("if "))
            {
                Statement s = new IfStatement(this, l.getLineNumber());
                pos = s.parseStatement(items, pos);
                statements.add(s);
                continue;
            }
            if (l.getLine().startsWith("while "))
            {
                Statement s = new WhileStatement(this, l.getLineNumber());
                pos = s.parseStatement(items, pos);
                statements.add(s);
                continue;
            }
            if (l.getLine().startsWith("dowhile "))
            {
                Statement s = new DowhileStatement(this, l.getLineNumber());
                pos = s.parseStatement(items, pos);
                statements.add(s);
                continue;
            }
            Statement s = new ExpressionStatement(this, l.getLineNumber());
            pos = s.parseStatement(items, pos);
            statements.add(s);
        }
        items.clear();
        items = null;
    }

    public ArrayList<Variable> getVariableScope()
    {
        return variableScope;
    }

    public ArrayList<Array> getArrayScope()
    {
        return arrayScope;
    }

    public void generate()
    {
        for (int i = 0; i < statements.size(); i++)
        {
            Statement s = statements.get(i);
            s.generate();
        }
        while (!variableScope.isEmpty())
        {
            Variable v = variableScope.remove(variableScope.size() - 1);
            boolean free = true;
            for (int i = 0; i < variablesNotToFree.size(); i++)
            {
                if (v.getName().equals(variablesNotToFree.get(i)))
                {
                    free = false;
                    break;
                }
            }
            if (free)
            {
                v.free();
            }
        }
        while (!arrayScope.isEmpty())
        {
            Array a = arrayScope.remove(arrayScope.size() - 1);
            boolean free = true;
            for (int i = 0; i < variablesNotToFree.size(); i++)
            {
                if (a.getName().equals(variablesNotToFree.get(i)))
                {
                    free = false;
                    break;
                }
            }
            if (free)
            {
                a.free();
            }
        }
    }

    public ArrayList<Subroutine> getSubScope()
    {
        return subScope;
    }

    public ArrayList<Function> getFuncScope()
    {
        return funcScope;
    }

    public ArrayList<String> getVariablesNotToFree()
    {
        return variablesNotToFree;
    }
}