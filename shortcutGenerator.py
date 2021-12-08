import tkinter as tk
from tkinter import filedialog, Text
import os
import datetime

root  = tk.Tk()
root.title("Shortcut Generator")
root.resizable(width=False, height=False)
apps = []

def addApp():

	for widget in frame.winfo_children():
		widget.destroy()

	filename = filedialog.askopenfilename(initialdir = "/", title = "Select File",
										filetypes = (("Executables", "*.exe"), ("All files", "*.*")))
	apps.append(filename)
	print(filename)

	for app in apps:
		label = tk.Label(frame, text = app, bg = "#2b2b2b", fg = "#ffffff")#
		label.pack()

def generateFile():
	d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
	with open('shortcut-' + d + '.bat', 'w+') as bat_file:
		bat_file.write("@echo off\n")
		for app in apps:
			bat_file.write('\nstart "shortcut" "' + app + '"')
	os._exit(0)
	

canvas = tk.Canvas(root, height = 500, width = 350, bg = "#2b2b2b") 
canvas.pack()

frame = tk.Frame(root, bg="#2b2b2b")
frame.place(relheight = 0.8, relwidth = 0.8, relx = 0.1, rely = 0.1)

openFile = tk.Button(root, text = "Open File", padx = 10, pady = 5,
					bg = "#2b2b2b", fg = "#ffffff", command = addApp)
openFile.pack(fill = tk.X)

generateFile = tk.Button(root, text = "Genetrate File", padx = 10, pady = 5, 
						bg = "#2b2b2b", fg = "#ffffff", command = generateFile)
generateFile.pack(fill = tk.X)

root.mainloop()