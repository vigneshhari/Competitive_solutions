#include <iostream>

using namespace std;


int c[52];
int numCoins;
long long table[52][252];
int calculated[52][252];
long long solve(int i, int make)
{
    if(make<0) return 0;
    if(make==0)return 1;
    if(i > numCoins) return 0;
    if(calculated[i][make] == 0){ //eliminating overlap
        table[i][make] = solve(i, make - c[i]) + solve(i+1, make);
        calculated[i][make] = 1;
    }
    return table[i][make];
}
int main(){
    
    int make,i,j;
    cin>>make>>numCoins;
    for(i = 0; i< 52; i++)
    for(j = 0; j< 252; j++)
    calculated[i][j] = 0;
    for(i=0;i<=numCoins;i++){
        cin>>c[i];
    }
    cout<<solve(1, make)<<endl;
    return 0;
}