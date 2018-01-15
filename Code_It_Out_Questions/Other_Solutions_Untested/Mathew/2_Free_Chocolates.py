'''
Motu visits a new chocolate shop in the town called BioChocolates . Its run by a Biology professor called Damu
Damu makes chocolates using uses special type of organic cells.

Damu agress to give Motu Free chocolates if he solves his problem.

Damu has two types of Cells A and B
The cells are highly active so in one step either Every cell from A regenerates and moves to B. Or Every cell from B regenerates and moves to A

For Example if you had 3 Cells of Type A and 2 Cells of Type B
Either you get 5 Cells of type A and 2 Cells of Type B
or You get 3 Cells of Type A and 5 Cells of Type B
Motu has to find the least number of steps it takes for one cell of type A and B to reach a given number of Cells

Example

if we have to reach 4,7
Initially we have A = 1 and B = 1while workwhile workingwhile workinging
After step 1 we have A = 1 and B = 2 ( A goes to B )
After step 2 we have A = 1 and B = 3 ( A goes to B )
After step 3 we have A = 4 and B = 3 ( B goes to A )
After step 4 we have A = 4 and B = 7 ( A goes to B )
So in 4 steps we reach required cell count

Input
The first line contains the number of test cases
The next line consists of the required cell counts of Cell A followed by required cell counts of Cell B

Output
Output one line containing the number of steps required to reach the required cell count from initial condition ( Initially Both Cell Counts are 1)
If a particular cell count cannot be achived Print "impossible"

Sample input        |  Sample Output
4                   |   
2 1                 |   1
4 7                 |   4
2 4                 |   impossible
4 2                 |   impossible

Constraints

N < 100000
M,F > 0
M,F < 10^50 

*You might wanna consider using large variable datatypes to avoid overflow errors and other issues*

'''

#Python 2

def recsol(a,b,lev):
    if (a <= 0 or b <= 0): return
    if (a == 1 and b == 1): return lev
    if(a > b and (( a / b ) -1) > 0 ):
        time = (a / b) -1
        a = a - b * ((a / b) - 1)
        return recsol(a, b, time + lev)
    elif(b> a and (( b / a ) -1) > 0 ):
        time = (( b / a ) ) -1
        b = b - a * (( b / a ) - 1)
        return recsol(a, b,time + lev)
    return recsol(a-b,b,lev+1) or recsol(a,b-a,lev+1)

inp = input()
for i in range(inp):
    M , F = map(int , raw_input("").split(" "))
    if(M > 10 ** 50 or F > 10 ** 50 or M < 0 or F < 0):print "-1"
    val = recsol(M,F,0)
    if(val == None):print "impossible"
    else: print val