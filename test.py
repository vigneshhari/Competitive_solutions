def locate(a, b, c):
    c = c / 2
    r = a - 1
    l = a - 1 - c
    if r == b or l == b:return a
    else:
        if b <= l:return locate(l, b, c)
        else:return locate(r, b, c)

def answer(h, q):
    root = (2 ** h) - 1
    result = []
    for i in range(len(q)):
        if q[i] < root and q[i] >= 1:
            x = locate(root, q[i], root - 1)
            result.append(x)
        else:result.append(-1)
    return result

print answer(5, [19, 14, 28])
