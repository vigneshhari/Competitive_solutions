#include<stdio.h>
// #include<conio.h>
void main(){
	int ar[100],size,i,largest,count=0;
	// clrscr();
	scanf("%d",&size);
	for(i=0;i<size;++i){
		scanf("%d",&ar[i]);
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
	printf("%d",count);
	// getch();

}