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

void parenthesis_matching(char str[],char arr[], int string_len){
    int arr_len=0;
    int didPop=0;
    for(int i=0; i<string_len; i++){
        if(str[i]=='['||str[i]=='{'||str[i]=='('||str[i]=='<'){
            push(arr,arr_len,str[i]);
            arr_len++;
            didPop++;
        }
        else if(str[i]==']'||str[i]=='}'||str[i]==')'||str[i]=='>'){
            if((arr[arr_len-1]=='('&&str[i]==')') || (arr[arr_len-1]=='{'&&str[i]=='}') || (arr[arr_len-1]=='['&&str[i]==']') || (arr[arr_len-1]=='<'&&str[i]=='>')){
                pop(arr,arr_len);
                arr_len--;
            }
        }
    }
    if(arr_len==0 && didPop!=0){
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

    int n=strlen(str);

    parenthesis_matching(str, arr, n);
    return 0;
}