inp = input()
valdict = {}
for _ in range(inp):
  name = raw_input()
  score = input()
  temp = valdict.get(score , [])
  temp.append(name)
  valdict[score] = temp

for i in sorted(valdict[sorted(valdict.keys())[1]]):
  print i


'''

5
Karen
40
Kim
38
Nutan
25
John
25
Paul
20
'''