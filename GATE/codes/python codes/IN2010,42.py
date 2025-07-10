
from sympy import symbols, Not, And, simplify_logic

X, Y = symbols('X Y')
# NAND gate implementation
def NAND(a, b):
    return Not(And(a, b))

not_X = NAND(X, X)  # ¬X
not_Y = NAND(Y, Y)  # ¬Y

a = NAND(X, not_Y)  # ¬(X ∧ ¬Y)
b = NAND(Y, not_X)  # ¬(Y ∧ ¬X)

xor = NAND(a, b)  # = (X ∧ ¬Y) ∨ (Y ∧ ¬X)

xnor = NAND(xor, xor)  # = ¬(X ⊕ Y)

simplified_output = simplify_logic(xnor)
print("Q.42  The logic gate circuit shown in the adjoining figure realizes the function:\n")
print("This program models the logic circuit using only NAND gates and shows that it implements the XNOR function:\n")
print(f"¬X = {not_X}")
print(f"¬Y = {not_Y}")
print(f"¬(X ∧ ¬Y) = {a}")
print(f"¬(Y ∧ ¬X) = {b}")
print(f"XOR = {xor}")
print(f"XNOR = {xnor}")
print("\nSimplified Output Expression for Z:")
print(simplified_output)
# Final Answer
print("\n✅ Correct Option: (B) XNOR")

