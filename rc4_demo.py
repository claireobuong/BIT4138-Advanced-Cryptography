message = input("Enter message: ")
key = 7

encrypted = ""

for char in message:
    encrypted += chr(ord(char) ^ key)

print("Encrypted:", encrypted)

decrypted = ""

for char in encrypted:
    decrypted += chr(ord(char) ^ key)

print("Decrypted:", decrypted)