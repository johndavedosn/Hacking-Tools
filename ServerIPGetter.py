# importting the modules
import socket
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("400x200")
text = Label(root, text="Write The Host Name")
hn = StringVar()
hn_input = Entry(root, width=30,textvariable=hn )
hn_value = str(hn.get())
def gsi():
    try:
        IPAddr = socket.gethostbyname(hn_value)
        global text2
        text2 = Label(root, text=IPAddr)
        text2.pack()
    except socket.gaierror:
        messagebox.showerror("Error", "Host Not Found...")
    print(hn.get())

btn = Button(root, text="Get Host IP", width=9, command=gsi(), borderwidth=0, fg="white", bg="red")
text.pack()
hn_input.pack()
btn.pack()
root.mainloop()