import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class linked_list {

    static class SinglyLinkedListNode {
        public int data;
        public SinglyLinkedListNode next;

        public SinglyLinkedListNode(int nodeData) {
            this.data = nodeData;
            this.next = null;
        }
    }

    static class SinglyLinkedList {
        public SinglyLinkedListNode head;

        public SinglyLinkedList() {
            this.head = null;
        }

      
    }

    public static void printSinglyLinkedList(SinglyLinkedListNode node, String sep) throws IOException {
        while (node != null) {

            System.out.println(node.data + "\n");

            node = node.next;

        }
    }




    static SinglyLinkedListNode insertNodeAtTail(SinglyLinkedListNode head, int data) {
        SinglyLinkedListNode temp = new SinglyLinkedListNode(data) ;
        SinglyLinkedListNode looper = head , loop = null ;
        while(looper != null){
            loop = looper ;
            looper = looper.next;
        }
        if(loop == null){
            head = temp ;
        }
        else
        loop.next = temp;
        return head;

    }






private static final Scanner scanner = new Scanner(System.in);

public static void main(String[] args) throws IOException {

    SinglyLinkedList llist = new SinglyLinkedList();

    int llistCount = scanner.nextInt();
    scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

    for (int i = 0; i < llistCount; i++) {
        int llistItem = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        
      SinglyLinkedListNode llist_head = insertNodeAtTail(llist.head, llistItem);

      llist.head = llist_head;
    }



    printSinglyLinkedList(llist.head, "\n");

    scanner.close();
}
}