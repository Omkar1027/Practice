#include <stdio.h>
#define MAX 2

int front = -1;
int rear = -1;
int my_c_queue[MAX];

void print_queue() {
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

int insert(int element) {
    if(front==-1&&rear==-1){
        front++;
        my_c_queue[++rear]=element;
    }
    else if (front==(rear+1)%MAX) {
        printf("Circular queue overflow\n");
        return 0;
    }
    else{
        my_c_queue[++rear]=element;
    }
}

void delete() {
    if (rear==-1) {
        printf("Circular queue is empty\n");
        return;
    } else {
        rear--;
        if(rear==-1){
            front=-1;
        }
    }
}

int main() {
    int choice = 0, element;
    while (choice != 4) {
        printf("Press 1 to insert, 2 to delete, 3 to print queue, 4 to exit: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter element to insert in circular queue: ");
                scanf("%d",&element);
                insert(element);
                break;
            case 2:
                delete();
                break;
            case 3:
                print_queue();
                break;
            case 4:
                break;
            default:
                printf("Invalid choice\n");
        }
    }
    return 0;
}
