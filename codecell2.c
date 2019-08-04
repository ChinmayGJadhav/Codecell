#include <stdio.h>


int main() {
    int digit,sum=0,ans=0;
    long long n=500,i,cube,ans_1,ans_2;
    for(i=1;i<=n;i++){
        cube=(i*i*i);
        while(cube!=0){
            digit=cube%10;
            sum+=digit;
            cube=cube/10;
        }

        sum=sum%9;
        if(sum%9==0)
            sum=9;
        ans+=sum;
        if(i==5)
        {
            ans_1=ans;

        }
        if(i==500)
            ans_2=ans;
        sum=0;
    }
    printf("%lld %lld \n",ans_1,ans_2);
    printf("%lld",(ans_1+ans_2+29999999997)%1000007);

}
