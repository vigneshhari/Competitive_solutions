package brainfuckcompiler.code.strings;

import brainfuckcompiler.statics;
import java.util.ArrayList;

/**
 *
 * @author vrighter
 */
public class StringTools
{

    static ArrayList<factorPair> factorPairs;

    /**
     *
     * @param s
     * @param t
     */
    public static void printString(String s)
    {
        int address = statics.t.allocContiguous(2);
        statics.t.to(address);
        int prev = 0;
        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);
            generate(prev, c);
            prev = c;
            statics.t.append('.');
        }
        statics.t.clear(address);
        statics.t.freeContiguous(address, 2);
    }

    static void generate(int prev, int c)
    {
        int difference = c - prev;
        if (difference == 0)
        {
            return;
        }
        boolean bigger = c > prev;
        factorPairs = new ArrayList<factorPair>();
        int absDifference = Math.abs(difference);
        for (int i = 2; i < absDifference + 11; i++)
        {
            int rest = absDifference - i;
            int max = i / 2 + 1;
            for (int j = 2; j < max; j++)
            {
                if (i % j == 0)
                {
                    int d = i / j;
                    factorPairs.add(new factorPair(j, d, rest));
                    max = d;
                }
            }
        }
        int shortest = absDifference;
        factorPair fShortest = null;
        for (int i = 0; i < factorPairs.size(); i++)
        {
            factorPair f = (factorPair) factorPairs.get(i);
            int l = f.getLength();
            if (l < shortest)
            {
                shortest = l;
                fShortest = f;
            }
        }
        if (shortest == absDifference)
        {
            outputNoLoop(absDifference, bigger);
        } else
        {
            fShortest.output(bigger);
        }
    }

    static void outputNoLoop(int difference, boolean bigger)
    {
        for (int i = 0; i < difference; i++)
        {
            statics.t.append(bigger ? '+' : '-');
        }
    }
}
