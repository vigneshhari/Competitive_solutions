package brainfuckcompiler.compiler.program;

import brainfuckcompiler.statics;

public class Array
{

    private int mempos, size;
    private String name;

    public Array(String name, int s)
    {
        size = s * 2 + 5;
        mempos = statics.t.allocContiguous(size);
        this.name = name;
    }

    public String getName()
    {
        return name;
    }

    public void free()
    {
        int amt = (size - 5) / 2;
        statics.t.plus(mempos + 3, amt);
        statics.t.append("[>[>>]+[<<]>-]>[>[-]>]<<[-<<]");
        statics.t.at(mempos + 2);
        statics.t.freeContiguous(mempos, size);
    }

    /**
     * Inserts a value into an array. Frees both pos and val
     *
     * @param pos the array position to insert to
     * @param val the value to insert
     */
    public void set(int pos, int val)
    {
        statics.t.move(mempos + 2, pos);
        statics.t.move(mempos + 1, val);
        statics.t.free(pos, val);
        statics.t.to(mempos);
        statics.t.append(">>[[>>]+[<<]>>-]+[>>]<[-]<[<<]>[>[>>]<+<[<<]>-]>[>>]<<[-<<]");
    }

    /**
     * Gets a value from the array. Assumes the destination cell is 0. Frees pos
     *
     * @param pos The position to extract
     * @param dest The destination cell
     */
    public void get(int pos, int dest)
    {
        statics.t.move(mempos + 2, pos);
        statics.t.free(pos);
        statics.t.to(mempos);
        statics.t.append(">>[[>>]+[<<]>>-]+[>>]<[<[<<]>+<");
        statics.t.inc(dest);
        statics.t.to(mempos);
        statics.t.append(">>[>>]<-]<[<<]>[>[>>]<+<[<<]>-]>[>>]<<[-<<]");
    }
}
