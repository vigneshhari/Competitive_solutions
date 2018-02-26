package brainfuckcompiler.compiler.expressions;

import brainfuckcompiler.compiler.expressions.operators.Operator;
import brainfuckcompiler.compiler.expressions.operators.Operators;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.statics;
import java.util.ArrayList;
import java.util.Stack;
import java.util.regex.Matcher;

/**
 *
 * @author vrighter
 */
public class ExpressionGenerator
{

    private static String[] convertInfixToPostfix(String e)
    {
        Operator paren = new Operator("(", "\\(", Integer.MAX_VALUE, true), temp;
        Stack<Operator> s = new Stack<Operator>();
        ArrayList<String> retArrayList = new ArrayList<String>();
        String[] tokens = tokenize(e);
        if (tokens == null)
        {
            return null;
        }
        for (int i = 0; i < tokens.length; i++)
        {
            String t = tokens[i];
            if (t.matches("([_a-zA-Z][_0-9a-zA-Z]*\\[.*\\])|([_a-zA-Z][_0-9a-zA-Z]*\\(.*\\))|([_a-zA-Z][_0-9a-zA-Z]*)|([0-9]+)"))
            {
                retArrayList.add(t);
            } else if (t.equals("("))
            {
                s.push(paren);
            } else if (t.equals(")"))
            {
                while (!(temp = s.pop()).getOp().equals("("))
                {
                    retArrayList.add(temp.getOp());
                }
            } else
            {
                Operator o = statics.ops.getOperator(t);
                if (s.empty())
                {
                    s.push(o);
                } else
                {
                    while (true)
                    {
                        if (s.empty())
                        {
                            s.push(o);
                            break;
                        }
                        Operator topStack = (Operator) s.peek();
                        if ((topStack.isLeftAssociative() && topStack.getPrecedence() <= o.getPrecedence()) || (!topStack.isLeftAssociative() && topStack.getPrecedence() < o.getPrecedence()))
                        {
                            retArrayList.add(s.pop().getOp());
                        } else
                        {
                            s.push(o);
                            break;
                        }
                    }
                }
            }
        }
        while (!s.empty())
        {
            retArrayList.add(s.pop().getOp());
        }
        String[] ret = new String[retArrayList.size()];
        retArrayList.toArray(ret);
        return ret;
    }

    private static String[] tokenize(String e)
    {
        Matcher m = statics.p.matcher(e);
        ArrayList<String> l = new ArrayList<String>();
        while (m.find())
        {
            String s = m.group();
            if (s.contains("(") && (s.length() > 1))
            {
                int startingPosition = e.indexOf(s);
                int endingPosition = startingPosition + s.length();
                int counter = 1;
                boolean found = false;
                for (int i = endingPosition; i < e.length(); i++)
                {
                    endingPosition++;
                    char c = e.charAt(i);
                    if (c == '(')
                    {
                        counter++;
                    } else if ((c == ')') && (--counter == 0))
                    {
                        l.add(e.substring(startingPosition, endingPosition));
                        e = e.substring(endingPosition);
                        m.reset(e);
                        found = true;
                        break;
                    }
                }
                if (!found)
                {
                    System.err.println("No matching ) found");
                    System.exit(1);
                }
            } else if (s.contains("["))
            {
                int startingPosition = e.indexOf(s);
                int endingPosition = startingPosition + s.length();
                int counter = 1;
                boolean found = false;
                for (int i = endingPosition; i < e.length(); i++)
                {
                    endingPosition++;
                    char c = e.charAt(i);
                    if (c == '[')
                    {
                        counter++;
                    } else if ((c == ']') && (--counter == 0))
                    {
                        l.add(e.substring(startingPosition, endingPosition));
                        e = e.substring(endingPosition);
                        m.reset(e);
                        found = true;
                        break;
                    }
                }
                if (!found)
                {
                    System.err.println("No matching ] found");
                    System.exit(1);
                }
            } else if (s.matches("[0-9]+"))
            {
                int position = e.indexOf(s) + s.length();
                if (position == e.length())
                {
                    l.add(s);
                } else
                {
                    char c = e.charAt(position);
                    if (c != '_' && (!((c >= 'a') && (c <= 'z'))) && (!((c >= 'A') && (c <= 'Z'))))
                    {
                        l.add(s);
                        e = e.substring(position);
                        m.reset(e);
                    } else
                    {
                        System.err.println("Could not match token");
                        System.exit(1);
                    }
                }
            } else
            {
                l.add(s);
            }
        }
        String[] ret = new String[l.size()];
        l.toArray(ret);
        return ret;
    }

    public static Node generateExpression(String s, int lineNumber, Block parentBlock)
    {
        if (s.equals(""))
        {
            System.err.println("Empty expression on line " + lineNumber);
            System.exit(1);
        }
        return generatePostfixExpression(convertInfixToPostfix(s), lineNumber, parentBlock);
    }

    private static Node generatePostfixExpression(String[] tokens, int lineNumber, Block parentBlock)
    {
        Node tree = Operators.createNode(tokens[tokens.length - 1], lineNumber, parentBlock);
        if (tree.populate(tokens, tokens.length - 2) != -1)
        {
            System.err.println("Error in expression. Not all detected tokens were used. Please recheck Expression on line " + lineNumber);
            System.exit(1);
        }
        return tree;
    }
}