#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    int i, dig, *arr;

    arr = (int *)malloc(10 * sizeof(int));

    char str[1000];

    scanf("%s", &str);

    for (i = 0; i <= strlen(str); i++)
    {
        if (str[i] >= '0' && str[i] <= '9')
        {
            dig = (int)str[i] - '0';
            *(arr + dig) = *(arr + dig) + 1;
        }
    }

    for (int i = 0; i < 10; i++)
    {
        printf("%d ", *(arr + i));
    }

    return 0;
}
