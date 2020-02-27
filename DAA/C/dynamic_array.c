#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    int size, sum = 0, temp;
    scanf("%d", &size);
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &temp);
        sum += temp;
    }
    printf("%d", sum);
    return 0;
}
