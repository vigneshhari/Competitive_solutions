'''
Our Code Monk recently learnt about Graphs and is very excited!

He went over to the Graph-making factory to watch some freshly prepared graphs. Incidentally, one of the workers at the factory was ill today, so Monk decided to step in and do her job.

The Monk's Job is to Identify whether the incoming graph is a tree or not. He is given N, the number of vertices in the graph and the degree of each vertex.

Find if the graph is a tree or not.

Input:
First line contains an integer N, the number of vertices.
Second line contains N space-separated integers, the degrees of the N vertices.

Output:
Print "Yes" (without the quotes) if the graph is a tree or "No" (without the quotes) otherwise.

Constraints:
1 <= N <= 100
1 <= Degreei <= 1000

References:
Graphs and Trees

SAMPLE INPUT
3
1 2 1
SAMPLE OUTPUT
Yes
Time Limit:

'''


n = int(raw_input())
l = map(int, raw_input().split())
ans = sum(l)
if ans == 2*(n-1):
	print "Yes"
else:
	print "No"