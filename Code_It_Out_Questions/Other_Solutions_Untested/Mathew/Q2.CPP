#include <iostream>

using namespace std;

unsigned long long int recsol(unsigned long long int a,unsigned long long int b,unsigned long long int lev) {
    unsigned long long int time;
    while (a >= 1 && b >= 1) {
	cout<<a<<' '<<b<<"\n";
	if (a > b && ((a / b) - 1) > 0 )
	{
	    time = (a / b) - 1;
	    a = a - b * ((a / b) - 1);
	    lev = time + lev;
	}
	else if(b > a && ((b / a) - 1) > 0 ){
	    time = ((b / a)) - 1;
	    b = b - a * ((b / a) - 1);
	    lev =time + lev;
	}
	else{
	    if (b-a > 0)
		b = b - a;
	    else if (a-b > 0)
		a = a-b;
	}
	if (a == 1 && b == 1)
	    return lev;
	if(a <0 || b < 0 )

	    return -1;
    }
}

int main(){
    cout<<recsol(1,12345678912345678999,0);
}