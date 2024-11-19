#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(0)); // Seed the random number generator
    printf("Random number: %d\n", rand());
    return 0;
}