'''
Question
Motu is a skydiver. Every time he jumps off an airplane, he tries to land on one of the highest available buildings in his premises. Given the height of all available buildings in the locality, calculate the number of buildings on which he can land.

Input 
First line contains an integer N denoting the total number of buildings in the area.
The second line contains N space-separated integers, where each integer I denotes the height of the Ith building.

Output
Print the available number of buildings on a new line.


Sample Cases

Sample input  	|	Sample Output
6				|	
3 8 4 1 7 8		|	2

Explanation:
Here the buildings with height 8 has the maximum heights. As there are 2 such buildings, hence it is the answer.

Constraints

1 <= N <= 100
1 <= Height <= 1000

'''

#Answer in Python 3

input()
a=list(map(int,input().split()))
print (a.count(max(a)))
