# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:23:37 2020

@author: Ruslan Polyak
"""

from tkinter import (Tk, Label, Entry, StringVar, W, 
                    IntVar, CENTER, Button,
                    Toplevel,Listbox, Scrollbar, END, Text,
                    DoubleVar, RIGHT, Y, LEFT, BOTH, INSERT, BOTTOM, WORD, OptionMenu,EXTENDED,SUNKEN,simpledialog)
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from datetime import date
import backend
import pandas as pd
import sqlite3
import os
import sys
import getpass

window = Tk()
window.wm_title("ELF")
global primary_key_pk0
global primary_key_pk_data

def view_all():
    try:
        root = tk.Tk()
    
        xscrollbar = tk.Scrollbar(root, orient='horizontal')
        xscrollbar.pack(side=BOTTOM, fill='x')
    
        yscrollbar = tk.Scrollbar(root)
        yscrollbar.pack(side=RIGHT, fill='y')
            
        lb = tk.Listbox(root, width=150, height=20,
                        xscrollcommand=xscrollbar.set,
                        yscrollcommand=yscrollbar.set,
                        selectmode=EXTENDED,
                        relief=SUNKEN,
                        font='Times')
        yscrollbar.config(command=lb.yview)
        xscrollbar.config(command=lb.xview)
    #    yscrollbar.pack(side="right", fill="y")
        lb.pack(side="left",fill="both", expand=True)
        lb.delete(0,END)
    
        for row in backend.view():
            lb.insert(END,row)
    
        def get_selected_row(event):
            #index is cursor selection
            #select the first number in the tuple
            #try:
            global selected_tuple
            index = lb.curselection()[0]
            selected_tuple = lb.get(index)
            #this is global for UPDATE statement
            global primary_key_pk_data
            primary_key_pk_data = selected_tuple[0]
            global primary_key_pk0
            primary_key_pk0 = selected_tuple[1]
            iteration = selected_tuple[2]
            project_type = selected_tuple[3]
            project_title = selected_tuple[4]
            project_description = selected_tuple[5]
            business_unit = selected_tuple[6]
            project_name = selected_tuple[7]
            status = selected_tuple[8] 
            portfolio_alignment = selected_tuple[9]
            customer = selected_tuple[10]
            request_id = selected_tuple[11]
            notes = selected_tuple[12]
            last_update_date = selected_tuple[13]
            last_update_user = selected_tuple[14]
            receipt_date = selected_tuple[15]
            due_date = selected_tuple[16]
            erb_date = selected_tuple[17]
            manager_review_date = selected_tuple[18]
            int_finops_date = selected_tuple[19]
            boe_date = selected_tuple[20]
            date_cancelled = selected_tuple[21]
            primary_est = selected_tuple[22]
            secondary_est = selected_tuple[23]
            proj_mgr = selected_tuple[24]
            requestor = selected_tuple[25]
            technical_focal = selected_tuple[26]
            finops_focal = selected_tuple[27]
            nr_cost_est = selected_tuple[28]
            npv = selected_tuple[29]
            mirr = selected_tuple[30]
            payback = selected_tuple[31]
            bc_ratio = selected_tuple[32]
            benefit_type = selected_tuple[33]
            benefit_owner = selected_tuple[34]
            date_completed = selected_tuple[35]        
            keys = str(primary_key_pk_data) + ',' + str(primary_key_pk0)
            id_0.set("{}".format(keys))
    
            #iteration
            e1.delete(0,END)
            e1.insert(END,iteration)
            #Project Type
            tkvar_pt.set(project_type)
            #Project/Program Title
            e3.delete(0,END)
            e3.insert(END,project_title)
            #Project Program Description
            e4.delete(0,END)
            e4.insert(END,project_description)
            #Business Unit
            tkvar_bu.set(business_unit)
            #Project Name
            tkvar_pn.set(project_name)
            #Status
            tkvar_s.set(status)
            #Portfolio Alignment
            e9.delete(0,END)
            e9.insert(END,portfolio_alignment)
            #Customer
            e10.delete(0,END)
            e10.insert(END,customer)
            #Request ID
            e8.delete(0,END)
            e8.insert(END,request_id)
            #notes
            l00.delete('1.0',END)
            l00.insert(END,notes)
            #Last Update Date
            e25.delete(0,END)
            e25.insert(END,last_update_date)
            #Last Update User
            e24.delete(0,END)
            e24.insert(END,last_update_user)
            #Receipt Date
            e11.delete(0,END)
            e11.insert(END,receipt_date)
            #Due Date
            e12.delete(0,END)
            e12.insert(INSERT,due_date)
            #ERB Date
            e13.delete(0,END)
            e13.insert(INSERT,erb_date)
            #Manager Review Date
            e14.delete(0,END)
            e14.insert(INSERT,manager_review_date)
            #Integration FinOps Date
            e15.delete(0,END)
            e15.insert(INSERT,int_finops_date)
            #BOE Date
            e16.delete(0,END)
            e16.insert(INSERT,boe_date)
            #Date Cancelled
            e17.delete(0,END)
            e17.insert(INSERT,date_cancelled)
            #Primary Estimator
            e18.delete(0,END)
            e18.insert(END,primary_est)
            #Secondary Estimator
            e19.delete(0,END)
            e19.insert(END,secondary_est)
            #Project Manager
            e20.delete(0,END)
            e20.insert(END,proj_mgr)
            #Requestor
            e21.delete(0,END)
            e21.insert(END,requestor)
            #Technical Focal
            e22.delete(0,END)
            e22.insert(END,technical_focal)
            #FinOps Focal
            e23.delete(0,END)
            e23.insert(END,finops_focal)
            #NR Cost Estimate
            e26.delete(0,END)
            e26.insert(END,nr_cost_est)
            #NPV
            e27.delete(0,END)
            e27.insert(END,npv)
            #MIRR
            e28.delete(0,END)
            e28.insert(END,mirr)
            #Payback
            e29.delete(0,END)
            e29.insert(END,payback)
            #Benefit Cost Ratio
            e30.delete(0,END)
            e30.insert(END,bc_ratio)
            #Benefit Type
            e31.delete(0,END)
            e31.insert(END,benefit_type)
            #Benefit Owner
            e32.delete(0,END)
            e32.insert(END,benefit_owner)
            #Date Completed
            e33.delete(0,END)
            e33.insert(END,date_completed)
            
            #use DataFrame to load cost/benefit data
            conn = sqlite3.connect('ELF_db.db')
            sql_query = pd.read_sql_query("SELECT pk_data,pk0,Iteration,RequestId,Year,Value,Type \
                                          FROM ELF_data \
                                          ORDER BY pk0,pk_data ASC", conn)
            df1 = pd.DataFrame(sql_query, columns=['pk_data','pk0','Iteration','RequestID','Year', 'Value', 'Type'])
            #iterate over typle and store year/value in list to populate Entry windows
            df1_t = df1.T
            fkey_c = []
            fkey_b = []
            for row in df1.itertuples(index=False):
                if row[6] == "Cost" and row[1] == primary_key_pk0:
                    fkey_c.append(row[0])
                elif row[6] == "Benefit" and row[1] == primary_key_pk0:
                    fkey_b.append(row[0])
            #Cost
            for row in df1.itertuples(index=False):
                i = row[0]
                if i == min(fkey_c):
                    e1y.delete(0,END),e1c.delete(0,END)
                    e1y.insert(END,df1_t[i-1][4]), e1c.insert(END,df1_t[i-1][5])
                if i == (min(fkey_c)+1):
                    e2y.delete(0,END),e2c.delete(0,END)
                    e2y.insert(END,df1_t[i-1][4]), e2c.insert(END,df1_t[i-1][5])
                if i == (min(fkey_c)+2):
                    e3y.delete(0,END),e3c.delete(0,END)
                    e3y.insert(END,df1_t[i-1][4]), e3c.insert(END,df1_t[i-1][5])            
                if i == (min(fkey_c)+3):
                    e4y.delete(0,END),e4c.delete(0,END)
                    e4y.insert(END,df1_t[i-1][4]), e4c.insert(END,df1_t[i-1][5])
                if i == (min(fkey_c)+4):
                    e5y.delete(0,END),e5c.delete(0,END)
                    e5y.insert(END,df1_t[i-1][4]), e5c.insert(END,df1_t[i-1][5])
                if i == (min(fkey_c)+5):
                    e6y.delete(0,END),e6c.delete(0,END)
                    e6y.insert(END,df1_t[i-1][4]), e6c.insert(END,df1_t[i-1][5])
                if i == (min(fkey_c)+6):
                    e7y.delete(0,END),e7c.delete(0,END)
                    e7y.insert(END,df1_t[i-1][4]),e7c.insert(END,df1_t[i-1][5])
                if i == (min(fkey_c)+7):
                    e8y.delete(0,END),e8c.delete(0,END)
                    e8y.insert(END,df1_t[i-1][4]),e8c.insert(END,df1_t[i-1][5])
                if i == (min(fkey_c)+8):
                    e9y.delete(0,END),e9c.delete(0,END)
                    e9y.insert(END,df1_t[i-1][4]), e9c.insert(END,df1_t[i-1][5])
                if i == (min(fkey_c)+9):
                    e10y.delete(0,END),e10c.delete(0,END)
                    e10y.insert(END,df1_t[i-1][4]), e10c.insert(END,df1_t[i-1][5])
            #Benefit
            for row in df1.itertuples(index=False):
                t = row[0]
                if t == min(fkey_b):    
                    e1_b.delete(0,END),e1b.delete(0,END)
                    e1_b.insert(END,df1_t[t-1][4]), e1b.insert(END,df1_t[t-1][5])
                if t == (min(fkey_b)+1):
                    e2_b.delete(0,END),e2b.delete(0,END)
                    e2_b.insert(END,df1_t[t-1][4]), e2b.insert(END,df1_t[t-1][5])
                if t == (min(fkey_b)+2):
                    e3_b.delete(0,END),e3b.delete(0,END)
                    e3_b.insert(END,df1_t[t-1][4]), e3b.insert(END,df1_t[t-1][5])
                if t == (min(fkey_b)+3):
                    e4_b.delete(0,END),e4b.delete(0,END)
                    e4_b.insert(END,df1_t[t-1][4]), e4b.insert(END,df1_t[t-1][5])   
                if t == (min(fkey_b)+4):
                    e5_b.delete(0,END),e5b.delete(0,END)
                    e5_b.insert(END,df1_t[t-1][4]), e5b.insert(END,df1_t[t-1][5])
                if t == (min(fkey_b)+5):
                    e6_b.delete(0,END),e6b.delete(0,END)
                    e6_b.insert(END,df1_t[t-1][4]), e6b.insert(END,df1_t[t-1][5])
                if t == (min(fkey_b)+6):
                    e7_b.delete(0,END),e7b.delete(0,END)
                    e7_b.insert(END,df1_t[t-1][4]), e7b.insert(END,df1_t[t-1][5])
                if t == (min(fkey_b)+7):
                    e8_b.delete(0,END),e8b.delete(0,END)
                    e8_b.insert(END,df1_t[t-1][4]), e8b.insert(END,df1_t[t-1][5])                    
                if t == (min(fkey_b)+8):
                    e9_b.delete(0,END),e9b.delete(0,END)
                    e9_b.insert(END,df1_t[t-1][4]), e9b.insert(END,df1_t[t-1][5])
                if t == (min(fkey_b)+9):
                    e10_b.delete(0,END),e10b.delete(0,END)
                    e10_b.insert(END,df1_t[t-1][4]), e10b.insert(END,df1_t[t-1][5])

        lb.bind('<<ListboxSelect>>', get_selected_row)
    except Exception as e:
            print(str(e))
            tk.messagebox.showerror(title='Oooooops!', message='Could not compile your view: \n{}!'.format(str(e)))

def export_to_excel():
    try:
        location = os.getcwd()  
        conn = sqlite3.connect('ELF_db.db')
        df = pd.read_sql_query("SELECT * FROM ELF0, ELF_data \
                               WHERE ELF_data.pk0=ELF0.pk0", conn)
        writer = pd.ExcelWriter('ELF_export.xlsx',engine='xlsxwriter')
        df.to_excel(writer,sheet_name='ELF export')
        writer.save()
        tk.messagebox.showinfo(title='Excellent!', message='Export was a success: your file was saved here {}'.format(location))
        conn.close()
    except Exception as e:
        tk.messagebox.showwarning(title='Ooops!', message='Could not export: \n{}.'.format(str(e)))


def import_from_excel():
    try:
       #window.withdraw()
       currdir=os.getcwd()
       tempdir=filedialog.askdirectory(parent=window,initialdir=currdir,title='Please select your directory')
       if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
       
    except Exception as e:
        tk.messagebox.showerror(title='Ooops',message='Something went wrong {}'.format(e))

def find_command():
    try:
        root = tk.Tk()
        scrollbar = tk.Scrollbar(root, orient="vertical")
        global lb0
        lb0 = tk.Listbox(root, width=200, height=20, yscrollcommand=scrollbar.set, selectmode=EXTENDED, relief=SUNKEN)
        scrollbar.config(command=lb0.yview)
        
        scrollbar.pack(side="right", fill="y")
        lb0.pack(side="left",fill="both", expand=True)
        lb0.delete(0,END)
        for search in backend.search(iteration.get(), request_id.get(), primary_est.get(),tkvar_s.get()):
            lb0.insert(END, " {} ".format(search))
    except Exception as e:
        print(str(e))
        tk.messagebox.showerror(title='Oooooops!', message="Could not complete your search, please make sure the mandatory fields are populated!\nError: {}".format(str(e)))

def help_command():
    root = tk.Tk()
    scrollbar = tk.Scrollbar(root, orient="vertical")
    lb0 = tk.Listbox(root, width=200, height=20, yscrollcommand=scrollbar.set, selectmode=EXTENDED, relief=SUNKEN)
    scrollbar.config(command=lb0.yview)
    scrollbar.pack(side="right", fill="y")
    lb0.pack(side="left",fill="both", expand=True)
    lb0.insert(END,'{}'.format("ELF 3.0! Welcome. As question arise, I will continue to add the answers here."))
    lb0.insert(END,'{}'.format(""))
    lb0.insert(END,'{}'.format("0) This .db is time down. This means when looking at all records through View All, you will see multiple rows, one for every year."))
    lb0.insert(END,'{}'.format(""))
    lb0.insert(END,'{}'.format("1) Search function will not work unless you enter Primary Estimator's name, Request ID, Status, and Iteration. Look for the asterix next to the entry windows."))
    lb0.insert(END,'{}'.format(""))
    lb0.insert(END,'{}'.format("2) When making new entries, make sure to finish by clicking New Entry before Viewing All. If you select a record in the View All window, it will overwrite your current entries in the entry windows."))
    lb0.insert(END,'{}'.format(""))
    lb0.insert(END,'{}'.format("3) You can export everything in this .db into Excel for ease of use"))
    lb0.insert(END,'{}'.format(""))

def clear():
    try: 
        e1.delete(0,END), e1.insert(INSERT,'0'), 
        tkvar_pt.set(''),
        e3.delete(0,END), e3.insert(INSERT,''), 
        e4.delete(0,END), 
        e4.insert(INSERT,''),
        tkvar_bu.set(''), tkvar_pn.set(''), tkvar_s.set(''),
        e8.delete(0,END),e8.insert(INSERT,''),
        e9.delete(0,END),e9.insert(INSERT,''), 
        e10.delete(0,END),e10.insert(INSERT,''),
        e11.delete(0,END),e11.insert(INSERT,'yyyy-dd-mm'),
        e12.delete(0,END),e12.insert(INSERT,'yyyy-dd-mm'),
        e13.delete(0,END),e13.insert(INSERT,'yyyy-dd-mm'),
        e14.delete(0,END),e14.insert(INSERT,'yyyy-dd-mm'),
        e15.delete(0,END),e15.insert(INSERT,'yyyy-dd-mm'),
        e16.delete(0,END),e16.insert(INSERT,'yyyy-dd-mm'),
        e17.delete(0,END),e17.insert(INSERT,'yyyy-dd-mm'),
        e18.delete(0,END),e18.insert(INSERT,''),
        e19.delete(0,END),e19.insert(INSERT,''),
        e20.delete(0,END),e20.insert(INSERT,''),
        e21.delete(0,END),e21.insert(INSERT,''),
        e22.delete(0,END),e22.insert(INSERT,''),
        e23.delete(0,END),e23.insert(INSERT,''),
        username = getpass.getuser()
        e24.delete(0,END),e24.insert(INSERT,username),
        today=date.today()
        e25.delete(0,END),e25.insert(INSERT,today),
        e26.delete(0,END),e26.insert(INSERT,'0'),
        e27.delete(0,END),e27.insert(INSERT,'0'),
        e28.delete(0,END),e28.insert(INSERT,'0'),
        e29.delete(0,END),e29.insert(INSERT,'0'),
        e30.delete(0,END),e30.insert(INSERT,'0'),
        e31.delete(0,END),e31.insert(INSERT,''),
        e32.delete(0,END),e32.insert(INSERT,''),
        e33.delete(0,END),e33.insert(INSERT,'yyyy-dd-mm'),
        e34.delete(0,END),e34.insert(INSERT,''),
        l00.delete('1.0',END),l00.insert(INSERT,'Notes ({} on {}):'.format(username,today)),
        e1b.delete(0,END),e1b.insert(INSERT,'0'),e1_b.delete(0,END),e1_b.insert(INSERT,'0'),
        e2b.delete(0,END),e2b.insert(INSERT,'0'),e2_b.delete(0,END),e2_b.insert(INSERT,'0'),
        e3b.delete(0,END),e3b.insert(INSERT,'0'),e3_b.delete(0,END),e3_b.insert(INSERT,'0'),
        e4b.delete(0,END),e4b.insert(INSERT,'0'),e4_b.delete(0,END),e4_b.insert(INSERT,'0'),
        e5b.delete(0,END),e5b.insert(INSERT,'0'),e5_b.delete(0,END),e5_b.insert(INSERT,'0'),
        e6b.delete(0,END),e6b.insert(INSERT,'0'),e6_b.delete(0,END),e6_b.insert(INSERT,'0'),
        e7b.delete(0,END),e7b.insert(INSERT,'0'),e7_b.delete(0,END),e7_b.insert(INSERT,'0'),
        e8b.delete(0,END),e8b.insert(INSERT,'0'),e8_b.delete(0,END),e8_b.insert(INSERT,'0'),
        e9b.delete(0,END),e9b.insert(INSERT,'0'),e9_b.delete(0,END),e9_b.insert(INSERT,'0'),
        e10b.delete(0,END),e10b.insert(INSERT,'0'),e10_b.delete(0,END),e10_b.insert(INSERT,'0'),    
        e1y.delete(0,END),e1y.insert(INSERT,'0'),e1c.delete(0,END),e1c.insert(INSERT,'0'),
        e2y.delete(0,END),e2y.insert(INSERT,'0'),e2c.delete(0,END),e2c.insert(INSERT,'0'),
        e3y.delete(0,END),e3y.insert(INSERT,'0'),e3c.delete(0,END),e3c.insert(INSERT,'0'),
        e4y.delete(0,END),e4y.insert(INSERT,'0'),e4c.delete(0,END),e4c.insert(INSERT,'0'),
        e5y.delete(0,END),e5y.insert(INSERT,'0'),e5c.delete(0,END),e5c.insert(INSERT,'0'),
        e6y.delete(0,END),e6y.insert(INSERT,'0'),e6c.delete(0,END),e6c.insert(INSERT,'0'),
        e7y.delete(0,END),e7y.insert(INSERT,'0'),e7c.delete(0,END),e7c.insert(INSERT,'0'),
        e8y.delete(0,END),e8y.insert(INSERT,'0'),e8c.delete(0,END),e8c.insert(INSERT,'0'),
        e9y.delete(0,END),e9y.insert(INSERT,'0'),e9c.delete(0,END),e9c.insert(INSERT,'0'),
        e10y.delete(0,END),e10y.insert(INSERT,'0'),e10c.delete(0,END),e10c.insert(INSERT,'0')
    except Exception as e:
        print(str(e))
        tk.messagebox.showerror(title='Oooooops!', message='Could not clear your entries: \n{}!'.format(str(e)))
   
def new_entry():
    try:
        cost_year = {'year1':year_1.get(),'year2':year_2.get(),'year3':year_3.get(),'year4':year_4.get(),'year5':year_5.get(),'year6':year_6.get(),'year7':year_7.get(),'year8':year_8.get(),'year9':year_9.get(),'year10':year_10.get()}
        cost_value = {'cost1':cost_1.get(),'cost2':cost_2.get(),'cost3':cost_3.get(),'cost4':cost_4.get(),'cost5':cost_5.get(),'cost6':cost_6.get(),'cost7':cost_7.get(),'cost8':cost_8.get(),'cost9':cost_9.get(),'cost10':cost_10.get()}
        benefit_year = {'year1':byear_1.get(),'year2':byear_2.get(),'year3':byear_3.get(),'year4':byear_4.get(),'year5':byear_5.get(),'year6':byear_6.get(),'year7':byear_7.get(),'year8':byear_8.get(),'year9':byear_9.get(),'year10':byear_10.get()}        
        benefit_value = {'year1':benefit_1.get(),'year2':benefit_2.get(),'year3':benefit_3.get(),'year4':benefit_4.get(),'year5':benefit_5.get(),'year6':benefit_6.get(),'year7':benefit_7.get(),'year8':benefit_8.get(),'year9':benefit_9.get(),'year10':benefit_10.get()}                
    
        typo = {'type1':"Cost",'type2':"Benefit"}
        fields_entry = {'Iteration':e1.get(),'Project Type':tkvar_pt.get(),'Project Title':e3.get(),'Project Description':e4.get(),'Business Unit':tkvar_bu.get(),'Program Name':tkvar_pn.get(),'Status':tkvar_s.get(),'Request Id':e8.get(),'Portfolio_Alignment':e9.get(),'Customer':e10.get(),'Notes':l00.get("1.0",END),'Receipt Date':e11.get(),'Due Date':e12.get(),'ERB Date':e13.get(),'Manager Review Date':e14.get(),'FinOps Date':e15.get(),'BOE Date':e16.get(),'Date Cancelled':e17.get(),'Primary Estimator':e18.get(),'Secondary Estimator':e19.get(),'Project Manager':e20.get(),'Requestor':e21.get(),'Technical Focal':e22.get(),'FinOps Focal':e23.get(),'Last Update User':e24.get(),'Last Update Date':e25.get(),'NRE Estimate':e26.get(),'NPV ($mill)':e27.get(),'MIRR':e28.get(),'Payback(discounted)':e29.get(),'B/C Ratio':e30.get(),'Benefit Type':e31.get(),'Benefit Owner':e32.get(), 'Date Completed':e33.get()}
        counter = 0
        empty_fields = []
        for key,value  in fields_entry.items():
            if not value:
                counter += 1
                empty_fields.append(key)
                
        backend.insert_ELF(benefit_year,benefit_value,typo,cost_year,cost_value,iteration.get(),tkvar_pt.get(),proj_title.get(),proj_description.get(),tkvar_bu.get(),tkvar_pn.get(),tkvar_s.get(),port_align.get(),customer.get(),request_id.get(),l00.get("1.0",END),last_update_date.get(),last_update_user.get(),receipt_date.get(),due_date.get(),erb_date.get(),mgr_review.get(),fin_ops_date.get(),boe_date.get(),date_cancelled.get(),primary_est.get(),secondary_est.get(),proj_mgr.get(),requestor.get(),tech_focal.get(),finops_focal.get(),nr_estimate.get(),npv_mill.get(),mirr.get(),pay_backdis.get(),bc_ratio.get(),benefit_type.get(),benefit_owner.get(),date_comp.get())
        
        tk.messagebox.showinfo(title='Excellent!', message='Entry was a success!\nYou left {} field(s) empty.\n{}'.format(counter,empty_fields))
    except Exception as e:
        tk.messagebox.showerror(title='Oooooops!',message="Ooops, something went wrong: {}.".format(str(e)))

def update_command():
    try:
        year_c = {'year':e1y.get(), 'year2':e2y.get(),'year3':e3y.get(),'year4':e4y.get(),'year5':e5y.get(),'year6':e6y.get(),'year7':e7y.get(),'year8':e8y.get(),'year9':e9y.get(),'year10':e10y.get()}
        cost_c = {'year1':e1c.get(),'year2':e2c.get(),'year3':e3c.get(),'year4':e4c.get(),'year5':e5c.get(),'year6':e6c.get(),'year7':e7c.get(),'year8':e8c.get(),'year9':e9c.get(),'year10':e10c.get()}
        year_b = {'year1':e1_b.get(),'year2':e2_b.get(),'year3':e3_b.get(),'year4':e4_b.get(),'year5':e5_b.get(),'year6':e6_b.get(),'year7':e7_b.get(),'year8':e8_b.get(),'year9':e9_b.get(),'year10':e10_b.get()}
        value_b = {'year1':e1b.get(),'year2':e2b.get(),'year3':e3b.get(),'year4':e4b.get(),'year5':e5b.get(),'year6':e6b.get(),'year7':e7b.get(),'year8':e8b.get(),'year9':e9b.get(),'year10':e10b.get()}                        
        cost_year = {'year1':year_1.get(),'year2':year_2.get(),'year3':year_3.get(),'year4':year_4.get(),'year5':year_5.get(),'year6':year_6.get(),'year7':year_7.get(),'year8':year_8.get(),'year9':year_9.get(),'year10':year_10.get()}
        cost_value = {'cost1':cost_1.get(),'cost2':cost_2.get(),'cost3':cost_3.get(),'cost4':cost_4.get(),'cost5':cost_5.get(),'cost6':cost_6.get(),'cost7':cost_7.get(),'cost8':cost_8.get(),'cost9':cost_9.get(),'cost10':cost_10.get()}
        benefit_year = {'year1':byear_1.get(),'year2':byear_2.get(),'year3':byear_3.get(),'year4':byear_4.get(),'year5':byear_5.get(),'year6':byear_6.get(),'year7':byear_7.get(),'year8':byear_8.get(),'year9':byear_9.get(),'year10':byear_10.get()}
        benefit_value = {'bene1':benefit_1.get(),'bene2':benefit_2.get(),'bene3':benefit_3.get(),'bene4':benefit_4.get(),'bene5':benefit_5.get(),'bene6':benefit_6.get(),'bene7':benefit_7.get(),'bene8':benefit_8.get(),'bene9':benefit_9.get(),'bene10':benefit_10.get()}
        
        typo = {'type1':"Cost",'type2':"Benefit"}
        fields_entry = {'Iteration':e1.get(),'Project Type':tkvar_pt.get(),'Project Title':e3.get(),'Project Description':e4.get(),'Business Unit':tkvar_bu.get(),'Program Name':tkvar_pn.get(),'Status':tkvar_s.get(),'Request Id':e8.get(),'Portfolio_Alignment':e9.get(),'Customer':e10.get(),'Notes':l00.get("1.0",END),'Receipt Date':e11.get(),'Due Date':e12.get(),'ERB Date':e13.get(),'Manager Review Date':e14.get(),'FinOps Date':e15.get(),'BOE Date':e16.get(),'Date Cancelled':e17.get(),'Primary Estimator':e18.get(),'Secondary Estimator':e19.get(),'Project Manager':e20.get(),'Requestor':e21.get(),'Technical Focal':e22.get(),'FinOps Focal':e23.get(),'Last Update User':e24.get(),'Last Update Date':e25.get(),'NRE Estimate':e26.get(),'NPV ($mill)':e27.get(),'MIRR':e28.get(),'Payback(discounted)':e29.get(),'B/C Ratio':e30.get(),'Benefit Type':e31.get(),'Benefit Owner':e32.get(), 'Date Completed':e33.get()}
    
        counter = 0
        empty_fields = []
        for key,value  in fields_entry.items():
            if not value:
                counter += 1
                empty_fields.append(key)

        backend.update_ELF(primary_key_pk0,primary_key_pk_data,cost_year,cost_value,benefit_year,benefit_value,typo,iteration.get(),tkvar_pt.get(),proj_title.get(),proj_description.get(),tkvar_bu.get(),tkvar_pn.get(),tkvar_s.get(),port_align.get(),customer.get(),request_id.get(),l00.get("1.0",END),last_update_date.get(),last_update_user.get(),receipt_date.get(),due_date.get(),erb_date.get(),mgr_review.get(),fin_ops_date.get(),boe_date.get(),date_cancelled.get(),primary_est.get(),secondary_est.get(),proj_mgr.get(),requestor.get(),tech_focal.get(),finops_focal.get(),nr_estimate.get(),npv_mill.get(),mirr.get(),pay_backdis.get(),bc_ratio.get(),benefit_type.get(),benefit_owner.get(),date_comp.get())
    
        tk.messagebox.showinfo(title='Excellent!', message='Update was a success!\nYou left {} field(s) empty.\n{}'.format(counter,empty_fields))
    except Exception as e:
        print(str(e))
        tk.messagebox.showerror(title='Oooooops!',message="Ooops, something went wrong: {}.".format(str(e)))
       
def delete_command():
    try:
        USER_INP = simpledialog.askstring(title="Delete", prompt="Password: ")
        if USER_INP != 'test':
            USER_INP = simpledialog.askstring(title="Delete", prompt="Password: ")
        else:
            USER_INP_KEY = simpledialog.askinteger(title="Delete", prompt="What is the Primary Key:  ")
            backend.delete(USER_INP_KEY)
    except BaseException as e:
        print(str(e))
        tk.messagebox.showerror(title='Oooooops!', message='Could not delete your record(s): \n{}!'.format(str(e)))

l0 = Label(window, text="id",width=21,anchor=W)
l0.grid(row=0,column=0)
id_0=IntVar()
e0l= Label(window, textvariable=id_0, width=5, anchor=CENTER)
e0l.grid(row=0,column=1)

l1 = Label(window, text="Iteration*",width=21,anchor=W)
l1.grid(row=1,column=0)
iteration=IntVar()
e1=Entry(window,textvariable=iteration, width=5)
e1.insert(INSERT,"")
e1.grid(row=1,column=1)

l2 = Label(window, text="Project Type",width=21,anchor=W)
l2.grid(row=2,column=0)
# Create a Tkinter variable
tkvar_pt = StringVar(window)
# Dictionary with options
choices = { 'Government Proposal','M&A','Business Case','Consultation'}
popupMenu = OptionMenu(window, tkvar_pt, *choices)
popupMenu.grid(row=2,column=1)

l3 = Label(window, text="Project/Program Title",width=21,anchor=W)
l3.grid(row=3,column=0)
proj_title=StringVar()
e3=Entry(window,textvariable=proj_title)
e3.grid(row=3,column=1)

l4 = Label(window, text="Project Program Description",width=21,anchor=W)
l4.grid(row=4,column=0)
proj_description=StringVar()
e4=Entry(window,textvariable=proj_description)
e4.grid(row=4,column=1)

l5 = Label(window, text="Business Unit",width=21,anchor=W)
l5.grid(row=5,column=0)
# Create a Tkinter variable
tkvar_bu = StringVar(window)
# Dictionary with options
choices = { 'BDS','BGS','ET&T','BCA','EFS','WHQ'}
popupMenu = OptionMenu(window, tkvar_bu, *choices)
#Label(window, text="Choose a dish").grid(row = 1, column = 1)
popupMenu.grid(row=5,column=1)

l6 = Label(window, text="Program Name",width=21,anchor=W)
l6.grid(row=6,column=0)
# Create a Tkinter variable
tkvar_pn = StringVar(window)
# Dictionary with options
choices = { '787','737','767','777','F16','F22'}
#tkvar_pn.set('Program Name') # set the default option
popupMenu = OptionMenu(window, tkvar_pn, *choices)
popupMenu.grid(row=6,column=1)

l7 = Label(window, text="Status*",width=21,anchor=W)
l7.grid(row=7,column=0)
status=StringVar()
# Create a Tkinter variable
tkvar_s = StringVar(window)
# Dictionary with options
choices = { 'Active','Complete','Cancelled','On-Hold'}
#tkvar_s.set('Status') # set the default option
popupMenu = OptionMenu(window, tkvar_s, *choices)
popupMenu.grid(row=7,column=1)


l8 = Label(window, text="Request ID(ex. PPOA#)*",width=21,anchor=W)
l8.grid(row=8,column=0)
request_id=StringVar()
e8=Entry(window, textvariable=request_id)
e8.grid(row=8,column=1)

l9 = Label(window, text="Portfolio Alignment",width=21,anchor=W)
l9.grid(row=9,column=0)
port_align=StringVar()
e9=Entry(window, textvariable=port_align)
e9.grid(row=9,column=1)

l10 = Label(window, text="Customer",width=21,anchor=W)
l10.grid(row=10,column=0)
customer=StringVar()
e10=Entry(window, textvariable=customer)
e10.grid(row=10,column=1)

l11 = Label(window, text="Receipt Date",width=21,anchor=W)
l11.grid(row=11,column=0)
receipt_date=StringVar()
e11=Entry(window, textvariable=receipt_date)
e11.insert(INSERT,'yyyy-dd-mm')
e11.grid(row=11,column=1)

l12 = Label(window, text="Due Date",width=21,anchor=W)
l12.grid(row=12,column=0)
due_date=StringVar()
e12=Entry(window, textvariable=due_date)
e12.insert(INSERT,'yyyy-dd-mm')
e12.grid(row=12,column=1)

l13 = Label(window, text="ERB Date",width=21,anchor=W)
l13.grid(row=13,column=0)
erb_date=StringVar()
e13=Entry(window, textvariable=erb_date)
e13.insert(INSERT,'yyyy-dd-mm')
e13.grid(row=13,column=1)

l14 = Label(window, text="Mgr Review Date",width=21,anchor=W)
l14.grid(row=14,column=0)
mgr_review=StringVar()
e14=Entry(window, textvariable=mgr_review)
e14.insert(INSERT,'yyyy-dd-mm')
e14.grid(row=14,column=1)

l20 = Label(window, text="Project Manager",width=21,anchor=W)
l20.grid(row=0,column=2)
proj_mgr=StringVar()
e20=Entry(window, textvariable=proj_mgr)
e20.grid(row=0,column=3)

l21 = Label(window, text="Requestor",width=21,anchor=W)
l21.grid(row=1,column=2)
requestor=StringVar()
e21=Entry(window, textvariable=requestor)
e21.grid(row=1,column=3)

l22 = Label(window, text="Technical Focal",width=21,anchor=W)
l22.grid(row=2,column=2)
tech_focal=StringVar()
e22=Entry(window, textvariable=tech_focal)
e22.grid(row=2,column=3)

l23 = Label(window, text="FinOps Focal",width=21,anchor=W)
l23.grid(row=3,column=2)
finops_focal=StringVar()
e23=Entry(window, textvariable=finops_focal)
e23.grid(row=3,column=3)

l24 = Label(window, text="Last Update User",width=21,anchor=W)
l24.grid(row=4,column=2)
last_update_user=StringVar()
e24=Entry(window, textvariable=last_update_user)
username = getpass.getuser()
e24.insert(INSERT,username)
e24.configure(state='disable')
e24.grid(row=4,column=3)

l25 = Label(window, text="Last Update Date",width=21,anchor=W)
l25.grid(row=5,column=2)
last_update_date=StringVar()
e25=Entry(window, textvariable=last_update_date)
today=date.today()
e25.insert(INSERT,today)
e25.configure(state='disabled')
e25.grid(row=5,column=3)

l26 = Label(window, text="NR Cost Estimate ($ in Mil.)",width=21,anchor=W)
l26.grid(row=6,column=2)
nr_estimate=DoubleVar()
e26=Entry(window, textvariable=nr_estimate)
e26.grid(row=6,column=3)

l27 = Label(window, text="NPV ($ in Mil.)",width=21,anchor=W)
l27.grid(row=7,column=2)
npv_mill=DoubleVar()
e27=Entry(window, textvariable=npv_mill)
e27.grid(row=7,column=3)

l28 = Label(window, text="MIRR",width=21,anchor=W)
l28.grid(row=8,column=2)
mirr=DoubleVar()
e28=Entry(window, textvariable=mirr)
e28.grid(row=8,column=3)

l29 = Label(window, text="Payback (Discounted)",width=21,anchor=W)
l29.grid(row=9,column=2)
pay_backdis=DoubleVar()
e29=Entry(window, textvariable=pay_backdis)
e29.grid(row=9,column=3)

l30 = Label(window, text="Benefit/Cost Ratio",width=21,anchor=W)
l30.grid(row=10,column=2)
bc_ratio=DoubleVar()
e30=Entry(window, textvariable=bc_ratio)
e30.grid(row=10,column=3)

l31 = Label(window, text="Benefit Type",width=21,anchor=W)
l31.grid(row=11,column=2)
benefit_type=StringVar()
e31=Entry(window, textvariable=benefit_type)
e31.grid(row=11,column=3)

l32 = Label(window, text="Benefit Owner",width=21,anchor=W)
l32.grid(row=12,column=2)
benefit_owner=StringVar()
e32=Entry(window, textvariable=benefit_owner)
e32.grid(row=12,column=3)

l33 = Label(window, text="Date Completed",width=21,anchor=W)
l33.grid(row=13,column=2)
date_comp=StringVar()
e33=Entry(window, textvariable=date_comp)
e33.insert(INSERT,'yyyy-dd-mm')
e33.grid(row=13,column=3)

l34 = Label(window, text="Free Field",width=21,anchor=W)
l34.grid(row=14,column=2)
ty_pe=StringVar()
e34=Entry(window, textvariable=ty_pe, state='disable')
e34.grid(row=14,column=3)
#----------------------------------------------------------------------
l15 = Label(window, text="Int/FinOps Date",width=21,anchor=W)
l15.grid(row=0,column=4)
fin_ops_date=StringVar()
e15=Entry(window, textvariable=fin_ops_date)
e15.insert(INSERT,'yyyy-dd-mm')
e15.grid(row=0,column=5)

l16 = Label(window, text="BOE Date",width=21,anchor=W)
l16.grid(row=1,column=4)
boe_date=StringVar()
e16=Entry(window, textvariable=boe_date)
e16.insert(INSERT,'yyyy-dd-mm')
e16.grid(row=1,column=5)

l17 = Label(window, text="Date Cancelled",width=21,anchor=W)
l17.grid(row=2,column=4)
date_cancelled=StringVar()
e17=Entry(window, textvariable=date_cancelled)
e17.insert(INSERT,'yyyy-dd-mm')
e17.grid(row=2,column=5)

l18 = Label(window, text="Primary Estimator*",width=21,anchor=W)
l18.grid(row=3,column=4)
primary_est=StringVar()
e18=Entry(window, textvariable=primary_est)
e18.grid(row=3,column=5)

l19 = Label(window, text="Secondary Estimator",width=21,anchor=W)
l19.grid(row=4,column=4)
secondary_est=StringVar()
e19=Entry(window, textvariable=secondary_est)
e19.grid(row=4,column=5)
#-------------------------------------------------------------------------


#Cost Label followed by window entries
c_year = Label(window, text="Cost Years",width=21,anchor=CENTER)
c_year.grid(row=21, column=0)

c_cost = Label(window, text="Cost ($)",width=21,anchor=CENTER)
c_cost.grid(row=21, column=1)


year_1=IntVar()
e1y=Entry(window, textvariable=year_1, width=5)
e1y.grid(row=22,column=0)
cost_1=DoubleVar()
e1c=Entry(window, textvariable=cost_1, width=10)
e1c.grid(row=22,column=1)

year_2=IntVar()
e2y=Entry(window, textvariable=year_2, width=5)
e2y.grid(row=23,column=0)
cost_2=DoubleVar()
e2c=Entry(window, textvariable=cost_2, width=10)
e2c.grid(row=23,column=1)

year_3=IntVar()
e3y=Entry(window, textvariable=year_3, width=5)
e3y.grid(row=24,column=0)
cost_3=DoubleVar()
e3c=Entry(window, textvariable=cost_3, width=10)
e3c.grid(row=24,column=1)

year_4=IntVar()
e4y=Entry(window, textvariable=year_4, width=5)
e4y.grid(row=25,column=0)
cost_4=DoubleVar()
e4c=Entry(window, textvariable=cost_4, width=10)
e4c.grid(row=25,column=1)

year_5=IntVar()
e5y=Entry(window, textvariable=year_5, width=5)
e5y.grid(row=26,column=0)
cost_5=DoubleVar()
e5c=Entry(window, textvariable=cost_5, width=10)
e5c.grid(row=26,column=1)

year_6=IntVar()
e6y=Entry(window, textvariable=year_6, width=5)
e6y.grid(row=27,column=0)
cost_6=DoubleVar()
e6c=Entry(window, textvariable=cost_6, width=10)
e6c.grid(row=27,column=1)

year_7=IntVar()
e7y=Entry(window, textvariable=year_7, width=5)
e7y.grid(row=28,column=0)
cost_7=DoubleVar()
e7c=Entry(window, textvariable=cost_7, width=10)
e7c.grid(row=28,column=1)

year_8=IntVar()
e8y=Entry(window, textvariable=year_8, width=5)
e8y.grid(row=29,column=0)
cost_8=DoubleVar()
e8c=Entry(window, textvariable=cost_8, width=10)
e8c.grid(row=29,column=1)

year_9=IntVar()
e9y=Entry(window, textvariable=year_9, width=5)
e9y.grid(row=30,column=0)
cost_9=DoubleVar()
e9c=Entry(window, textvariable=cost_9, width=10)
e9c.grid(row=30,column=1)

year_10=IntVar()
e10y=Entry(window, textvariable=year_10, width=5)
e10y.grid(row=31,column=0)
cost_10=DoubleVar()
e10c=Entry(window, textvariable=cost_10, width=10)
e10c.grid(row=31,column=1)

#Cost Label followed by window entries
b_year = Label(window, text="Benefit Years",width=21,anchor=CENTER)
b_year.grid(row=21, column=2)

b_cost = Label(window, text="Benefit($)",width=21,anchor=CENTER)
b_cost.grid(row=21, column=3)

byear_1=IntVar()
e1_b=Entry(window, textvariable=byear_1, width=5)
e1_b.grid(row=22,column=2)
benefit_1=DoubleVar()
e1b=Entry(window, textvariable=benefit_1, width=10)
e1b.grid(row=22,column=3)

byear_2=IntVar()
e2_b=Entry(window, textvariable=byear_2, width=5)
e2_b.grid(row=23,column=2)
benefit_2=DoubleVar()
e2b=Entry(window, textvariable=benefit_2, width=10)
e2b.grid(row=23,column=3)

byear_3=IntVar()
e3_b=Entry(window, textvariable=byear_3, width=5)
e3_b.grid(row=24,column=2)
benefit_3=DoubleVar()
e3b=Entry(window, textvariable=benefit_3, width=10)
e3b.grid(row=24,column=3)

byear_4=IntVar()
e4_b=Entry(window, textvariable=byear_4, width=5)
e4_b.grid(row=25,column=2)
benefit_4=DoubleVar()
e4b=Entry(window, textvariable=benefit_4, width=10)
e4b.grid(row=25,column=3)

byear_5=IntVar()
e5_b=Entry(window, textvariable=byear_5, width=5)
e5_b.grid(row=26,column=2)
benefit_5=DoubleVar()
e5b=Entry(window, textvariable=benefit_5, width=10)
e5b.grid(row=26,column=3)

byear_6=IntVar()
e6_b=Entry(window, textvariable=byear_6, width=5)
e6_b.grid(row=27,column=2)
benefit_6=DoubleVar()
e6b=Entry(window, textvariable=benefit_6, width=10)
e6b.grid(row=27,column=3)

byear_7=IntVar()
e7_b=Entry(window, textvariable=byear_7, width=5)
e7_b.grid(row=28,column=2)
benefit_7=DoubleVar()
e7b=Entry(window, textvariable=benefit_7, width=10)
e7b.grid(row=28,column=3)

byear_8=IntVar()
e8_b=Entry(window, textvariable=byear_8, width=5)
e8_b.grid(row=29,column=2)
benefit_8=DoubleVar()
e8b=Entry(window, textvariable=benefit_8, width=10)
e8b.grid(row=29,column=3)

byear_9=IntVar()
e9_b=Entry(window, textvariable=byear_9, width=5)
e9_b.grid(row=30,column=2)
benefit_9=DoubleVar()
e9b=Entry(window, textvariable=benefit_9, width=10)
e9b.grid(row=30,column=3)

byear_10=IntVar()
e10_b=Entry(window, textvariable=byear_10, width=5)
e10_b.grid(row=31,column=2)
benefit_10=DoubleVar()
e10b=Entry(window, textvariable=benefit_10, width=10)
e10b.grid(row=31,column=3)
#----------------------Textbox for notes----------------------
today=date.today()
small_font = ('Verdana',8)
l00=StringVar()
l00 = Text(window, height=23, font=small_font, width=30,wrap=WORD)
l00.grid(row=5, column=4, columnspan=2, rowspan=20)
username = getpass.getuser()
l00.insert(INSERT,'Notes ({} on {}):'.format(username,today))
l00.get('1.0',END)

#Label for buttons
l01 = Label(window, text="Actions",width=21,anchor=CENTER)
l01.grid(row=25, column=4, columnspan=2)

#Buttons for action items
b0 = Button(window, text="xlsx -> db", width =12, command = import_from_excel)
b0.grid(row=27, column=4)

b1 = Button(window, text="New Entry", width=12,command=new_entry)
b1.grid(row=28,column=4)

b2 = Button(window, text="Delete Record", width=12,command=delete_command)
b2.grid(row=28,column=5)
#, state='disable'

b3 = Button(window, text="Update Record", width=12, command=update_command)
b3.grid(row=29,column=4)

b4 = Button(window, text="View All", width=12,command=view_all)
b4.grid(row=29,column=5)

b5 = Button(window, text="db -> xlsx", width=12, command=export_to_excel)
b5.grid(row=30,column=4)

b6 = Button(window, text="Clear", width=12, command=clear)
b6.grid(row=30,column=5)

b7 = Button(window, text="Find*", width=12, command=find_command)
b7.grid(row=31,column=4)

b8 = Button(window, text="Close", width=12, command=window.destroy)
b8.grid(row=31,column=5)

b9 = Button(window, text='Help', width=12,command=help_command)
b9.grid(row=27,column=5)

window.mainloop()
    