print("Match the logic gates column A with their Equalents in Column B");
print("Column A")
def NOR(a, b):
    return int(not (a or b))

def NAND(a, b):
    return int(not (a and b))

def EXOR(a, b):
    return int(a ^ b)  # XOR

def EXNOR(a, b):
    return int(not (a ^ b))  # XNOR
P=NOR
Q=NAND
R=EXOR
S=EXNOR
# Test all combinations of two binary inputs
inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

print("A B |  P    Q    R    S")
print("------------------------")
for a, b in inputs:
    print(f"{a} {b} |  {NOR(a, b)}    {NAND(a, b)}    {EXOR(a, b)}    {EXNOR(a, b)}")


print("Column B")
print("A B |  1    2    3    4")
print("------------------------")
for a, b in inputs:
    print(f"{a} {b} |  {EXNOR(a, b)}    {NAND(a, b)}    {EXOR(a, b)}    {NOR(a, b)}")
if P==2 and Q==4 and R==1 and S==3:
    print("A");
elif P==2 and Q==4 and R==3 and S==1:
    print("C")
elif P==4 and Q==2 and R==1 and S==3:
    print("B")
else:
    print("D")