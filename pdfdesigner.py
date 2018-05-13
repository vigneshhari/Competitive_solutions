mapper = map(int , raw_input().split())
letters = "abcdefghijklmnopqrstuvwxyz"
inp = raw_input()
print max([mapper[letters.index(i)] for i in inp ]) * len(inp)
