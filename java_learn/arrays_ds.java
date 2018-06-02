import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class arrays_ds {

    private static final Scanner scanner = new Scanner(System.in);


public static void main(String args[]) throws IOException {


    int arrCount = scanner.nextInt();

    scanner.nextLine();

    String[] arr = scanner.nextLine().split(" ");


    String[] revarr = new String[arrCount];

    for (int i = arrCount-1 , j = 0 ; j < arrCount ; i-- , j++){
        revarr[j] = arr[i];

    }

    for (String x : revarr ){
        System.out.print(x + " ");
    } 

    scanner.close();

}

}