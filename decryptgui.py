import tkinter
from EncryptionWare import EncryptionWare
import pyperclip as pyclip
import time

root = tkinter.Tk()

out = tkinter.Entry(root, width=100)
out.pack()

def process():
    decrypt = EncryptionWare(string_entry.get(), password_entry.get())
    decrypted = decrypt.decrypt()
    out.delete(0, tkinter.END)
    out.insert(0, decrypted)
    pyclip.copy(decrypted)
    notification = tkinter.Tk()
    notification.geometry("60x10+0+0")
    notifier_text = tkinter.Label(notification, text="Copied to clipboard!")
    notifier_text.pack()
    t1 = time.time()
    while (time.time() - t1) < 2:
        notification.update_idletasks()
        notification.update()
    notification.destroy()


main_canvas = tkinter.Canvas(root, width=200, height=50)
main_canvas.pack()

label1 = tkinter.Label(main_canvas, text="Enter string")
label1.pack()

string_entry = tkinter.Entry(root, width=100)
string_entry.pack()

label2 = tkinter.Label(root, text="Enter password")
label2.pack()

password_entry = tkinter.Entry(root)
password_entry.pack()

process_button = tkinter.Button(root, command=process, text="Decrypt")
process_button.pack()

root.mainloop()