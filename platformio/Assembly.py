from sympy import symbols, Or, Not, simplify_logic

P, Q, R = symbols('P Q R')

A = Not(Or(P, Q))   # Gate 1: NOR(P, Q)
B = Not(Or(Q, R))   # Gate 2: NOR(Q, R)
C = Not(Or(P, R))   # Gate 3: NOR(P, R)
D = Not(Or(Q, R))   # Gate 4: NOR(Q, R) again

E = Not(Or(A, B))   # Gate 5: NOR(A, B)
F = Not(Or(C, D))   # Gate 6: NOR(C, D)

f = Not(Or(E, F))   # Gate 7: NOR(E, F)

simplified_f = simplify_logic(f, form='dnf')
print("This program computes the Boolean expression for the output 'f' of a given NOR gate-based logic circuit step by step:\n")

print("Q.31  what is the boolean expression for the output f of the combinational logic circuit of nor gates given below?")
print("Solution: This program computes the Boolean expression for the output 'f' of a given NOR gate-based logic circuit step by step:\n")
print("First Layer Outputs:")
print(f"A = NOR(P, Q) = {A}")
print(f"B = NOR(Q, R) = {B}")
print(f"C = NOR(P, R) = {C}")
print(f"D = NOR(Q, R) = {D}")
print("\nSecond Layer Outputs:")
print(f"E = NOR(A, B) = {E}")
print(f"F = NOR(C, D) = {F}")
print("\nFinal Output:")
print(f"f = NOR(E, F) = {f}")
print("\nSimplified Boolean Expression for output f:")
print(simplified_f)