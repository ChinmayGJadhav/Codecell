#include <stdio.h>




int main()
{
    long int sum=0;
    long int sum1,sum2;
    int i;
    for(i=1;i<=200;i++)
    {
        sum+=i;
        if(i==10)
            sum1=sum;
        if(i==100)
            sum2=sum;

    }
    printf("%d \n",sum1);
    printf("%d \n",sum2);
    printf("%d \n",sum+sum1+sum2);



}
