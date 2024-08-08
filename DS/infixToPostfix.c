#include <stdio.h>
#include <string.h>

int stackIndex=-1;

int preference(char c){
    if(c=='^') return 3;
    else if(c=='*'||c=='/') return 2;
    else if(c=='+'||c=='-') return 1;
    else return -1;
}

void push(char stack[], char store){  
    stack[++stackIndex]=store;
} 

int pop(char stack[]){
    return stack[stackIndex--];
}

void iToP(char infix[]){
    char postfix[100], stack[100];
    int postfixInd=0, len;
    stack[++stackIndex]='(';
    len=strlen(infix);
    infix[len++]=')';
    infix[len]='\0';

    for(int i=0; i<len; i++){
        char ichar= infix[i];
        if((ichar>='0'&& ichar<='9')||(ichar>='a'&& ichar<='z') || (ichar>='A'&& ichar<='Z')){
            postfix[postfixInd++]=ichar;        
        }
        else if(ichar=='('){
            stack[++stackIndex] = ichar;
        }
        else if(ichar==')'){
            while(stackIndex>=0 && stack[stackIndex]!='('){
                postfix[postfixInd++]=stack[stackIndex--];
            }
            stackIndex--;
        }
        else {
            // && raiseTo(ichar) == 'L')
            while(stackIndex>=0 && (preference(ichar) <= preference(stack[stackIndex]) )){
                postfix[postfixInd++]=stack[stackIndex--];
            }
            stack[++stackIndex] = ichar;
        }
    }

    while (stackIndex >= 0) {
        postfix[postfixInd++] = stack[stackIndex--];
    }
    postfix[postfixInd] = '\0';
    
    if(stackIndex==-1){
        printf("Postfix expression: %s",postfix);
    }
    else{
        printf("Invalid infix expression :`)      ");
    }
}   


int main(){
    char infix[100];

    printf("Enter the infix expression: ");
    scanf("%s", &infix);

    iToP(infix);
    return 0;
}