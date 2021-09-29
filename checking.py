from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import random
import os

root = Tk()
root.minsize(600,600)
root.maxsize(600,600)

root.title("Hi")
root.configure(bg ='white')

open_img = ImageTk.PhotoImage(Image.open("open.png"))
close_img = ImageTk.PhotoImage(Image.open("exit.jpg"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))


label = Label(root,text = "File  Name : ")
label.place(relx = 0.4,rely = 0.1,anchor = CENTER)

entry = Entry(root)
entry.place(relx = 0.6,rely = 0.1,anchor = CENTER)

text = Text(root,height=26,width=50,bg="white")
text.place(relx = 0.5,rely = 0.5,anchor = CENTER)

name = ""
def openfilename():
    global name
    text.delete(1.0,END)
    entry.delete(0,END)
    text_file = filedialog.askopenfilename(title = "Text open file",filetypes =(("text files","*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    entry.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(name,'r')
    paragragh = text_file.read()
    text.insert(END,paragragh)
    text_file.close()
   
def save():
    var = entry.get()
    varfile = open(var + ".txt","w")
    data = text.get("1.0",END)
    print(data)
    varfile.write(data)
    entry.delete(0,END)
    text.delete(1.0,END)
    messagebox.showinfo("HELLO","Your file is saved")
   
def clear():
    root.destroy()
   

   
   
   
   
btn_open = Button(root,image = open_img,text = "cti",command = openfilename)
btn_open.place(relx = 0.1,rely = 0.1,anchor = CENTER)


btn_save = Button(root,image = save_img,text = "ati",command = save)
btn_save.place(relx = 0.2,rely = 0.1,anchor = CENTER)

btn_close = Button(root,image = close_img,text = "cta",command = clear)
btn_close.place(relx = 0.3,rely = 0.1,anchor = CENTER)


root.mainloop()