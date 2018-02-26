package brainfuckcompiler.compiler.expressions.nodes;

import brainfuckcompiler.compiler.expressions.nodetypes.ArrayNode;
import brainfuckcompiler.compiler.expressions.nodetypes.BinaryOperator;
import brainfuckcompiler.compiler.expressions.nodetypes.VariableNode;
import brainfuckcompiler.compiler.program.Array;
import brainfuckcompiler.compiler.program.Variable;
import brainfuckcompiler.compiler.program.structure.Block;
import brainfuckcompiler.statics;

public class AssignmentOperator extends BinaryOperator
{

    public AssignmentOperator(int lineNumber, Block parentBlock)
    {
        super(lineNumber, parentBlock);
    }

    @Override
    public int generateBF()
    {
        if (parentNode != null)
        {
            System.err.println("Assignment operator must be root node of expression tree at line " + lineNumber);
            System.exit(1);
        }
        if (left instanceof VariableNode)
        {
            Variable v = ((VariableNode) left).getVariable();
            int address = right.generateBF();
            statics.t.clear(v.getMemoryPosition());
            statics.t.move(v.getMemoryPosition(), address);
            statics.t.free(address);
        } else if (left instanceof ArrayNode)
        {
            Array a = ((ArrayNode) left).getArray();
            int pos = ((ArrayNode) left).getExpression().generateBF();
            int val = right.generateBF();
            a.set(pos, val);
        } else
        {
            System.err.println("Assignment must be done to an array or a variable at line " + lineNumber);
            System.exit(1);
        }
        return -1;
    }
}
