'''

Motu wants to play a game with his friends.
All of his play a new game where every player is named numbers from 1 and are made to stand in a circle,
And from player 1 they would shout numbers from 1 .. if its a multiple of 2 they are removed from the game. the game continues the cyle (last one left --> first one left)
The last player standing wins the game

Motu wants to know where he has to stand to win. You are asked to find the position he has to stand given the number of players

Input Format
The first line indicates N the number of test cases.
N test cases follow the first Line Each with the Number of Players (P)

Constraints
1 ≤ P ≤ 100000

1 ≤ N < 10000

Output Format
The position That will win has to be outputted for each test case

Sample input        |  Sample Output
4                   |   
2                   |   1
3                   |   3
4                   |   1
6                   |   5


Explanation
There are four test cases in the input.

With 6 Players,  First Player Yells 1 , Second Player Yells 2 and he is removed , Third Player Yells 3 , Fourth Player Yells 4 and he is removed , 
5th Player yells 5 , 6th Player Yells 6 and is removed , 1st player yells 7 , 3rd player yells 8 and is removed , 5th player yells 9 , 
1st player yells 10 and is removed
Only 5th player Remains

With 5 Players, First Player Yells 1 , Second Player Yells 2 and he is removed , Third Player Yells 3 , Fourth Player Yells 4 and he is removed , 
5th Player yells 5, First Player Yells 6 and is removed, Third player yells 7 , 5th Player yells 8 anb is removed , 
Only Third Player remains and he wins the game

'''


#Solution for python 3 Py3

for _ in range(int(input())):
    num = int(input())
    last_roll = 2 ** (num.bit_length() - 1)
    n = (num - (last_roll - 1)) * 2 - 1
    print(n)

