
#include<iostream>
#include<math.h>
using namespace std;

int main()
{
    int y,n;
    //for _ in range(int(input()))
    cin>>y;
    for(int x=0;x<y;x++)
    {
        int num, last_roll;
        cout<<'\n';
        cin>>num;
        last_roll = pow(2,(floor(log2(num))));
        n = (num - (last_roll - 1)) * 2 - 1;
        cout<<n;
    }

    return 0;
}
