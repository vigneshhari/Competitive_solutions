package brainfuckcompiler.compiler.expressions.operators;

/**
 *
 * @author vrighter
 */
public class Operator implements Comparable
{

    private String op, regex;
    private int precedence;
    private boolean leftAssociative;

    /**
     *
     * @return
     */
    public boolean isLeftAssociative()
    {
        return leftAssociative;
    }

    /**
     *
     * @return
     */
    public int getPrecedence()
    {
        return precedence;
    }

    /**
     *
     * @return
     */
    public String getOp()
    {
        return op;
    }

    /**
     *
     * @param op
     * @param regex 
     * @param precedence
     * @param leftAssociative
     */
    public Operator(String op, String regex, int precedence, boolean leftAssociative)
    {
        this.op = op;
        this.precedence = precedence;
        this.leftAssociative = leftAssociative;
        this.regex=regex;
    }

    public int compareTo(Object ob)
    {
        Operator o = (Operator) ob;
        if (o.op.length() == this.op.length())
        {
            return 0;
        }
        if (o.op.length() < this.op.length())
        {
            return -1;
        } else
        {
            return 1;
        }
    }

    public String getRegex()
    {
        return regex;
    }
}
