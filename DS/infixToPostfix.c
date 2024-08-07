#include <stdio.h>

int stackIndex=-1;

void preference()

void print_stack(char arr[], int array_index){
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

void iToP(int infix[]){
    int postfix[100], stack[100];
    for(int i=0; i<strlen(infix); i++){
        int ichar= infix[i];
        if(ichar>='0'&& ichar<='9'){
            push(stack,ichar);
        }
    }
    
}

int main(){
    int infix[100];

    printf("Enter the infix expression: ");
    scanf("%s", &infix);

    iToP(infix);
    return 0;
}