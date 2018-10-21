
stack1 = []
stack2 = []

s1 = []
s2 = []

done = False

def findperfect(brackets,seq):
    if(brackets == []):return seq
    if(brackets[0] == ")" ):
        if(stack1[0] == "("):
            stack1.pop()
            s1.append(")")
            seq.append("1")
            findperfect(brackets[1:],seq)
        if(stack2[0] == "("):
            stack2.pop()
            s2.append(")")
            seq.append("2")
            findperfect(brackets[1:],seq)
        return -1

    if(brackets[0] == "]" ):
        if(stack1[0] == "["):
            stack1.pop()
            s1.append("]")
            seq.append("1")
            findperfect(brackets[1:],seq)
        if(stack2[0] == "["):
            stack2.pop()
            s2.append("]")
            seq.append("2")
            findperfect(brackets[1:],seq)
        return -1

    if(brackets[0] == "("):
        stack1.append("(")
        s2.append("1")
        seq.append("1")
        findperfect(brackets[1:],seq)
        stack1.pop()
        s2.pop()
        seq.pop()

# Incomplete
