#include <stdio.h>
#include <stdbool.h> // For using bool type

// --- Basic Logic Gate Functions ---

// AND Gate: Returns true if both inputs are true
bool AND(bool A, bool B) {
    return A && B;
}

// OR Gate: Returns true if at least one input is true
bool OR(bool A, bool B) {
    return A || B;
}

// NOT Gate: Returns the inverse of the input
bool NOT(bool A) {
    return !A;
}

// --- Composite Logic Gate Functions (Column A & B) ---

// P / Column B-1: NOR Gate (NOT OR)
bool NOR(bool A, bool B) {
    return NOT(OR(A, B));
}

// Q / Column B-4: AND Gate (already defined, but for clarity)
// bool AND(bool A, bool B) { return A && B; }

// R / Column B-3: NAND Gate (NOT AND)
bool NAND(bool A, bool B) {
    return NOT(AND(A, B));
}

// S / Column B-2: OR Gate (already defined, but for clarity)
// bool OR(bool A, bool B) { return A || B; }


// Function to print boolean values as 0 or 1
void print_bool(bool val) {
    printf("%d", val ? 1 : 0);
}

int main() {
    printf("--- Logic Gate Equivalents Explanation ---\n\n");
    printf("Following the pairings from Option D:\n");
    printf("P (NOR) -> 4 (AND)\n");
    printf("Q (AND) -> 2 (OR)\n");
    printf("R (NAND) -> 3 (NAND)\n");
    printf("S (OR)  -> 1 (NOR)\n\n");

    printf("Verifying these specific pairings for all input combinations (A, B):\n\n");

    // Updated header for Option D pairings
    printf("| A | B | P (NOR) | B-4 (AND) | Q (AND) | B-2 (OR) | R (NAND) | B-3 (NAND) | S (OR) | B-1 (NOR) |\n");
    printf("|---|---|---------|-----------|---------|----------|----------|------------|--------|-----------|\n");

    // Test all possible input combinations for A and B
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            bool A = (bool)i;
            bool B = (bool)j;

            // Outputs of Column A gates
            bool p_nor_output = NOR(A, B);
            bool q_and_output = AND(A, B);
            bool r_nand_output = NAND(A, B);
            bool s_or_output = OR(A, B);

            // Outputs of Column B gates (all are calculated, we just pick the ones for Option D)
            bool b1_nor_output = NOR(A, B);
            bool b2_or_output = OR(A, B);
            bool b3_nand_output = NAND(A, B);
            bool b4_and_output = AND(A, B);

            printf("| ");
            print_bool(A);
            printf(" | ");
            print_bool(B);
            printf(" |    ");
            print_bool(p_nor_output);
            printf("    |     ");
            print_bool(b4_and_output); // P (NOR) vs B-4 (AND)
            printf("     |    ");
            print_bool(q_and_output);
            printf("    |    ");
            print_bool(b2_or_output);   // Q (AND) vs B-2 (OR)
            printf("    |     ");
            print_bool(r_nand_output);
            printf("    |      ");
            print_bool(b3_nand_output); // R (NAND) vs B-3 (NAND)
            printf("     |   ");
            print_bool(s_or_output);
            printf("  |     ");
            print_bool(b1_nor_output);  // S (OR) vs B-1 (NOR)
            printf("    |\n");
        }
    }

    printf("\nBased on the table above, we can observe the following:\n");
    printf("- P (NOR) and B-4 (AND) are NOT equivalent.\n");
    printf("- Q (AND) and B-2 (OR) are NOT equivalent.\n");
    printf("- R (NAND) and B-3 (NAND) ARE equivalent.\n");
    printf("- S (OR) and B-1 (NOR) are NOT equivalent.\n");
    printf("Therefore, while option D provides a set of pairings, only the R-3 pairing shows logical equivalence.\n");

    return 0;
}