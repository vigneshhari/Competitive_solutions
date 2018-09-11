'''

Motu Has Just recieved some amount of money from the bank and as he reaches home he hears news of demonetisation ! 
Given the type of Money Denominations in Existence Show how many different ways he can make change for his money,
Motu is Really desparate for your help ! 

Assume we have infinite amount of Each Denominations

Explanation

If there are 5 avaliable notes now [7,6,3,1,2] if Motu took 3 Rs from Bank he can 
Change it into ( (1,1,1),(2,1),(3) ) So there are 3 ways to change his notes 


Input Format
First Line contains the Money he has With him Followed by the number of denominations of Notes avaliable
Second line contatins all the various denominations that are avaliable

Output Format
Output one number containing the number of possible ways to get change

Constraints

Each Denomination <= 50 
Number of Denominations <= 50
Money He Has <= 250

Sample Cases

Sample input        |  Sample Output
4 4                 |   
8 1 2 3             |   4

'''
// Solution In C++

#include <bits/stdc++.h>

using namespace std;

int c[52];
int numCoins;
long long table[52][252];
bool calculated[52][252];
long long solve(int i, int make)
{
    if(make<0) return 0;
    if(make==0)return 1;
    if(i > numCoins) return 0;
    if(calculated[i][make] == false){ //eliminating overlap
        table[i][make] = solve(i, make - c[i]) + solve(i+1, make);
        calculated[i][make] = true;
    }
    return table[i][make];
}
int main(){

    int make;
    cin>>make>>numCoins;
    for(int i=1;i<=numCoins;i++){
        cin>>c[i];
    }
    cout<<solve(1, make)<<endl;
    return 0;
}



