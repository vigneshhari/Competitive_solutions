#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, temp, *arr, i, tempnum;
    scanf("%d", &num);
    arr = (int *)malloc(num * sizeof(int));
    for (i = 0; i < num; i++)
    {
        scanf("%d", arr + i);
    }
    tempnum = num - 1;
    for (i = 0; i < num / 2; i++, tempnum -= 1)
    {
        temp = *(arr + tempnum);
        *(arr + tempnum) = *(arr + i);
        *(arr + i) = temp;
    }

    for (i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}
