#include <stdio.h>
#define Max 100
int top = -1;
int arr[Max];

void push(int ele) {
    if(top == Max-1)
        printf("Stack is full.\n");
    else {
        arr[++top] = ele;
    }
}

void peek(){
    if (top == -1) {
        printf("Array is empty, cannot peek.\n");
    } else {
        printf("Top element is %d\n", arr[top]);
    }
}

void isEmpty(){
    if (top == -1)
        printf("Stack is empty.\n");
    else
        printf("Stack is not empty.\n");
}

void isFull() {
    if (top == Max-1)
        printf("Stack is full.\n");
    else
        printf("Stack is not full.\n");
}

void pop() {
    if (top == -1) {
        printf("Array is empty, cannot pop.\n");
    } else {
        top--;
    }
}

int main() {
    int choice = 0,ele;
    while (choice != 6) {
        printf("\nPress 1 to push, 2 to pop, 3 to peek, 4 to isEmpty, 5 to is Full, 6 to exit: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter element to push: ");
                scanf("%d", &ele);
                push(ele);
                break;
            case 2:
                pop();
                break;
            case 3:
                peek();
                break;
            case 4:
                isEmpty();
                break;
            case 5:
                isFull();
                break;
            case 6:
                printf("Exited the loop.\n");
                break;
            default:
                printf("Invalid choice.\n");
        }
    }
    return 0;
}
