import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class d2_array {

    private static final Scanner scanner = new Scanner(System.in);
    static int hourglassval;

public static void main(String args[]) throws IOException {

    int array[][] = new int[6][6] ;

    for (int i =0 ; i < 6 ; i++){
        String values[] = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int j = 0 ;j < 6 ; j++ ){
            array[i][j] = Integer.parseInt(values[j]);
        }
    }

    int max_val = Integer.MIN_VALUE ;

    for (int i=0 ;i <6;i++){

        for(int j=0 ; j<6 ;j++){

            try {
                hourglassval = array[i][j] + array[i][j+1] + array[i][j+2] + array[i+1][j+1] + array[i+2][j] + array[i+2][j+1] + array[i+2][j+2] ;
                if(hourglassval > max_val) max_val = hourglassval;

            } catch (Exception e) {
                hourglassval = 0;
            }

        }
    }

    System.out.print(max_val);

    scanner.close();

}

}