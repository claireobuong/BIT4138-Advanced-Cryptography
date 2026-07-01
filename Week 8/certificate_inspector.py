import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from datetime import datetime, timedelta

# =====================================
# Main Window
# =====================================

root = tk.Tk()

root.title("Certificate Inspector")
root.geometry("900x650")
root.configure(bg="#f4f6f8")
root.resizable(False, False)

# =====================================
# Main Frame
# =====================================

frame = tk.Frame(
    root,
    bg="#f4f6f8"
)

frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=15
)

# =====================================
# Title
# =====================================

title = tk.Label(
    frame,
    text="CERTIFICATE INSPECTOR",
    font=("Segoe UI", 22, "bold"),
    bg="#f4f6f8",
    fg="#003366"
)

title.grid(
    row=0,
    column=0,
    columnspan=3,
    pady=(0, 20)
)

# =====================================
# Output Box
# =====================================

output_box = tk.Text(
    frame,
    width=90,
    height=24,
    font=("Consolas", 10),
    wrap="word"
)

output_box.grid(
    row=2,
    column=0,
    columnspan=3,
    sticky="nsew"
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
    row=2,
    column=3,
    sticky="ns"
)

output_box.configure(
    yscrollcommand=scrollbar.set
)

# =====================================
# Allow Output Box to Expand
# =====================================

frame.grid_rowconfigure(
    2,
    weight=1
)

frame.grid_columnconfigure(
    0,
    weight=1
)

# =====================================
# Helper Functions
# =====================================

def extract_line(lines, keyword):

    for line in lines:

        if keyword in line:

            return line.strip()

    return "Not Available"


def calculate_status(expiry_date):

    try:

        # Remove GMT because Python often
        # struggles to parse it with %Z
        expiry_date = expiry_date.replace("GMT", "").strip()

        expiry = datetime.strptime(
            expiry_date,
            "%b %d %H:%M:%S %Y"
        )

    except:

        return (
            "UNKNOWN",
            "Unknown",
            "Unknown"
        )

    today = datetime.now()

    days_remaining = (expiry - today).days

    if days_remaining < 0:

        status = "EXPIRED"
        risk = "HIGH"

    elif days_remaining <= 30:

        status = "EXPIRING SOON"
        risk = "MEDIUM"

    else:

        status = "VALID"
        risk = "LOW"

    return (
        status,
        days_remaining,
        risk
    )

# =====================================
# Load Certificate
# =====================================

def load_certificate():

    file_path = filedialog.askopenfilename(

        filetypes=[
            ("PEM Files", "*.pem"),
            ("All Files", "*.*")
        ]

    )

    if file_path == "":
        return

    output_box.delete("1.0", tk.END)

    try:

        result = subprocess.run(

            [
                "openssl",
                "x509",
                "-in",
                file_path,
                "-text",
                "-noout"
            ],

            capture_output=True,
            text=True

        )

        if result.returncode != 0:

            messagebox.showerror(
                "OpenSSL Error",
                result.stderr
            )

            return

        certificate = result.stdout

        lines = certificate.splitlines()

        issuer = extract_line(lines, "Issuer:")
        subject = extract_line(lines, "Subject:")
        signature = extract_line(lines, "Signature Algorithm:")
        valid_from = extract_line(lines, "Not Before:")
        expiry = extract_line(lines, "Not After :")

        expiry_value = expiry.replace(
            "Not After :",
            ""
        ).strip()

        status, days_remaining, risk = calculate_status(expiry_value)

        output_box.insert(
            tk.END,
            "========================================\n"
        )

        output_box.insert(
            tk.END,
            "      CERTIFICATE INFORMATION\n"
        )

        output_box.insert(
            tk.END,
            "========================================\n\n"
        )

        output_box.insert(
            tk.END,
            issuer + "\n\n"
        )

        output_box.insert(
            tk.END,
            subject + "\n\n"
        )

        output_box.insert(
            tk.END,
            signature + "\n\n"
        )

        output_box.insert(
            tk.END,
            valid_from + "\n\n"
        )

        output_box.insert(
            tk.END,
            expiry + "\n\n"
        )

        output_box.insert(
            tk.END,
            "Certificate Status : " + status + "\n\n"
        )

        output_box.insert(
            tk.END,
            "Days Remaining : " + str(days_remaining) + "\n\n"
        )

        output_box.insert(
            tk.END,
            "Risk Level : " + risk
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# =====================================
# Clear Results
# =====================================

def clear_results():

    output_box.delete("1.0", tk.END)


# =====================================
# Export Results
# =====================================

def export_results():

    content = output_box.get("1.0", tk.END).strip()

    if content == "":

        messagebox.showwarning(
            "No Results",
            "There are no results to export."
        )

        return

    file_path = filedialog.asksaveasfilename(

        defaultextension=".txt",

        filetypes=[
            ("Text Files", "*.txt")
        ]

    )

    if file_path == "":

        return

    try:

        with open(file_path, "w", encoding="utf-8") as file:

            file.write(content)

        messagebox.showinfo(
            "Export Successful",
            "Certificate information exported successfully."
        )

    except Exception as e:

        messagebox.showerror(
            "Export Error",
            str(e)
        )


# =====================================
# Buttons
# =====================================

load_btn = tk.Button(

    frame,

    text="Load Certificate",

    command=load_certificate,

    width=18,

    bg="#1E90FF",

    fg="white",

    font=("Segoe UI", 11, "bold")

)

load_btn.grid(
    row=1,
    column=0,
    padx=10,
    pady=(0, 15),
    sticky="w"
)


export_btn = tk.Button(

    frame,

    text="Export Results",

    command=export_results,

    width=18,

    bg="#228B22",

    fg="white",

    font=("Segoe UI", 11, "bold")

)

export_btn.grid(
    row=1,
    column=1,
    padx=10,
    pady=(0, 15)
)


clear_btn = tk.Button(

    frame,

    text="Clear",

    command=clear_results,

    width=18,

    bg="#DC143C",

    fg="white",

    font=("Segoe UI", 11, "bold")

)

clear_btn.grid(
    row=1,
    column=2,
    padx=10,
    pady=(0, 15),
    sticky="e"
)


# =====================================
# Run Program
# =====================================

root.mainloop()