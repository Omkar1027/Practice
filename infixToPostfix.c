#include <stdio.h>
#include <string.h>

void print_array(char arr[], int array_index){
     for(int i=0;i<array_index;i++){
        printf("\narr[%d]=%c ",i,arr[i]);
    }
}

void push(char arr[], int array_index, char store){  
    arr[array_index]=store;
} 

void pop(char arr[], int array_index){   
    arr[array_index]=0;
}

char parenthesis_matching(char infix[]){
    char postfix[100],stack[100];
    int postIndex=0,stackIndex=1,len=strlen(infix);
    infix[len+1]=')';
    stack[0]='(';

    for(int i=0;i<strlen(infix);i++){
        int n=infix[i];
        if(n>47 && n<58){
            push(postfix,postIndex,infix[i]);
            return;
        }
        else{
            if(infix[i]=='('){
            push(stack,stackIndex,infix[i]);
            }
        }
    }
}

int main(){
    char infix[100];
    printf("Enter the infix string: ");
    scanf("%d",infix);

    iToP(infix);
}