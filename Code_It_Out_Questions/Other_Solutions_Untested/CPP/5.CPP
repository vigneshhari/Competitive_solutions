
#include <iostream>

using namespace std;

unsigned long long int array[501], list[501][501];

unsigned long long int natsum(unsigned long long int n){
    return ((n*(n+1))/2);
}

unsigned long long int smallsteps(unsigned long long int num,unsigned long long int lim){
    if(list[num][lim] != 0)return list[num][lim]; 
    unsigned long long int sum = 0, nlim,i;
    if(natsum(num-1) < lim) return 0;
    for (i=num-1; i>0; i--){
        if(i > lim){ continue;}
        nlim = lim - i;
        if(nlim == 0){ sum = sum + 1;}
        else sum = sum + smallsteps(i,nlim);
    }
    list[num][lim] = sum;
    return sum;
}

unsigned long long int step(unsigned long long int num) {
    
    if(array[num] != 0)return array[num];
    unsigned long long int ss=0,i,temp;
    if(num <= 2) return 0;
    if(num < 5) return 1;
    for (i=num-1;i>0;i--){
        
        if ((num - i) > i ){
            ss = ss + smallsteps(i,num-i);continue;
        }
        else if(i == (num - i))
        {}
        else{
            ss += 1;}
            temp = step(num - i);
            ss = ss + temp;
    }
    array[num] = ss;
    return ss;
}

int main()
{
    for(int i =0; i<501; i++) 
    {array[i] = 0;
    for(int j =0; j<501; j++) {
        list[i][j] = 0;
    }
    }
    cout<<step(500);
    return 0;
}