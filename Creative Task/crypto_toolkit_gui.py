import tkinter as tk
from tkinter import messagebox
import random
import hashlib


# ==========================
# XOR STREAM CIPHER
# ==========================
def xor_encrypt():
    try:
        text = message_entry.get()
        key = int(key_entry.get())

        encrypted = ""

        for ch in text:
            encrypted += chr(ord(ch) ^ key)

        decrypted = ""

        for ch in encrypted:
            decrypted += chr(ord(ch) ^ key)

        output.delete("1.0", tk.END)

        output.insert(
            tk.END,
            "===== XOR STREAM CIPHER =====\n\n"
        )

        output.insert(
            tk.END,
            "Original Message:\n" + text + "\n\n"
        )

        output.insert(
            tk.END,
            "Encrypted Message:\n" + encrypted + "\n\n"
        )

        output.insert(
            tk.END,
            "Decrypted Message:\n" + decrypted
        )

    except:
        messagebox.showerror(
            "Error",
            "Please enter a valid XOR key."
        )


# ==========================
# RANDOMNESS ANALYZER
# ==========================
def randomness_test():

    sequence = [random.randint(0, 1) for i in range(20)]

    zeros = sequence.count(0)
    ones = sequence.count(1)

    output.delete("1.0", tk.END)

    output.insert(
        tk.END,
        "===== RANDOMNESS ANALYZER =====\n\n"
    )

    output.insert(
        tk.END,
        "Generated Sequence:\n"
    )

    output.insert(
        tk.END,
        str(sequence) + "\n\n"
    )

    output.insert(
        tk.END,
        "Zeros : " + str(zeros) + "\n"
    )

    output.insert(
        tk.END,
        "Ones  : " + str(ones) + "\n\n"
    )

    if abs(zeros - ones) <= 2:
        output.insert(
            tk.END,
            "Result: Good Frequency Balance"
        )
    else:
        output.insert(
            tk.END,
            "Result: Frequency Imbalance Detected"
        )


# ==========================
# BLOCK CIPHER SIMULATOR
# ==========================
def block_cipher():

    text = message_entry.get()

    blocks = [
        text[i:i+2]
        for i in range(0, len(text), 2)
    ]

    substituted = [b[::-1] for b in blocks]

    permuted = substituted[::-1]

    ciphertext = "".join(permuted)

    output.delete("1.0", tk.END)

    output.insert(
        tk.END,
        "===== BLOCK CIPHER SIMULATOR =====\n\n"
    )

    output.insert(
        tk.END,
        "Blocks:\n"
    )

    output.insert(
        tk.END,
        str(blocks) + "\n\n"
    )

    output.insert(
        tk.END,
        "Ciphertext:\n"
    )

    output.insert(
        tk.END,
        ciphertext
    )


# ==========================
# AVALANCHE EFFECT
# ==========================
def avalanche():

    text1 = message_entry.get()

    if len(text1) == 0:
        return

    text2 = text1[:-1] + "X"

    hash1 = hashlib.sha256(
        text1.encode()
    ).hexdigest()

    hash2 = hashlib.sha256(
        text2.encode()
    ).hexdigest()

    difference = 0

    for a, b in zip(hash1, hash2):
        if a != b:
            difference += 1

    percentage = (
        difference / len(hash1)
    ) * 100

    output.delete("1.0", tk.END)

    output.insert(
        tk.END,
        "===== AVALANCHE EFFECT =====\n\n"
    )

    output.insert(
        tk.END,
        "Original Message:\n"
        + text1 + "\n\n"
    )

    output.insert(
        tk.END,
        "Modified Message:\n"
        + text2 + "\n\n"
    )

    output.insert(
        tk.END,
        "Hash Difference:\n"
    )

    output.insert(
        tk.END,
        str(round(percentage, 2))
        + "%"
    )


# ==========================
# DIGITAL FINGERPRINT
# ==========================
def fingerprint():

    text = message_entry.get()

    hash_value = hashlib.sha256(
        text.encode()
    ).hexdigest()

    output.delete("1.0", tk.END)

    output.insert(
        tk.END,
        "===== DIGITAL FINGERPRINT =====\n\n"
    )

    output.insert(
        tk.END,
        "SHA-256 Hash:\n\n"
    )

    output.insert(
        tk.END,
        hash_value
    )


# ==========================
# WINDOW
# ==========================
root = tk.Tk()
root.title("Advanced Cryptography Toolkit")
root.geometry("700x600")


title = tk.Label(
    root,
    text="ADVANCED CRYPTOGRAPHY TOOLKIT",
    font=("Arial", 16, "bold")
)

title.pack(pady=10)


tk.Label(
    root,
    text="Message"
).pack()

message_entry = tk.Entry(
    root,
    width=50
)

message_entry.pack()


tk.Label(
    root,
    text="XOR Key"
).pack()

key_entry = tk.Entry(
    root,
    width=10
)

key_entry.pack()


tk.Button(
    root,
    text="XOR Stream Cipher",
    width=25,
    command=xor_encrypt
).pack(pady=4)


tk.Button(
    root,
    text="Randomness Analyzer",
    width=25,
    command=randomness_test
).pack(pady=4)


tk.Button(
    root,
    text="Block Cipher Simulator",
    width=25,
    command=block_cipher
).pack(pady=4)


tk.Button(
    root,
    text="Avalanche Effect",
    width=25,
    command=avalanche
).pack(pady=4)


tk.Button(
    root,
    text="Digital Fingerprint",
    width=25,
    command=fingerprint
).pack(pady=4)


output = tk.Text(
    root,
    height=16,
    width=75
)

output.pack(pady=10)


root.mainloop()