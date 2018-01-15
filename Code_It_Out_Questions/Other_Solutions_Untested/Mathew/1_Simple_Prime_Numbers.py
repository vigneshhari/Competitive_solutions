'''
Question
Today Motu learned a new concept in maths called least prime factor, 
(ie It is the smallest prime divisor of a number), The teacher gave Motu an assignment 
to find all numbers with the same smallest prime factor as a number X upto a limit L
Motu is really lazy and is asking you to solve it for him. Can you take up the challenge ?

Input
The first line takes into account N and L 
N is the number of questions Teacher asked and L is the limit upto which we have to check the numbers
After that N lines follow Each with one input X

Output
Output the number of numbers upto L (Inclusive) with the same least prime factor as the number X (Inclusive)


0 and 1 are not considered as least prime factors and hence excluded from all calculations

Sample Cases

Sample input        |  Sample Output
4 16                |   
3                   |   3
2                   |   8
5                   |   1
10                  |   0

Explanation

For 3 the numbers 3 , 9 , 15 has their least prime divisor as 3
For 2 the numbers 2 , 4 , 6 , 8 , 10 , 12 , 14 , 16 has their least prime divisor as 2
For 5 There is no other number other than 5 
For 10 , 10 itself is not the least prime divisor , hence the answer is 0

Constraints

N <= 100000
L <= 10^7

'''

#Answer in Python 2


X,M = map(int , raw_input().split(" "))


P = [1 for _ in xrange(M+1)]
P[0] , P[1] = 0,0 
i = 2
while i*i <= M :
    if P[i] == 1 :
        for j in xrange(i*i,M+1,i) :
            if P[j] == 1:
                P[j] = 0
                P[i] += 1
    i += 1

for i in range(X):
    num = input()
    print P[num]

