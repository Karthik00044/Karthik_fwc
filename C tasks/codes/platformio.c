#include <stdio.h>

// Function to simulate the 4-to-1 multiplexer
// P and Q are select lines, R is the data input
// All inputs are assumed to be 0 or 1 (binary)
int simulateMultiplexer(int P, int Q, int R) {
    int f; // Output of the multiplexer

    // The select lines P (S1) and Q (S0) determine which input is passed to the output.
    // The inputs are:
    // I0 = R (when P=0, Q=0)
    // I1 = NOT R (when P=0, Q=1)
    // I2 = NOT R (when P=1, Q=0)
    // I3 = R (when P=1, Q=1)

    if (P == 0 && Q == 0) {
        // Selects input 0, which is R
        f = R;
    } else if (P == 0 && Q == 1) {
        // Selects input 1, which is NOT R
        f = !R; // !R performs logical NOT operation (0 becomes 1, 1 becomes 0)
    } else if (P == 1 && Q == 0) {
        // Selects input 2, which is NOT R
        f = !R;
    } else if (P == 1 && Q == 1) {
        // Selects input 3, which is R
        f = R;
    } else {
        // This case should ideally not be reached if inputs are strictly 0 or 1.
        // However, for robustness, we can set an error value or handle it.
        // For this simulation, we'll assume valid binary inputs.
        f = -1; // Indicate an error or invalid input
    }

    return f;
}

int main() {
    int P, Q, R;
    int result_f;

    printf("--- 4-to-1 Multiplexer Simulation ---\n");
    printf("Enter binary values (0 or 1) for P, Q, and R.\n\n");

    // Get input for P
    printf("Enter value for P (S1): ");
    // Loop until a valid binary input is received for P
    while (scanf("%d", &P) != 1 || (P != 0 && P != 1)) {
        printf("Invalid input. Please enter 0 or 1 for P: ");
        // Clear the input buffer to prevent infinite loop on invalid input
        while (getchar() != '\n');
    }

    // Get input for Q
    printf("Enter value for Q (S0): ");
    // Loop until a valid binary input is received for Q
    while (scanf("%d", &Q) != 1 || (Q != 0 && Q != 1)) {
        printf("Invalid input. Please enter 0 or 1 for Q: ");
        while (getchar() != '\n');
    }

    // Get input for R
    printf("Enter value for R: ");
    // Loop until a valid binary input is received for R
    while (scanf("%d", &R) != 1 || (R != 0 && R != 1)) {
        printf("Invalid input. Please enter 0 or 1 for R: ");
        while (getchar() != '\n');
    }

    // Simulate the multiplexer with the given inputs
    result_f = simulateMultiplexer(P, Q, R);

    // Print the solution (output f)
    if (result_f != -1) {
        printf("\nBased on the inputs:\n");
        printf("P = %d, Q = %d, R = %d\n", P, Q, R);
        printf("The output f = %d\n", result_f);
    } else {
        printf("\nAn error occurred due to invalid input values.\n");
    }

    return 0;
}