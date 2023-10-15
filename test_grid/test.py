from tkinter import Tk,Frame,Button,Label,W,E
from tkinter import BooleanVar,BOTH,Listbox,StringVar,END
from PIL import Image, ImageTk
from tkinter.ttk import Frame,Style
import tkinter.messagebox as mbox

class Example(Frame):
    def __init__(self,parent):
        Frame .__init__(self,parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Listbox")
        self.pack(fill=BOTH,expand=True)
        Style().configure("TFrame",background = "#FFE4E1")
        label0 = Label(self,text="CHOOSE ONE",font=("Helvetia 25 bold italic"),background="#FFE4E1",foreground="#104E8B")
        label0.grid(row=0,columnspan=3)
        bard = Image.open("D:\\STUDY\\python\\test_grid\\a.jpg")
        bard = bard.resize((300,424),Image.LANCZOS)
        routunda = ImageTk.PhotoImage(bard)
        label = Label(self, image=routunda)
        label.image = routunda
        label.grid(row=1,column=0,padx=5,pady=5)

        bard = Image.open("D:\\STUDY\\python\\test_grid\\q.jpg")
        bard = bard.resize((300,424),Image.LANCZOS)
        routunda = ImageTk.PhotoImage(bard)
        label = Label(self, image=routunda)
        label.image = routunda
        label.grid(row=1,column=1,padx=5,pady=5)

        bard = Image.open("D:\\STUDY\\python\\test_grid\\ajz.jpg")
        bard = bard.resize((300,424),Image.LANCZOS)
        routunda = ImageTk.PhotoImage(bard)
        label = Label(self, image=routunda)
        label.image = routunda
        label.grid(row=1,column=2,padx=5,pady=5)
        
        question = Button(self,text="CLICK!",font="Helvetia 15 bold italic",command=self.onClick,background="#FFCCCC",foreground="#6959CD")
        question.grid(row=2,column=0,padx=5,pady=5)
        
        question = Button(self,text="CLICK!",font="Aclonica 15 bold italic",command=self.onClick,background="#FFCCCC",foreground="#6959CD")
        question.grid(row=2,column=1,padx=5,pady=5)
        
        question = Button(self,text="CLICK!",font="abc 15 bold italic",command=self.onClick,background="#FFCCCC",foreground="#6959CD")
        question.grid(row=2,column=2,padx=5,pady=5)

    def onClick(self):
        mbox.askquestion("Question","Bạn có chắc chắn chứ")
        
root = Tk()
ex = Example(root)
root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
root.mainloop()
