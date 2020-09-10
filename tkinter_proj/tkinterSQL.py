# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:38:45 2020

@author: Ruslan Polyak
"""

from tkinter import Label, Tk, Entry, StringVar, W, Listbox, Scrollbar, Button, END
import tkinterSQL_be
#because the outcome is a tuple, we'll need to create a function
#for readability

def view_command():
    #ensures you're deleting everything from 0 to END
    list1.delete(0,END)
    for row in tkinterSQL_be.view():
        #END means new rows will be placed at the END of the list box
        list1.insert(END, row)
        
#not e1, but title_text=StringVar
def search_command():
    list1.delete(0,END)
    for search in tkinterSQL_be.search(prog_title.get(),analyst.get(),notes.get(),pid_aid.get()):
        list1.insert(END,search)
    
def add_command():
    try:
        tkinterSQL_be.insert(prog_title.get(),analyst.get(),notes.get(),pid_aid.get())
        list1.delete(0, END)
        list1.insert(END,(prog_title.get(),analyst.get(),notes.get(),pid_aid.get()))
    except:
        tkinterSQL_be.connect()
    
#bind function expects an event. this will give us an id which we can then pass to 
#delete command
def get_selected_row(event):
    #index is cursor selection
    #select the first number in the tuple
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)        
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except Exception as e:
        print(str(e))
    
def delete_command():
    tkinterSQL_be.delete(selected_tuple[0])
    
def update_command():
    tkinterSQL_be.update(selected_tuple[0],prog_title.get(),analyst.get(),notes.get(),pid_aid.get())
    
window = Tk()

window.wm_title("AID")

l1 = Label(window, width=25, text="Program/Title", anchor=W)
l1.grid(row=0,column=0)

l2 = Label(window, width=25, text="Analyst", anchor=W)
l2.grid(row=1,column=0)

l3 = Label(window, width=25, text="Notes", anchor=W)
l3.grid(row=2,column=0)

l4 = Label(window, width=25, text="PID/AID", anchor=W)
l4.grid(row=3,column=0)

#datatype for window entry
prog_title=StringVar()
e1=Entry(window, width=20, textvariable=prog_title)
e1.grid(row=0,column=1)

analyst=StringVar()
e2=Entry(window, width=20, textvariable=analyst)
e2.grid(row=1,column=1)

notes=StringVar()
e3=Entry(window, width=20, textvariable=notes)
e3.grid(row=2,column=1)

pid_aid=StringVar()
e4=Entry(window, width=20, textvariable=pid_aid)
e4.grid(row=3,column=1)

#, height=6, width=36

list1 = Listbox(window, height=6, width=50)
list1.grid(row=4,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#this bind is for deleting what the user selected vs entering data
#we will need to bind a selection to a method called get_selected_row
list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width=12,command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window, text="Search Entry", width=12,command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window, text="Add Entry", width=12,command=add_command)
b3.grid(row=4,column=3)

b4 = Button(window, text="Update Selected", width=12, command = update_command)
b4.grid(row=5,column=3)

b5 = Button(window, text="Delete Selected", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(window, text="Close", width=12, command = window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
