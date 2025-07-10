#include <stdio.h>

// Define logic gates
int AND(int a, int b) { return a & b; }
int OR(int a, int b) { return a | b; }
int NOT(int a) { return !a; }

// Simulate each circuit output
int circuit_A(int A, int B) {
    int or_out = OR(A, B);
    int not_b = NOT(B);
    return AND(or_out, not_b);
}

int circuit_B(int A, int B) {
    int not_b = NOT(B);
    return AND(A, not_b);
}

int circuit_C(int A, int B) {
    int not_b = NOT(B);
    int and1 = AND(A, not_b);
    int and2 = AND(not_b, B);
    return OR(and1, and2);
}

int circuit_D(int A, int B) {
    int not_a = NOT(A);
    return AND(not_a, B);
}

int main() {
    int mismatch[4] = {0};  // To track mismatches
    for (int A = 0; A <= 1; A++) {
        for (int B = 0; B <= 1; B++) {
            int outA = circuit_A(A, B);
            int outB = circuit_B(A, B);
            int outC = circuit_C(A, B);
            int outD = circuit_D(A, B);

            if (outA != outB) mismatch[0]++;
            if (outB != outC) mismatch[1]++;
            if (outC != outD) mismatch[2]++;
            if (outA != outD) mismatch[3]++;
        }
    }

    // Question
    printf("Q: For any set of inputs A and B, the following circuits give the same output Q, except one. Which one is it?\n");
    printf("(A) Q = (A + B) . ~B\n");
    printf("(B) Q = A . ~B\n");
    printf("(C) Q = (A . ~B) + (~B . B)\n");
    printf("(D) Q = ~A . B\n");

    // Identify mismatched circuit
    if (mismatch[2] > 0)
        printf("Answer: (C)\n");
    else
        printf("Answer: Unable to determine mismatch\n");

    return 0;
}