#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct Node {
    char *event;
    struct Node *left;
    struct Node *right;
} Node;

typedef struct Player {
    int health;
    int hasSword;
    int hasPotion;
} Player;

Node* createNode(char *event);
Node* createRandomTree(int depth, Player *player);
void traverseTree(Node *root, Player *player);
void fight(Player *player);
void displayOptions();
void pickUpItem(Player *player, char *item);
void encounter(Player *player, char *event);
void playGame();
char* getRandomEvent(Player *player);
void freeTree(Node *root);

char* commonEvents[] = {
    "You found a potion.",
    "You found a monster! Prepare to fight.",
};

char* rareEvents[] = {
    "You found a sword.",
    "You found a treasure! You win.",
    "Dead end."
};

int main() {
    srand(time(0));
    playGame();
    return 0;
}

Node* createNode(char *event) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->event = event;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

Node* createRandomTree(int depth, Player *player) {
    if (depth == 0) {
        return NULL;
    }
    Node *root = createNode(getRandomEvent(player));
    
    if (depth > 1 || (rand() % 2 == 0)) {
        root->left = createRandomTree(depth - 1, player);
    }
    if (depth > 1 || (rand() % 2 == 0)) {
        root->right = createRandomTree(depth - 1, player);
    }
    
    return root;
}

char* getRandomEvent(Player *player) {
    int randomIndex;

    if (rand() % 100 < 70) {
        randomIndex = rand() % 2;
        return commonEvents[randomIndex];
    } else {
        while (1) {
            randomIndex = rand() % 3;
            if (strcmp(rareEvents[randomIndex], "You found a sword.") == 0 && player->hasSword) {
                continue;
            }
            return rareEvents[randomIndex];
        }
    }
}

void fight(Player *player) {
    int monsterHealth = 100;
    int choice;
    
    while (monsterHealth > 0 && player->health > 0) {
        printf("\nMonster Health: %d | Your Health: %d\n", monsterHealth, player->health);
        displayOptions();
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                if (player->hasSword) {
                    printf("You strike with your sword and defeat the monster in one blow!\n");
                    monsterHealth = 0;
                } else {
                    printf("You hit the monster! It loses 30 health.\n");
                    monsterHealth -= 30;
                }
                break;
            case 2:
                printf("You defend yourself! You take only 10 damage.\n");
                player->health -= 10;
                break;
            case 3:
                if (player->hasPotion) {
                    printf("You drink a potion and recover 20 health.\n");
                    player->health += 20;
                    player->hasPotion = 0;
                } else {
                    printf("You have no potion left!\n");
                }
                break;
            default:
                printf("Invalid choice. Try again.\n");
                continue;
        }

        if (monsterHealth > 0 && (rand() % 2 == 0)) {
            printf("The monster attacks you! You lose 15 health.\n");
            player->health -= 15;
        }
    }

    if (player->health > 0) {
        printf("You have defeated the monster!\n");
    } else {
        printf("You have been defeated by the monster...\nGame Over.\n");
        exit(0);
    }
}

void displayOptions() {
    printf("\nChoose your action:\n");
    printf("1. Fight\n");
    printf("2. Defend\n");
    printf("3. Drink Potion\n");
    printf("Enter your choice: ");
}

void pickUpItem(Player *player, char *item) {
    if (strcmp(item, "sword") == 0) {
        player->hasSword = 1;
        printf("You have picked up a sword!\n");
    } else if (strcmp(item, "potion") == 0) {
        player->hasPotion = 1;
        printf("You have picked up a potion!\n");
    }
}

void encounter(Player *player, char *event) {
    if (strstr(event, "monster")) {
        fight(player);
    } else if (strstr(event, "sword")) {
        pickUpItem(player, "sword");
    } else if (strstr(event, "potion")) {
        pickUpItem(player, "potion");
    } else if (strstr(event, "treasure")) {
        printf("Congratulations! You found the treasure and won the game!\n");
        exit(0);
    } else if (strstr(event, "Dead end")) {
        printf("You reached a dead end. Game Over.\n");
        exit(0);
    }
}

void traverseTree(Node *root, Player *player) {
    if (root == NULL) return;

    if (strcmp(root->event, "Start of your adventure.") != 0) {
        printf("\n%s\n", root->event);
        encounter(player, root->event);
    }
    
    int choice;
    if (root->left != NULL || root->right != NULL) {
        do {
            printf("\nWhich direction do you want to go?\n");
            printf("1. Left\n2. Right\n");
            scanf("%d", &choice);
            switch (choice) {
                case 1:
                    traverseTree(root->left, player);
                    break;
                case 2:
                    traverseTree(root->right, player);
                    break;
                default:
                    printf("Enter valid choice");
                    break;
            }
        } while (choice != 1 && choice != 2);
    }
}

void playGame() {
    Player player = {100, 0, 0};
    int randomHeight = 5 + rand() % 4;
    Node *root = createRandomTree(randomHeight, &player);

    printf("Welcome to the Adventure Game!\n");
    printf("You are at the start of your adventure. Choose your path:\n");
    traverseTree(root, &player);
    freeTree(root);
}

void freeTree(Node *root) {
    if (root == NULL) return;
    freeTree(root->left);
    freeTree(root->right);
    free(root);
}
