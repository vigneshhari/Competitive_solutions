
#include<stdio.h>
#include<math.h>

int main()
{
    int y,n;
    //for _ in range(int(input()))
    scanf("%d",&y);
    for(int x=0;x<y;x++)
    {
	int num, last_roll;
	scanf("%d",&num);
	last_roll = pow(2,floor(log(num)/log(2)));
        n = (num - (last_roll - 1)) * 2 - 1;
        printf("%d",n);
    }

    return 0;
}
