import tkinter as tk
import pyperclip as pyclip
import time
from EncryptionWare import EncryptionWare
from tkinter import filedialog

root = tk.Tk()

root.title("BitCrypt")
root.resizable(True, True)

out = tk.Text(root, width=100, height=10)
out.pack()

def process_encrypt():
    encrypt = EncryptionWare(string_entry.get("1.0",'end-1c'), password_entry.get())
    encrypted = encrypt.encrypt()
    out.delete("1.0", tk.END)
    out.insert("1.0", encrypted)
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
    decrypt = EncryptionWare(string_entry.get("1.0",'end-1c'), password_entry.get())
    decrypted = decrypt.decrypt()
    out.delete("1.0",'end-1c')
    out.insert("1.0", decrypted)
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

def paste_clip():
    string_entry.delete("1.0",'end-1c')
    string_entry.insert("1.0", pyclip.paste())

def paste_file():
    to_paste = filedialog.askopenfile(filetypes=[("All Files", "*")]).read()
    string_entry.delete("1.0",'end-1c')
    string_entry.insert("1.0", to_paste)

def save_file():
    try:
        to_save = filedialog.asksaveasfilename(filetypes=[("All Files", "*")])
        save_string = out.get("1.0",'end-1c')
        file_to_save = open(to_save, mode="w")
        file_to_save.write(save_string)
    except:
        pass
main_canvas = tk.Canvas(root, width=200, height=50)
main_canvas.pack()

label1 = tk.Label(root, text="Enter string")
label1.pack()

string_entry = tk.Text(root, height=20)
string_entry.pack()

label2 = tk.Label(root, text="Enter password")
label2.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

encrypt_button = tk.Button(root, command=process_encrypt, text="Encrypt")
encrypt_button.pack(side=tk.LEFT, padx=15, pady=10)

decrypt_button = tk.Button(root, command=process_decrypt, text="Decrypt")
decrypt_button.pack(side=tk.RIGHT, padx=15, pady=10)

clipboard_button = tk.Button(root, command=save_file, text="To File")
clipboard_button.pack(side=tk.BOTTOM, pady = 10)

clipboard_button = tk.Button(root, command=paste_file, text="From File")
clipboard_button.pack(side=tk.BOTTOM, pady = 1)

clipboard_button = tk.Button(root, command=paste_clip, text="From Clipboard")
clipboard_button.pack(side=tk.BOTTOM, pady = 10)

root.mainloop()
