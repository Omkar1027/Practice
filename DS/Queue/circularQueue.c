#include <stdio.h>
#define MAX 5

int front = -1;
int rear = -1;
int my_c_queue[MAX];

void print_queue() {
    if (front == -1) {
        printf("Circular queue is empty\n");
        return;
    }
    for(int i = front; i!=rear;i=(i+1)%MAX)
        printf("%d -> ",my_c_queue[i]);
    printf("%d -> NULL\n\n", my_c_queue[rear]); // Print the last element
}

void enqueue(int ele) {
    if ((rear + 1) % MAX == front) {
        printf("Circular queue overflow\n");
        return;
    }
    if (front == -1 && rear == -1) {
        front = 0;
    }
    rear = (rear + 1) % MAX;
    my_c_queue[rear] = ele;
}

void dequeue() {
    if (front == -1) {
        printf("Circular queue is empty\n");
        return;
    }
    if (front == rear) {
        front = rear = -1;
    } else {
        front = (front + 1) % MAX;
    }
}

int main() {
    int choice = 0, ele;
    while (choice != 4) {
        printf("Press 1 to push, 2 to pop, 3 to print queue, 4 to exit: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter element to push in circular queue: ");
                scanf("%d", &ele);
                enqueue(ele);
                break;
            case 2:
                dequeue();
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
