#include <stdio.h>

int main() {
    int Q, R, f;

    printf("Q R | f = ~(Q + R)\n");
    printf("-------------------\n");

    for (Q = 0; Q <= 1; Q++) {
        for (R = 0; R <= 1; R++) {
            f = !(Q || R);  // Logical NOR
            printf("%d %d |     %d\n", Q, R, f);
        }
    }

    return 0;
}
