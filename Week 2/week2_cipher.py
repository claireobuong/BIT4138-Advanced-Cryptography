def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char

    return result


message = input("Enter message: ")

while True:
    try:
        shift = int(input("Enter Caesar shift value: "))
        break
    except:
        print("Please enter a valid number.")

key = input("Enter Vigenere keyword: ")

caesar = caesar_encrypt(message, shift)
vigenere = vigenere_encrypt(message, key)

print("\n--- RESULTS ---")
print("Original :", message)
print("Caesar Encrypted :", caesar)
print("Caesar Decrypted :", caesar_decrypt(caesar, shift))
print("Vigenere Encrypted :", vigenere)