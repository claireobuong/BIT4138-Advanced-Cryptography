while True:
    print("\n===== MINI CRYPTANALYSIS TOOLKIT =====")
    print("1. LFSR Generator")
    print("2. Randomness Testing")
    print("3. RC4 Stream Cipher Simulation")
    print("4. AES Encryption Tool")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        print("LFSR Generator selected.")
        print("Used for generating and analyzing binary sequences.")

    elif choice == "2":
        print("Randomness Testing selected.")
        print("Performs frequency, runs, and mean analysis.")

    elif choice == "3":
        print("RC4 Stream Cipher Simulation selected.")
        print("Demonstrates XOR-based stream encryption.")

    elif choice == "4":
        print("AES Encryption Tool selected.")
        print("Provides secure symmetric encryption and decryption.")

    elif choice == "5":
        print("Exiting toolkit.")
        break

    else:
        print("Invalid option.")