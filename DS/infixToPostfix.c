#include <stdio.h>
#include <string.h>

int stackIndex=-1;

int preference(char c){
    if(c=='^') return 3;
    else if(c=='*'||c=='/') return 2;
    else if(c=='+'||c=='-') return 1;
    else return -1;
}

void print_stack(char arr[], int index){
     for(int i=0;i<index;i++){
        printf("%c",arr[i]);
    }
}

void push(char stack[], char store){  
    stack[++stackIndex]=store;
} 

int pop(char stack[]){
    return stack[stackIndex--];
}

void iToP(char infix[]){
    char postfix[100], stack[100];
    int postfixInd=-1, checkP, checkPI, len;
    push(stack,'(');
    len=strlen(infix);
    len++;
    infix[len]=')';

    for(int i=0; i<len; i++){
        char ichar= infix[i];
        if((ichar>='0'&& ichar<='9')||(ichar>='a'&& ichar<='z') || (ichar>='A'&& ichar<='Z')){
            postfix[++postfixInd]=ichar;        
            printf("Enter if 1\n");
        }
        else if(ichar=='('){
            push(stack,ichar);
            printf("Enter else if 1\n");
        }
        else if(ichar==')'){
            while(stackIndex>-1 && stack[stackIndex]!='('){
                postfix[postfixInd++]=stack[stackIndex--];
            }
            stackIndex--;
            printf("Enter else if 2\n");
        }
        else {
            checkP = preference(ichar);
            checkPI =preference(stack[stackIndex-1]) ;
            if(checkPI!=-1){
                if(checkP>checkPI){
                    while(stack[stackIndex]!='('){
                        postfix[postfixInd++]=stack[stackIndex--];
                    }
                }
                else{
                    push(stack,ichar);
                }
            }
            
        }
        
    }
    if(stackIndex==-1){
        printf("Postfix expression: ");
        print_stack(postfix,postfixInd);
    }
    else{
        printf("Invalid infix expression :`)");
        print_stack(postfix,postfixInd);
    }
}   


int main(){
    char infix[100];

    printf("Enter the infix expression: ");
    scanf("%s", &infix);

    iToP(infix);
    return 0;
}