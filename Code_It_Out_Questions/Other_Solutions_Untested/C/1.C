
#include <stdio.h>

int main()
{
    int X,M,i,num;
    scanf("%d",&X);
    scanf("%d",&M);
    X = 1;
    M = 200;
    //P = [1 for _ in xrange(M+1)]
    int P[M+1];
    for(int x=0; x < M+1; x++)
        P[x] = 1;

    P[0] = 0, P[1] = 0;
    i = 2;
    while(i*i <= M)
    {
        if(P[i] == 1)
        {
            //for j in xrange(i*i,M+1,i)
            for(int j=i*i; j < M+1; j+=i)
            {
                if (P[j] == 1)
                {
                    P[j] = 0;
                    P[i] += 1;
                }
            }
        }
        i += 1;
    }

    for(i=0; i<X; i++)
    {
        scanf("%d",&num);
        printf("%d",P[num]);
    }
    return 0;
}
