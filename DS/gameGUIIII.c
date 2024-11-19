#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct Node {
    char *event;           // Description of the event
    struct Node *left;    // Left child node
    struct Node *right;   // Right child node
} Node;

typedef struct Player {
    int health;           // Player's health points
    int hasSword;         // Does the player have a sword?
    int hasPotion;        // Does the player have a potion?
} Player;

// Function prototypes
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

// Common and rare events in the game
char* commonEvents[] = {
    "You found a potion.",
    "You encountered a monster! Prepare for battle.",
};

char* rareEvents[] = {
    "You discovered a sword!",
    "You found a treasure! You are victorious!",
    "This path leads to a dead end."
};

int main() {
    srand(time(0)); // Seed random number generator
    playGame();
    return 0;
}

// Create a new node with the given event
Node* createNode(char *event) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->event = event;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Build a random binary tree to represent the adventure
Node* createRandomTree(int depth, Player *player) {
    if (depth == 0) {
        return NULL; // No more nodes to create
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

// Get a random event based on the player's inventory
char* getRandomEvent(Player *player) {
    int randomIndex;

    // 70% chance for a common event
    if (rand() % 100 < 70) {
        randomIndex = rand() % 2;
        return commonEvents[randomIndex];
    } else {
        // 30% chance for a rare event
        while (1) {
            randomIndex = rand() % 3;
            // Ensure the player doesn't find a sword they already possess
            if (strcmp(rareEvents[randomIndex], "You discovered a sword!") == 0 && player->hasSword) {
                continue;
            }
            return rareEvents[randomIndex];
        }
    }
}

// Handle a fight between the player and a monster
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
                    player->hasPotion = 0; // Potion is used up
                } else {
                    printf("You have no potions left!\n");
                }
                break;
            default:
                printf("Invalid choice. Please try again.\n");
                continue;
        }

        // Monster attacks
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

// Display action options to the player
void displayOptions() {
    printf("\nChoose your action:\n");
    printf("1. Attack\n");
    printf("2. Defend\n");
    printf("3. Use Potion\n");
    printf("Enter your choice: ");
}

// Allow the player to pick up an item
void pickUpItem(Player *player, char *item) {
    if (strcmp(item, "sword") == 0) {
        player->hasSword = 1;
        printf("You have picked up a sword!\n");
    } else if (strcmp(item, "potion") == 0) {
        player->hasPotion = 1;
        printf("You have picked up a potion!\n");
    }
}

// Handle encounters based on the event description
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
    } else if (strstr(event, "dead end")) {
        printf("You reached a dead end. Game Over.\n");
        exit(0);
    }
}

// Traverse the tree to navigate through events
void traverseTree(Node *root, Player *player) {
    if (root == NULL) return;

    // Display the current event
    printf("\n%s\n", root->event);
    encounter(player, root->event);
    
    // Choose direction for the next event
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
                    printf("Please enter a valid choice.\n");
                    break;
            }
        } while (choice != 1 && choice != 2);
    }
}

// Start the game and initialize the player's state
void playGame() {
    Player player = {100, 0, 0}; // Starting health, sword, and potion
    int randomHeight = 5 + rand() % 4; // Random tree depth between 5 and 8
    Node *root = createRandomTree(randomHeight, &player);

    printf("Welcome to the Adventure Game!\n");
    printf("You are at the start of your adventure. Choose your path:\n");
    traverseTree(root, &player);
    freeTree(root); // Clean up memory after the game
}

// Free the memory allocated for the tree
void freeTree(Node *root) {
    if (root == NULL) return;
    freeTree(root->left);
    freeTree(root->right);
    free(root);
}
