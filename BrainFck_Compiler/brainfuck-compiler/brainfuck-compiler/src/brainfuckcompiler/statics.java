package brainfuckcompiler;

import brainfuckcompiler.code.BrainfuckTools;
import brainfuckcompiler.code.random.RandomNumberGenerator;
import brainfuckcompiler.compiler.expressions.operators.Operators;
import java.util.ArrayList;
import java.util.regex.Pattern;

public class statics
{

    public static BrainfuckTools t = null;
    public static Operators ops = null;
    public static Pattern p = null;
    public static RandomNumberGenerator gen = null;

    public static String[] splitOnComma(String s, int lineNumber)
    {
        if (s.trim().equals(""))
        {
            return new String[]
                    {
                        ""
                    };
        }
        ArrayList<String> aRet = new ArrayList<String>();
        int startIndex = 0, index = 0;
        char c = 0;
        while (index < s.length())
        {
            c = s.charAt(index);
            if (c == ',')
            {
                aRet.add(s.substring(startIndex, index));
                index++;
                startIndex = index;
                continue;
            }
            if (c == '(')
            {
                int counter = 1;
                int tempIndex = index + 1;
                while (tempIndex < s.length())
                {
                    if (s.charAt(tempIndex) == '(')
                    {
                        counter++;
                    }
                    if (s.charAt(tempIndex) == ')')
                    {
                        counter--;
                    }
                    tempIndex++;
                    if (counter == 0)
                    {
                        index = tempIndex;
                        break;
                    }
                }
                if (counter > 0)
                {
                    System.err.println("Unmatched ( on line " + lineNumber);
                    System.exit(1);
                }
                continue;
            }
            if (c == '[')
            {
                int counter = 1;
                int tempIndex = index + 1;
                while (tempIndex < s.length())
                {
                    if (s.charAt(tempIndex) == '[')
                    {
                        counter++;
                    }
                    if (s.charAt(tempIndex) == ']')
                    {
                        counter--;
                    }
                    tempIndex++;
                    if (counter == 0)
                    {
                        index = tempIndex;
                        break;
                    }
                }
                if (counter > 0)
                {
                    System.err.println("Unmatched [ on line " + lineNumber);
                    System.exit(1);
                }
                continue;
            }
            index++;
        }
        if (startIndex < s.length())
        {
            aRet.add(s.substring(startIndex, s.length()).trim());
        } else
        {
            aRet.add("");
        }
        String[] ret = new String[aRet.size()];
        aRet.toArray(ret);
        return ret;
    }
}
