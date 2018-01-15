#include<iostream.h>
// #include<conio.h>
void main(){
	int ar[100],size,i,largest,count=0;
	// clrscr();
	cin>>size;
	for(i=0;i<size;++i){
		cin>>ar[i];
	}
	largest=ar[0];
	for(i=0;i<size;++i){
		if (ar[i]>largest){
			largest=ar[i];
		}
	}
	for(i=0;i<size;++i){
		if (ar[i] == largest){
			++count;
		}
	}
	cout<<count;
	// getch();

}