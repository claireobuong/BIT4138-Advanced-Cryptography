def xor_encrypt(text, key):
    result = ""
    for char in text:
        if char == " ":
            result += " "
        else:
            result += chr(ord(char) ^ key)
    return result


while True:
    print("\n===== STREAM CIPHER MENU =====")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        message = input("Enter message: ")
        key = int(input("Enter numeric key: "))
        encrypted = xor_encrypt(message, key)
        print("Encrypted Message:", encrypted)

    elif choice == "2":
        message = input("Enter encrypted message: ")
        key = int(input("Enter numeric key: "))
        decrypted = xor_encrypt(message, key)
        print("Decrypted Message:", decrypted)

    elif choice == "3":
        print("Program Closed.")
        break

    else:
        print("Invalid choice.")