import tkinter as tk
from cryptography.fernet import Fernet

# ======================
# GLOBAL VARIABLES
# ======================

secret_key = None
encrypted_data = None


# ======================
# FUNCTIONS
# ======================

def hide_demo_widgets():

    message_label.pack_forget()
    message_entry.pack_forget()
    encrypt_button.pack_forget()
    key_label.pack_forget()
    encrypted_label.pack_forget()
    decrypt_button.pack_forget()
    decrypted_label.pack_forget()


def show_symmetric():

    hide_demo_widgets()

    content_title.config(text="Symmetric Cryptography")

    content_text.config(state="normal")
    content_text.delete("1.0", tk.END)

    content_text.insert(
        tk.END,
        """DEFINITION

Symmetric cryptography uses the same secret key for both encryption and decryption.


HOW IT WORKS

1. The sender creates a message.
2. The message is encrypted using a secret key.
3. The encrypted message is transmitted.
4. The receiver uses the same secret key to decrypt the message.


EXAMPLES

• AES (Advanced Encryption Standard)
• DES (Data Encryption Standard)
• Triple DES (3DES)
• Blowfish
• RC4
• Twofish


ADVANTAGES

• Fast encryption and decryption
• Efficient for large amounts of data
• Requires less computational power
• Easy to implement
• Suitable for real-time communication
• Faster than asymmetric cryptography
• Ideal for encrypting files and databases


DISADVANTAGES

• Secure key sharing is difficult
• If the key is stolen, data can be compromised
• Poor scalability for many users
• Key management becomes challenging
• No built-in non-repudiation
• Both parties must trust each other
• Difficult to manage many secret keys


----------------------------------------------------

SYMMETRIC ENCRYPTION DEMONSTRATION

Enter a message below and click Encrypt Message.
"""
    )

    content_text.config(state="disabled")

    message_label.pack(pady=(10, 0))
    message_entry.pack(pady=5)

    encrypt_button.pack(pady=5)

    key_label.pack(pady=5)

    encrypted_label.pack(pady=5)

    decrypt_button.pack(pady=5)

    decrypted_label.pack(pady=5)


def encrypt_message():

    global secret_key
    global encrypted_data

    message = message_entry.get()

    if message == "":
        return

    secret_key = Fernet.generate_key()

    cipher = Fernet(secret_key)

    encrypted_data = cipher.encrypt(
        message.encode()
    )

    key_label.config(
        text="SECRET KEY:\n\n" + secret_key.decode()
    )

    encrypted_label.config(
        text="ENCRYPTED MESSAGE:\n\n" +
        encrypted_data.decode()
    )

    decrypted_label.config(text="")


def decrypt_message():

    global secret_key
    global encrypted_data

    if secret_key is None or encrypted_data is None:
        return

    cipher = Fernet(secret_key)

    decrypted = cipher.decrypt(
        encrypted_data
    )

    decrypted_label.config(
        text="DECRYPTED MESSAGE:\n\n" +
        decrypted.decode()
    )


# ======================
# MAIN WINDOW
# ======================

window = tk.Tk()

window.title("Advanced Cryptography")

window.state("zoomed")

# ======================
# TOP HEADING
# ======================

title_label = tk.Label(
    window,
    text="ADVANCED CRYPTOGRAPHY",
    font=("Times New Roman", 22, "bold")
)

title_label.pack(pady=15)

# ======================
# MAIN FRAME
# ======================

main_frame = tk.Frame(window)

main_frame.pack(fill="both", expand=True)

# ======================
# LEFT PANEL
# ======================

left_frame = tk.Frame(main_frame)

left_frame.pack(
    side="left",
    fill="y",
    padx=15,
    pady=10
)

btn_symmetric = tk.Button(
    left_frame,
    text="Symmetric Cryptography",
    width=25,
    height=2,
    font=("Times New Roman", 11),
    command=show_symmetric
)

btn_symmetric.pack(pady=5)

btn_asymmetric = tk.Button(
    left_frame,
    text="Asymmetric Cryptography",
    width=25,
    height=2,
    font=("Times New Roman", 11)
)

btn_asymmetric.pack(pady=5)

btn_hashing = tk.Button(
    left_frame,
    text="Hashing",
    width=25,
    height=2,
    font=("Times New Roman", 11)
)

btn_hashing.pack(pady=5)

btn_threats = tk.Button(
    left_frame,
    text="Emerging Threats",
    width=25,
    height=2,
    font=("Times New Roman", 11)
)

btn_threats.pack(pady=5)

# ======================
# RIGHT PANEL
# ======================

right_frame = tk.Frame(main_frame)

right_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=15,
    pady=10
)

content_title = tk.Label(
    right_frame,
    text="Welcome",
    font=("Times New Roman", 18, "bold")
)

content_title.pack(pady=10)

# ======================
# CONTENT FRAME
# ======================

welcome_frame = tk.Frame(
    right_frame,
    bd=2,
    relief="groove"
)

welcome_frame.pack(
    fill="x",
    pady=5
)

scrollbar = tk.Scrollbar(
    welcome_frame
)

scrollbar.pack(
    side="right",
    fill="y"
)

content_text = tk.Text(
    welcome_frame,
    height=10,
    font=("Times New Roman", 12),
    wrap="word",
    borderwidth=0,
    yscrollcommand=scrollbar.set
)

scrollbar.config(
    command=content_text.yview
)

content_text.pack(
    fill="both",
    padx=15,
    pady=15
)

content_text.insert(
    "1.0",
    """WELCOME TO THE ADVANCED CRYPTOGRAPHY LEARNING SYSTEM

This application demonstrates important concepts used in modern information security and cryptography.


TOPICS COVERED

• Symmetric Cryptography
• Asymmetric Cryptography
• Hashing
• Emerging Security Threats


FEATURES

• Clear explanations of each concept

• Examples of commonly used algorithms

• Advantages and disadvantages

• Practical cryptography demonstrations

• Information on modern cybersecurity threats


Select a topic from the menu on the left to begin exploring cryptography.
"""
)

content_text.config(state="disabled")

# ======================
# DEMONSTRATION WIDGETS
# ======================

message_label = tk.Label(
    right_frame,
    text="Enter Message:",
    font=("Times New Roman", 12, "bold")
)

message_entry = tk.Entry(
    right_frame,
    width=70,
    font=("Times New Roman", 12)
)

encrypt_button = tk.Button(
    right_frame,
    text="Encrypt Message",
    font=("Times New Roman", 11),
    command=encrypt_message
)

key_label = tk.Label(
    right_frame,
    text="",
    font=("Times New Roman", 11),
    justify="left",
    wraplength=500
)

encrypted_label = tk.Label(
    right_frame,
    text="",
    font=("Times New Roman", 11),
    justify="left",
    wraplength=500
)

decrypt_button = tk.Button(
    right_frame,
    text="Decrypt Message",
    font=("Times New Roman", 11),
    command=decrypt_message
)

decrypted_label = tk.Label(
    right_frame,
    text="",
    font=("Times New Roman", 11),
    justify="left",
    wraplength=500
)

# ======================
# RUN APPLICATION
# ======================

window.mainloop()