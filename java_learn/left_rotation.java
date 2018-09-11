import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class left_rotation {

    private static final Scanner scanner = new Scanner(System.in);


public static void main(String args[]) throws IOException {


    int arrCount = scanner.nextInt();
    int rotations = scanner.nextInt();
    scanner.nextLine();

    String[] arr = scanner.nextLine().split(" ");

    for (int i =0 ; i<arrCount ; i++){
        if(i + rotations >= arrCount){
            System.out.print(arr[rotations - arrCount + i ] + " ");
        }
        else{
            System.out.print(arr[rotations+i] + " ");
        }
    }

    scanner.close();

}

}

/*
5 1
1 2 3 4 5

*/