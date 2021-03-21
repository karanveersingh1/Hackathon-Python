from tkinter import *
from game import *
from game2 import *
root = Tk()
root.title("Menu")
root.geometry("600x600")
root.configure(bg="Black")




btn1 = Button(root, text="ez mode", command= lambda: call2(root) )

btn2 = Button(root, text="hard mode", command= lambda: call1(root) )

btn1.pack(side="top",pady=20, padx=50 )
btn2.pack(side="top",pady=20, padx=50 )


def call1(root):
	root.destroy()
	initiatehardmode()

def call2(root):
	root.destroy()	
	initiateezmode()

root.mainloop()	