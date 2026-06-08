import random
import time

while True:
    print("\n===== RANDOMNESS TEST MENU =====")
    print("1. Generate Random Sequence")
    print("2. Exit")

    choice = input("Choose option: ")

    if choice == "1":

        length = int(input("Enter sequence length: "))

        sequence = [random.randint(0, 1) for i in range(length)]

        print("\nGenerated Sequence:")
        print(sequence)

        zeros = sequence.count(0)
        ones = sequence.count(1)

        print("\nFrequency Test")
        print("Zeros:", zeros)
        print("Ones :", ones)

        runs = 1
        for i in range(1, len(sequence)):
            if sequence[i] != sequence[i - 1]:
                runs += 1

        print("\nRuns Test")
        print("Total Runs:", runs)

        mean = sum(sequence) / len(sequence)

        print("\nMean Test")
        print("Mean:", mean)

        with open("results.txt", "w") as file:
            file.write("Generated Sequence:\n")
            file.write(str(sequence))
            file.write("\n\nZeros: " + str(zeros))
            file.write("\nOnes: " + str(ones))
            file.write("\nRuns: " + str(runs))
            file.write("\nMean: " + str(mean))

        print("\nResults saved to results.txt")

    elif choice == "2":
        break

    else:
        print("Invalid choice.")