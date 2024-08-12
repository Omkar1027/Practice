#include <stdio.h>
#define MAX 2

int front = -1;
int rear = -1;

void print_queue(int my_c_queue[]) {
    if (front==-1 && rear == -1) {
        printf("Circular queue is empty\n");
        return;
    }
    int i=0;
    for ( i = front; i != rear; i=(i+1) % MAX) {
        printf("%d -> ", my_c_queue[i]);
    }
    printf("%d -> ", my_c_queue[i]);
    printf("NULL\n\n");
}

int push(int my_c_queue[]) {
    if(front==-1&&rear==-1){
        front++;
        printf("Enter element to push in circular queue: ");
        scanf("%d", &my_c_queue[++rear]);
    }
    else if (front==(rear+1)%MAX) {
        printf("Circular queue overflow\n");
        return 0;
    }
    else{
        printf("Enter element to push in circular queue: ");
        scanf("%d", &my_c_queue[++rear]);
    }
}

void pop(int my_c_queue[]) {
    if (rear==-1) {
        printf("Circular queue is empty\n");
    } else {
        rear--;
        if(rear==-1){
            front=-1;
        }
    }
}

int main() {
    int my_c_queue[MAX], choice = 0;
    while (choice != 4) {
        printf("Press 1 to push, 2 to pop, 3 to print queue, 4 to exit: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                push(my_c_queue);
                break;
            case 2:
                pop(my_c_queue);
                break;
            case 3:
                print_queue(my_c_queue);
                break;
            case 4:
                break;
            default:
                printf("Invalid choice\n");
        }
    }
    return 0;
}



char temp=popChar(stack);
                push(stack,temp);