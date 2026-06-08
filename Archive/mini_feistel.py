left = int(input("Enter Left Value: "))
right = int(input("Enter Right Value: "))
key = int(input("Enter Key: "))

print("\nBefore Encryption")
print("Left :", left)
print("Right:", right)

new_left = right
new_right = left ^ (right ^ key)

print("\nAfter One Feistel Round")
print("Left :", new_left)
print("Right:", new_right)