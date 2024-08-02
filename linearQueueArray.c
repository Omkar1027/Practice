#include <stdio.h>
#include <string.h>

void print_queue(int queue[], int rear){
    for(int i=0;i<rear;i++){
        printf("%d -> ",queue[i]);
    }
    printf("NULL");
}

int push(int queue[],int *rear){  
    printf("Enter queue[%d]: ",*rear);
    scanf("%d",&queue[*rear]);
    (*rear)++;

} 

void pop(int queue[],int *rear){   
    if(*rear>0){
        for(int i=0;i<*rear;i++){
            queue[i]=queue[i+1];
        }
        (*rear)--;
    }
    else printf("Queue is empty.");
}


int main(){
    int queue[100],n,rear=0,choice;
    printf("Enter number of elements to push in the queue: ");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        printf("Enter queue[%d]: ",i);
        scanf("%d",&queue[i]);
        rear++;
    }

    while(1){
        printf("\nPress 1 to push, 2 to pop, 3 to print queue: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                push(queue, &rear);
                break;
            case 2:
                pop(queue, &rear);
                break;
            case 3:
                print_queue(queue, rear);
                break;
            default:
                printf("Invalid");
        }
    }
       
}


