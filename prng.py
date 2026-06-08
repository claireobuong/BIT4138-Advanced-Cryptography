seed = int(input("Enter seed value: "))

a = 5
c = 3
m = 16

print("\nGenerated Sequence:")

for i in range(20):
    seed = (a * seed + c) % m
    print(seed)