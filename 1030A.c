#include <stdio.h>
 
int main()
{
    int n,count;
    count = 0;
    scanf("%d",&n);
    int arr[n];
    for (int i=0;i < n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for (int i=0; i<n; i++)
    {
        if (arr[i]== 1)
        {
         count++;
        }
    }
    if (count >= 1)
    {
        printf("HARD");
    }
    else
    {
        printf("EASY");
    }
    return 0;
}