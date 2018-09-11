'''

Motu Has got a special formula fertilizer for growing plants,
one applying one unit of the fertilizer the plant grows one unit

Motu wants to know how many ways he can plant his plants in such a way that he has atleast two plants and  
-> Two plants should not have same height 
-> Each plant must have increasing heights
-> every unit of the fertilizer has to be used

Given the amount of fertilizer. Find how many ways motu can plant his plants. 

Assuming he has an unlimited supply of plant seeds

Explanation

Given that he has 5 units of fertilizer 

he can plant the plants in the following fasion

|   
|                   |
|                   | |
| |         or      | |   
4 1                 3 2 

Constraint
He can have a maximum of 500 units of fertilizers

Input
It has an input of F , The amount of fertilizer he has

Output
The different number of ways he can plant his plants 

Sample Cases

Sample input        |  Sample Output
                    |   
6                   |   3
7                   |   4
10                  |   9

'''

'''
def answer(n):
    combinations = [[0 for rows in range(n)] for cols in range(n + 1)]

    # If n < 3, there are no possibilities for building the stairwell.
    for first_three in range(3):
        for num in range(first_three, n):
            combinations[first_three][num] = 1

    # For the rest of them, the formula is incremental.
    for num in range(3, n + 1):
        for bot in range(2, n):
            combinations[num][bot] = combinations[num][bot - 1]
            if bot <= num:
                combinations[num][bot] += combinations[num - bot][bot - 1]

    # This index on the matrix should contain our solution to the number of distinct combinations.
    return combinations[n][n - 1]

if __name__ == '__main__':
    # This prints out the results of this function on any value between (including) 3 and 200.
    # It's just for debugging.
    print("Format:\n Number of Bricks --> Distinct Partitions")
    for bricks in range(3, 200):
        print('   ', bricks, " --> ", str(answer(bricks)))

'''


# Alternate solutions


steps = 0

#Grandest Staircase

def memoize(f):

    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

@memoize
def step(num):
    ss=0
    if(num <= 2):return 0
    if(num < 5):return 1
    for i in range(num-1,0,-1):
        if ((num - i) > i  ):ss = ss + smallsteps(i,num-i);continue
        elif(i == (num - i)):pass
        else:ss += 1
        temp = step(num - i)
        ss = ss + temp
    return ss

def natsum(n):return ((n*(n+1))/2)

@memoize
def smallsteps(num,lim):
    sum = 0
    if(natsum(num-1) < lim):return 0
    for i in range(num - 1 , 0 , -1):
        if(i > lim):continue
        nlim = lim - i
        if(nlim == 0):sum = sum + 1
        else:sum = sum + smallsteps(i,nlim)
    return sum

print(step(int(input())))
