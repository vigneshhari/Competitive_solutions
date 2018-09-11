from UnionSize import Size_Set

test = Size_Set(6)
print test.ds
test.Union(0,1)
print test.ds
test.Union(1,2)
print test.ds
test.Union(5,6)
print test.ds
for i in range(7):
    print i , test.Find(i)