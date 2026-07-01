import tkinter as tk
from tkinter import messagebox, filedialog

# =====================================
# Main Window
# =====================================

root = tk.Tk()
root.title("Diffie-Hellman Key Exchange")
root.geometry("780x650")
root.configure(bg="#f4f6f8")
root.resizable(False, False)

# =====================================
# Main Frame
# =====================================

frame = tk.Frame(root, bg="#f4f6f8")
frame.pack(fill="both", expand=True, padx=20, pady=20)

# =====================================
# Title
# =====================================

title = tk.Label(
    frame,
    text="DIFFIE-HELLMAN KEY EXCHANGE",
    font=("Segoe UI", 20, "bold"),
    bg="#f4f6f8",
    fg="#003366"
)
title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# =====================================
# Public Parameters
# =====================================

tk.Label(
    frame,
    text="Public Prime (p)",
    font=("Segoe UI", 11),
    bg="#f4f6f8"
).grid(row=1, column=0, sticky="w", pady=5)

p_entry = tk.Entry(frame, width=30, font=("Segoe UI", 11))
p_entry.grid(row=1, column=1, sticky="w", pady=5)

tk.Label(
    frame,
    text="Generator (g)",
    font=("Segoe UI", 11),
    bg="#f4f6f8"
).grid(row=2, column=0, sticky="w", pady=5)

g_entry = tk.Entry(frame, width=30, font=("Segoe UI", 11))
g_entry.grid(row=2, column=1, sticky="w", pady=5)

# =====================================
# Private Keys
# =====================================

tk.Label(
    frame,
    text="Alice's Private Key",
    font=("Segoe UI", 11),
    bg="#f4f6f8"
).grid(row=3, column=0, sticky="w", pady=5)

alice_entry = tk.Entry(frame, width=30, font=("Segoe UI", 11))
alice_entry.grid(row=3, column=1, sticky="w", pady=5)

tk.Label(
    frame,
    text="Bob's Private Key",
    font=("Segoe UI", 11),
    bg="#f4f6f8"
).grid(row=4, column=0, sticky="w", pady=5)

bob_entry = tk.Entry(frame, width=30, font=("Segoe UI", 11))
bob_entry.grid(row=4, column=1, sticky="w", pady=(5, 20))

# =====================================
# Button Frame
# =====================================

button_frame = tk.Frame(frame, bg="#f4f6f8")
button_frame.grid(row=5, column=0, columnspan=2, pady=10)

# =====================================
# Output Box
# =====================================

output_box = tk.Text(
    frame,
    width=90,
    height=18,
    font=("Consolas", 10),
    wrap="word"
)

output_box.grid(
    row=6,
    column=0,
    columnspan=2,
    pady=10
)

# =====================================
# Scrollbar
# =====================================

scrollbar = tk.Scrollbar(
    frame,
    orient="vertical",
    command=output_box.yview
)

scrollbar.grid(
    row=6,
    column=2,
    sticky="ns"
)

output_box.configure(
    yscrollcommand=scrollbar.set
)

# =====================================
# Generate Shared Secret
# =====================================

def generate_key():

    output_box.delete("1.0", tk.END)

    try:
        p = int(p_entry.get())
        g = int(g_entry.get())

        alice_private = int(alice_entry.get())
        bob_private = int(bob_entry.get())

    except ValueError:

        messagebox.showerror(
            "Input Error",
            "Please enter valid whole numbers."
        )

        return

    alice_public = pow(g, alice_private, p)
    bob_public = pow(g, bob_private, p)

    alice_secret = pow(bob_public, alice_private, p)
    bob_secret = pow(alice_public, bob_private, p)

    if alice_secret == bob_secret:
        verification = "SUCCESS"
        communication = "Secure"
    else:
        verification = "FAILED"
        communication = "Not Secure"

    output_box.insert(
        tk.END,
        "========================================\n"
    )

    output_box.insert(
        tk.END,
        "      DIFFIE-HELLMAN KEY EXCHANGE\n"
    )

    output_box.insert(
        tk.END,
        "========================================\n\n"
    )

    output_box.insert(
        tk.END,
        f"Public Prime (p) : {p}\n"
    )

    output_box.insert(
        tk.END,
        f"Generator (g)    : {g}\n\n"
    )

    output_box.insert(
        tk.END,
        f"Alice Private Key : {alice_private}\n"
    )

    output_box.insert(
        tk.END,
        f"Bob Private Key   : {bob_private}\n\n"
    )

    output_box.insert(
        tk.END,
        f"Alice Public Key : {alice_public}\n"
    )

    output_box.insert(
        tk.END,
        f"Bob Public Key   : {bob_public}\n\n"
    )

    output_box.insert(
        tk.END,
        f"Alice Secret : {alice_secret}\n"
    )

    output_box.insert(
        tk.END,
        f"Bob Secret   : {bob_secret}\n\n"
    )

    output_box.insert(
        tk.END,
        f"Verification : {verification}\n"
    )

    output_box.insert(
        tk.END,
        f"Shared Secret : {alice_secret}\n\n"
    )

    output_box.insert(
        tk.END,
        "========================================\n"
    )

    output_box.insert(
        tk.END,
        "Security Summary\n"
    )

    output_box.insert(
        tk.END,
        "========================================\n\n"
    )

    output_box.insert(
        tk.END,
        f"Shared Secret Established : {'Yes' if verification == 'SUCCESS' else 'No'}\n"
    )

    output_box.insert(
        tk.END,
        f"Verification Status       : {verification}\n"
    )

    output_box.insert(
        tk.END,
        f"Communication Status      : {communication}"
    )


# =====================================
# Clear Results
# =====================================

def clear_results():

    p_entry.delete(0, tk.END)
    g_entry.delete(0, tk.END)
    alice_entry.delete(0, tk.END)
    bob_entry.delete(0, tk.END)

    output_box.delete("1.0", tk.END)


# =====================================
# Export Results
# =====================================

def export_results():

    content = output_box.get("1.0", tk.END).strip()

    if content == "":

        messagebox.showwarning(
            "No Results",
            "Nothing to export."
        )

        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt")
        ]
    )

    if not file_path:
        return

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    messagebox.showinfo(
        "Export Successful",
        "Results exported successfully."
    )


# =====================================
# Buttons
# =====================================

generate_btn = tk.Button(
    button_frame,
    text="Generate",
    command=generate_key,
    width=16,
    bg="#1E90FF",
    fg="white",
    font=("Segoe UI", 11, "bold")
)

generate_btn.grid(
    row=0,
    column=0,
    padx=5
)

export_btn = tk.Button(
    button_frame,
    text="Export Results",
    command=export_results,
    width=16,
    bg="#228B22",
    fg="white",
    font=("Segoe UI", 11, "bold")
)

export_btn.grid(
    row=0,
    column=1,
    padx=5
)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_results,
    width=16,
    bg="#DC143C",
    fg="white",
    font=("Segoe UI", 11, "bold")
)

clear_btn.grid(
    row=0,
    column=2,
    padx=5
)

# =====================================
# Run Program
# =====================================

root.mainloop()