# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 13:41:38 2022

@author: Swasti
"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Classes")
root.geometry("900x600")

gui_elements = ["Label", "Button", "Dropdown"]

dropdown = ttk.Combobox(root, state = "readonly", values = gui_elements)
dropdown.pack()

class createElements:
    
    def __init__(self):
        print("This is Create Elements Class")
        
    def createLbl(self):
        lbl = Label(root, text = "Label")
        lbl.pack()
        
    def createBtn(self):
        btn = Button(root, text = "Button", command = self.message)
        btn.pack(padx = 20, pady = 10)
        
    def createDropdown(self):
        val = [1, 2, 3, 4]
        class_dropdown = ttk.Combobox(root, state = "readonly", values = val)
        class_dropdown.pack()
        
        
    def choose(self):
        global dropdown
        
        element = dropdown.get()
        
        if(element == "Label"):
            self.createLbl()
            
        elif(element == "Button"):
            self.createBtn()
            
        elif(element == "Dropdown"):
            self.createDropdown()
        
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the Button using Class.")
        
obj = createElements()

main_btn = Button(root, text = "Create Element", command = obj.choose)
main_btn.pack(padx = 20, pady = 10)

root.mainloop()
