#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data; 
    struct Node* link;
};

struct Node *front=NULL,*rear=NULL;

struct Node *GetNode(){
    return (struct Node*)malloc(sizeof(struct Node));
}

void enqueue(int ele){
    struct Node *I=GetNode();
    I->data = ele;
    I->link=NULL;
    if(front==NULL){
        front=rear=I;
    }
    else{
        rear->link=I;
        rear=I;
    }
}

void dequeue(){
    if(front==NULL){
        printf("Queue is empty.\n");
        return;
    }
    struct Node* temp=front;
    front=front->link;
    if(front==NULL){
        rear=NULL;
    }
    printf("The dequeued element is: %d\n", temp->data);
    free(temp);
}

void display(){
    if(front==NULL){
        printf("Queue is empty.\n");
        return;
    }
    struct Node* temp=front;
    printf("front-> ");
    while(temp!=NULL){
        printf("%d -> ",temp->data);
        temp=temp->link;
    }
    printf("rear\n");
}

void peek(){
    if(front==NULL){
        printf("Queue is empty.\n");
    }
    else{
        printf("The value at front of the queue is: %d\n",front->data);
    }
}

int main(int argc, char const *argv[])
{
    int c=0,ele;
    do{
    printf("\n1: Enqueue, 2: Dequeue, 3: Display, 4: Peek, 5: Break\nEnter your choice: ");
    scanf("%d",&c);
        switch (c)
        {
        case 1:
            printf("Enter element to enqueue: ");
            scanf("%d",&ele);
            enqueue(ele);
            break;
        case 2:
            dequeue();
            break;
        case 3:
            display();
            break;
        case 4: 
            peek();
            break;
        case 5:
            printf("adios amigos");
            break;
        default:
            printf("Invalid choice");
            break;
        }
    }while(c!=5);
    return 0;
}

