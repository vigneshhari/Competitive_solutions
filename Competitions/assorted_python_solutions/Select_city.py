'''
James has decided to take a break from his work. He makes a plan to visit India for a few days with his family. He knows a lot about India, and also about the various cities he could visit. He decides to write down all the cities on a paper. Let the number of cities be n. Now, he shows the list to his wife and asks her, the city/cities she wants to visit. He tells her that she can select any city/cities and any number of cities. The wife says, she needs a day to decide.

After this, James calls his son and tells him all about the trip, and the list of cities. He gives him a task and asks him, the number of ways the city/cities can be chosen from the list, if the total number of cities written on the list is n. The cities are numbered from 1 to n. At least 1 city has to be selected.

He now asks your help to find the answer for the question that was asked to him. 
The problem consists of a number of test cases.

INPUT:
The first line of input contains the number of test cases t.
Then t lines follow, each contains a number n, the number of cities.

OUTPUT:
Output contains t lines; each line contains the answer for that test case. As the answer can be large, print the answer modulo 10^9+7

CONSTRAINTS
1<=t<=100000
1<=n<=1012

Tester:
SAMPLE INPUT 
2
2
1
SAMPLE OUTPUT 
3
1
Explanation
For test case 1: The only ways to select the cities is 1 2 1 2 Therefore the answer is 3.

For test case 2: The only way to select a city is 1 Therefore the answer is 1.

Source : Hacker Earth

'''

def find(num):
    return (2 ** num - 1) % 10**9+7
for loop in range(input()):
    print find(input())
