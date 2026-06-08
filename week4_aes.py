from cryptography.fernet import Fernet
import time

# Generate Key
key = Fernet.generate_key()
cipher = Fernet(key)

print("Generated Key:")
print(key.decode())

# User input
message = input("\nEnter message to encrypt: ")

# Encryption
start = time.time()
encrypted = cipher.encrypt(message.encode())
end = time.time()

print("\nEncrypted Message:")
print(encrypted.decode())

# Decryption
decrypted = cipher.decrypt(encrypted)

print("\nDecrypted Message:")
print(decrypted.decode())

print("\nEncryption Time:")
print(end - start, "seconds")

# Save encrypted data
with open("encrypted.txt", "wb") as file:
    file.write(encrypted)

print("\nEncrypted file saved as encrypted.txt")