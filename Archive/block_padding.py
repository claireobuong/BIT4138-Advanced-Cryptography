text = input("Enter text: ")

block_size = 4

while len(text) % block_size != 0:
    text += "X"

blocks = [text[i:i+block_size] for i in range(0, len(text), block_size)]

print("\nPadded Text:")
print(text)

print("\nBlocks:")
for block in blocks:
    print(block)