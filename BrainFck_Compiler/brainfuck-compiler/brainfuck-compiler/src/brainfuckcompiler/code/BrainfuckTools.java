package brainfuckcompiler.code;

/**
 *
 * @author vrighter
 */
public class BrainfuckTools
{

    private boolean[] memory;
    private int pointer, startmemorysearch, largestmemorylocation;
    private StringBuffer b;

    /**
     * Creates a new BrainfuckTools object and initializes the memory manager
     *
     * @param memory The amount of memory in cells
     */
    public BrainfuckTools(int memory)
    {
        this.memory = new boolean[memory];
        pointer = 0;
        startmemorysearch = 0;
        largestmemorylocation = -1;
        this.b = new StringBuffer();
    }

    public int getPointer()
    {
        return pointer;
    }

    public void setB(StringBuffer b)
    {
        this.b = b;
    }

    /**
     *
     * @return
     */
    public StringBuffer getB()
    {
        return b;
    }

    /**
     * Set the current memory location. Used when literal code is added using
     * unbalanced loops
     *
     * @param p The current memory location
     */
    public void at(int p)
    {
        pointer = p;
    }

    /**
     * Moves the pointer to the specified location. Pointer ends at p.
     *
     * @param p The address to move the pointer to
     */
    public void to(int p)
    {
        int diff = Math.abs(pointer - p);
        if (p == pointer)
        {
            return;
        }
        if (p > pointer)
        {
            for (int i = 0; i < diff; i++)
            {
                b.append('>');
            }
        } else
        {
            for (int i = 0; i < diff; i++)
            {
                b.append('<');
            }
        }
        pointer = p;
    }

    /**
     * Free addresses in memory
     *
     * @param addresses The addresses to mark as free
     */
    public void free(int... addresses)
    {
        for (int i = 0; i < addresses.length; i++)
        {
            memory[addresses[i]] = false;
            if (addresses[i] < startmemorysearch)
            {
                startmemorysearch = addresses[i];
            }
        }
    }

    /**
     * Free a block of memory
     *
     * @param address The starting address of the block
     * @param amt The size of the block
     */
    public void freeContiguous(int address, int amt)
    {
        for (int i = 0; i < amt; i++)
        {
            free(address + i);
        }
    }

    /**
     * Allocates a cell of memory
     *
     * @return The address of the allocated cell or -1 if the memory is full
     */
    public int alloc()
    {
        for (int i = startmemorysearch; i < memory.length; i++)
        {
            if (!memory[i])
            {
                memory[i] = true;
                startmemorysearch = i + 1;
                if (i > largestmemorylocation)
                {
                    largestmemorylocation = i;
                }
                return i;
            }
        }
        return -1;
    }

    /**
     * Allocate a number of cells of memory. The cells may not necessarily be
     * contiguous
     *
     * @param amt The number of cells to allocate
     * @return An array containing the allocated addresses
     */
    public int[] alloc(int amt)
    {
        int[] ret = new int[amt];
        for (int i = 0; i < amt; i++)
        {
            ret[i] = alloc();
        }
        return ret;
    }

    /**
     * Allocates a block of contiguous memory
     *
     * @param amt The size of the block required
     * @return the starting address of the block or -1 if none can be found
     */
    public int allocContiguous(int amt)
    {
        for (int i = startmemorysearch; i < memory.length; i++)
        {
            boolean found = true;
            for (int j = 0; j < amt; j++)
            {
                if (memory[i + j])
                {
                    found = false;
                    break;
                }
            }
            if (!found)
            {
                continue;
            }
            for (int j = 0; j < amt; j++)
            {
                memory[i + j] = true;
                if ((i + j) > largestmemorylocation)
                {
                    largestmemorylocation = i + j;
                }
            }
            return i;
        }
        return -1;
    }

    public int getLargestMemorylocation()
    {
        return largestmemorylocation;
    }

    /**
     * Adds n to the current cell
     *
     * @param n The amount to add
     */
    public void plus(int n)
    {
        for (int i = 0; i < n; i++)
        {
            b.append('+');
        }
    }

    /**
     * Adds a specified amount to a particular cell<br>Pointer ends at address
     *
     * @param address The cell to add to.
     * @param n The amount to add
     */
    public void plus(int address, int n)
    {
        to(address);
        for (int i = 0; i < n; i++)
        {
            b.append('+');
        }
    }

    /**
     * Subtracts a specified amount from the current cell
     *
     * @param n the amount to subtract
     */
    public void minus(int n)
    {
        for (int i = 0; i < n; i++)
        {
            b.append('-');
        }
    }

    /**
     * Subtracts a specified amount from address<br>Pointer ends at address
     *
     * @param address The address from which to subtract
     * @param n The amount to subtract
     */
    public void minus(int address, int n)
    {
        to(address);
        for (int i = 0; i < n; i++)
        {
            b.append('-');
        }
    }

    /**
     * Creates a cell with a boolean value of 1 if the value at address is not 0
     * <br>The address is freed
     *
     * @param address The address to process
     * @return a new address with a boolean value
     */
    public int toBoolean(int address)
    {
        int temp = alloc();
        loop(address);
        inc(temp);
        celoop(address);
        free(address);
        return temp;
    }

    /**
     * set a value to address<br>pointer ends at address
     *
     * @param address the address in which to store the value
     * @param val the integer value to set
     */
    public void set(int address, int val)
    {
        clear(address);
        plus(val);
    }

    /**
     * moves the value in y into x<br>assumes x is blank<br>pointer ends at y
     *
     * @param x address to move to
     * @param y address of value to move
     */
    public void move(int x, int y)
    {
        loop(y);
        inc(x);
        deloop(y);
    }

    /**
     * copies y to a new memory location and returns the copy's
     * address<br>pointer ends at a freed cell
     *
     * @param y the value to copy
     * @return the address of the copy
     */
    public int copy(int y)
    {
        int x = alloc(), temp0 = alloc();
        loop(y);
        inc(x);
        inc(temp0);
        deloop(y);
        loop(temp0);
        inc(y);
        deloop(temp0);
        free(temp0);
        return x;
    }

    //copies y into x
    //returns x
    /**
     *
     * @param x
     * @param y
     * @return
     */
    public int copy(int x, int y)
    {
        int temp0 = alloc();
        loop(y);
        inc(x);
        inc(temp0);
        deloop(y);
        loop(temp0);
        inc(y);
        deloop(temp0);
        free(temp0);
        return x;
    }

    //copies y into x using temp0 as the temporary variable
    //assumes temp0 is cleared
    //returns x
    /**
     *
     * @param x
     * @param y
     * @param temp0
     * @return
     */
    public int copy(int x, int y, int temp0)
    {
        loop(y);
        inc(x);
        inc(temp0);
        deloop(y);
        loop(temp0);
        inc(y);
        deloop(temp0);
        return x;
    }

    //clears the cell at address
    /**
     *
     * @param address
     */
    public void clear(int address)
    {
        to(address);
        b.append("[-]");
    }

    //adds a character to the output stream
    /**
     *
     * @param c
     */
    public void append(char c)
    {
        b.append(c);
    }

    //adds a string to the output stream
    /**
     *
     * @param c
     */
    public void append(String c)
    {
        b.append(c);
    }

    //increments the cell at address
    //pointer ends at address
    /**
     *
     * @param address
     */
    public void inc(int address)
    {
        to(address);
        b.append('+');
    }

    //decrements the cell at address
    //pointer ends at address
    /**
     *
     * @param address
     */
    public void dec(int address)
    {
        to(address);
        b.append('-');
    }

    //starts a loop at the current memory location
    /**
     *
     */
    public void loop()
    {
        b.append('[');
    }

    /**
     *
     * @param address
     */
    public void loop(int address)
    {
        to(address);
        b.append('[');
    }

    /**
     *
     */
    public void eloop()
    {
        b.append(']');
    }

    /**
     *
     * @param n
     */
    public void teloop(int n)
    {
        to(n);
        b.append(']');
    }

    /**
     *
     * @param n
     */
    public void deloop(int n)
    {
        dec(n);
        b.append(']');
    }

    /**
     *
     * @param n
     */
    public void celoop(int n)
    {
        clear(n);
        b.append(']');
    }

    /**
     *
     * @param address
     */
    public void one(int address)
    {
        clear(address);
        b.append('+');
    }

    /**
     *
     * @param left
     * @param right
     * @return
     */
    public int add(int left, int right)
    {
        loop(right);
        inc(left);
        deloop(right);
        return left;
    }

    /**
     *
     * @param left
     * @param right
     * @return
     */
    public int subtract(int left, int right)
    {
        loop(right);
        dec(left);
        deloop(right);
        return left;
    }

    /**
     *
     * @param x
     * @param y
     * @return
     */
    public int multiply(int x, int y)
    {
        int[] temp = alloc(2);
        loop(x);
        inc(temp[1]);
        deloop(x);
        loop(temp[1]);
        loop(y);
        inc(x);
        inc(temp[0]);
        deloop(y);
        loop(temp[0]);
        inc(y);
        deloop(temp[0]);
        deloop(temp[1]);
        free(temp);
        return x;
    }

    public int divide(int x, int y)
    {
        int[] temp = alloc(4);
        move(temp[0], x);
        loop(temp[0]);
        copy(temp[1], y, temp[2]);
        loop(temp[1]);
        inc(temp[2]);
        dec(temp[0]);
        loop(temp[0]);
        clear(temp[2]);
        inc(temp[3]);
        deloop(temp[0]);
        loop(temp[3]);
        inc(temp[0]);
        deloop(temp[3]);
        loop(temp[2]);
        dec(temp[1]);
        loop(temp[1]);
        dec(x);
        celoop(temp[1]);
        inc(temp[1]);
        deloop(temp[2]);
        deloop(temp[1]);
        inc(x);
        teloop(temp[0]);
        free(temp);
        return x;
    }

    /**
     *
     * @param x
     * @param y
     * @return
     */
    public int mod(int x, int y)
    {
        int temp = copy(x);
        divide(temp, y);
        multiply(temp, y);
        subtract(x, temp);
        free(temp);
        return x;
    }

    /**
     *
     * @param x
     * @param y
     * @return
     */
    public int equal(int x, int y)
    {
        int[] temp = alloc(2);
        loop(x);
        inc(temp[1]);
        deloop(x);
        append('+');
        loop(y);
        dec(temp[1]);
        inc(temp[0]);
        deloop(y);
        loop(temp[0]);
        inc(y);
        deloop(temp[0]);
        loop(temp[1]);
        dec(x);
        celoop(temp[1]);
        free(temp);
        return x;
    }

    /**
     *
     * @param x
     * @param y
     * @return
     */
    public int notequal(int x, int y)
    {
        int[] temp = alloc(2);
        loop(x);
        inc(temp[1]);
        deloop(x);
        loop(y);
        dec(temp[1]);
        inc(temp[0]);
        deloop(y);
        loop(temp[0]);
        inc(y);
        deloop(temp[0]);
        loop(temp[1]);
        inc(x);
        celoop(temp[1]);
        free(temp);
        return x;
    }

    /**
     *
     * @param x
     * @return
     */
    public int not(int x)
    {
        int temp = alloc();
        loop(x);
        inc(temp);
        celoop(x);
        append('+');
        loop(temp);
        dec(x);
        deloop(temp);
        free(temp);
        return x;
    }

    /**
     *
     * @param x
     * @param y
     * @return
     */
    public int and(int x, int y)
    {
        int[] temp = alloc(2);
        loop(x);
        inc(temp[1]);
        deloop(x);
        loop(temp[1]);
        clear(temp[1]);
        loop(y);
        inc(temp[1]);
        inc(temp[0]);
        deloop(y);
        loop(temp[0]);
        inc(y);
        deloop(temp[0]);
        loop(temp[1]);
        inc(x);
        celoop(temp[1]);
        eloop();
        free(temp);
        return x;
    }

    /**
     *
     * @param x
     * @param y
     * @return
     */
    public int or(int x, int y)
    {
        int temp = alloc();
        loop(x);
        inc(temp);
        celoop(x);
        loop(y);
        one(temp);
        celoop(y);
        free(x, y);
        return temp;
    }

    /**
     *
     * @param x
     * @param y
     * @return
     */
    public int smallerthan(int x, int y)
    {
        int temp0 = alloc();
        int temp1 = allocContiguous(3);
        inc(temp1 + 1);
        loop(y);
        inc(temp0);
        inc(temp1);
        deloop(y);
        loop(temp0);
        inc(y);
        deloop(temp0);
        loop(x);
        inc(temp0);
        dec(x);
        append("]+");
        loop(temp1);
        append(">-]>[<");
        dec(x);
        clear(temp0);
        to(temp1);
        append(">->]<+<");
        loop(temp0);
        dec(temp1);
        append("[>-]>[<");
        dec(x);
        one(temp0);
        to(temp1);
        append(">->]<+<");
        deloop(temp0);
        clear(temp1);
        clear(temp1 + 1);
        free(temp0);
        freeContiguous(temp1, 3);
        return x;
    }

    /**
     *
     * @param x
     * @param y
     * @return
     */
    public int smallerthanorequal(int x, int y)
    {
        int temp0 = alloc();
        int temp1 = allocContiguous(3);
        to(temp1);
        append(">+<");
        loop(y);
        inc(temp0);
        inc(temp1);
        deloop(y);
        loop(temp1);
        inc(y);
        deloop(temp1);
        loop(x);
        inc(temp1);
        deloop(x);
        loop(temp1);
        append(">-]>[<");
        inc(x);
        clear(temp0);
        to(temp1);
        append(">->]<+<");
        loop(temp0);
        dec(temp1);
        append("[>-]>[<");
        inc(x);
        one(temp0);
        to(temp1);
        append(">->]<+<");
        deloop(temp0);
        clear(temp1);
        clear(temp1 + 1);
        free(temp0);
        freeContiguous(temp1, 3);
        return x;
    }

    /**
     *
     * @param x
     * @param y
     * @return
     */
    public int pow(int x, int y)
    {
        int z = alloc();
        int t = allocContiguous(5);
        free(z);
        move(t, x);
        copy(t + 1, y);
        to(t);
        b.append(">>+<[->[-<<[->>>+>+<<<<]>>>>[-<<<<+>>>>]<<]>[-<+>]<<]<");
        move(x, t + 2);
        clear(t);
        freeContiguous(t, 5);
        return x;
    }
}
