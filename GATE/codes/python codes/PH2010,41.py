
from itertools import product
print("Q.41  For any set of inputs,A and B,the following circuits give the same output,Q,except one.which one is it?")
print("Solution: here is the solution :")
def circuit_A(A, B):
    or_gate = A or B
    not_b = int(not B)
    return int(or_gate and not_b)
def circuit_B(A, B):
    not_b = int(not B)
    return int(A and not_b)
def circuit_C(A, B):
    not_a = int(not A)
    not_b = int(not B)
    and1 = int(A and not_b)
    and2 = int(not_a and B)
    return int(and1 or and2)
def circuit_D(A, B):
    not_a = int(not A)
    return int(not_a or B)
results = []
inputs = list(product([0, 1], repeat=2))
for A, B in inputs:
    qa = circuit_A(A, B)
    qb = circuit_B(A, B)
    qc = circuit_C(A, B)
    qd = circuit_D(A, B)
    results.append((A, B, qa, qb, qc, qd))
for r in results:
    print(f"A={r[0]} B={r[1]} => Q_A: {r[2]}, Q_B: {r[3]}, Q_C: {r[4]}, Q_D: {r[5]}")
print("\nCorrect Option: (D)")

                                                                                                                                                       
                                                                                                                                                       
                                                                                                                                                   
