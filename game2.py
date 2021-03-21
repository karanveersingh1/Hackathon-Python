from tkinter import *
from PIL import ImageTk, Image
import random 
from tkinter import messagebox

count = 0
btn_count=[]
for i in range (0,20):
	btn_count.append(0)
answer_list = []
answer_dict = {}
score = 0
def initiateezmode():

	root = Tk()
	root.title('Test Ya Memori')
	root.geometry("700x550")
	root.configure(bg="gray")
	
	messagebox.showinfo("INFO", "Pairs will be locked when found, clicked tiles turn white")	

	#--------------------import images and name them-------------------------------#
	barrel_image = Image.open('barrel.png')
	boat_image   = Image.open('boat.png')
	bomb_image   = Image.open('bomb.png')
	cannon_image = Image.open('cannon.png')
	chains_image = Image.open('chains.png')
	chest_image  = Image.open('chest.png')
	museum_image = Image.open('museum.png')
	books_image  = Image.open('books.png')
	ctrnif_image = Image.open('cutterknife.png')
	acrlcs_image = Image.open('acrylics.png')
	q_mark_image = Image.open('question.png')
	
	#---------------------resize images--------------------------------------------#
	barrel_image = barrel_image.resize( (50,50), Image.ANTIALIAS)
	boat_image   = boat_image.resize(   (50,50), Image.ANTIALIAS)
	bomb_image   = bomb_image.resize(   (50,50), Image.ANTIALIAS)
	cannon_image = cannon_image.resize( (50,50), Image.ANTIALIAS)
	chains_image = chains_image.resize( (50,50), Image.ANTIALIAS)
	chest_image  = chest_image.resize(  (50,50), Image.ANTIALIAS)
	museum_image = museum_image.resize( (50,50), Image.ANTIALIAS)
	books_image  = books_image.resize(  (50,50), Image.ANTIALIAS)
	ctrnif_image = ctrnif_image.resize( (50,50), Image.ANTIALIAS)
	acrlcs_image = acrlcs_image.resize( (50,50), Image.ANTIALIAS)
	q_mark_image = q_mark_image.resize( (50,50), Image.ANTIALIAS)
	
	#---------------------assign images to button images---------------------------#
	btn_barrel_image = ImageTk.PhotoImage(barrel_image)
	btn_boat_image   = ImageTk.PhotoImage(boat_image)
	btn_bomb_image   = ImageTk.PhotoImage(bomb_image)
	btn_cannon_image = ImageTk.PhotoImage(cannon_image)
	btn_chains_image = ImageTk.PhotoImage(chains_image)
	btn_chest_image  = ImageTk.PhotoImage(chest_image)
	btn_museum_image = ImageTk.PhotoImage(museum_image)
	btn_books_image  = ImageTk.PhotoImage(books_image)
	btn_ctrnif_image = ImageTk.PhotoImage(ctrnif_image)
	btn_acrlcs_image = ImageTk.PhotoImage(acrlcs_image)
	btn_q_mark_image = ImageTk.PhotoImage(q_mark_image)
	
	matches=[]
	
	matches.append(btn_barrel_image)
	matches.append(btn_barrel_image)
	matches.append(btn_boat_image)
	matches.append(btn_boat_image)
	matches.append(btn_bomb_image)
	matches.append(btn_bomb_image)
	matches.append(btn_cannon_image)
	matches.append(btn_cannon_image)
	matches.append(btn_chains_image)
	matches.append(btn_chains_image)
	matches.append(btn_chest_image)
	matches.append(btn_chest_image)
	matches.append(btn_museum_image)
	matches.append(btn_museum_image)
	matches.append(btn_books_image)
	matches.append(btn_books_image)
	matches.append(btn_ctrnif_image)
	matches.append(btn_ctrnif_image)
	matches.append(btn_acrlcs_image)
	matches.append(btn_acrlcs_image)
	
	random.shuffle(matches)
		
	my_label = Label(root, text=" ", bg="gray")
	my_label.pack(pady=20)

	score_label = Label(root, text = str(score), relief = RAISED, bg="black", fg="white")
	score_label.pack(side="bottom")	
	
	def click(btn, number):

		global count
		global answer_list
		global answer_dict
		global btn_count
		global score
		score += 1
		score_label.config(text = "Your Score: "+str(score))		
		
		if btn_count[number] == 0 and count < 2 :	
			btn["image"] = matches[number]
			btn["bg"] = "white"
			btn_count[number] = 1
			answer_list.append(number)
			answer_dict[btn] = matches[number]
			count +=1
	
		if len(answer_list) == 2 :
			if matches[answer_list[0]] == matches[answer_list[1]]:
				count = 0
				for key in answer_dict:
					key["state"] = "disabled"
				answer_list = []
				answer_dict = {}
				btn_count = []
				for i in range (0,20):
					btn_count.append(0)	
			else:
				my_label.config(text="Press Enter when windows pops up")
				count = 0
				answer_list = []	
				messagebox.showinfo("cmon man", "hehe...LOL")
				for key in answer_dict:
					key["image"] = btn_q_mark_image
				answer_dict = {}	
				btn_count = [	]
				for i in range (0,20):
					btn_count.append(0)
				print(btn_count)	
	
	
				
	
	button_frame = Frame(root, bg="gray")
	button_frame.pack(pady=15)
	
	
	
	b0 =  Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click (b0, 0) )
	b1 =  Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click (b1, 1) )
	b2 =  Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click (b2, 2) )
	b3 =  Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click (b3, 3) )
	b4 =  Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click (b4, 4) )
	b5 =  Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click (b5, 5) )
	b6 =  Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click (b6, 6) )
	b7 =  Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click (b7, 7) )
	b8 =  Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click (b8, 8) )
	b9 =  Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click (b9, 9) )
	b10 = Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click(b10, 10))
	b11 = Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click(b11, 11))
	b12 = Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click(b12, 12))
	b13 = Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click(b13, 13))
	b14 = Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click(b14, 14))
	b15 = Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click(b15, 15))
	b16 = Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click(b16, 16))
	b17 = Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click(b17, 17))
	b18 = Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click(b18, 18))
	b19 = Button(button_frame, image=btn_q_mark_image, bg='black', bd=5, relief=GROOVE, command=lambda: click(b19, 19))
	
	b0.grid( row=0 , column=0, padx=2, pady=2)
	b1.grid( row=0 , column=1, padx=2, pady=2)
	b2.grid( row=0 , column=2, padx=2, pady=2)
	b3.grid( row=0 , column=3, padx=2, pady=2)
	b4.grid( row=0 , column=4, padx=2, pady=2)
	b5.grid( row=1 , column=0, padx=2, pady=2)
	b6.grid( row=1 , column=1, padx=2, pady=2)
	b7.grid( row=1 , column=2, padx=2, pady=2)
	b8.grid( row=1 , column=3, padx=2, pady=2)
	b9.grid( row=1 , column=4, padx=2, pady=2)
	b10.grid(row=2 , column=0, padx=2, pady=2)
	b11.grid(row=2 , column=1, padx=2, pady=2)
	b12.grid(row=2 , column=2, padx=2, pady=2)
	b13.grid(row=2 , column=3, padx=2, pady=2)
	b14.grid(row=2 , column=4, padx=2, pady=2)
	b15.grid(row=3 , column=0, padx=2, pady=2)
	b16.grid(row=3 , column=1, padx=2, pady=2)
	b17.grid(row=3 , column=2, padx=2, pady=2)
	b18.grid(row=3 , column=3, padx=2, pady=2)
	b19.grid(row=3 , column=4, padx=2, pady=2)
	
	
	
	root.mainloop()	