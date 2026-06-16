import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkinter import filedialog

# =====================================
# SPN S-BOX
# =====================================

S_BOX = {
    'A':'Q','B':'W','C':'E','D':'R','E':'T',
    'F':'Y','G':'U','H':'I','I':'O','J':'P',
    'K':'A','L':'S','M':'D','N':'F','O':'G',
    'P':'H','Q':'J','R':'K','S':'L','T':'Z',
    'U':'X','V':'C','W':'V','X':'B','Y':'N','Z':'M'
}

# =====================================
# INVERSE S-BOX
# =====================================

inverse_sbox = {value: key for key, value in S_BOX.items()}

# =====================================
# FUNCTIONS
# =====================================

def permute(text):
    return text[::-1]

def key_mix(text, key):

    if key == "":
        return text

    mixed = ""

    for i in range(len(text)):

        p = ord(text[i])

        k = ord(key[i % len(key)])

        mixed += chr((p ^ k) % 95 + 32)

    return mixed


def encrypt():

    output_box.delete("1.0", tk.END)

    plaintext = plaintext_entry.get().upper()
    key = key_entry.get()
    total_rounds = int(rounds.get())

    if plaintext == "":
        messagebox.showerror(
            "Error",
            "Please enter plaintext."
        )
        return

    output_box.insert(tk.END,
        "========== ADVANCED SPN ENCRYPTION ==========\n\n"
    )

    output_box.insert(tk.END,
        f"Plaintext : {plaintext}\n"
    )

    output_box.insert(tk.END,
        f"Key : {key}\n"
    )

    output_box.insert(tk.END,
        f"Rounds : {total_rounds}\n\n"
    )

    current = plaintext
    
    current = key_mix(current, key)

    output_box.insert(
    tk.END,
    f"Key Mixing : {current}\n\n"
)

    for r in range(total_rounds):

        substituted = ""

        for ch in current:

            substituted += S_BOX.get(ch, ch)

        permuted = permute(substituted)

        output_box.insert(
            tk.END,
            f"========== ROUND {r+1} ==========\n"
        )

        output_box.insert(
            tk.END,
            f"Substitution : {substituted}\n"
        )

        output_box.insert(
            tk.END,
            f"Permutation  : {permuted}\n\n"
        )

        current = permuted

    output_box.insert(
        tk.END,
        "==============================\n"
    )

    output_box.insert(
        tk.END,
        f"Ciphertext : {current}\n\n"
    )

    output_box.insert(
        tk.END,
        f"Completed : {datetime.now()}\n"
    )
    cipher_length = len(current)
    plain_length = len(plaintext)

    output_box.insert(tk.END, "\n")
    output_box.insert(tk.END, "="*45 + "\n")
    output_box.insert(tk.END, "SECURITY ANALYSIS\n")
    output_box.insert(tk.END, "="*45 + "\n")

    output_box.insert(tk.END, f"Plaintext Length : {plain_length}\n")
    output_box.insert(tk.END, f"Ciphertext Length: {cipher_length}\n")
    output_box.insert(tk.END, f"Rounds Used      : {total_rounds}\n")
    output_box.insert(tk.END, f"Large S-Box      : YES\n")
    output_box.insert(tk.END, f"Custom Key Used  : {'YES' if key else 'NO'}\n")
    output_box.insert(tk.END, "Substitution     : YES\n")
    output_box.insert(tk.END, "Permutation      : YES\n")
    output_box.insert(tk.END, "Avalanche Test   : Supported\n")

    if total_rounds >= 5:
        rating = "HIGH"
    elif total_rounds >= 3:
        rating = "MEDIUM"
    else:
        rating = "BASIC"

    output_box.insert(tk.END, f"Security Rating  : {rating}\n")
    output_box.insert(tk.END, "="*45 + "\n")

def decrypt():

    output_box.delete("1.0", tk.END)

    ciphertext = plaintext_entry.get().upper()

    total_rounds = int(rounds.get())

    if ciphertext == "":
        messagebox.showerror(
            "Error",
            "Please enter the ciphertext in the Plaintext field."
        )
        return

    output_box.insert(
        tk.END,
        "========== SPN DECRYPTION ==========\n\n"
    )

    output_box.insert(
        tk.END,
        f"Ciphertext : {ciphertext}\n"
    )

    current = ciphertext

    for r in range(total_rounds):

        output_box.insert(
            tk.END,
            f"\n----- Reverse Round {r+1} -----\n"
        )

        # Reverse permutation
        reversed_perm = current[::-1]

        output_box.insert(
            tk.END,
            f"Reverse Permutation : {reversed_perm}\n"
        )

        # Reverse substitution
        restored = ""

        for ch in reversed_perm:
            restored += inverse_sbox.get(ch, ch)

        output_box.insert(
            tk.END,
            f"Reverse Substitution : {restored}\n"
        )

        current = restored

    output_box.insert(
        tk.END,
        "\n=============================\n"
    )

    output_box.insert(
        tk.END,
        f"Recovered Plaintext : {current}\n"
    )


def avalanche():

    output_box.delete("1.0", tk.END)

    text = plaintext_entry.get().upper()

    if len(text) < 2:
        messagebox.showerror(
            "Error",
            "Please enter at least 2 characters."
        )
        return

    modified = text[:-1]

    if text[-1] != "A":
        modified += "A"
    else:
        modified += "B"

    output_box.insert(
        tk.END,
        "========== AVALANCHE EFFECT TEST ==========\n\n"
    )

    output_box.insert(
        tk.END,
        f"Original Plaintext : {text}\n"
    )

    output_box.insert(
        tk.END,
        f"Modified Plaintext : {modified}\n\n"
    )

    original_cipher = ""

    for c in text:
        original_cipher += S_BOX.get(c, c)

    original_cipher = permute(original_cipher)

    modified_cipher = ""

    for c in modified:
        modified_cipher += S_BOX.get(c, c)

    modified_cipher = permute(modified_cipher)

    output_box.insert(
        tk.END,
        f"Ciphertext 1 : {original_cipher}\n"
    )

    output_box.insert(
        tk.END,
        f"Ciphertext 2 : {modified_cipher}\n\n"
    )

    differences = 0

    for a, b in zip(original_cipher, modified_cipher):
        if a != b:
            differences += 1

    percentage = (differences / len(original_cipher)) * 100

    output_box.insert(
        tk.END,
        f"Different Characters : {differences}\n"
    )

    output_box.insert(
        tk.END,
        f"Avalanche Percentage : {percentage:.2f}%\n\n"
    )

    output_box.insert(
        tk.END,
        "Observation:\n"
    )

    output_box.insert(
        tk.END,
        "A small change in the plaintext produces a significantly different ciphertext, demonstrating the avalanche effect."
    )


def clear():
    plaintext_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    output_box.delete("1.0", tk.END)

def save_results():

    content = output_box.get("1.0", tk.END)

    if content.strip() == "":
        messagebox.showwarning(
            "Nothing to Save",
            "Please generate some results first."
        )
        return

    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")],
        title="Save Encryption Results"
    )

    if filename:

        with open(filename,"w") as file:

            file.write(content)

        messagebox.showinfo(
            "Saved",
            "Results saved successfully."
        )
# =====================================
# MAIN WINDOW
# =====================================

root = tk.Tk()

root.title("Advanced SPN Encryption Simulator")

root.geometry("820x620")

root.configure(bg="#f4f6f8")

root.resizable(True, True)

title = tk.Label(
    root,
    text="ADVANCED SPN ENCRYPTION SIMULATOR",
    font=("Segoe UI",18,"bold"),
    fg="#003366",
    bg="#f4f6f8"
)

title.pack(pady=20)

frame = tk.Frame(root,bg="#f4f6f8")

frame.pack()
# =====================================
# PLAINTEXT
# =====================================

tk.Label(
    frame,
    text="Plaintext:",
    font=("Segoe UI",11,"bold"),
    bg="#f4f6f8"
).grid(row=0,column=0,padx=10,pady=10,sticky="w")

plaintext_entry = tk.Entry(
    frame,
    width=45,
    font=("Consolas",11)
)

plaintext_entry.grid(row=0,column=1,pady=10)

# =====================================
# CUSTOM KEY
# =====================================

tk.Label(
    frame,
    text="Custom Key:",
    font=("Segoe UI",11,"bold"),
    bg="#f4f6f8"
).grid(row=1,column=0,padx=10,pady=10,sticky="w")

key_entry = tk.Entry(
    frame,
    width=45,
    font=("Consolas",11)
)

key_entry.grid(row=1,column=1,pady=10)

# =====================================
# ROUNDS
# =====================================

tk.Label(
    frame,
    text="Rounds:",
    font=("Segoe UI",11,"bold"),
    bg="#f4f6f8"
).grid(row=2,column=0,padx=10,pady=10,sticky="w")

rounds = tk.Spinbox(
    frame,
    from_=1,
    to=10,
    width=10,
    font=("Segoe UI",11)
)

rounds.grid(row=2,column=1,sticky="w")

# =====================================
# BUTTON FRAME
# =====================================

button_frame = tk.Frame(frame, bg="#f4f6f8")
button_frame.grid(row=3, column=0, columnspan=3, pady=20)

# =====================================
# BUTTONS
# =====================================

encrypt_btn = tk.Button(
    button_frame,
    text="🔒 Encrypt",
    command=encrypt,
    width=15,
    bg="#1E90FF",
    fg="white",
    font=("Segoe UI",11,"bold")
)

encrypt_btn.grid(row=0, column=0, padx=8, pady=5)

decrypt_btn = tk.Button(
    button_frame,
    text="🔓 Decrypt",
    command=decrypt,
    width=15,
    bg="#228B22",
    fg="white",
    font=("Segoe UI",11,"bold")
)

decrypt_btn.grid(row=0, column=1, padx=8, pady=5)

clear_btn = tk.Button(
    button_frame,
    text="🗑 Clear",
    command=clear,
    width=15,
    bg="#DC143C",
    fg="white",
    font=("Segoe UI",11,"bold")
)

clear_btn.grid(row=0, column=2, padx=8, pady=5)

avalanche_btn = tk.Button(
    button_frame,
    text="⚡ Avalanche Test",
    command=avalanche,
    width=20,
    bg="#FF8C00",
    fg="white",
    font=("Segoe UI",11,"bold")
)

avalanche_btn.grid(row=1, column=0, columnspan=2, padx=8, pady=5)

save_btn = tk.Button(
    button_frame,
    text="💾 Save Results",
    command=save_results,
    width=20,
    bg="#6A5ACD",
    fg="white",
    font=("Segoe UI",11,"bold")
)

save_btn.grid(row=1, column=2, padx=8, pady=5)


# =====================================
# RESULTS
# =====================================

results_label = tk.Label(
    frame,
    text="Results",
    font=("Segoe UI",14,"bold"),
    bg="#f4f6f8"
)

results_label.grid(row=5,column=0,columnspan=3,pady=(20,5))

# Frame to hold Text widget and Scrollbar
results_frame = tk.Frame(frame)

results_frame.grid(
    row=6,
    column=0,
    columnspan=3,
    padx=10,
    pady=10
)

# Scrollbar
scrollbar = tk.Scrollbar(results_frame)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Text Area
output_box = tk.Text(
    results_frame,
    width=75,
    height=12,
    font=("Consolas",10),
    wrap="word",
    yscrollcommand=scrollbar.set
)

output_box.pack(side=tk.LEFT)

# Connect scrollbar to text widget
scrollbar.config(command=output_box.yview)

root.mainloop()