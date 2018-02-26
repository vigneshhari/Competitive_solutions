package brainfuckcompiler.code;

import brainfuckcompiler.statics;

public class BFStack
{
    
    public static void parseStackCalls()
    {
        StringBuffer b = statics.t.getB();
        statics.t.setB(new StringBuffer());
        for (int i = 0; i < b.length(); i++)
        {
            char c = b.charAt(i);
            if ((c != '.') && (c != ',') && (c != '+') && (c != '-') && (c != '<') && (c != '>') && (c != '[') && (c != ']') && (c != '#'))
            {
                int op = c;
                int st = i + 1;
                String params = null;
                for (int j = st; j < b.length(); j++)
                {
                    c = b.charAt(j);
                    if (c == 'e')
                    {
                        params = b.substring(i + 1, j);
                        i = j;
                        break;
                    }
                }
                switch (op)
                {
                    case 's':
                        push(params);
                        break;
                    case 'l':
                        pop(params);
                        break;
                    case 'c':
                        clearPop(params);
                        break;
                }
            } else
            {
                statics.t.append(c);
            }
        }
    }
    
    private static void push(String params)
    {
        int cpos = Integer.parseInt(params);
        statics.t.at(cpos);
        int stackPosition = statics.t.getLargestMemorylocation() + 1;
        statics.t.move(stackPosition + 1, cpos);
        statics.t.to(stackPosition + 1);
        statics.t.append(">[>>]+[<<]>[>[>>]<+<[<<]>-]");
        statics.t.to(cpos);
    }
    
    private static void pop(String params)
    {
        int cpos = Integer.parseInt(params);
        statics.t.at(cpos);
        int stackPosition = statics.t.getLargestMemorylocation() + 1;
        statics.t.to(stackPosition + 2);
        statics.t.append("[>>]<[<[<<]");
        statics.t.at(stackPosition);
        statics.t.plus(cpos, 1);
        statics.t.to(stackPosition + 2);
        statics.t.append("[>>]<-]<-<<[<<]");
        statics.t.at(stackPosition);
        statics.t.to(cpos);
    }
    
    private static void clearPop(String params)
    {
        statics.t.append("#");
        int cpos = Integer.parseInt(params);
        statics.t.at(cpos);
        int stackPosition = statics.t.getLargestMemorylocation() + 1;
        statics.t.to(stackPosition + 2);
        statics.t.append("[>>]<[-]<-<<[<<]");
        statics.t.at(stackPosition);
        statics.t.to(cpos);
    }
    
    public static void free()
    {
        int stackPosition = statics.t.getLargestMemorylocation() + 1;
        statics.t.to(stackPosition + 2);
        statics.t.append("[>[-]>]<<[-<<]");
        statics.t.at(stackPosition);
    }
}
