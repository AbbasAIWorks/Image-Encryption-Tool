import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

# =======================
# Encryption Logic
# =======================
def process_image(input_path, output_path, key):
    try:
        img = Image.open(input_path).convert("RGB")
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                r = r ^ key
                g = g ^ key
                b = b ^ key

                pixels[x, y] = (r, g, b)

        img.save(output_path)
        return True

    except Exception as e:
        messagebox.showerror("Error", str(e))
        return False


# =======================
# GUI Functions
# =======================
def select_file():
    path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    entry_path.delete(0, tk.END)
    entry_path.insert(0, path)


def encrypt():
    path = entry_path.get()
    key = entry_key.get()

    if not path or not key:
        messagebox.showwarning("Warning", "Please select file and enter key")
        return

    try:
        key = int(key)
    except:
        messagebox.showerror("Error", "Key must be a number")
        return

    output = os.path.splitext(path)[0] + "_encrypted.png"

    if process_image(path, output, key):
        messagebox.showinfo("Success", f"Encrypted saved at:\n{output}")


def decrypt():
    path = entry_path.get()
    key = entry_key.get()

    if not path or not key:
        messagebox.showwarning("Warning", "Please select file and enter key")
        return

    try:
        key = int(key)
    except:
        messagebox.showerror("Error", "Key must be a number")
        return

    output = os.path.splitext(path)[0] + "_decrypted.png"

    if process_image(path, output, key):
        messagebox.showinfo("Success", f"Decrypted saved at:\n{output}")


# =======================
# UI Design
# =======================
root = tk.Tk()
root.title("🔐 Image Encryption Tool")
root.geometry("500x300")
root.resizable(False, False)

# Gradient-like background (simple modern color)
root.configure(bg="#0f172a")  # dark blue

# Title
title = tk.Label(
    root,
    text="Image Encryption Tool",
    font=("Segoe UI", 18, "bold"),
    fg="white",
    bg="#0f172a"
)
title.pack(pady=15)

# File selection
frame_file = tk.Frame(root, bg="#0f172a")
frame_file.pack(pady=10)

entry_path = tk.Entry(frame_file, width=35)
entry_path.pack(side=tk.LEFT, padx=5)

btn_browse = tk.Button(
    frame_file,
    text="Browse",
    command=select_file,
    bg="#2563eb",
    fg="white"
)
btn_browse.pack(side=tk.LEFT)

# Key input
frame_key = tk.Frame(root, bg="#0f172a")
frame_key.pack(pady=10)

label_key = tk.Label(
    frame_key,
    text="Enter Key:",
    fg="white",
    bg="#0f172a"
)
label_key.pack(side=tk.LEFT)

entry_key = tk.Entry(frame_key, width=10)
entry_key.pack(side=tk.LEFT, padx=10)

# Buttons
frame_buttons = tk.Frame(root, bg="#0f172a")
frame_buttons.pack(pady=20)

btn_encrypt = tk.Button(
    frame_buttons,
    text="Encrypt",
    command=encrypt,
    width=12,
    bg="#16a34a",
    fg="white"
)
btn_encrypt.pack(side=tk.LEFT, padx=10)

btn_decrypt = tk.Button(
    frame_buttons,
    text="Decrypt",
    command=decrypt,
    width=12,
    bg="#dc2626",
    fg="white"
)
btn_decrypt.pack(side=tk.LEFT, padx=10)

# Footer
footer = tk.Label(
    root,
    text="ProDigy InfoTech | Cyber Security Internship",
    font=("Segoe UI", 8),
    fg="gray",
    bg="#0f172a"
)
footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
