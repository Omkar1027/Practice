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

int main(int argc, char const *argv[])
{
    
    switch (c)
    {
    case 1:
        /* code */
        break;
    
    default:
        break;
    }
    return 0;
}
