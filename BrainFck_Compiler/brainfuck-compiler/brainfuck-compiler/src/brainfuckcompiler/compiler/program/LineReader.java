package brainfuckcompiler.compiler.program;

import brainfuckcompiler.compiler.program.structure.Line;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class LineReader
{

    private BufferedReader r = null;
    private String lastLine = null;
    private boolean open = false;
    private int lineNumber = 0;

    public LineReader(String path)
    {
        try
        {
            r = new BufferedReader(new FileReader(path));
            open = true;
        } catch (IOException ex)
        {
            System.err.println("Could not open file");
            System.exit(1);
        }
    }

    public int getIndentLevel()
    {
        String s = lastLine.trim();
        if ((s.length() == 0) || (s.charAt(0) == '\''))
        {
            return -1;
        }
        int ret = 0;
        for (int i = 0; i < lastLine.length(); i++)
        {
            if (lastLine.charAt(i) == '\t')
            {
                ret++;
            } else
            {
                break;
            }
        }
        return ret;
    }

    public boolean isOpen()
    {
        return open;
    }

    private Line getLastLine()
    {
        return new Line(getIndentLevel(), lastLine.trim(), null, lineNumber);
    }

    public Line readLine()
    {
        if (!open)
        {
            return null;
        }
        try
        {
            lastLine = r.readLine();
            lineNumber++;
            if (lastLine == null)
            {
                closeFile();
                return null;
            } else
            {
                return getLastLine();
            }
        } catch (IOException ex)
        {
            closeFile();
            return null;
        }
    }

    public void closeFile()
    {
        try
        {
            if (r != null)
            {
                r.close();
            }
        } catch (IOException ex)
        {
            System.err.println("Error in closing file");
        }
        open = false;
    }
}
