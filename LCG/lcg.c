#include <stdio.h>
#include <stdlib.h> // For rand() and srand()
#include <stdbool.h>
#include <time.h>   // For time()

bool seeded = false;
int time_seed = true;

// Function to set the seed and return a random number
int random_number(long seed) {
    // dropping seed support for now, using unix epoch.
    if(seeded){
        if(time_seed){
            srand(time(NULL));
        } else {
            srand(seed);
        }
        seeded = true;
    }
    return rand();
}
/*
MIN = 0
MAX = 10000
*/
int random_range(long seed, int min, int max){
    if(seeded){
        if(time_seed){
            srand(time(NULL));
        } else {
            srand(seed);
        }
        seeded = true;
    }
    return (rand() % (max - min + 1)) + min;
}
