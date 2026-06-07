from cryptography.fernet import Fernet

# Generate a secret key
key = Fernet.generate_key()

# Create a cipher object
cipher = Fernet(key)

# Message to encrypt
message = b"Hello Advanced Cryptography"

# Encrypt the message
encrypted = cipher.encrypt(message)

# Decrypt the message
decrypted = cipher.decrypt(encrypted)

print("Original Message :", message.decode())
print("Encrypted Message:", encrypted.decode())
print("Decrypted Message:", decrypted.decode())