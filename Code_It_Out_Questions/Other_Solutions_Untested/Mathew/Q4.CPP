#include<iostream.h>
#include<conio.h>

void main()
{
    clrscr();
    int n=1,counter,num;
    while(n)
    {
    cin>>n;
    counter = 0;
    num = long(n);
    while(num > 1){
	if (num % 2 == 0)
	    num = num / 2;
	else if (num == 3 || num % 4 == 1)
	    num -= 1;
	else if (num % 4 == 3)
	    num += 1;
	else
	    break;
	counter += 1;
    }
    cout<<"Ans:"<<counter;
    }
getch();
}