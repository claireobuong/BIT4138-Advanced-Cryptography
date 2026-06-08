text = input("Enter text: ")

round1 = text[::-1]
round2 = round1.upper()
round3 = round2[::-1]

print("\nOriginal Text :", text)
print("Round 1       :", round1)
print("Round 2       :", round2)
print("Round 3       :", round3)