#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node *link;
};

struct Node* start=NULL;

struct Node* GetNode(){
    return ((struct Node*) malloc(sizeof (struct Node)));
}

void CreateList();
int CountNodes();
void Insert();
void InsertBefore();
void InsertAfter();
void InsertAtPosition();
void Delete();
void DeleteByValue();
void DeleteAtPosition();
void Display();

int main(int argc, char const *argv[])
{
    int ch;
    //printf("%d",sizeof(struct Node *));
	do
	{
		//clrscr();
		printf("\n\n********** CHOICES *********");
		printf("\n\n1 : CREATE LIST");
		printf("\n2 : INSERT A NODE");
		printf("\n3 : DELETE A NODE");
		printf("\n4 : DISPLAY LIST");
		printf("\n5 : EXIT");
		printf("\n\nENTER YOUR CHOICE : \t");
		scanf("%d",&ch);

		switch(ch)
		{
			case 1: // create list
			{
				CreateList();
				printf("\n\nNODES PRESENT : %d",CountNodes());
			}
			break;

			case 2: // insert node
			{
				Insert();
			}
			break;

			case 3: // delete node
			{
				Delete();
			}
			break;

			case 4: // display list
			{
				Display();
			}
			break;

			case 5: // exit
			break;

			default :
				printf("\n\nWRONG ENTRY ! TRY AGAIN ...");
		}
		//getch();
	}while(ch!=5);
    return 0;
}


void CreateList(){
    struct Node * end,*I;
    char ch;

    if(start!=NULL){
        printf("SLL already created.");
        return;
    }

    do{
        I = GetNode();
		printf("\n\nENTER THE DATA TO BE INSERTED : \t");
		scanf("%d",&I->data);

        I->link=NULL;
        if(start==NULL){
            start=I;
        }
        else{
            end->link=I;
        }
        end=I;
        printf("\nDO YOU WANT TO CONTINUE (Y/N) ... ");
		scanf("%c",&ch);
	}while(ch == 'Y' || ch == 'y');   
}

void Insert()
{
	int ch;
	// we can check here - if the list is existing
	do
	{
		//clrscr();

		printf("\n\n******* INSERT OPTIONS *******");
		printf("\n\n1 : INSERT BEFORE A NODE");
		printf("\n2 : INSERT AFTER A NODE");
		printf("\n3 : INSERT AT A POSITION");
		printf("\n4 : DISPLAY");
		printf("\n5 : BACK TO MAIN MENU");
		printf("\n\nENTER YOUR CHOICE : \t");
		scanf("%d",&ch);

		switch(ch)
		{
			case 1: // INSERT BEFORE
			{
				InsertBefore();
			}
			break;

			case 2: // insert after a node
			{
				InsertAfter();
			}
			break;

			case 3: // insert at a position
			{
				InsertAtPosition();
			}
			break;

			case 4: // display list
			{
				Display();
			}
			break;

			case 5: // BACK TO MAIN MENU
			return;
			//break;

			default :
				printf("\n\nWRONG ENTRY ! TRY AGAIN ...");
		}
		//getch();
	}while(1);		//while(ch!=5);
}

void InsertAfter(){
	struct Node* ptrAtValue, *I;
	int val;

	if(start==NULL){
		printf("LL is not created");
		return;
	}

	printf("\n\nENTER THE DATA AFTER WHICH NEW NODE TO BE INSERTED : \t");
	scanf("%d",&val);

	ptrAtValue=start;

	while(ptrAtValue->data!=val){
		ptrAtValue=ptrAtValue->link;
			if(ptrAtValue==NULL){
				printf("Value not found");
				return;
		}
	}

	I->link=ptrAtValue->link;
	ptrAtValue->link=I;
}

void InsertBefore(){
	struct Node *ptrBeforeVal,*ptrAtVal, *I;
	int val;

	if(start==NULL){
		printf("LL is not created");
		return;
	}
	printf("\n\nENTER THE DATA AFTER WHICH NEW NODE TO BE INSERTED : \t");
	scanf("%d",&val);

	ptrAtVal=start;

	while(ptrAtVal->data!=val){
		ptrAtVal=ptrAtVal->link;
		if(ptrAtVal==NULL){
			printf("Value not found");
			return;
		}
	}

	I = GetNode();
	printf("\n\nENTER THE DATA TO BE INSERTED : \t");
	scanf("%d",&I->data);

	if(ptrAtVal==start){
		I->link=start;
		start=I;
	}
	else{
		ptrBeforeVal=start;
		while(ptrBeforeVal->link!=ptrAtVal){
			ptrBeforeVal=ptrBeforeVal->link;
		}
		I->link=ptrAtVal;
		ptrBeforeVal->link=I;
	}
}

int CountNodes(){
	if(start==NULL){
		printf("LL not created");
		return 0;
	}
	struct Node *temp=start;
	int count=0;
	while(temp!=NULL){
		count++;
		temp=temp->link;
	}
	return count;
}

void InsertAtPosition(){
	if(start==NULL){
		printf("LL is not created");
		return;
	}

	struct Node *ptrAtPos, *I;
	int pos, nodeCount;
	nodeCount=CountNodes();
	printf("\n\nNODES PRESENT IN LIST : %d",nodeCount);
	printf("\n\nENTER A VALUE BETWEEN %d & %d",1,nodeCount+1);
	scanf("%d",&pos);
	if(pos<1||pos>nodeCount+1){
		printf("\n\nINVALID VALUE !");
		return;
	}

	I=GetNode();
	printf("\n\nENTER THE DATA TO BE INSERTED : \t");
	scanf("%d",&I->data);

	if(pos==1){
		I->link=start;
		start=I;
	}
	else{
		ptrAtPos=start;
		for(int i=0;i<pos-2;i++){
			ptrAtPos=ptrAtPos->link;
		}
		I->link=ptrAtPos->link;
		ptrAtPos->link=I;
	}
}

void Delete()
{
	int ch;
	do
	{
		//clrscr();
		// we can check here - if list is existing
		printf("\n\n******* DELETE OPTIONS *******");
		printf("\n\n1 : DELETE NODE BY VALUE");
		printf("\n2 : DELETE NODE AT A POSITION");
		printf("\n3 : DISPLAY");
		printf("\n4 : BACK TO MAIN MENU");
		printf("\n\nENTER YOUR CHOICE : \t");
		scanf("%d",&ch);

		switch(ch)
		{
			case 1: // DELETE BY VALUE
			{
				DeleteByValue();
			}
			break;

			case 2: // delete node at a position
			{
				DeleteAtPosition();
			}
			break;

			case 3: //display
			{
				Display();
			}
			break;

			case 4: // BACK TO MAIN MENU
			return;
			//break;

			default :
				printf("\n\nWRONG ENTRY ! TRY AGAIN ...");
		}
		getchar();
	}while(1);		//while(ch!=4);

}

void DeleteByValue(){
	if(start==NULL){
		printf("LL is not created");
		return;
	}

	struct Node *ptrBeforeValue,*ptrAtValue,*I;
	int val;

	printf("\n\nENTER THE OF THE NODE TO BE DELETED : \t");
	scanf("%d",&val);

	ptrAtValue=start;
	while(ptrAtValue->data!=val){
		ptrAtValue=ptrAtValue->link;
		if(ptrAtValue==NULL){
			printf("Value not found");
			return;
		}
	}

	if(ptrAtValue==start){
		start=start->link;
		return;
	}
	ptrBeforeValue=start;
	while(ptrBeforeValue->link!=ptrAtValue){
		ptrBeforeValue=ptrBeforeValue->link;
	}
	ptrBeforeValue->link=ptrAtValue->link;
	printf("\n\nTHE NODE HAVING DATA  %d IS DELETED.",ptrAtValue->data);
	ptrAtValue -> link = NULL;
	free(ptrAtValue);
}

void DeleteAtPosition(){
	if(start==NULL){
		printf("LL is not created");
		return;
	}

	struct Node *ptrBeforePos,*ptrAtPos,*I;
	int pos,nodeCount = CountNodes();
	printf("\n\nNODES PRESENT IN LIST : %d",nodeCount);
	printf("\n\nENTER A VALUE BETWEEN %d & %d",1,nodeCount);

	printf("\n\nENTER POSITION OF NODE TO BE DELETED : \t");
	scanf("%d",&pos);
	if(pos<1 || pos>nodeCount)
	{
		printf("\n\nINVALID VALUE !");
		return;
	}

	if(pos==1){
		start=start->link;
		return;
	}
	ptrBeforePos=start;
	ptrAtPos=ptrBeforePos->link;
	for(int i=1;i<pos-2;i++){
		ptrBeforePos=ptrBeforePos->link;
	}
	ptrAtPos=ptrBeforePos->link;
	ptrBeforePos->link=ptrAtPos->link;
	printf("\n\nTHE NODE HAVING DATA  %d IS DELETED.",ptrAtPos->data);
	ptrAtPos->link = NULL;
	free(ptrAtPos);
}

void Display(){
	struct Node * temp = start;
	if(temp == NULL)
	{
		printf("\n\nLIST IS EMPTY !!!");
		return;
	}
	printf("\n");
	while(temp != NULL)
	{
		printf("%d",temp->data);
		if(temp->link != NULL)
			printf(" -> ");
		temp = temp->link;
	}
}

void Search() {
    struct Node* temp = GetNode();
	temp=start;
    int pos=1,val;

    printf("Enter element to search: ");
    scanf("%d",&val);
    
    if(temp==NULL){
        printf("Linked list does not exist.\n");
        return;
    }
    while (temp != NULL) {
        if (temp->data == val) {
            printf("Element %d found at position %d.\n", val, pos);
            return; 
        }
        temp = temp->next;
        pos++; 
    }
    printf("Element %d not found.\n", val);