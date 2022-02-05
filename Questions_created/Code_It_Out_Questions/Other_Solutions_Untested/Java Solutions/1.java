package com.company;

import java.util.Scanner;

public class codeitout {

    public static void main(String[] args) {

    Scanner scan = new Scanner(System.in);
    int X = scan.nextInt();
    int M = scan.nextInt();
    int P[] = new int[M+1];
        scan.nextLine();

        for(int i = 0 ; i <= M ; i++){
            P[i] = 1;
        }
    P[0] = 0;
    P[1] = 0;
    int i = 2;
    while(i*i <= M) {
        if(P[i] == 1) {
            for (int j = i * i; j <= M;j+=i ) {
                if (P[j] == 1) {
                    P[j] = 0;
                    P[i] += 1;
                }}}
        i += 1;
    }

        for(i = 0 ; i < X ; i++){
        System.out.println(P[Integer.parseInt(scan.nextLine())]);
    }

}


}
