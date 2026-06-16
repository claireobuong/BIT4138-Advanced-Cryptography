# ===============================
# Basic SPN Encryption
# Week 6 - Practical Task 1
# ===============================

# Simple S-Box (Substitution Box)
sbox = {
    'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T',
    'F': 'Y', 'G': 'U', 'H': 'I', 'I': 'O', 'J': 'P',
    'K': 'A', 'L': 'S', 'M': 'D', 'N': 'F', 'O': 'G',
    'P': 'H', 'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'Z',
    'U': 'X', 'V': 'C', 'W': 'V', 'X': 'B', 'Y': 'N',
    'Z': 'M'
}

# -------------------------------
# Substitution Function
# -------------------------------
def substitute(text):
    result = ""

    for char in text:
        if char in sbox:
            result += sbox[char]
        else:
            result += char

    return result


# -------------------------------
# Permutation Function
# -------------------------------
def permute(text):
    return text[::-1]


# -------------------------------
# Main Program
# -------------------------------
print("=" * 40)
print("      BASIC SPN ENCRYPTION")
print("=" * 40)

plaintext = input("Enter plaintext: ").upper()

substituted = substitute(plaintext)

ciphertext = permute(substituted)

print("\nAfter Substitution :", substituted)
print("After Permutation  :", ciphertext)
print("\nCiphertext :", ciphertext)