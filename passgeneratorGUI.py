import random 
import pyperclip 
from tkinter import *
from tkinter.ttk import *

def low(): 
	entry.delete(0, END) 

	length = var1.get() 
 
	chars = ('!', '@', '#', '$', '%', '&')

	level1 = tuple(map(chr, range(ord('a'), ord('z')+1))) + tuple(map(str, range(0, 10)))
	level2 = level1 + tuple(map(chr, range(ord('A'), ord('Z')+1)))
	level3 = level2 + chars
	password = "" 

	if var.get() == 1: 
		for i in range(0, length): 
			password = password + random.choice(level1) 
		return password 

	elif var.get() == 0: 
		for i in range(0, length): 
			password = password + random.choice(level2) 
		return password 

	elif var.get() == 3: 
		for i in range(0, length): 
			password = password + random.choice(level3) 
		return password 
	else: 
		print("Please choose an option") 

def generate(): 
	password1 = low() 
	entry.insert(10, password1) 

def copy1(): 
	random_password = entry.get() 
	pyperclip.copy(random_password) 


root = Tk() 
var = IntVar() 
var1 = IntVar() 

root.title("Password Generator") 

Random_password = Label(root, text="Password : ") 
Random_password.grid(row=0) 
entry = Entry(root) 
entry.grid(row=0, column=1) 


c_label = Label(root, text="Length : ") 
c_label.grid(row=1) 


copy_button = Button(root, text="Copy", command=copy1) 
copy_button.grid(row=0, column=2) 
generate_button = Button(root, text="Generate", command=generate) 
generate_button.grid(row=0, column=3) 


radio_low = Radiobutton(root, text="Low", variable=var, value=1) 
radio_low.grid(row=1, column=2, sticky='E') 
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0) 
radio_middle.grid(row=1, column=3, sticky='E') 
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3) 
radio_strong.grid(row=1, column=4, sticky='E') 
combo = Combobox(root, textvariable=var1) 

 
combo['values'] = tuple(map(str, range(8, 33))) 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=1, row=1) 


root.mainloop() 
