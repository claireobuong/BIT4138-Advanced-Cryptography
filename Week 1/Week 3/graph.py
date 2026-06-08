import random
import matplotlib.pyplot as plt

length = int(input("Enter sequence length: "))

sequence = [random.randint(0, 1) for i in range(length)]

plt.plot(sequence, marker='o')
plt.title("Random Binary Sequence")
plt.xlabel("Position")
plt.ylabel("Bit Value")
plt.grid(True)

plt.show()