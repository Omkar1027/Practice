#include <stdio.h>
#include <string.h>

int stackIndex = -1;


void push(char stack[], char store) {
    stack[++stackIndex] = store;
}



int main(int argc, char const *argv[])
{
    char infix[100];

    printf("Enter the infix expression: ");
    scanf("%s", infix);

    int len = strlen(infix), count=0;

    for (int i = 0; i < len; i++) {
        if(infix[i]=='1'){
            count++;
        }
    }
    printf("%d",count);


    return 0;
}
