#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node *next;
};

struct Node* start;

struct Node* GetNode(){
	return (struct Node*)malloc(sizeof(struct Node));
}

char choice;

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
void Search();

int main()
{
	int c=0;
	do{
		printf("\n\n***Main Menu***");
		printf("\n1: Create List\n2: Insert\n3: Delete\n4: Display\n5: Search\n6: Break\nEnter the choice: ");
		scanf("%d",&c);
		switch (c)
		{
		case 1:
			CreateList();
			break;
		case 2:
			Insert();
			break;
		case 3:
			Delete();
			break;
		case 4:
			Display();
			break;
		case 5:
			Search();
			break;
		case 6:
			printf("Exited the loop");
			break;
		default:
		printf("Invalid choice");
			break;
		}
	}while(c!=6);
	return 0;
}

void CreateList()
{
	char c;
    struct Node *end=NULL;
    if(start!=NULL){
        printf("Already created list");
        return;
    }
    do{
        struct Node *I=GetNode();
        printf("Enter data to enter: ");
        scanf("%d",&I->data);
        I->next=NULL;
        if(start==NULL){
            start=I;
        }
        else{
            end->next=I;
        }
        end=I;
        printf("Want to continue? (0/1): ");
        scanf("%d",&c);
    }while(c==1);
}

void Insert()
{
	int c=0;
	do{
		printf("\n\n***Insert Menu***");
		printf("\n1: Insert Before Value\n2: Insert After Value\n3: Insert At Position\n4: Display\n5: To Main Menu\nEnter the choice: ");
		scanf("%d",&c);
		switch (c)
		{
		case 1:
			InsertBefore();
			break;
		case 2:
			InsertAfter();
			break;
		case 3:
			InsertAtPosition();
			break;
		case 4:
			Display();
			break;
		case 5:
			printf("To Main Menu");
			break;
		default:
		printf("Invalid choice");
			break;
		}
	}while(c!=5);
}


void InsertBefore(){
    int val;
    struct Node *ptrBeforeVal, *ptrAtVal, *I;
    if(start==NULL){
        printf("LL empty");
        return;
    }

    printf("Enter the element before which node is to be added: ");
    scanf("%d",&val);

    ptrAtVal=start;
    while(ptrAtVal->data!=val ){
        ptrAtVal=ptrAtVal->next;
		if(ptrAtVal!=NULL){
			printf("Node not found");
			return;
		}
    }

    I=GetNode();
    printf("Enter the value to be inserted:");
    scanf("%d",&I->data);

    if(ptrAtVal==start){
        I->next=start;
        start=I;
    }
    else{
        ptrBeforeVal=start;
        while(ptrBeforeVal->next != ptrAtVal){
            ptrBeforeVal=ptrBeforeVal->next;
        }
		ptrBeforeVal->next=I;
        I->next=ptrAtVal;
    }
}

void InsertAfter(){
    int val;
    struct Node *ptrAtVal, *I;
    if(start==NULL){
        printf("LL is empty");
        return;
    }

    printf("Enter the element after which node is to be added: ");
    scanf("%d",&val);

    ptrAtVal=start;
    while(ptrAtVal->data!=val){
        ptrAtVal=ptrAtVal->next;
		if(ptrAtVal==NULL){
			printf("Node not found");
			return;
		}
    }
    I=GetNode();
    printf("Enter the value to be inserted:");
    scanf("%d",&I->data);

    I->next=ptrAtVal->next;
    ptrAtVal->next =I;
}

int CountNodes()
{
	struct Node * temp = start;
	int count = 0;
	if(temp == NULL)
	{
		printf("\n\nLIST IS EMPTY !!!");
		return 0;
	}
	while(temp != NULL)
	{
		temp = temp->next;
		count++;
	}
	return count;
}

void InsertAtPosition(){
    int pos, totalNodes ;
    struct Node *ptrBeforePos, *I;
    if(start==NULL){
        printf("LL is empty");
        return;
    }
    totalNodes=CountNodes();
    printf("Total number of  nodes is %d\n", totalNodes);
    printf("Enter value to enter at position between %d to %d: ", 1, totalNodes+1);
    scanf("%d",&pos);

    if(pos<1 || pos>totalNodes+1){
        printf("Invalid Nodes position");
        return;
    }
    I=GetNode();
    printf("Enter the value to be inserted:");
    scanf("%d",&I->data);

    if(pos==1){
        I->next=start;
        start=I;
        return;
    }
    
    ptrBeforePos=start;
    for(int i=0;i<pos-2;i++){
        ptrBeforePos= ptrBeforePos->next;
    }
    I->next=ptrBeforePos->next;
    ptrBeforePos->next=I;
}
void Delete()
{
	int c=0;
	do{
		printf("\n\n***Delete Menu***");
		printf("\n1: Delete By Value\n2: Delete At Position\n3: Display\n4: To Main Menu\nEnter the choice: ");
		scanf("%d",&c);
		switch (c){
		case 1:
			DeleteByValue();
			break;
		case 2:
			DeleteAtPosition();
			break;
		case 3:
			Display();
			break;
		case 4:
			printf("To Main Menu");
			break;
		default:
		printf("Invalid choice");
			break;
		}
	}while(c!=4);
}

void DeleteByValue()
{
    int val;
    struct Node *ptrAtValue,*ptrBeforeValue;
    if(start==NULL){
        printf("LL is empty");
    } 
    printf("Enter the value to be deleted: ");
    scanf("%d",&val);

    ptrAtValue=start;
    while(ptrAtValue->data!=val && ptrAtValue!=NULL){
        ptrAtValue=ptrAtValue->next;
    }
    if(ptrAtValue==NULL){
        printf("Value not found in LL");
        return;
    }

    if(ptrAtValue==start){
        start=start->next;
    }
    else{
        ptrBeforeValue=start;
        while(ptrBeforeValue->next!=ptrAtValue)
            ptrBeforeValue=ptrBeforeValue->next;
        ptrBeforeValue->next=ptrAtValue->next;
    }
	printf("The node having data '%d' is deleted", ptrAtValue->data);
	ptrAtValue->next=NULL;
	free(ptrAtValue);
}

void DeleteAtPosition()
{
    int pos, totalNodes;
    struct Node *ptrBeforePos,*ptrAtPos;

	if(start==NULL){
		printf("Linked List is Empty");
		return;
	}
	totalNodes=CountNodes();
	printf("Enter the position to delete element between %d to %d: ",1,totalNodes);
	scanf("%d",&pos);
	if(pos<0 || pos>totalNodes){
		printf("Position is out of bound");
		return;
	}
	if(pos==1){
		start=start->next;
	}
	else{
		ptrAtPos=start;
		for(int t=1;t<pos;t++){
			ptrBeforePos=ptrAtPos;
			ptrAtPos=ptrAtPos->next;
		}
		ptrBeforePos->next=ptrAtPos->next;
	}
	printf("\nThe node having data '%d' is deleted", ptrAtPos->data);
	ptrAtPos->next=NULL;
	free(ptrAtPos);
}

void Display(){
	if(start==NULL){
		printf("\nLinked List is Empty");
		return;
	}
	struct Node* temp=start;
	while(temp!=NULL){
		printf("%d -> ",temp->data);
		temp=temp->next;
	}
	printf("NULL\n");
}

void Search() {
    struct Node* temp = start;
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
}