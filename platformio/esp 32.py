# Define logic gate functions
def AND(x, y):
    return x & y

def OR(x, y):
    return x | y

def NOR(x, y):
    return int(not (x | y))

# Define the circuit output function
def logic_circuit_output(A, B, C):
    and1 = AND(A, B)
    and2 = AND(B, C)
    or1 = OR(and1, and2)
    F = NOR(or1, C)
    return F

# Define all options
options = {
    "A": (1, 1, 0),
    "B": (1, 0, 0),
    "C": (0, 1, 0),
    "D": (0, 0, 1),
}

# Check each option
print("Verifying each option for output F = 1\n")
for key, (A, B, C) in options.items():
    result = logic_circuit_output(A, B, C)
    print(f"Option {key}: A={A}, B={B}, C={C} -> F = {result} {'✅ Valid' if result == 1 else '❌ Invalid'}")

# Final answer
print("\nCorrect Option: C (A = 0, B = 1, C = 0)")