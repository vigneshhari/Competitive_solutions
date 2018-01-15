#include<iostream>
using namespace std;

int main()
{
    string n;
    int counter=0,num;
    cin>>num;
    while(num > 1)
    {
        if(num % 2 == 0)
            num = num / 2;
        else if(num == 3 || num % 4 == 1)
            num -= 1;
        else if(num % 4 == 3)
            num += 1;
        else
            break;
        counter += 1;
    }
    cout<<counter;
    return 0;
}
