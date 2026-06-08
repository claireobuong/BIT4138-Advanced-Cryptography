while True:
    print("\n===== ENCRYPTION MENU =====")
    print("1. Reverse Text")
    print("2. Convert to Uppercase")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        text = input("Enter text: ")
        print("Encrypted:", text[::-1])

    elif choice == "2":
        text = input("Enter text: ")
        print("Encrypted:", text.upper())

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")