#include <stdio.h>

// Function to simulate a NOR gate
// NOR(A, B) is equivalent to NOT (A OR B)
int norGate(int A, int B) {
    return !(A || B);
}

// Function to simulate the entire combinational logic circuit
// Inputs: P, Q, R (binary: 0 or 1)
// Output: f
int simulateNorCircuit(int P, int Q, int R) {
    // First stage NOR gates
    int nor1_pq = norGate(P, Q); // Output of NOR gate with inputs P and Q
    int nor2_qr = norGate(Q, R); // Output of NOR gate with inputs Q and R
    int nor3_pr = norGate(P, R); // Output of NOR gate with inputs P and R
    int nor4_qr = norGate(Q, R); // Output of NOR gate with inputs Q and R (repeated from nor2_qr)

    // Second stage NOR gates
    // The diagram shows the output of nor1_pq and nor2_qr feeding into another NOR gate
    int nor5_top = norGate(nor1_pq, nor2_qr); // Output of NOR gate with inputs (P NOR Q) and (Q NOR R)

    // The diagram shows the output of nor3_pr and nor4_qr feeding into another NOR gate
    int nor6_bottom = norGate(nor3_pr, nor4_qr); // Output of NOR gate with inputs (P NOR R) and (Q NOR R)

    // Final stage NOR gate
    // The outputs of nor5_top and nor6_bottom feed into the final NOR gate to produce 'f'
    int f = norGate(nor5_top, nor6_bottom);

    return f;
}

int main() {
    int P, Q, R;
    int f_output;

    printf("--- NOR Gate Combinational Logic Circuit Simulation ---\n");
    printf("Truth table for the circuit:\n\n");

    printf("P | Q | R | f\n");
    printf("--|---|---|---\n");

    // Iterate through all possible binary combinations for P, Q, and R
    for (P = 0; P <= 1; P++) {
        for (Q = 0; Q <= 1; Q++) {
            for (R = 0; R <= 1; R++) {
                // Simulate the circuit for the current combination
                f_output = simulateNorCircuit(P, Q, R);

                // Print the inputs and the final output 'f'
                printf("%d | %d | %d | %d\n", P, Q, R, f_output);
            }
        }
    }

    printf("\nAnalysis of the truth table:\n");
    printf("By observing the truth table, we can determine the boolean expression for 'f'.\n");
    printf("Let's compare the output 'f' with the given options:\n");
    printf("Option (A): NOT (Q OR R)\n");
    printf("Option (B): P OR Q\n");
    printf("Option (C): NOT (P OR R)\n");
    printf("Option (D): NOT (P OR Q OR R)\n");
    printf("\nAfter running the simulation and comparing the 'f' column with the truth tables of the options,\n");
    printf("it is found that the output 'f' matches Option (A): NOT (Q OR R).\n");

    return 0;
}