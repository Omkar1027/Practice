#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int stackIndex=-1;

int preference(char c){
    if(c=='^') return 3;
    else if(c=='*'||c=='/') return 2;
    else if(c=='+'||c=='-') return 1;
    else return -1;
}
void print_array(char arr[], int array_index){
     for(int i=0;i<array_index;i++){
        printf("\narr[%d]=%c ",i,arr[i]);
    }
}

void push(char stack[], char store){  
    stack[++stackIndex]=store;
} 

int pop(char stack[]){
    return stack[stackIndex--];
}

void iToP(char postfix[]){
    char stack[100],topRight[1],Left[1];
    int postfixInd=0, len, temp=0;
    len=strlen(postfix);

    for(int i=0; i<len; i++){
        char ichar= postfix[i];
        if((ichar>='0'&& ichar<='9')){
            stack[stackIndex++]=ichar;        
        }
        else {
            topRight[0] = pop(stack);
            Left[0] = pop(stack);
            int r=atoi(topRight);
            int l=atoi(Left);
            switch (ichar) {
            case '+':
                push(stack, r + l);
                break;
            case '-':
                push(stack, r - l);
                break;
            case '*':
                push(stack, r * l);
                break;
            case '/':
                push(stack, r / l);
                break;
            }
        }
    }
    // while (stackIndex >= 0) {
    //     postfix[postfixInd++] = stack[stackIndex--];
    // }
    // postfix[postfixInd] = '\0';
    
    printf("%c",stack[0]);
}   


int main(){
    char postfix[100];

    printf("Enter the infix expression: ");
    scanf("%s", &postfix);

    iToP(postfix);
    return 0;
}