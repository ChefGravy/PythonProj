# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:50:32 2020

@author: ruslan polyak
"""
from tkinter import END
import frontend
def get_selected_row(event):
    #index is cursor selection
    #select the first number in the tuple
    try:
        global selected_tuple
        index = frontend.view_all.lb.curselection()[1]
        #index = list1.curselection()[0]
        print(index)
        selected_tuple = frontend.view_all.lb.get(index)
        print(selected_tuple)
        frontend.e1.delete(0,END)
        frontend.e1.insert(END,selected_tuple[1])
#        e2.delete(0,END)
#        e2.insert(END,selected_tuple[2])
#        e3.delete(0,END)
#        e3.insert(END,selected_tuple[3])
#        e4.delete(0,END)
#        e4.insert(END,selected_tuple[4])
    except:
        pass