'''

Motu was called in for an emergency at the hospital. 
A Disease is spereading and only Motu can solve it

He is given with a bacteria count of a person and he has to reuce the bacteria count to zero in the most minimun no of steps

The hospital has 3 methods to control the count of the bacteria

1) They can use their advanced machines to remove one Bacteria
2) They can use their bacteria Inserter to insert one Bacteria
3) They have a speical prototype machine which can exactly divide the number of bacteria into two . (since its a prototype machine only even number of bacteria can be divided using this method)

Motu cannot handle all the cases at the hospial so he is asking for your help ! Can you help Him ?

You will be given a Bacteria count as input , You have to find the least no of steps to reduce the number of bacteria to 0 with the provided 3 methods in the hospital

For example:

Given Input 4 :> 
4 --> 2 --> 1 --> 0
In 3 steps we can reduce to 0 hence the answer is 0

Given Input 15 :> 
15 --> 16 --> 8 --> 4 --> 2 --> 1 --> 0
We can reduce to 0 in 6 steps hence 6 is the answer

Since the bacteria is spreading quickly you can expect bacteria count upto 10^19 . So Use Large datatypes to input data and handle it.

Input
The first line takes into account N  
N is the number of Test Cases that follow
After that N lines contain the bacteria count for each test case

Output
Output the number of steps required to reduce the bacteria count to 0 with the methods given in the questions

Sample Cases

Sample input        |  Sample Output
4                   |   
4                   |   3
5                   |   4
15                  |   6
20                  |   6


'''

def answer(n):
    counter = 0
    num = long(n)
    while(num > 1):
        if num % 2 == 0:
            num = num / 2
        elif num == 3 or num % 4 == 1:
            num -= 1
        elif num % 4 == 3 :
            num += 1
        else:
            break
        counter += 1
    return counter + 1

for i in range(input()):
    print answer(input())