# ==========================================
# Week 7 Practical Task 1
# Differential Cryptanalysis Simulation
# ==========================================

print("=" * 50)
print("DIFFERENTIAL CRYPTANALYSIS SIMULATION")
print("=" * 50)

plaintext1 = input("Enter first plaintext : ").upper()
plaintext2 = input("Enter second plaintext: ").upper()

print("\nComparing plaintexts...\n")

length = min(len(plaintext1), len(plaintext2))

differences = 0

for i in range(length):

    if plaintext1[i] != plaintext2[i]:
        differences += 1
        print(
            f"Position {i+1}: "
            f"{plaintext1[i]} -> {plaintext2[i]}"
        )

print("\n-----------------------------")
print("Total Differences :", differences)

if differences == 0:
    print("Observation: Both plaintexts are identical.")
else:
    print("Observation: The plaintexts contain different characters.")