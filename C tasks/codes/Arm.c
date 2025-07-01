#include <stdio.h>

// Function to simulate Circuit (A)
// Logic: NOT ((A XOR B) AND (NOT B))
int simulateCircuitA(int A, int B) {
    int xor_ab = (A ^ B);      // A XOR B
    int not_b = (!B);          // NOT B
    return !(xor_ab && not_b); // NOT ((A XOR B) AND (NOT B))
}

// Function to simulate Circuit (B)
// Logic: NOT (A AND (NOT B))
int simulateCircuitB(int A, int B) {
    int not_b = (!B);          // NOT B
    return !(A && not_b);      // NOT (A AND (NOT B))
}

// Function to simulate Circuit (C)
// Logic: (A AND (NOT B)) OR (B AND (NOT A)) which is equivalent to A XOR B
int simulateCircuitC(int A, int B) {
    int not_a = (!A);          // NOT A
    int not_b = (!B);          // NOT B
    int and1 = (A && not_b);   // A AND (NOT B)
    int and2 = (B && not_a);   // B AND (NOT A)
    return (and1 || and2);     // (A AND (NOT B)) OR (B AND (NOT A))
}

// Function to simulate Circuit (D)
// Logic: (NOT A) OR B
int simulateCircuitD(int A, int B) {
    int not_a = (!A);          // NOT A
    return (not_a || B);       // (NOT A) OR B
}

int main() {
    int A, B;
    int qA, qB, qC, qD;

    printf("--- Logic Circuit Comparison ---\n");
    printf("Truth table for each circuit (A, B, C, D):\n\n");

    printf("A | B | Q(A) | Q(B) | Q(C) | Q(D)\n");
    printf("--|---|------|------|------|------\n");

    // Iterate through all possible binary combinations for A and B
    for (A = 0; A <= 1; A++) {
        for (B = 0; B <= 1; B++) {
            // Simulate each circuit with the current inputs
            qA = simulateCircuitA(A, B);
            qB = simulateCircuitB(A, B);
            qC = simulateCircuitC(A, B);
            qD = simulateCircuitD(A, B);

            // Print the inputs and the outputs of all circuits
            printf("%d | %d | %4d | %4d | %4d | %4d\n", A, B, qA, qB, qC, qD);
        }
    }

    printf("\nAnalysis of the truth tables:\n");
    printf("- Circuits (A), (B), and (D) produce identical outputs, which is equivalent to (NOT A) OR B.\n");
    printf("- Circuit (C) produces the output for A XOR B, which is different from the other three.\n");
    printf("\nTherefore, Circuit (C) is the one that gives a different output compared to A, B, and D.\n");

    return 0;
}