#include<iostream>
using namespace std;

int answer(int n)
{
    int combinations[n][n+1];
    //combinations = [[0 for rows in range(n)] for cols in range(n + 1)]
    for(int rows=0; rows < n; rows++)
    {
        for (int cols=0; cols < n+1; cols++)
        {
            combinations[rows][cols] = 0;
        }
    }

    // If n < 3, there are no possibilities for building the stairwell.
    //for first_three in range(3)
    for(int first_three=0; first_three < 3; first_three++)
    {
        for(int num=first_three; num < n; num++)
            combinations[first_three][num] = 1;
    }

    // For the rest of them, the formula is incremental.
    //for num in range(3, n + 1):
    for(int num=3; num < n+1; num++)
    {
        for(int bot=2; bot <n; bot++)
        {
            combinations[num][bot] = combinations[num][bot - 1];
            if(bot <= num)
                combinations[num][bot] += combinations[num - bot][bot - 1];
        }
    }
    // This index on the matrix should contain our solution to the number of distinct combinations.
    return combinations[n][n - 1];
}

int main()
{
    int bricks;
    cout<<"Format:\n Number of Bricks --> Distinct Partitions\n";
    //for bricks in range(3, 200):
    cin>>bricks;
    cout<<"   "<<bricks<<" --> "<<answer(bricks);
    return 0;
}
