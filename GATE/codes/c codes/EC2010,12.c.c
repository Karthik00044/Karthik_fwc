#include <stdio.h>

// Logic gate functions
int OR(int a, int b) { return a | b; }
int NOR(int a, int b) { return !(a | b); }

int main() {
    int A, B, C, F;

    printf("Checking all input combinations for F = (NOT(A OR B)) OR C:\n\n");
    printf(" A B C | F\n");
    printf("-------|---\n");

    for (A = 0; A <= 1; A++) {
        for (B = 0; B <= 1; B++) {
            for (C = 0; C <= 1; C++) {
                int or_ab = OR(A, B);
                int z = !or_ab;     // NOR of same inputs = NOT(OR)
                F = OR(z, C);

                printf(" %d %d %d | %d\n", A, B, C, F);

                // Print the matching input
                if (F == 1) {
                    printf(">> Valid Input for F = 1: A = %d, B = %d, C = %d\n\n", A, B, C);
                }
            }
        }
    }
      printf("\nAnswer: Option (D)\n");

    return 0;
}