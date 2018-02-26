package brainfuckcompiler.compiler.program.statements;

import brainfuckcompiler.compiler.expressions.ExpressionGenerator;
import brainfuckcompiler.compiler.expressions.Node;
import brainfuckcompiler.compiler.expressions.nodes.AssignmentOperator;
import brainfuckcompiler.compiler.expressions.nodetypes.SubNode;
import brainfuckcompiler.compiler.program.Array;
import brainfuckcompiler.compiler.program.Variable;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.compiler.program.structure.Item;
import brainfuckcompiler.compiler.program.structure.Line;
import brainfuckcompiler.compiler.program.structure.Statement;
import brainfuckcompiler.statics;
import java.util.ArrayList;

public class DeclareStatement extends Statement
{

    Node expression = null;
    String variableName;

    public DeclareStatement(Block parentBlock, int lineNumber)
    {
        super(parentBlock, lineNumber);
    }

    public int parseStatement(ArrayList<Item> items, int currentPosition)
    {
        Line l = (Line) items.get(currentPosition);
        currentPosition++;
        String[] parts = statics.splitOnComma(l.getLine().substring(8), l.getLineNumber());
        if (parts.length == 0)
        {
            System.err.println("Incomplete declare statement at line " + l.getLineNumber());
            System.exit(1);
        }
        if (parts.length > 2)
        {
            System.err.println("Invalid number of arguments in declare statement at line " + l.getLineNumber());
        }
        if (!parts[0].trim().matches("([_a-zA-Z][_0-9a-zA-Z]*)"))
        {
            System.err.println("Invalid variable name at line " + l.getLineNumber());
            System.exit(1);
        }
        variableName = parts[0].trim();
        if (!Statement.isValidVariableName(variableName))
        {
            System.err.println("Invalid variable name at line " + lineNumber);
            System.exit(1);
        }
        if (parts.length == 1)
        {
            return currentPosition;
        }
        expression = ExpressionGenerator.generateExpression(parts[1], l.getLineNumber(), parentBlock);
        if (expression instanceof AssignmentOperator)
        {
            System.err.println("Initializer on line " + l.getLineNumber() + " cannot use an assignment operator");
            System.exit(1);
        }
        return currentPosition;
    }

    @Override
    public void generate()
    {
        if (!nameExists())
        {
            Variable v = new Variable(variableName);
            parentBlock.getVariableScope().add(v);
            if (expression != null)
            {
                if ((expression instanceof SubNode) && (((SubNode) expression).getType() == SubNode.SUB))
                {
                    System.err.println("Cannot use sub in an initializer on line " + lineNumber);
                    System.exit(1);
                }
                int address = expression.generateBF();
                statics.t.move(v.getMemoryPosition(), address);
                statics.t.free(address);
            }
        } else
        {
            System.err.println("Double declaration of variable " + variableName + " at line " + lineNumber);
            System.exit(1);
        }
    }

    private boolean nameExists()
    {
        ArrayList<Variable> variables = parentBlock.getVariableScope();
        for (Variable v : variables)
        {
            if (v.getName().equals(variableName))
            {
                return true;
            }
        }
        ArrayList<Array> arrays = parentBlock.getArrayScope();
        for (Array a : arrays)
        {
            if (a.getName().equals(variableName))
            {
                return true;
            }
        }
        return false;
    }
}
