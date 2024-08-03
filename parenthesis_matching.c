#include <stdio.h>
#include <string.h>

int array_index=0;

void print_array(char arr[], int array_index){
     for(int i=0;i<array_index;i++){
        printf("\narr[%d]=%c ",i,arr[i]);
    }
}

void push(char arr[], char store){  
    arr[array_index]=store;
    array_index++;
} 

void pop(char arr[]){   
    arr[array_index]=0;
    array_index--;
}

void parenthesis_matching(char str[],char arr[]){
    int didPop=0,string_len=strlen(str);

    for(int i=0; i<string_len; i++){
        if(str[i]=='['||str[i]=='{'||str[i]=='('||str[i]=='<'){
            push(arr,str[i]);
            didPop++;
        }
        else if(str[i]==']'||str[i]=='}'||str[i]==')'||str[i]=='>'){
            if((arr[array_index-1]=='('&&str[i]==')') || (arr[array_index-1]=='{'&&str[i]=='}') || (arr[array_index-1]=='['&&str[i]==']') || (arr[array_index-1]=='<'&&str[i]=='>')){
                pop(arr);
            }
        }
    }

    if(array_index==0 && didPop!=0){
        printf("All parenthesis are matched");
    }
    else{
        printf("Parenthesis are not matched.");
    }
}

int main(){
    char str[100];
    char arr[100];

    printf("Enter the brackets: ");
    scanf("%s", &str);

    parenthesis_matching(str, arr);
    return 0;
}