#include <stdio.h>

int main() {
    int X, Y, Z;

    printf("X Y | X ⊕ Y = Z\n");
    printf("----------------\n");

    for (X = 0; X <= 1; X++) {
        for (Y = 0; Y <= 1; Y++) {
            Z = X ^ Y;  // XOR operation
            printf("%d %d |   %d\n", X, Y, Z);
        }
    }

    return 0;
}
