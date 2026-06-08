text = input("Enter text: ")

# Block division
blocks = [text[i:i+2] for i in range(0, len(text), 2)]

print("\nBlocks:")
print(blocks)

# Simple substitution
substituted = [block[::-1] for block in blocks]

print("\nSubstitution:")
print(substituted)

# Simple permutation
permuted = substituted[::-1]

print("\nPermutation:")
print(permuted)

print("\nFinal Cipher:")
print("".join(permuted))