import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
import random
import string

# ============================
# Main Window
# ============================

root = tk.Tk()
root.title("Block Cipher Security Analyzer")
root.geometry("800x600")
root.configure(bg="#f4f6f8")
root.resizable(True, True)

# ============================
# Title
# ============================

title = tk.Label(
    root,
    text="BLOCK CIPHER SECURITY ANALYZER",
    font=("Segoe UI", 20, "bold"),
    bg="#f4f6f8",
    fg="#003366"
)
title.pack(pady=10)

# ============================
# Main Frame
# ============================

frame = tk.Frame(root, bg="#f4f6f8")
frame.pack(pady=5)

# ============================
# Plaintext 1
# ============================

tk.Label(
    frame,
    text="Plaintext 1:",
    font=("Segoe UI", 11, "bold"),
    bg="#f4f6f8"
).grid(row=0, column=0, padx=10, pady=10, sticky="w")

plaintext1_entry = tk.Entry(
    frame,
    width=50,
    font=("Consolas", 11)
)
plaintext1_entry.grid(row=0, column=1, pady=10)

# ============================
# Plaintext 2
# ============================

tk.Label(
    frame,
    text="Plaintext 2:",
    font=("Segoe UI", 11, "bold"),
    bg="#f4f6f8"
).grid(row=1, column=0, padx=10, pady=10, sticky="w")

plaintext2_entry = tk.Entry(
    frame,
    width=50,
    font=("Consolas", 11)
)
plaintext2_entry.grid(row=1, column=1, pady=10)

# ============================
# Results Area
# ============================

tk.Label(
    frame,
    text="Results",
    font=("Segoe UI", 14, "bold"),
    bg="#f4f6f8"
).grid(row=5, column=0, columnspan=3, pady=(15, 5))

output_box = tk.Text(
    frame,
    width=75,
    height=16,
    font=("Consolas",10)
)
output_box.grid(row=6, column=0, columnspan=3, padx=20, pady=5)

# Vertical Scrollbar

vertical_scroll = tk.Scrollbar(
    frame,
    orient="vertical",
    command=output_box.yview
)

vertical_scroll.grid(
    row=6,
    column=3,
    sticky="ns"
)

# Horizontal Scrollbar

horizontal_scroll = tk.Scrollbar(
    frame,
    orient="horizontal",
    command=output_box.xview
)

horizontal_scroll.grid(
    row=7,
    column=0,
    columnspan=3,
    sticky="ew"
)

output_box.config(
    yscrollcommand=vertical_scroll.set,
    xscrollcommand=horizontal_scroll.set,
    wrap="none"
)

# ============================
# Export Results
# ============================

def export_results():

    data = output_box.get("1.0", tk.END)

    if data.strip() == "":

        messagebox.showwarning(
            "No Data",
            "There are no results to export."
        )

        return

    filename = filedialog.asksaveasfilename(

        defaultextension=".txt",

        filetypes=[
            ("Text Files","*.txt"),
            ("All Files","*.*")
        ]
    )

    if filename:

        with open(filename,"w") as file:

            file.write(data)

        messagebox.showinfo(
            "Export Successful",
            "Results exported successfully."
        )

# ============================
# Avalanche Effect
# ============================

def avalanche():

    output_box.delete("1.0", tk.END)

    text1 = plaintext1_entry.get().upper()
    text2 = plaintext2_entry.get().upper()

    if text1 == "" or text2 == "":
        output_box.insert(
            tk.END,
            "Please enter both plaintext inputs."
        )
        return

    length = max(len(text1), len(text2))

    text1 = text1.ljust(length)
    text2 = text2.ljust(length)

    changed = 0

    for i in range(length):

        if text1[i] != text2[i]:
            changed += 1

    percentage = (changed / length) * 100

    output_box.insert(
        tk.END,
        "========== AVALANCHE EFFECT ==========\n\n"
    )

    output_box.insert(
        tk.END,
        f"Characters Compared : {length}\n"
    )

    output_box.insert(
        tk.END,
        f"Characters Changed  : {changed}\n"
    )

    output_box.insert(
        tk.END,
        f"Change Percentage   : {percentage:.2f}%\n\n"
    )

    if percentage >= 50:
        output_box.insert(
            tk.END,
            "Observation: Strong avalanche effect."
        )
    elif percentage >= 25:
        output_box.insert(
            tk.END,
            "Observation: Moderate avalanche effect."
        )
    else:
        output_box.insert(
            tk.END,
            "Observation: Weak avalanche effect."
        )

# ============================
# Statistical Bias
# ============================

def statistical_bias():

    output_box.delete("1.0", tk.END)

    text = plaintext1_entry.get().upper().replace(" ", "")

    if text == "":
        output_box.insert(
            tk.END,
            "Please enter Plaintext 1."
        )
        return

    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    total = len(text)
    unique = len(frequency)

    most_common = max(frequency, key=frequency.get)
    highest = frequency[most_common]

    bias = (highest / total) * 100

    output_box.insert(
        tk.END,
        "========== STATISTICAL BIAS ==========\n\n"
    )

    output_box.insert(
        tk.END,
        f"Total Characters : {total}\n"
    )

    output_box.insert(
        tk.END,
        f"Unique Characters: {unique}\n"
    )

    output_box.insert(
        tk.END,
        f"Most Common      : {most_common}\n"
    )

    output_box.insert(
        tk.END,
        f"Occurrences      : {highest}\n"
    )

    output_box.insert(
        tk.END,
        f"Bias Percentage  : {bias:.2f}%\n\n"
    )

    if bias > 40:
        output_box.insert(
            tk.END,
            "Observation: High statistical bias detected."
        )
    elif bias > 25:
        output_box.insert(
            tk.END,
            "Observation: Moderate statistical bias detected."
        )
    else:
        output_box.insert(
            tk.END,
            "Observation: Low statistical bias detected."
        )
# ============================
# Random Plaintext Generator
# ============================

def generate_random():

    plaintext_entry = ''.join(
        random.choice(string.ascii_uppercase)
        for _ in range(12)
    )

    plaintext1_entry.delete(0, tk.END)
    plaintext1_entry.insert(0, plaintext_entry)

    plaintext2_entry.delete(0, tk.END)
    plaintext2_entry.insert(0, plaintext_entry) 

# ============================
# Frequency Analysis
# ============================

def frequency_analysis():

    output_box.delete("1.0", tk.END)

    text = plaintext1_entry.get().upper()

    if text == "":
        output_box.insert(
            tk.END,
            "Please enter Plaintext 1."
        )
        return

    output_box.insert(
        tk.END,
        "========== FREQUENCY ANALYSIS ==========\n\n"
    )

    frequency = {}

    for char in text:

        if char != " ":

            frequency[char] = frequency.get(char, 0) + 1

    output_box.insert(
        tk.END,
        "Character    Frequency\n"
    )

    output_box.insert(
        tk.END,
        "-----------------------------\n"
    )

    for char in sorted(frequency):

        output_box.insert(
            tk.END,
            f"{char:^10} {frequency[char]:>8}\n"
        )

    output_box.insert(
        tk.END,
        "\n----------------------------------\n"
    )

    output_box.insert(
        tk.END,
        f"Total Characters : {len(text.replace(' ', ''))}\n"
    )

    # ============================
    # Frequency Chart
    # ============================

    characters = list(frequency.keys())
    counts = list(frequency.values())

    plt.figure(figsize=(8,4))

    plt.bar(
        characters,
        counts,
        edgecolor="black"
    )

    plt.title("Character Frequency Distribution")

    plt.xlabel("Characters")

    plt.ylabel("Frequency")

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()

    plt.show()

# ============================
# Clear Function
# ============================

def clear():

    plaintext1_entry.delete(0, tk.END)

    plaintext2_entry.delete(0, tk.END)

    output_box.delete("1.0", tk.END)

# ============================
# Analyze Function
# ============================

def analyze():

    output_box.delete("1.0", tk.END)

    text1 = plaintext1_entry.get().upper()
    text2 = plaintext2_entry.get().upper()

    if text1 == "" or text2 == "":
        output_box.insert(
            tk.END,
            "Please enter both plaintext inputs."
        )
        return

    output_box.insert(
        tk.END,
        "========== DIFFERENCE ANALYSIS ==========\n\n"
    )

    length = min(len(text1), len(text2))
    differences = 0

    for i in range(length):

        if text1[i] != text2[i]:

            differences += 1

            output_box.insert(
                tk.END,
                f"Position {i+1}: {text1[i]} → {text2[i]}\n"
            )

    output_box.insert(
        tk.END,
        "\n----------------------------------\n"
    )

    output_box.insert(
        tk.END,
        f"Total Differences : {differences}\n"
    )

    output_box.insert(
        tk.END,
        f"Length Compared   : {length}\n"
    )

    if differences == 0:
        output_box.insert(
            tk.END,
            "\nObservation: Both plaintexts are identical."
        )
    else:
        output_box.insert(
            tk.END,
            "\nObservation: Differences were detected."
        )

# ============================
# Buttons
# ============================

# First Row

analyze_btn = tk.Button(
    frame,
    text="Analyze",
    command=analyze,
    width=16,
    bg="#1E90FF",
    fg="white",
    font=("Segoe UI",11,"bold")
)
analyze_btn.grid(row=2, column=0, padx=8, pady=10)

frequency_btn = tk.Button(
    frame,
    text="Frequency",
    command=frequency_analysis,
    width=16,
    bg="#228B22",
    fg="white",
    font=("Segoe UI",11,"bold")
)
frequency_btn.grid(row=2, column=1, padx=8, pady=10)

avalanche_btn = tk.Button(
    frame,
    text="Avalanche Test",
    command=avalanche,
    width=16,
    bg="#FF8C00",
    fg="white",
    font=("Segoe UI",11,"bold")
)
avalanche_btn.grid(row=2, column=2, padx=8, pady=10)

# Second Row

bias_btn = tk.Button(
    frame,
    text="Statistical Bias",
    command=statistical_bias,
    width=16,
    bg="#8B008B",
    fg="white",
    font=("Segoe UI",11,"bold")
)
bias_btn.grid(row=3, column=0, padx=8, pady=10)

export_btn = tk.Button(
    frame,
    text="Export",
    command=export_results,
    width=16,
    bg="#800080",
    fg="white",
    font=("Segoe UI",11,"bold")
)
export_btn.grid(row=3, column=1, padx=8, pady=10)

random_btn = tk.Button(
    frame,
    text="Random",
    command=generate_random,
    width=16,
    bg="#20B2AA",
    fg="white",
    font=("Segoe UI",11,"bold")
)
random_btn.grid(row=3, column=2, padx=8, pady=10)

clear_btn = tk.Button(
    frame,
    text="Clear",
    command=clear,
    width=16,
    bg="#DC143C",
    fg="white",
    font=("Segoe UI",11,"bold")
)
clear_btn.grid(row=4, column=0, columnspan=3, pady=15)

# ============================
# Start Program
# ============================

root.mainloop()