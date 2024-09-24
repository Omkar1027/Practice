#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node *next;
};

struct Node* start=NULL;

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

int main()
{
	int c=0;
	do{
		printf("\n\n***Main Menu***");
		printf("\n1: Create List\n2: Insert\n3: Delete\n4: Display\n5: Break\nEnter the choice: ");
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
			printf("Exited the loop");
			break;
		default:
		printf("Invalid choice");
			break;
		}
	}while(c!=5);
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
        // I->next=NULL;
        if(start==NULL){
            start=I;
        }
        else{
            end->next=I;
        }
        end=I;
        I->next=start;
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
    while(ptrAtVal->data!=val && ptrAtVal->next!=start){ //
        ptrAtVal=ptrAtVal->next;
    }
    if(ptrAtVal->data!=val){
        printf("Node not found");
        return;
    }

    I=GetNode();
    printf("Enter the value to be inserted:");
    scanf("%d",&I->data);

    ptrBeforeVal=start;
    while(ptrBeforeVal->next != ptrAtVal){
        ptrBeforeVal=ptrBeforeVal->next;
    }
    ptrBeforeVal->next=I;
    I->next=ptrAtVal;

    if(ptrAtVal==start){
        start=I;
    }


    // if(ptrAtVal==start){
    //     I->next=start;
    //     start=I;
    // }
    // else{
        // ptrBeforeVal=start;
        // while(ptrBeforeVal->next != ptrAtVal){
        //     ptrBeforeVal=ptrBeforeVal->next;
        // }
		// ptrBeforeVal->next=I;
        // I->next=ptrAtVal;
    // }
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
    while(ptrAtVal->data!=val && ptrAtVal->next!=start){//
        ptrAtVal=ptrAtVal->next;
    }
    if(ptrAtVal->data!=val){
        printf("Node not found");
        return;
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
	int count = 1;
	if(start == NULL)
	{
		printf("\n\nLIST IS EMPTY !!!");
		return 0;
	}
	while(temp->next != start)
	{
		temp = temp->next;
		count++;
	}
	return count;
}

void InsertAtPosition(){
    int pos, totalNodes ;
    struct Node *ptrBeforePos,*ptrAtPos, *I;
    if(start==NULL){
        printf("LL is empty");
        return;
    }
    totalNodes=CountNodes();
    printf("Total number of  nodes is %d\n", totalNodes);
    printf("Enter value to enter at position between %d to %d: ", 1, totalNodes+1);
    scanf("%d",&pos);

    ptrAtPos=start;
    for(int i=0;i<pos-1;i++)
        ptrAtPos=ptrAtPos->next;
    
    ptrBeforePos=start;
    while(ptrBeforePos->next!=ptrAtPos)
        ptrBeforePos=ptrBeforePos->next;
    
    I=GetNode();
    printf("Enter the value to be inserted:");
    scanf("%d",&I->data);

    I->next=ptrBeforePos->next;
    ptrBeforePos->next=I;

    if(pos==1){
        start=I;
    }


    // if(pos<1 || pos>totalNodes+1){
    //     printf("Invalid Nodes position");
    //     return;
    // }
    // I=GetNode();
    // printf("Enter the value to be inserted:");
    // scanf("%d",&I->data);

    // if(pos==1){
    //     I->next=start;
    //     start=I;
    //     return;
    // }
    
    // ptrBeforePos=start;
    // for(int i=0;i<pos-2;i++){
    //     ptrBeforePos= ptrBeforePos->next;
    // }
    // I->next=ptrBeforePos->next;
    // ptrBeforePos->next=I;
}
void Delete()
{
	int c=0;
	do{
		printf("\n\n***Delete Menu***");
		printf("\n1: Delete By Value\n2: Delete At Position\n3: Display\n4: Break\nEnter the choice: ");
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
    while(ptrAtValue->data!=val && ptrAtValue->next!=start){
        ptrAtValue=ptrAtValue->next;
    }
    if(ptrAtValue->next==start){
        printf("Value not found in LL");
        return;
    }

    ptrBeforeValue=start;
    while(ptrBeforeValue->next!=ptrAtValue)
        ptrBeforeValue=ptrBeforeValue->next;
    
    if(ptrAtValue==ptrBeforeValue){
        start=NULL;
    }
    else{
        
        ptrBeforeValue->next=ptrAtValue->next;
        if(ptrAtValue==start){
            start=start->next;
    }
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
    printf("Total Nodes are: %d\n",totalNodes);
	printf("Enter the position to delete element between %d to %d: ",1,totalNodes);
	scanf("%d",&pos);
	if(pos<1 || pos>totalNodes){
		printf("Position is out of bound");
		return;
	}
    
	ptrAtPos=start;
	for(int t=0;t<pos-1;t++){
		ptrAtPos=ptrAtPos->next;
	}

    ptrBeforePos=start;
    while(ptrBeforePos->next != ptrAtPos)
		ptrBeforePos = ptrBeforePos->next;

	if(ptrBeforePos==ptrAtPos){
		start=NULL;
	}
	else{
		ptrBeforePos->next=ptrAtPos->next;
        if(ptrAtPos==start){
            start=start->next;
        }
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
	while(temp->next!=start){
		printf("%d -> ",temp->data);
		temp=temp->next;
	}
    printf("%d",temp->data);
}