package brainfuckcompiler;

import brainfuckcompiler.code.BFStack;
import brainfuckcompiler.code.BrainfuckTools;
import brainfuckcompiler.code.random.RandomNumberGenerator;
import brainfuckcompiler.compiler.expressions.operators.Operators;
import brainfuckcompiler.compiler.program.LineReader;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.compiler.program.structure.Item;
import brainfuckcompiler.compiler.program.structure.Line;
import java.util.ArrayList;

public class Main
{

	public static void main(String[] args)
	{
		int numberOfCells = 1;
		int argspos = 0;
		if (args[argspos].startsWith("-"))
		{
			String s = args[argspos].trim();
			if (s.length() >= 2)
			{
				char c = s.charAt(1);
				switch (c)
				{
					case 'c':
						if (s.length() > 2)
						{
							String s2 = s.substring(2).trim();
							try
							{
								numberOfCells = Integer.parseInt(s2);
								argspos++;
							} catch (NumberFormatException ex)
							{
								System.err.println("Invalid argument: " + args[argspos]);
								System.exit(1);
							}
						} else
						{
							System.err.println("Please specify number of cells in -c switch.\nOptions are:\n\t1 (default)\n\t2\n\t4");
							System.exit(1);
						}
						break;
					default:
				}
			} else
			{
				System.err.println("Invalid argument: " + s);
				System.exit(1);
			}
		}
		if (argspos >= args.length)
		{
			System.err.println("Please enter a filename to compile");
			System.exit(1);
		}
		initializeCompiler();
		Block b = createBlockFromFile(args[argspos]);
		b.generateStatements();
		b.generate();
		BFStack.free();
		statics.gen.free();
		statics.t.to(0);
		BFStack.parseStackCalls();
		switch (numberOfCells)
		{
			case 1:
				output8Bit(statics.t.getB().toString());
				break;
			case 2:
				output16Bit(statics.t.getB().toString());
				break;
			case 4:
				output32Bit(statics.t.getB().toString());
				break;
			default:
				System.err.println("Invalid number of cells specified");
				break;
		}
	}

	private static void initializeCompiler()
	{
		statics.t = new BrainfuckTools(30000);
		statics.ops = new Operators();
		statics.gen = new RandomNumberGenerator();
		statics.ops.createRegex();
	}

	private static Block createBlockFromFile(String path)
	{
		LineReader r = new LineReader(path);
		ArrayList<Item> l = new ArrayList<Item>();
		int startingLineNumber = -1;
		if (r.isOpen())
		{
			Line line;
			while ((line = r.readLine()) != null)
			{
				if (line.getIndentLevel() >= 0)
				{
					l.add(line);
					if (startingLineNumber == -1)
					{
						startingLineNumber = line.getLineNumber();
					}
				}
			}
			r.closeFile();
		}
		return new Block(l, 0, null, startingLineNumber);
	}

	private static void output8Bit(String s)
	{
		int amt = s.length() / 80;
		for (int i = 0; i < amt; i++)
		{
			System.out.println(s.substring(i * 80, (i + 1) * 80));
		}
		if ((amt * 80) < s.length())
		{
			System.out.println(s.substring(amt * 80));
		}
	}

	private static void output16Bit(String s)
	{
		System.out.print(">");
		for (int i = 0; i < s.length(); i++)
		{
			char c = s.charAt(i);
			switch (c)
			{
				case '[':
					System.out.print("[>>+>>>+<<<<<-]>>>>>[<<<<<+>>>>>-]<<<[[-]<<<+>>>]<[>+>>>+<<<<-]>>>>[<<<<+>>>>-]<<<[[-]<<<+>>>]<<<[[-]>");
					break;
				case ']':
					System.out.print("[>>+>>>+<<<<<-]>>>>>[<<<<<+>>>>>-]<<<[[-]<<<+>>>]<[>+>>>+<<<<-]>>>>[<<<<+>>>>-]<<<[[-]<<<+>>>]<<<]>");
					break;
				case '+':
					System.out.print("+[<+>>>+<<-]<[>+<-]+>>>[<<<->>>[-]]<<<[->>+<<]>");
					break;
				case '-':
					System.out.print("[<+>>>+<<-]<[>+<-]+>>>[<<<->>>[-]]<<<[->>-<<]>-");
					break;
				case '<':
					System.out.print("<<<");
					break;
				case '>':
					System.out.print(">>>");
					break;
				default:
					System.out.print(c);
					break;
			}
		}
		System.out.println();
	}

	private static void output32Bit(String s)
	{
		System.out.print(">");
		for (int i = 0; i < s.length(); i++)
		{
			char c = s.charAt(i);
			switch (c)
			{
				case '[':
					System.out.print("[>>>>+>>>>>+<<<<<<<<<-]>>>>>>>>>[<<<<<<<<<+>>>>>>>>>-]<<<<<[[-]<<<<<+>>>>>]<<<[>>>+>>>>>+<<<<<<<<-]>>>>>>>>[<<<<<<<<+>>>>>>>>-]<<<<<[[-]<<<<<+>>>>>]<<[>>+>>>>>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<<<<<[[-]<<<<<+>>>>>]<[>+>>>>>+<<<<<<-]>>>>>>[<<<<<<+>>>>>>-]<<<<<[[-]<<<<<+>>>>>]<<<<<[[-]>");
					break;
				case ']':
					System.out.print("[>>>>+>>>>>+<<<<<<<<<-]>>>>>>>>>[<<<<<<<<<+>>>>>>>>>-]<<<<<[[-]<<<<<+>>>>>]<<<[>>>+>>>>>+<<<<<<<<-]>>>>>>>>[<<<<<<<<+>>>>>>>>-]<<<<<[[-]<<<<<+>>>>>]<<[>>+>>>>>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<<<<<[[-]<<<<<+>>>>>]<[>+>>>>>+<<<<<<-]>>>>>>[<<<<<<+>>>>>>-]<<<<<[[-]<<<<<+>>>>>]<<<<<]>");
					break;
				case '+':
					System.out.print("+[<+>>>>>+<<<<-]<[>+<-]+>>>>>[<<<<<->>>>>[-]]<<<<<[->>+[<<+>>>>>+<<<-]<<[>>+<<-]+>>>>>[<<<<<->>>>>[-]]<<<<<[->>>+[<<<+>>>>>+<<-]<<<[>>>+<<<-]+>>>>>[<<<<<->>>>>[-]]<<<<<[->>>>+<<<<]]]>");
					break;
				case '-':
					System.out.print("[<+>>>>>+<<<<-]<[>+<-]+>>>>>[<<<<<->>>>>[-]]<<<<<[->>[<<+>>>>>+<<<-]<<[>>+<<-]+>>>>>[<<<<<->>>>>[-]]<<<<<[->>>[<<<+>>>>>+<<-]<<<[>>>+<<<-]+>>>>>[<<<<<->>>>>[-]]<<<<<[->>>>-<<<<]>>>-<<<]>>-<<]>-");
					break;
				case '<':
					System.out.print("<<<<<");
					break;
				case '>':
					System.out.print(">>>>>");
					break;
				default:
					System.out.print(c);
					break;
			}
		}
		System.out.println();
	}
}