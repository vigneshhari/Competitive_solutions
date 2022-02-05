
#include<stdio.h>


unsigned long long int recsol(unsigned long long int a,unsigned long long int b,unsigned long long int lev) {
    unsigned long long int time;
    while (a >= 1 && b >= 1) {
        if (a > b && ((a / b) - 1) > 0 )
        {
            time = (a / b) - 1;
            a = (a) - b * ((a / b) - 1);
            lev = time + lev;
        }
        else if(b > a && ((b / a) - 1) > 0 ){
            time = ((b / a)) - 1;
            b = (b) - a * ((b / a) - 1);
            lev =time + lev;
        }
        else{
            if (b > a){
                b = b - a;
                lev = lev + 1;}
            else if (a > b){
                a = a-b;
                lev = lev + 1;}
            else
                return 0;
        }
        if (a == 1 && b == 1)
            return lev;
        if(a <= 0 || b <= 0 )
            return -1;
    }
}

int main(){
    int inp ;
    unsigned long long int data1 , data2 , ans ;
    scanf("%d",&inp) ;
    for(int i=0 ; i < inp ; i++){
        scanf("%llu %llu",&data1,&data2); 
        ans =  recsol(data1,data2,0);
        if(ans == 0){
            printf("impossible\n");
            continue;
        }
    
    printf("%llu\n" , ans);
        
    }
    return 0;
    
}