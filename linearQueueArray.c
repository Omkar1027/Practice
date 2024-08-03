#include <stdio.h>
#include <string.h>

int rear=0;

void print_queue(int queue[]){
    for(int i=0;i<rear;i++){
        printf("%d -> ",queue[i]);
    }
    printf("NULL\n");
}

int push(int queue[]){  
    printf("Enter queue[%d]: ",rear);
    scanf("%d",&queue[rear]);
    rear++;
} 

void pop(int queue[]){   
    if(rear>0){
        for(int i=0;i<rear;i++){
            queue[i]=queue[i+1];
        }
        rear--;
    }
    else printf("Queue is empty.");
}


int main(){
    int queue[100],choice;

    while(choice!=4){
        printf("Press 1 to push, 2 to pop, 3 to print queue, 4 to exit: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                push(queue);
                break;
            case 2:
                pop(queue);
                break;
            case 3:
                print_queue(queue);
                break;
            default:
                printf("Invalid");
        }
    }      
}


