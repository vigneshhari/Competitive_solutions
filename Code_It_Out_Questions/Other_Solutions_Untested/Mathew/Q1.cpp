//
// Created by Mathew Alex on 05-01-2018.
//


#include<iostream.h>
#include<conio.h>
void main()
{
    int X,M,*P, i,j,num;
    cin>>X>>M;

    P = new int[M+1];
    P[0]= P[1]= 0;
    for(int _=2; _<=M; _++)
        P[_]= 1;
    i=2;
    while(i*i <=M)
    {
        if(P[i] ==1)
            for(j= i*i; j<M+1; j+=i)
                if(P[j]== 1)
                {
                    P[j]= 0;
                    P[i]+=1;
                }
        i+= 1;
    }

    for(i=0;i<X;i++)
    {
        cin>>num;
        cout<<P[num]<<"\n";
    }
    getch();
}
