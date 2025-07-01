#include <stdio.h>

// Function to simulate the logic circuit
// A, B, C are binary inputs (0 or 1)
// The function returns the output F
int simulateLogicCircuit(int A, int B, int C) {
    int output_xor1;    // Output of the first XOR gate (A XOR B)
    int output_xnor2;   // Output of the second XNOR gate (A XNOR B)
    int F;              // Final output of the three-input XNOR gate

    // First gate: XOR (A, B)
    // The symbol '^' in C performs bitwise XOR.
    output_xor1 = (A ^ B);

    // Second gate: XNOR (A, B)
    // XNOR is equivalent to NOT (A XOR B)
    // Or, it can be implemented as (A == B) for binary inputs
    output_xnor2 = !(A ^ B); // Using NOT (XOR) for XNOR

    // Final gate: Three-input XNOR gate
    // Inputs are output_xor1, output_xnor2, and C
    // An n-input XNOR gate can be implemented as NOT (input1 XOR input2 XOR ... XOR inputN)
    // So, F = NOT ( (output_xor1 XOR output_xnor2) XOR C )
    F = !((output_xor1 ^ output_xnor2) ^ C);

    // The output of the final XNOR gate is F
    return F;
}

int main() {
    int A, B, C;
    int F;
    int found_solution = 0; // Flag to check if a solution is found

    printf("--- Logic Circuit Simulation ---\n");
    printf("Finding input combination (A, B, C) for which output F = 1.\n\n");

    // Iterate through all possible binary combinations for A, B, and C
    for (A = 0; A <= 1; A++) {
        for (B = 0; B <= 1; B++) {
            for (C = 0; C <= 1; C++) {
                // Simulate the circuit for the current combination
                F = simulateLogicCircuit(A, B, C);

                // Check if the output F is 1
                if (F == 1) {
                    printf("Solution found: F = 1 when A = %d, B = %d, C = %d\n", A, B, C);
                    found_solution = 1; // Set flag to true
                }
            }
        }
    }

    if (!found_solution) {
        printf("No input combination found that results in F = 1.\n");
    }

    printf("\n--- Truth Table for the Logic Circuit ---\n");
    printf("A | B | C | F\n");
    printf("--|---|---|---\n");
    for (A = 0; A <= 1; A++) {
        for (B = 0; B <= 1; B++) {
            for (C = 0; C <= 1; C++) {
                F = simulateLogicCircuit(A, B, C);
                printf("%d | %d | %d | %d\n", A, B, C, F);
            }
        }
    }

    return 0;
}