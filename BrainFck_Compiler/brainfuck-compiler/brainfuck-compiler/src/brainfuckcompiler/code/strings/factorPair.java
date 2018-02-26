package brainfuckcompiler.code.strings;

import brainfuckcompiler.statics;

class factorPair
{

    int f1, f2, rest;

    factorPair(int f1, int f2, int rest)
    {
        this.f1 = f1;
        this.f2 = f2;
        this.rest = rest;
    }

    int getLength()
    {
        return 7 + f1 + f2 + Math.abs(rest);
    }

    void output(boolean bigger)
    {
        statics.t.append('>');
        for (int i = 0; i < f1; i++)
        {
            statics.t.append('+');
        }
        statics.t.append("[<");
        char r = bigger ? '+' : '-';
        for (int i = 0; i < f2; i++)
        {
            statics.t.append(r);
        }
        statics.t.append(">-]<");
        r = ((rest < 0 && bigger) || (rest > 0 && (!bigger))) ? '-' : '+';
        rest = Math.abs(rest);
        for (int i = 0; i < rest; i++)
        {
            statics.t.append(r);
        }
    }
}
