# =====================================
# Diffie-Hellman Key Exchange
# =====================================

try:

    # Accept public values
    p = int(input("Enter the public prime (p): "))
    g = int(input("Enter the generator (g): "))

    print()

    # Accept private keys
    alice_private = int(input("Enter Alice's private key: "))
    bob_private = int(input("Enter Bob's private key: "))

except ValueError:

    print("\nError: Please enter whole numbers only.")

    exit()

# Generate public keys
alice_public = (g ** alice_private) % p
bob_public = (g ** bob_private) % p

# Compute shared secrets
alice_secret = (bob_public ** alice_private) % p
bob_secret = (alice_public ** bob_private) % p

# Display results
print("\n========================================")
print("     DIFFIE-HELLMAN KEY EXCHANGE")
print("========================================")

print("\nPublic Parameters")
print("------------------------------")
print("Public Prime (p) :", p)
print("Generator (g)    :", g)

print("\nPrivate Keys")
print("------------------------------")
print("Alice Private Key :", alice_private)
print("Bob Private Key   :", bob_private)

print("\nPublic Keys")
print("------------------------------")
print("Alice Public Key  :", alice_public)
print("Bob Public Key    :", bob_public)

print("\nShared Secret")
print("------------------------------")
print("Alice Secret      :", alice_secret)
print("Bob Secret        :", bob_secret)

if alice_secret == bob_secret:

    print("\nVerification      : SUCCESS")
    print("Shared Secret Key :", alice_secret)

else:

    print("\nVerification      : FAILED")