#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data; 
    struct Node* link;
};

struct Node* top=NULL;

struct Node* GetNode(){
    return (struct Node*) malloc (sizeof (struct Node));
}

void push(int ele){
    struct Node * I = GetNode();
    I->data=ele;
    if(top == NULL){
        top=I;
        I->link=NULL;
    }
    else{
        I->link=top;
        top=I;
    }
}

void pop(){
    if(top==NULL){
        printf("Stack is empty.\n");
    }
    else{
        struct Node* temp;
        temp=top;
        top=top->link;
        printf("Popped data is %d\n",temp->data);
        free(temp);
    }
}

void display(){
    if(top==NULL){
        return;
    }
        struct Node* temp;
        temp=top;
        printf("top");
        while(temp!=NULL){
            printf("-> %d",temp->data);
            temp=temp->link;
        }
        printf("\n");
}

void peek(){
    if(top==NULL){
        printf("Stack is empty\n");
    }
    else{
        printf("Top element is: %d\n", top->data );
    }
}

int main(int argc, char const *argv[])
{
    int c=0,ele;
    printf("%d",5%2);