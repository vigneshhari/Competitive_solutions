#include <stdio.h>

struct Node
{
    int data;
    struct Node *next;
};


struct Node* add_num(int num,struct Node* Pointer) {
    struct Node* new_element = malloc(sizeof(struct Node));
    new_element -> data = num;
    new_element -> next = NULL;
    Pointer -> next = new_element;
    return new_element;

}

void print_list(struct Node* Head ) {
    printf("\nPrinting List \n \n ");
    while( Head -> next != NULL ) {
        Head = Head -> next ;
        printf("  %d  " , Head -> data);
    }
    printf(" \n \nPrinting List Complete \n");
}

void delete_value(int value , struct Node* Head) {
    struct Node* previous ;
    previous = Head;
    int flag = 0 ;
    while (Head -> next != NULL) {
        Head = Head -> next;
        if(Head -> data == value) {
            flag = 1;
            previous -> next = Head -> next ;
        }
        previous = Head;
    }
}


int main() {
    struct Node* HEAD = malloc(sizeof(struct Node));
    struct Node* Pointer = HEAD;
    char inp = '9';
    printf("\n \n Welcome to the linked list program \nPlease Enter the option to continue..\n1. Add Element\n2. Print List\n3. Remove Value\n");
    while(inp != '0') {
        inp = getchar();
        int value;
        switch(inp)
        {
        case '1':
            printf("Enter Value to be Added  ");
            scanf("%d",&value);
            Pointer = add_num(value,Pointer);
            break;

        case '2':
            print_list(HEAD);
            break;
        case '3':
            printf("Enter Value to be Removed  ");
            scanf("%d",&value);
            delete_value(value, HEAD);
            break;
        }
    }
    return 1;
}

