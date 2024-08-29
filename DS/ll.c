#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void createll(){
    if 
}

int main(int argc, char const *argv[])
{
    int c;
    printf("Menu is:\n 1. Create\n 2.Insert\n 3.Delete\n 4.Exit\n ");
    scanf("%d",&c);
    switch (c)
    {
    case 1:
        createll();
        break;
    default:
        break;
    }
    return 0;
}
