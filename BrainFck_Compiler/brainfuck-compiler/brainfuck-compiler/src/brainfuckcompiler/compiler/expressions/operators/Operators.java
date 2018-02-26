package brainfuckcompiler.compiler.expressions.operators;

import brainfuckcompiler.compiler.expressions.Node;
import brainfuckcompiler.compiler.expressions.nodes.*;
import brainfuckcompiler.compiler.expressions.nodetypes.*;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.statics;
import java.util.Arrays;
import java.util.regex.Pattern;

/**
 *
 * @author vrighter
 */
public class Operators
{

    private Operator[] operators;

    /**
     *
     */
    public Operators()
    {
        operators = new Operator[]
        {
            new Operator("!", "!", 0, false),
            new Operator("^", "\\^", 1, false),
            new Operator("*", "\\*", 2, true),
            new Operator("/", "/", 2, true),
            new Operator("%", "%", 2, true),
            new Operator("+", "\\+", 3, true),
            new Operator("-", "-", 3, true),
            new Operator("<", "<", 4, true),
            new Operator("<=", "<=", 4, true),
            new Operator(">", ">", 4, true),
            new Operator(">=", ">=", 4, true),
            new Operator("==", "==", 5, true),
            new Operator("!=", "!=", 5, true),
            new Operator("&&", "\\&\\&", 6, true),
            new Operator("||", "\\|\\|", 7, true),
            new Operator("=", "=", 8, false)
        };
        Arrays.sort(operators);
    }

    /**
     *
     * @param token
     * @return
     */
    public Operator getOperator(String token)
    {
        for (Operator o : operators)
        {
            if (o.getOp().equals(token))
            {
                return o;
            }
        }
        return null;
    }

    /**
     *
     * @param exp
     * @param index
     * @return
     */
    public String findOperator(String exp, int index)
    {
        for (Operator o : operators)
        {
            String s = o.getOp();
            if ((index + s.length()) > exp.length())
            {
                continue;
            }
            if (exp.substring(index, index + s.length()).equals(s))
            {
                return s;
            }
        }
        return null;
    }

    /**
     *
     * @param token
     * @return
     */
    public static Node createNode(String token, int lineNumber, Block parentBlock)
    {
        if (token.equals("*"))
        {
            return new MultiplyOperator(lineNumber, parentBlock);
        }
        if (token.equals("/"))
        {
            return new DivideOperator(lineNumber, parentBlock);
        }
        if (token.equals("+"))
        {
            return new AddOperator(lineNumber, parentBlock);
        }
        if (token.equals("-"))
        {
            return new SubtractOperator(lineNumber, parentBlock);
        }
        if (token.equals("=="))
        {
            return new EqualityOperator(lineNumber, parentBlock);
        }
        if (token.equals("!"))
        {
            return new NotOperator(lineNumber, parentBlock);
        }
        if (token.equals("&&"))
        {
            return new AndOperator(lineNumber, parentBlock);
        }
        if (token.equals("||"))
        {
            return new OrOperator(lineNumber, parentBlock);
        }
        if (token.equals("<"))
        {
            return new SmallerThanOperator(lineNumber, parentBlock);
        }
        if (token.equals(">"))
        {
            return new LargerThanOperator(lineNumber, parentBlock);
        }
        if (token.equals("<="))
        {
            return new SmallerThanOrEqualOperator(lineNumber, parentBlock);
        }
        if (token.equals(">="))
        {
            return new LargerThanOrEqualOperator(lineNumber, parentBlock);
        }
        if (token.equals("!="))
        {
            return new NonEqualityOperator(lineNumber, parentBlock);
        }
        if (token.equals("%"))
        {
            return new ModuloOperator(lineNumber, parentBlock);
        }
        if (token.equals("^"))
        {
            return new ExponentiationOperator(lineNumber, parentBlock);
        }
        if (token.equals("="))
        {
            return new AssignmentOperator(lineNumber, parentBlock);
        }
        if (token.equals("random"))
        {
            return new RandomNode(lineNumber, parentBlock);
        }
        if (token.equals("pop"))
        {
            return new PopNode(lineNumber, parentBlock);
        }
        if (token.equals("in"))
        {
            return new InNode(lineNumber, parentBlock);
        }
        if (token.matches("[_a-zA-Z][_0-9a-zA-Z]*\\[.*\\]"))
        {
            return new ArrayNode(lineNumber, parentBlock);
        }
        if (token.matches("[_a-zA-Z][_0-9a-zA-Z]*\\(.*\\)"))
        {
            return new SubNode(lineNumber, parentBlock);
        }
        if (token.matches("[_a-zA-Z][_0-9a-zA-Z]*"))
        {
            return new VariableNode(lineNumber, parentBlock);
        }
        if (token.matches("[0-9]+"))
        {
            return new ConstantNode(lineNumber, parentBlock);
        }
        return null;
    }

    public void createRegex()
    {
        StringBuilder b = new StringBuilder("([_a-zA-Z][_0-9a-zA-Z]*\\[)|([_a-zA-Z][_0-9a-zA-Z]*\\()|([_a-zA-Z][_0-9a-zA-Z]*)|([0-9]+)|(\\()|(\\))");
        for (Operator o : operators)
        {
            b.append("|(");
            b.append(o.getRegex());
            b.append(")");
        }
        statics.p = Pattern.compile(b.toString());
    }
}
