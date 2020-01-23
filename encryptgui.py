import tkinter as tk
from EncryptionWare import EncryptionWare
import pyperclip as pyclip
import time

root = tk.Tk()

out = tk.Entry(root, width=100)
out.pack()

def process_encrypt():
    encrypt = EncryptionWare(string_entry.get(), password_entry.get())
    encrypted = encrypt.encrypt()
    out.delete(0, tk.END)
    out.insert(0, encrypted)
    pyclip.copy(encrypted)
    notification = tk.Tk()
    notification.overrideredirect(True)
    notification.geometry(f"150x20+{root.winfo_screenwidth() - 150}+{root.winfo_screenheight() - 80}")
    notifier_text = tk.Label(notification, text="Copied to clipboard!")
    notifier_text.pack()
    t1 = time.time()
    while (time.time() - t1) < 2:
        notification.update_idletasks()
        notification.update()
    notification.destroy()

def process_decrypt():
    decrypt = EncryptionWare(string_entry.get(), password_entry.get())
    decrypted = decrypt.decrypt()
    out.delete(0, tk.END)
    out.insert(0, decrypted)
    pyclip.copy(decrypted)
    notification = tk.Tk()
    notification.overrideredirect(True)
    notification.geometry(f"150x20+{root.winfo_screenwidth() - 150}+{root.winfo_screenheight() - 80}")
    notifier_text = tk.Label(notification, text="Copied to clipboard!")
    notifier_text.pack()
    t1 = time.time()
    while (time.time() - t1) < 2:
        notification.update_idletasks()
        notification.update()
    notification.destroy()

main_canvas = tk.Canvas(root, width=200, height=50)
main_canvas.pack()

label1 = tk.Label(root, text="Enter string")
label1.pack()

string_entry = tk.Entry(root)
string_entry.pack()

label2 = tk.Label(root, text="Enter password")
label2.pack()

password_entry = tk.Entry(root)
password_entry.pack()

encrypt_button = tk.Button(root, command=process_encrypt, text="Encrypt")
encrypt_button.pack(side=tk.LEFT, padx=15, pady=10)

decrypt_button = tk.Button(root, command=process_decrypt, text="Decrypt")
decrypt_button.pack(side=tk.RIGHT, padx=15, pady=10)

root.mainloop()
