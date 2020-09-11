# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:23:37 2020

@author: Pepper
"""

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from datetime import date
import backend
import pandas as pd
import sqlite3
import os
import getpass

window = Tk()
window.wm_title("ELF")
global primary_key_pk0
global primary_key_pk_data


def view_all():
    try:
        root = tk.Tk()
        # horizontal scroll
        xscrollbar = tk.Scrollbar(root, orient='horizontal')
        xscrollbar.pack(side=BOTTOM, fill='x')

        # vertical scroll
        yscrollbar = tk.Scrollbar(root)
        yscrollbar.pack(side=RIGHT, fill='y')
        # selectmode = EXTENDED,
        # relief = SUNKEN,

        data_box = LabelFrame(root, text='Estimating Log Form', bd=4, labelanchor='n', font='Arial 10 bold', fg='navy blue', width=160, height=20)
        data_box.pack(fill='both', expand='yes')

        lb = tk.Listbox(data_box, width=160, height=20,
                        xscrollcommand=xscrollbar.set,
                        yscrollcommand=yscrollbar.set,
                        font='Times')

        yscrollbar.config(command=lb.yview)
        xscrollbar.config(command=lb.xview)

        lb.pack(side="top", fill='both', expand=True)
        lb.delete(0, END)

        for row in backend.view():
            lb.insert(END, row)


        def get_selected_row(event):
            # index is cursor selection
            # select the first number in the tuple
            # try:
            global selected_tuple
            index = lb.curselection()[0]
            selected_tuple = lb.get(index)
            # this is global for UPDATE statement
            global primary_key_pk_data
            #foreign key
            primary_key_pk_data = selected_tuple[0]
            print(primary_key_pk_data)
            global primary_key_pk0
            #primary key
            primary_key_pk0 = selected_tuple[1]
            # iteration
            iteration_tup = selected_tuple[2]
            iteration_ver.delete(0, END)
            iteration_ver.insert(END, iteration_tup)
            # Project Type
            project_type_tup = selected_tuple[3]
            tkvar_pt.set(project_type_tup)
            # Program Title
            project_title_tup = selected_tuple[4]
            prog_title.delete(0, END)
            prog_title.insert(END, project_title_tup)
            #primary and foreign keys
            keys = str(primary_key_pk_data) + ',' + str(primary_key_pk0)
            id_0.set("{}".format(keys))
            #Program Description
            project_description_tup = selected_tuple[5]
            prog_desc.delete(0, END)
            prog_desc.insert(END, project_description_tup)
            # Business Unit
            business_unit_tup = selected_tuple[6]
            tkvar_bu.set(business_unit_tup)
            # Project Name
            project_name_tup = selected_tuple[7]
            tkvar_pn.set(project_name_tup)
            # Status
            status_tup = selected_tuple[8]
            tkvar_s.set(status_tup)
            # Portfolio Alignment
            portfolio_alignment_tup = selected_tuple[9]
            pfm_align.delete(0, END)
            pfm_align.insert(END, portfolio_alignment_tup)
            # Customer
            customer_tup = selected_tuple[10]
            cust.delete(0, END)
            cust.insert(END, customer_tup)
            # Request #
            request_id_tup = selected_tuple[11]
            req_id.delete(0, END)
            req_id.insert(END, request_id_tup)
            # notes
            notes_tup = selected_tuple[12]
            usr_notes.delete('1.0', END)
            usr_notes.insert(END, notes_tup)
            # Last Update Date
            last_update_date_tup = selected_tuple[13]
            last_update.delete(0, END)
            last_update.insert(END, last_update_date_tup)
            # Last Update User
            last_update_user_tup = selected_tuple[14]
            last_update_usr.delete(0, END)
            last_update_usr.insert(END, last_update_user_tup)
            # Receipt Date
            receipt_date_tup = selected_tuple[15]
            date_receipt.delete(0, END)
            date_receipt.insert(END, receipt_date_tup)
            # Due Date
            due_date_tup = selected_tuple[16]
            date_due.delete(0, END)
            date_due.insert(INSERT, due_date_tup)
            # ERB Date
            erb_date_tup = selected_tuple[17]
            date_erb.delete(0, END)
            date_erb.insert(INSERT, erb_date_tup)
            # Manager Review Date
            manager_review_date_tup = selected_tuple[18]
            manager_date.delete(0, END)
            manager_date.insert(INSERT, manager_review_date_tup)
            # Integration Finance Date
            int_finops_date_tup = selected_tuple[19]
            finops_date.delete(0, END)
            finops_date.insert(INSERT, int_finops_date_tup)
            # BOE Date
            boe_date_tup = selected_tuple[20]
            date_boe.delete(0, END)
            date_boe.insert(INSERT, boe_date_tup)
            # Date Cancelled
            date_cancelled_tup = selected_tuple[21]
            date_cnl.delete(0, END)
            date_cnl.insert(INSERT, date_cancelled_tup)
            # Primary analyst
            primary_est_tup = selected_tuple[22]
            prime_analyst.delete(0, END)
            prime_analyst.insert(END, primary_est_tup)
            # Secondary Estimator
            secondary_est_tup = selected_tuple[23]
            sec_analyst.delete(0, END)
            sec_analyst.insert(END, secondary_est_tup)
            # Project Manager
            proj_mgr_tup = selected_tuple[24]
            project_mgr.delete(0, END)
            project_mgr.insert(END, proj_mgr_tup)
            # Requester
            requester_tup = selected_tuple[25]
            requester.delete(0, END)
            requester.insert(END, requester_tup)
            # Technical Focal
            technical_focal_tup = selected_tuple[26]
            tech_analyst.delete(0, END)
            tech_analyst.insert(END, technical_focal_tup)
            # Finance analyst
            finops_focal_tup = selected_tuple[27]
            finops_analyst.delete(0, END)
            finops_analyst.insert(END, finops_focal_tup)
            # NR Cost Estimate
            nr_cost_est_tup = selected_tuple[28]
            nr_cost.delete(0, END)
            nr_cost.insert(END, nr_cost_est_tup)
            # NPV
            npv_tup = selected_tuple[29]
            npv.delete(0, END)
            npv.insert(END, npv_tup)
            # MIRR
            mirr_tup = selected_tuple[30]
            modirr.delete(0, END)
            modirr.insert(END, mirr_tup)
            # Payback
            payback_tup = selected_tuple[31]
            payback_disc.delete(0, END)
            payback_disc.insert(END, payback_tup)
            # Benefit Cost Ratio
            bc_ratio_tup = selected_tuple[32]
            bc_rat.delete(0, END)
            bc_rat.insert(END, bc_ratio_tup)
            # Benefit Type
            benefit_type_tup = selected_tuple[33]
            ben_type.delete(0, END)
            ben_type.insert(END, benefit_type_tup)
            # Benefit Owner
            benefit_owner_tup = selected_tuple[34]
            ben_owner.delete(0, END)
            ben_owner.insert(END, benefit_owner_tup)
            # Date Completed
            date_completed_tup = selected_tuple[35]
            date_completed.delete(0, END)
            date_completed.insert(END, date_completed_tup)

            # use DataFrame to load cost/benefit data
            conn = sqlite3.connect('ELF_db.db')
            sql_query = pd.read_sql_query("SELECT pk_data,pk0,Iteration,RequestId,Year,Value,Type \
                                          FROM ELF_data \
                                          ORDER BY pk0,pk_data ASC", conn)
            df1 = pd.DataFrame(sql_query, columns=['pk_data', 'pk0', 'Iteration', 'RequestID', 'Year', 'Value', 'Type'])
            # iterate over typle and store year/value in list to populate Entry windows
            df1_t = df1.T
            fkey_c = []
            fkey_b = []
            for row in df1.itertuples(index=False):
                if row[6] == "Cost" and row[1] == primary_key_pk0:
                    fkey_c.append(row[0])
                elif row[6] == "Benefit" and row[1] == primary_key_pk0:
                    fkey_b.append(row[0])
            # Cost
            for row in df1.itertuples(index=False):
                i = row[0]
                if i == min(fkey_c):
                    yr_1_cost.delete(0, END), cost_yr_1.delete(0, END)
                    yr_1_cost.insert(END, df1_t[i - 1][4]), cost_yr_1.insert(END, df1_t[i - 1][5])
                if i == (min(fkey_c) + 1):
                    yr_2_cost.delete(0, END), cost_yr_2.delete(0, END)
                    yr_2_cost.insert(END, df1_t[i - 1][4]), cost_yr_2.insert(END, df1_t[i - 1][5])
                if i == (min(fkey_c) + 2):
                    yr_3_cost.delete(0, END), cost_yr_3.delete(0, END)
                    yr_3_cost.insert(END, df1_t[i - 1][4]), cost_yr_3.insert(END, df1_t[i - 1][5])
                if i == (min(fkey_c) + 3):
                    yr_4_cost.delete(0, END), cost_yr_4.delete(0, END)
                    yr_4_cost.insert(END, df1_t[i - 1][4]), cost_yr_4.insert(END, df1_t[i - 1][5])
                if i == (min(fkey_c) + 4):
                    yr_5_cost.delete(0, END), cost_yr_5.delete(0, END)
                    yr_5_cost.insert(END, df1_t[i - 1][4]), cost_yr_5.insert(END, df1_t[i - 1][5])
                if i == (min(fkey_c) + 5):
                    yr_6_cost.delete(0, END), cost_year_6.delete(0, END)
                    yr_6_cost.insert(END, df1_t[i - 1][4]), cost_year_6.insert(END, df1_t[i - 1][5])
                if i == (min(fkey_c) + 6):
                    yr_7_cost.delete(0, END), cost_year_7.delete(0, END)
                    yr_7_cost.insert(END, df1_t[i - 1][4]), cost_year_7.insert(END, df1_t[i - 1][5])
                if i == (min(fkey_c) + 7):
                    yr_8_cost.delete(0, END), cost_year_8.delete(0, END)
                    yr_8_cost.insert(END, df1_t[i - 1][4]), cost_year_8.insert(END, df1_t[i - 1][5])
                if i == (min(fkey_c) + 8):
                    yr_9_cost.delete(0, END), cost_yr_9.delete(0, END)
                    yr_9_cost.insert(END, df1_t[i - 1][4]), cost_yr_9.insert(END, df1_t[i - 1][5])
                if i == (min(fkey_c) + 9):
                    yr_10_cost.delete(0, END), cost_yr_10.delete(0, END)
                    yr_10_cost.insert(END, df1_t[i - 1][4]), cost_yr_10.insert(END, df1_t[i - 1][5])
            # Benefit
            for row in df1.itertuples(index=False):
                t = row[0]
                if t == min(fkey_b):
                    yr_1_ben.delete(0, END), ben_yr_1.delete(0, END)
                    yr_1_ben.insert(END, df1_t[t - 1][4]), ben_yr_1.insert(END, df1_t[t - 1][5])
                if t == (min(fkey_b) + 1):
                    yr_2_ben.delete(0, END), ben_yr_2.delete(0, END)
                    yr_2_ben.insert(END, df1_t[t - 1][4]), ben_yr_2.insert(END, df1_t[t - 1][5])
                if t == (min(fkey_b) + 2):
                    yr_3_ben.delete(0, END), ben_yr_3.delete(0, END)
                    yr_3_ben.insert(END, df1_t[t - 1][4]), ben_yr_3.insert(END, df1_t[t - 1][5])
                if t == (min(fkey_b) + 3):
                    yr_4_ben.delete(0, END), ben_yr_4.delete(0, END)
                    yr_4_ben.insert(END, df1_t[t - 1][4]), ben_yr_4.insert(END, df1_t[t - 1][5])
                if t == (min(fkey_b) + 4):
                    yr_5_ben.delete(0, END), ben_yr_5.delete(0, END)
                    yr_5_ben.insert(END, df1_t[t - 1][4]), ben_yr_5.insert(END, df1_t[t - 1][5])
                if t == (min(fkey_b) + 5):
                    yr_6_ben.delete(0, END), ben_yr_6.delete(0, END)
                    yr_6_ben.insert(END, df1_t[t - 1][4]), ben_yr_6.insert(END, df1_t[t - 1][5])
                if t == (min(fkey_b) + 6):
                    yr_7_ben.delete(0, END), ben_yr_7.delete(0, END)
                    yr_7_ben.insert(END, df1_t[t - 1][4]), ben_yr_7.insert(END, df1_t[t - 1][5])
                if t == (min(fkey_b) + 7):
                    yr_8_ben.delete(0, END), ben_yr_8.delete(0, END)
                    yr_8_ben.insert(END, df1_t[t - 1][4]), ben_yr_8.insert(END, df1_t[t - 1][5])
                if t == (min(fkey_b) + 8):
                    yr_9_ben.delete(0, END), ben_yr_9.delete(0, END)
                    yr_9_ben.insert(END, df1_t[t - 1][4]), ben_yr_9.insert(END, df1_t[t - 1][5])
                if t == (min(fkey_b) + 9):
                    yr10_ben.delete(0, END), ben_yr_10.delete(0, END)
                    yr10_ben.insert(END, df1_t[t - 1][4]), ben_yr_10.insert(END, df1_t[t - 1][5])

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
        writer = pd.ExcelWriter('ELF_export.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='ELF export')
        writer.save()
        tk.messagebox.showinfo(title='Excellent!',
                               message='Export was a success: your file was saved here {}'.format(location))
        conn.close()
    except Exception as e:
        tk.messagebox.showwarning(title='Ooops!', message='Could not export: \n{}.'.format(str(e)))


def update_enmasse():
    try:
        currdir = os.getcwd()
        window = tk.Tk()
        window.withdraw()
        # ask for file
        file_path = filedialog.askopenfilename()
        data = pd.read_excel(file_path)
        # backend for sql connection
        backend.update_enmasse(data)

    except Exception as e:
        tk.messagebox.showerror(title='Ooops', message='Something went wrong {}'.format(e))


def find_command():
    try:
        root = tk.Tk()
        scrollbar = tk.Scrollbar(root, orient="vertical")
        global find_btn
        find_btn = tk.Listbox(root, width=200, height=20, yscrollcommand=scrollbar.set, selectmode=EXTENDED, relief=SUNKEN)
        scrollbar.config(command=find_btn.yview)

        scrollbar.pack(side="right", fill="y")
        find_btn.pack(side="left", fill="both", expand=True)
        find_btn.delete(0, END)
        for search in backend.search(iteration.get(), request_id.get(), primary_est.get(), tkvar_s.get()):
            find_btn.insert(END, " {} ".format(search))
    except Exception as e:
        print(str(e))
        tk.messagebox.showerror(title='Oooooops!',
                                message="Could not complete your search, please make sure the mandatory fields are populated!\nError: {}".format(
                                    str(e)))


def help_command():
    root = tk.Tk()
    scrollbar = tk.Scrollbar(root, orient="vertical")
    help_btn = tk.Listbox(root, width=200, height=20, yscrollcommand=scrollbar.set, selectmode=EXTENDED, relief=SUNKEN)
    scrollbar.config(command=help_btn.yview)
    scrollbar.pack(side="right", fill="y")
    help_btn.pack(side="left", fill="both", expand=True)
    help_btn.insert(END, '{}'.format("Welcome. As question arise, I will continue to add the answers here."))
    help_btn.insert(END, '{}'.format(""))
    help_btn.insert(END, '{}'.format(
        "0) This .db is time down. This means when looking at all records through View All, you will see multiple rows, one for every year."))
    help_btn.insert(END, '{}'.format(""))
    help_btn.insert(END, '{}'.format(
        "1) Search function will not work unless you enter Primary Analyst's name, Request #, Status, and Iteration. Look for the asterix next to the entry windows."))
    help_btn.insert(END, '{}'.format(""))
    help_btn.insert(END, '{}'.format(
        "2) When making new entries, make sure to finish by clicking New Entry before Viewing All. If you select a record in the View All window, it will overwrite your current entries in the entry windows."))
    help_btn.insert(END, '{}'.format(""))
    help_btn.insert(END, '{}'.format("3) You can export everything in this .db into Excel for ease of use"))
    help_btn.insert(END, '{}'.format(""))
    help_btn.insert(END, '{}'.format("4) You can mass update everything in this .db from Excel for ease of use. To do so, please keep the format of the exported file or else you will experience errors."))
    help_btn.insert(END, '{}'.format(""))


def clear():
    try:
        iteration_ver.delete(0, END), iteration_ver.insert(INSERT, '0'),
        tkvar_pt.set(''),
        prog_title.delete(0, END), prog_title.insert(INSERT, ''),
        prog_desc.delete(0, END),
        prog_desc.insert(INSERT, ''),
        tkvar_bu.set(''), tkvar_pn.set(''), tkvar_s.set(''),
        req_id.delete(0, END), req_id.insert(INSERT, ''),
        pfm_align.delete(0, END), pfm_align.insert(INSERT, ''),
        cust.delete(0, END), cust.insert(INSERT, ''),
        date_receipt.delete(0, END), date_receipt.insert(INSERT, 'yyyy-dd-mm'),
        date_due.delete(0, END), date_due.insert(INSERT, 'yyyy-dd-mm'),
        date_erb.delete(0, END), date_erb.insert(INSERT, 'yyyy-dd-mm'),
        manager_date.delete(0, END), manager_date.insert(INSERT, 'yyyy-dd-mm'),
        finops_date.delete(0, END), finops_date.insert(INSERT, 'yyyy-dd-mm'),
        date_boe.delete(0, END), date_boe.insert(INSERT, 'yyyy-dd-mm'),
        date_cnl.delete(0, END), date_cnl.insert(INSERT, 'yyyy-dd-mm'),
        prime_analyst.delete(0, END), prime_analyst.insert(INSERT, ''),
        sec_analyst.delete(0, END), sec_analyst.insert(INSERT, ''),
        project_mgr.delete(0, END), project_mgr.insert(INSERT, ''),
        requester.delete(0, END), requester.insert(INSERT, ''),
        tech_analyst.delete(0, END), tech_analyst.insert(INSERT, ''),
        finops_analyst.delete(0, END), finops_analyst.insert(INSERT, ''),
        username = getpass.getuser()
        last_update_usr.delete(0, END), last_update_usr.insert(INSERT, username),
        today = date.today()
        last_update.delete(0, END), last_update.insert(INSERT, today),
        nr_cost.delete(0, END), nr_cost.insert(INSERT, '0'),
        npv.delete(0, END), npv.insert(INSERT, '0'),
        modirr.delete(0, END), modirr.insert(INSERT, '0'),
        payback_disc.delete(0, END), payback_disc.insert(INSERT, '0'),
        bc_rat.delete(0, END), bc_rat.insert(INSERT, '0'),
        ben_type.delete(0, END), ben_type.insert(INSERT, ''),
        ben_owner.delete(0, END), ben_owner.insert(INSERT, ''),
        date_completed.delete(0, END), date_completed.insert(INSERT, 'yyyy-dd-mm'),
        free_field.delete(0, END), free_field.insert(INSERT, ''),
        usr_notes.delete('1.0', END), usr_notes.insert(INSERT, 'Notes ({} on {}):'.format(username, today)),
        ben_yr_1.delete(0, END), ben_yr_1.insert(INSERT, '0'), yr_1_ben.delete(0, END), yr_1_ben.insert(INSERT, '0'),
        ben_yr_2.delete(0, END), ben_yr_2.insert(INSERT, '0'), yr_2_ben.delete(0, END), yr_2_ben.insert(INSERT, '0'),
        ben_yr_3.delete(0, END), ben_yr_3.insert(INSERT, '0'), yr_3_ben.delete(0, END), yr_3_ben.insert(INSERT, '0'),
        ben_yr_4.delete(0, END), ben_yr_4.insert(INSERT, '0'), yr_4_ben.delete(0, END), yr_4_ben.insert(INSERT, '0'),
        ben_yr_5.delete(0, END), ben_yr_5.insert(INSERT, '0'), yr_5_ben.delete(0, END), yr_5_ben.insert(INSERT, '0'),
        ben_yr_6.delete(0, END), ben_yr_6.insert(INSERT, '0'), yr_6_ben.delete(0, END), yr_6_ben.insert(INSERT, '0'),
        ben_yr_7.delete(0, END), ben_yr_7.insert(INSERT, '0'), yr_7_ben.delete(0, END), yr_7_ben.insert(INSERT, '0'),
        ben_yr_8.delete(0, END), ben_yr_8.insert(INSERT, '0'), yr_8_ben.delete(0, END), yr_8_ben.insert(INSERT, '0'),
        ben_yr_9.delete(0, END), ben_yr_9.insert(INSERT, '0'), yr_9_ben.delete(0, END), yr_9_ben.insert(INSERT, '0'),
        ben_yr_10.delete(0, END), ben_yr_10.insert(INSERT, '0'), yr10_ben.delete(0, END), yr10_ben.insert(INSERT, '0'),
        yr_1_cost.delete(0, END), yr_1_cost.insert(INSERT, '0'), cost_yr_1.delete(0, END), cost_yr_1.insert(INSERT, '0'),
        yr_2_cost.delete(0, END), yr_2_cost.insert(INSERT, '0'), cost_yr_2.delete(0, END), cost_yr_2.insert(INSERT, '0'),
        yr_3_cost.delete(0, END), yr_3_cost.insert(INSERT, '0'), cost_yr_3.delete(0, END), cost_yr_3.insert(INSERT, '0'),
        yr_4_cost.delete(0, END), yr_4_cost.insert(INSERT, '0'), cost_yr_4.delete(0, END), cost_yr_4.insert(INSERT, '0'),
        yr_5_cost.delete(0, END), yr_5_cost.insert(INSERT, '0'), cost_yr_5.delete(0, END), cost_yr_5.insert(INSERT, '0'),
        yr_6_cost.delete(0, END), yr_6_cost.insert(INSERT, '0'), cost_year_6.delete(0, END), cost_year_6.insert(INSERT, '0'),
        yr_7_cost.delete(0, END), yr_7_cost.insert(INSERT, '0'), cost_year_7.delete(0, END), cost_year_7.insert(INSERT, '0'),
        yr_8_cost.delete(0, END), yr_8_cost.insert(INSERT, '0'), cost_year_8.delete(0, END), cost_year_8.insert(INSERT, '0'),
        yr_9_cost.delete(0, END), yr_9_cost.insert(INSERT, '0'), cost_yr_9.delete(0, END), cost_yr_9.insert(INSERT, '0'),
        yr_10_cost.delete(0, END), yr_10_cost.insert(INSERT, '0'), cost_yr_10.delete(0, END), cost_yr_10.insert(INSERT, '0')
    except Exception as e:
        print(str(e))
        tk.messagebox.showerror(title='Oooooops!', message='Could not clear your entries: \n{}!'.format(str(e)))


def new_entry():
    try:
        cost_year = {'year1': year_1.get(), 'year2': year_2.get(), 'year3': year_3.get(), 'year4': year_4.get(),
                     'year5': year_5.get(), 'year6': year_6.get(), 'year7': year_7.get(), 'year8': year_8.get(),
                     'year9': year_9.get(), 'year10': year_10.get()}
        cost_value = {'cost1': cost_1.get(), 'cost2': cost_2.get(), 'cost3': cost_3.get(), 'cost4': cost_4.get(),
                      'cost5': cost_5.get(), 'cost6': cost_6.get(), 'cost7': cost_7.get(), 'cost8': cost_8.get(),
                      'cost9': cost_9.get(), 'cost10': cost_10.get()}
        benefit_year = {'year1': byear_1.get(), 'year2': byear_2.get(), 'year3': byear_3.get(), 'year4': byear_4.get(),
                        'year5': byear_5.get(), 'year6': byear_6.get(), 'year7': byear_7.get(), 'year8': byear_8.get(),
                        'year9': byear_9.get(), 'year10': byear_10.get()}
        benefit_value = {'year1': benefit_1.get(), 'year2': benefit_2.get(), 'year3': benefit_3.get(),
                         'year4': benefit_4.get(), 'year5': benefit_5.get(), 'year6': benefit_6.get(),
                         'year7': benefit_7.get(), 'year8': benefit_8.get(), 'year9': benefit_9.get(),
                         'year10': benefit_10.get()}

        typo = {'type1': "Cost", 'type2': "Benefit"}
        fields_entry = {'Iteration': iteration_ver.get(), 'Project Type': tkvar_pt.get(), 'Project Title': prog_title.get(),
                        'Project Description': prog_desc.get(), 'Business Unit': tkvar_bu.get(),
                        'Program Name': tkvar_pn.get(), 'Status': tkvar_s.get(), 'Request Id': req_id.get(),
                        'Portfolio_Alignment': pfm_align.get(), 'Customer': cust.get(), 'Notes': usr_notes.get("1.0", END),
                        'Receipt Date': date_receipt.get(), 'Due Date': date_due.get(), 'ERB Date': date_erb.get(),
                        'Manager Review Date': manager_date.get(), 'FinOps Date': finops_date.get(), 'BOE Date': date_boe.get(),
                        'Date Cancelled': date_cnl.get(), 'Primary Estimator': prime_analyst.get(), 'Secondary Estimator': sec_analyst.get(),
                        'Project Manager': project_mgr.get(), 'Requester': requester.get(), 'Technical Focal': tech_analyst.get(),
                        'FinOps Focal': finops_analyst.get(), 'Last Update User': last_update_usr.get(), 'Last Update Date': last_update.get(),
                        'NRE Estimate': nr_cost.get(), 'NPV ($mill)': npv.get(), 'MIRR': modirr.get(),
                        'Payback(discounted)': payback_disc.get(), 'B/C Ratio': bc_rat.get(), 'Benefit Type': ben_type.get(),
                        'Benefit Owner': ben_owner.get(), 'Date Completed': date_completed.get()}
        counter = 0
        empty_fields = []
        for key, value in fields_entry.items():
            if not value:
                counter += 1
                empty_fields.append(key)

        backend.insert_ELF(benefit_year, benefit_value, typo, cost_year, cost_value, iteration.get(), tkvar_pt.get(),
                           proj_title.get(), proj_description.get(), tkvar_bu.get(), tkvar_pn.get(), tkvar_s.get(),
                           port_align.get(), customer.get(), request_id.get(), usr_notes.get("1.0", END),
                           last_update_date.get(), last_update_user.get(), receipt_date.get(), due_date.get(),
                           erb_date.get(), mgr_review.get(), fin_ops_date.get(), boe_date.get(), date_cancelled.get(),
                           primary_est.get(), secondary_est.get(), proj_mgr.get(), requester.get(), tech_focal.get(),
                           finops_focal.get(), nr_estimate.get(), npv_mill.get(), mirr.get(), pay_backdis.get(),
                           bc_ratio.get(), benefit_type.get(), benefit_owner.get(), date_comp.get())

        tk.messagebox.showinfo(title='Excellent!',
                               message='Entry was a success!\nYou left {} field(s) empty.\n{}'.format(counter,
                                                                                                      empty_fields))
    except Exception as e:
        tk.messagebox.showerror(title='Oooooops!', message="Ooops, something went wrong: {}.".format(str(e)))


def update_command():
     try:
        # entry window for year (not used)
        year_c = {'year1': yr_1_cost.get(), 'year2': yr_2_cost.get(), 'year3': yr_3_cost.get(), 'year4': yr_4_cost.get(), 'year5': yr_5_cost.get(),
                  'year6': yr_6_cost.get(), 'year7': yr_7_cost.get(), 'year8': yr_8_cost.get(), 'year9': yr_9_cost.get(), 'year10': yr_10_cost.get()}
        # entry window for cost in the actual year (not used)
        cost_c = {'year1': cost_yr_1.get(), 'year2': cost_yr_2.get(), 'year3': cost_yr_3.get(), 'year4': cost_yr_4.get(), 'year5': cost_yr_5.get(),
                  'year6': cost_year_6.get(), 'year7': cost_year_7.get(), 'year8': cost_year_8.get(), 'year9': cost_yr_9.get(), 'year10': cost_yr_10.get()}
        # entry window for year of the benefit (not used)
        year_b = {'year1': yr_1_ben.get(), 'year2': yr_2_ben.get(), 'year3': yr_3_ben.get(), 'year4': yr_4_ben.get(),
                  'year5': yr_5_ben.get(), 'year6': yr_6_ben.get(), 'year7': yr_7_ben.get(), 'year8': yr_8_ben.get(),
                  'year9': yr_9_ben.get(), 'year10': yr10_ben.get()}
        #entry window for benefit in the actual year (not used)
        value_b = {'year1': ben_yr_1.get(), 'year2': ben_yr_2.get(), 'year3': ben_yr_3.get(), 'year4': ben_yr_4.get(), 'year5': ben_yr_5.get(),
                   'year6': ben_yr_6.get(), 'year7': ben_yr_7.get(), 'year8': ben_yr_8.get(), 'year9': ben_yr_9.get(), 'year10': ben_yr_10.get()}
        # datatype.get() for date year
        cost_year = {'year1': year_1.get(), 'year2': year_2.get(), 'year3': year_3.get(), 'year4': year_4.get(),
                     'year5': year_5.get(), 'year6': year_6.get(), 'year7': year_7.get(), 'year8': year_8.get(),
                     'year9': year_9.get(), 'year10': year_10.get()}
        #datatype.get() for $value in year
        cost_value = {'cost1': cost_1.get(), 'cost2': cost_2.get(), 'cost3': cost_3.get(), 'cost4': cost_4.get(),
                      'cost5': cost_5.get(), 'cost6': cost_6.get(), 'cost7': cost_7.get(), 'cost8': cost_8.get(),
                      'cost9': cost_9.get(), 'cost10': cost_10.get()}
        # datatype.get() benefit year
        benefit_year = {'year1': byear_1.get(), 'year2': byear_2.get(), 'year3': byear_3.get(), 'year4': byear_4.get(),
                        'year5': byear_5.get(), 'year6': byear_6.get(), 'year7': byear_7.get(), 'year8': byear_8.get(),
                        'year9': byear_9.get(), 'year10': byear_10.get()}
        #datatype.get benefit $value in year
        benefit_value = {'bene1': benefit_1.get(), 'bene2': benefit_2.get(), 'bene3': benefit_3.get(),
                         'bene4': benefit_4.get(), 'bene5': benefit_5.get(), 'bene6': benefit_6.get(),
                         'bene7': benefit_7.get(), 'bene8': benefit_8.get(), 'bene9': benefit_9.get(),
                         'bene10': benefit_10.get()}
        ## typo: cost or benefit type
        typo = {'type1': "Cost", 'type2': "Benefit"}
        # fields_entry: dictionary used to determine empty fields during update
        fields_entry = {'Iteration': iteration_ver.get(), 'Project Type': tkvar_pt.get(), 'Project Title': prog_title.get(),
                        'Project Description': prog_desc.get(), 'Business Unit': tkvar_bu.get(),
                        'Program Name': tkvar_pn.get(), 'Status': tkvar_s.get(), 'Request Id': req_id.get(),
                        'Portfolio_Alignment': pfm_align.get(), 'Customer': cust.get(), 'Notes': usr_notes.get("1.0", END),
                        'Receipt Date': date_receipt.get(), 'Due Date': date_due.get(), 'ERB Date': date_erb.get(),
                        'Manager Review Date': manager_date.get(), 'FinOps Date': finops_date.get(), 'BOE Date': date_boe.get(),
                        'Date Cancelled': date_cnl.get(), 'Primary Estimator': prime_analyst.get(), 'Secondary Estimator': sec_analyst.get(),
                        'Project Manager': project_mgr.get(), 'Requester': requester.get(), 'Technical Focal': tech_analyst.get(),
                        'FinOps Focal': finops_analyst.get(), 'Last Update User': last_update_usr.get(), 'Last Update Date': last_update.get(),
                        'NRE Estimate': nr_cost.get(), 'NPV ($mill)': npv.get(), 'MIRR': modirr.get(),
                        'Payback(discounted)': payback_disc.get(), 'B/C Ratio': bc_rat.get(), 'Benefit Type': ben_type.get(),
                        'Benefit Owner': ben_owner.get(), 'Date Completed': date_completed.get()}

        #count empty fields
        counter = 0
        empty_fields = []
        for key, value in fields_entry.items():
            if not value:
                counter += 1
                empty_fields.append(key)
        # pass data to backend sql table
        backend.update_ELF(primary_key_pk0, cost_year, cost_value, benefit_year, benefit_value,
                           typo, iteration.get(), tkvar_pt.get(), proj_title.get(), proj_description.get(),
                           tkvar_bu.get(), tkvar_pn.get(), tkvar_s.get(), port_align.get(), customer.get(),
                           request_id.get(), usr_notes.get("1.0", END), last_update_date.get(), last_update_user.get(),
                           receipt_date.get(), due_date.get(), erb_date.get(), mgr_review.get(), fin_ops_date.get(),
                           boe_date.get(), date_cancelled.get(), primary_est.get(), secondary_est.get(), proj_mgr.get(),
                           requester.get(), tech_focal.get(), finops_focal.get(), nr_estimate.get(), npv_mill.get(),
                           mirr.get(), pay_backdis.get(), bc_ratio.get(), benefit_type.get(), benefit_owner.get(),
                           date_comp.get())
        # if success, display count and name of empty fields
        tk.messagebox.showinfo(title='Excellent!',
                               message='Update was a success!\nYou left {} field(s) empty.\n{}'.format(counter,
                                                                                                       empty_fields))
     except Exception as e:
         print(str(e))
         tk.messagebox.showerror(title='Oooooops!', message="Ooops, something went wrong: {}.".format(str(e)))

#delete from .db
def delete_command():
    try:
        user_inp = simpledialog.askstring(title="Delete", prompt="Password: ")
        if user_inp != 'test':
            user_inp = simpledialog.askstring(title="Delete", prompt="Password: ")
        else:
            USER_INP_KEY = simpledialog.askinteger(title="Delete", prompt="What is the Primary Key:  ")
            backend.delete(USER_INP_KEY)
    except BaseException as e:
        print(str(e))
        tk.messagebox.showerror(title='Oooooops!', message='Could not delete your record(s): \n{}!'.format(str(e)))


# window widgets
lbl_id_pk = Label(window, text="pk", width=21, anchor=W)
lbl_id_pk.grid(row=0, column=0)
id_0 = IntVar()
id_pk = Label(window, textvariable=id_0, width=5, anchor=CENTER)
id_pk.grid(row=0, column=1)

lbl_iteration_ver = Label(window, text="Iteration*", width=21, anchor=W)
lbl_iteration_ver.grid(row=1, column=0)
iteration = IntVar()
iteration_ver = Entry(window, textvariable=iteration, width=5)
iteration_ver.grid(row=1, column=1)

prj_type = Label(window, text="Project Type", width=21, anchor=W)
prj_type.grid(row=2, column=0)
tkvar_pt = StringVar(window)
choices = {'Business Case', 'Consultation'}
popupMenu = OptionMenu(window, tkvar_pt, *choices)
popupMenu.grid(row=2, column=1)

lbl_prog_title = Label(window, text="Program Title", width=21, anchor=W)
lbl_prog_title.grid(row=3, column=0)
proj_title = StringVar()
prog_title = Entry(window, textvariable=proj_title)
prog_title.grid(row=3, column=1)

lbl_prog_desc = Label(window, text="Program Description", width=21, anchor=W)
lbl_prog_desc.grid(row=4, column=0)
proj_description = StringVar()
prog_desc = Entry(window, textvariable=proj_description)
prog_desc.grid(row=4, column=1)

lbl_bu = Label(window, text="Business Unit", width=21, anchor=W)
lbl_bu.grid(row=5, column=0)
tkvar_bu = StringVar(window)
choices = {'Choice 1', 'Choice 2', 'Choice 3', 'Choice 4'}
popupMenu = OptionMenu(window, tkvar_bu, *choices)
popupMenu.grid(row=5, column=1)

lbl_prog_name = Label(window, text="Program Name", width=21, anchor=W)
lbl_prog_name.grid(row=6, column=0)
tkvar_pn = StringVar(window)
choices = {'Label 1', 'Label 2', 'Label 3', 'Label 4'}
popupMenu = OptionMenu(window, tkvar_pn, *choices)
popupMenu.grid(row=6, column=1)

lbl_stat = Label(window, text="Status*", width=21, anchor=W)
lbl_stat.grid(row=7, column=0)
status = StringVar()
tkvar_s = StringVar(window)
choices = {'Active', 'Complete', 'Cancelled'}
popupMenu = OptionMenu(window, tkvar_s, *choices)
popupMenu.grid(row=7, column=1)

lbl_req_id = Label(window, text="Request#*", width=21, anchor=W)
lbl_req_id.grid(row=8, column=0)
request_id = StringVar()
req_id = Entry(window, textvariable=request_id)
req_id.grid(row=8, column=1)

lbl_pfm_align = Label(window, text="Portfolio Alignment", width=21, anchor=W)
lbl_pfm_align.grid(row=9, column=0)
port_align = StringVar()
pfm_align = Entry(window, textvariable=port_align)
pfm_align.grid(row=9, column=1)

lbl_cust = Label(window, text="Customer", width=21, anchor=W)
lbl_cust.grid(row=10, column=0)
customer = StringVar()
cust = Entry(window, textvariable=customer)
cust.grid(row=10, column=1)

lbl_date_receipt = Label(window, text="Receipt Date", width=21, anchor=W)
lbl_date_receipt.grid(row=11, column=0)
receipt_date = StringVar()
date_receipt = Entry(window, textvariable=receipt_date)
date_receipt.insert(INSERT, 'yyyy-dd-mm')
date_receipt.grid(row=11, column=1)

lbl_date_due = Label(window, text="Due Date", width=21, anchor=W)
lbl_date_due.grid(row=12, column=0)
due_date = StringVar()
date_due = Entry(window, textvariable=due_date)
date_due.insert(INSERT, 'yyyy-dd-mm')
date_due.grid(row=12, column=1)

lbl_date_erb = Label(window, text="ERB Date", width=21, anchor=W)
lbl_date_erb.grid(row=13, column=0)
erb_date = StringVar()
date_erb = Entry(window, textvariable=erb_date)
date_erb.insert(INSERT, 'yyyy-dd-mm')
date_erb.grid(row=13, column=1)

lbl_manager_date = Label(window, text="Review Date", width=21, anchor=W)
lbl_manager_date.grid(row=14, column=0)
mgr_review = StringVar()
manager_date = Entry(window, textvariable=mgr_review)
manager_date.insert(INSERT, 'yyyy-dd-mm')
manager_date.grid(row=14, column=1)

lbl_project_mgr = Label(window, text="Project Manager", width=21, anchor=W)
lbl_project_mgr.grid(row=0, column=2)
proj_mgr = StringVar()
project_mgr = Entry(window, textvariable=proj_mgr)
project_mgr.grid(row=0, column=3)

lbl_requester = Label(window, text="Requester", width=21, anchor=W)
lbl_requester.grid(row=1, column=2)
request = StringVar()
requester = Entry(window, textvariable=request)
requester.grid(row=1, column=3)

lbl_tech_analyst = Label(window, text="Technical Analyst", width=21, anchor=W)
lbl_tech_analyst.grid(row=2, column=2)
tech_focal = StringVar()
tech_analyst = Entry(window, textvariable=tech_focal)
tech_analyst.grid(row=2, column=3)

lbl_finops_analyst = Label(window, text="Finance Analyst", width=21, anchor=W)
lbl_finops_analyst.grid(row=3, column=2)
finops_focal = StringVar()
finops_analyst = Entry(window, textvariable=finops_focal)
finops_analyst.grid(row=3, column=3)

lbl_last_update_usr = Label(window, text="Last Update User", width=21, anchor=W)
lbl_last_update_usr.grid(row=4, column=2)
last_update_user = StringVar()
last_update_usr = Entry(window, textvariable=last_update_user)
username = getpass.getuser()
last_update_usr.insert(INSERT, username)
last_update_usr.configure(state='disable')
last_update_usr.grid(row=4, column=3)

lbl_last_update = Label(window, text="Last Update Date", width=21, anchor=W)
lbl_last_update.grid(row=5, column=2)
last_update_date = StringVar()
last_update = Entry(window, textvariable=last_update_date)
today = date.today()
last_update.insert(INSERT, today)
last_update.configure(state='disabled')
last_update.grid(row=5, column=3)

lbl_nr_cost = Label(window, text="Cost Estimate($M)", width=21, anchor=W)
lbl_nr_cost.grid(row=6, column=2)
nr_estimate = DoubleVar()
nr_cost = Entry(window, textvariable=nr_estimate)
nr_cost.grid(row=6, column=3)

lbl_npv = Label(window, text="NPV($M)", width=21, anchor=W)
lbl_npv.grid(row=7, column=2)
npv_mill = DoubleVar()
npv = Entry(window, textvariable=npv_mill)
npv.grid(row=7, column=3)

lbl_modirr = Label(window, text="MIRR", width=21, anchor=W)
lbl_modirr.grid(row=8, column=2)
mirr = DoubleVar()
modirr = Entry(window, textvariable=mirr)
modirr.grid(row=8, column=3)

lbl_payback_disc = Label(window, text="Payback Period", width=21, anchor=W)
lbl_payback_disc.grid(row=9, column=2)
pay_backdis = DoubleVar()
payback_disc = Entry(window, textvariable=pay_backdis)
payback_disc.grid(row=9, column=3)

lbl_bc_rat = Label(window, text="B/C Ratio", width=21, anchor=W)
lbl_bc_rat.grid(row=10, column=2)
bc_ratio = DoubleVar()
bc_rat = Entry(window, textvariable=bc_ratio)
bc_rat.grid(row=10, column=3)

lbl_ben_type = Label(window, text="Benefit", width=21, anchor=W)
lbl_ben_type.grid(row=11, column=2)
benefit_type = StringVar()
ben_type = Entry(window, textvariable=benefit_type)
ben_type.grid(row=11, column=3)

lbl_ben_owner = Label(window, text="Benefit Owner", width=21, anchor=W)
lbl_ben_owner.grid(row=12, column=2)
benefit_owner = StringVar()
ben_owner = Entry(window, textvariable=benefit_owner)
ben_owner.grid(row=12, column=3)

lbl_date_completed = Label(window, text="Date Completed", width=21, anchor=W)
lbl_date_completed.grid(row=13, column=2)
date_comp = StringVar()
date_completed = Entry(window, textvariable=date_comp)
date_completed.insert(INSERT, 'yyyy-dd-mm')
date_completed.grid(row=13, column=3)

lbl_free_field = Label(window, text="Free Field", width=21, anchor=W)
lbl_free_field.grid(row=14, column=2)
ty_pe = StringVar()
free_field = Entry(window, textvariable=ty_pe, state='disable')
free_field.grid(row=14, column=3)
# ----------------------------------------------------------------------
lbl_finops_date = Label(window, text="Finance Integration", width=21, anchor=W)
lbl_finops_date.grid(row=0, column=4)
fin_ops_date = StringVar()
finops_date = Entry(window, textvariable=fin_ops_date)
finops_date.insert(INSERT, 'yyyy-dd-mm')
finops_date.grid(row=0, column=5)

lbl_date_boe = Label(window, text="BOE Date", width=21, anchor=W)
lbl_date_boe.grid(row=1, column=4)
boe_date = StringVar()
date_boe = Entry(window, textvariable=boe_date)
date_boe.insert(INSERT, 'yyyy-dd-mm')
date_boe.grid(row=1, column=5)

lbl_date_cnl = Label(window, text="Date Cancelled", width=21, anchor=W)
lbl_date_cnl.grid(row=2, column=4)
date_cancelled = StringVar()
date_cnl = Entry(window, textvariable=date_cancelled)
date_cnl.insert(INSERT, 'yyyy-dd-mm')
date_cnl.grid(row=2, column=5)

lbl_prime_analyst = Label(window, text="Primary Analyst*", width=21, anchor=W)
lbl_prime_analyst.grid(row=3, column=4)
primary_est = StringVar()
prime_analyst = Entry(window, textvariable=primary_est)
prime_analyst.grid(row=3, column=5)

lbl_sec_analyst = Label(window, text="Secondary Analyst", width=21, anchor=W)
lbl_sec_analyst.grid(row=4, column=4)
secondary_est = StringVar()
sec_analyst = Entry(window, textvariable=secondary_est)
sec_analyst.grid(row=4, column=5)
# -------------------------------------------------------------------------


# Cost Label for year(yr) and $amount(ben) with data type
cost_lbl_yr = Label(window, text="Cost Years", width=21, anchor=CENTER)
cost_lbl_yr.grid(row=21, column=0)

cost_lbl_amt = Label(window, text="Cost ($M)", width=21, anchor=CENTER)
cost_lbl_amt.grid(row=21, column=1)

year_1 = IntVar()
yr_1_cost = Entry(window, textvariable=year_1, width=5)
yr_1_cost.grid(row=22, column=0)
cost_1 = DoubleVar()
cost_yr_1 = Entry(window, textvariable=cost_1, width=10)
cost_yr_1.grid(row=22, column=1)

year_2 = IntVar()
yr_2_cost = Entry(window, textvariable=year_2, width=5)
yr_2_cost.grid(row=23, column=0)
cost_2 = DoubleVar()
cost_yr_2 = Entry(window, textvariable=cost_2, width=10)
cost_yr_2.grid(row=23, column=1)

year_3 = IntVar()
yr_3_cost = Entry(window, textvariable=year_3, width=5)
yr_3_cost.grid(row=24, column=0)
cost_3 = DoubleVar()
cost_yr_3 = Entry(window, textvariable=cost_3, width=10)
cost_yr_3.grid(row=24, column=1)

year_4 = IntVar()
yr_4_cost = Entry(window, textvariable=year_4, width=5)
yr_4_cost.grid(row=25, column=0)
cost_4 = DoubleVar()
cost_yr_4 = Entry(window, textvariable=cost_4, width=10)
cost_yr_4.grid(row=25, column=1)

year_5 = IntVar()
yr_5_cost = Entry(window, textvariable=year_5, width=5)
yr_5_cost.grid(row=26, column=0)
cost_5 = DoubleVar()
cost_yr_5 = Entry(window, textvariable=cost_5, width=10)
cost_yr_5.grid(row=26, column=1)

year_6 = IntVar()
yr_6_cost = Entry(window, textvariable=year_6, width=5)
yr_6_cost.grid(row=27, column=0)
cost_6 = DoubleVar()
cost_year_6 = Entry(window, textvariable=cost_6, width=10)
cost_year_6.grid(row=27, column=1)

year_7 = IntVar()
yr_7_cost = Entry(window, textvariable=year_7, width=5)
yr_7_cost.grid(row=28, column=0)
cost_7 = DoubleVar()
cost_year_7 = Entry(window, textvariable=cost_7, width=10)
cost_year_7.grid(row=28, column=1)

year_8 = IntVar()
yr_8_cost = Entry(window, textvariable=year_8, width=5)
yr_8_cost.grid(row=29, column=0)
cost_8 = DoubleVar()
cost_year_8 = Entry(window, textvariable=cost_8, width=10)
cost_year_8.grid(row=29, column=1)

year_9 = IntVar()
yr_9_cost = Entry(window, textvariable=year_9, width=5)
yr_9_cost.grid(row=30, column=0)
cost_9 = DoubleVar()
cost_yr_9 = Entry(window, textvariable=cost_9, width=10)
cost_yr_9.grid(row=30, column=1)

year_10 = IntVar()
yr_10_cost = Entry(window, textvariable=year_10, width=5)
yr_10_cost.grid(row=31, column=0)
cost_10 = DoubleVar()
cost_yr_10 = Entry(window, textvariable=cost_10, width=10)
cost_yr_10.grid(row=31, column=1)

# Benefit Label for year(yr) and $amount(ben) with data type
benefit_yr_lbl = Label(window, text="Benefit Years", width=21, anchor=CENTER)
benefit_yr_lbl.grid(row=21, column=2)

benefit_lbl = Label(window, text="Benefit($)", width=21, anchor=CENTER)
benefit_lbl.grid(row=21, column=3)

byear_1 = IntVar()
yr_1_ben = Entry(window, textvariable=byear_1, width=5)
yr_1_ben.grid(row=22, column=2)
benefit_1 = DoubleVar()
ben_yr_1 = Entry(window, textvariable=benefit_1, width=10)
ben_yr_1.grid(row=22, column=3)

byear_2 = IntVar()
yr_2_ben = Entry(window, textvariable=byear_2, width=5)
yr_2_ben.grid(row=23, column=2)
benefit_2 = DoubleVar()
ben_yr_2 = Entry(window, textvariable=benefit_2, width=10)
ben_yr_2.grid(row=23, column=3)

byear_3 = IntVar()
yr_3_ben = Entry(window, textvariable=byear_3, width=5)
yr_3_ben.grid(row=24, column=2)
benefit_3 = DoubleVar()
ben_yr_3 = Entry(window, textvariable=benefit_3, width=10)
ben_yr_3.grid(row=24, column=3)

byear_4 = IntVar()
yr_4_ben = Entry(window, textvariable=byear_4, width=5)
yr_4_ben.grid(row=25, column=2)
benefit_4 = DoubleVar()
ben_yr_4 = Entry(window, textvariable=benefit_4, width=10)
ben_yr_4.grid(row=25, column=3)

byear_5 = IntVar()
yr_5_ben = Entry(window, textvariable=byear_5, width=5)
yr_5_ben.grid(row=26, column=2)
benefit_5 = DoubleVar()
ben_yr_5 = Entry(window, textvariable=benefit_5, width=10)
ben_yr_5.grid(row=26, column=3)

byear_6 = IntVar()
yr_6_ben = Entry(window, textvariable=byear_6, width=5)
yr_6_ben.grid(row=27, column=2)
benefit_6 = DoubleVar()
ben_yr_6 = Entry(window, textvariable=benefit_6, width=10)
ben_yr_6.grid(row=27, column=3)

byear_7 = IntVar()
yr_7_ben = Entry(window, textvariable=byear_7, width=5)
yr_7_ben.grid(row=28, column=2)
benefit_7 = DoubleVar()
ben_yr_7 = Entry(window, textvariable=benefit_7, width=10)
ben_yr_7.grid(row=28, column=3)

byear_8 = IntVar()
yr_8_ben = Entry(window, textvariable=byear_8, width=5)
yr_8_ben.grid(row=29, column=2)
benefit_8 = DoubleVar()
ben_yr_8 = Entry(window, textvariable=benefit_8, width=10)
ben_yr_8.grid(row=29, column=3)

byear_9 = IntVar()
yr_9_ben = Entry(window, textvariable=byear_9, width=5)
yr_9_ben.grid(row=30, column=2)
benefit_9 = DoubleVar()
ben_yr_9 = Entry(window, textvariable=benefit_9, width=10)
ben_yr_9.grid(row=30, column=3)

byear_10 = IntVar()
yr10_ben = Entry(window, textvariable=byear_10, width=5)
yr10_ben.grid(row=31, column=2)
benefit_10 = DoubleVar()
ben_yr_10 = Entry(window, textvariable=benefit_10, width=10)
ben_yr_10.grid(row=31, column=3)
# ----------------------Textbox for notes----------------------
today = date.today()
small_font = ('Verdana', 8)
usr_notes = StringVar()
usr_notes = Text(window, height=23, font=small_font, width=30, wrap=WORD)
usr_notes.grid(row=5, column=4, columnspan=2, rowspan=20)
username = getpass.getuser()
usr_notes.insert(INSERT, 'Notes ({} on {}):'.format(username, today))
usr_notes.get('1.0', END)

# Label for buttons
lbl_actions = Label(window, text="Actions", width=21, anchor=CENTER)
lbl_actions.grid(row=25, column=4, columnspan=2)

# Buttons for action items
btn_mass_update = Button(window, text=".xlsx to .db", width=12, command=update_enmasse)
btn_mass_update.grid(row=27, column=4)

btn_new_entry = Button(window, text="New Entry", width=12, command=new_entry)
btn_new_entry.grid(row=28, column=4)

btn_delete_record = Button(window, text="Delete Record", width=12, command=delete_command)
btn_delete_record.grid(row=28, column=5)
# , state='disable'

btn_update = Button(window, text="Update Record", width=12, command=update_command)
btn_update.grid(row=29, column=4)

btn_view_all = Button(window, text="View All", width=12, command=view_all)
btn_view_all.grid(row=29, column=5)

btn_db_xlsx = Button(window, text=".db to .xlsx", width=12, command=export_to_excel)
btn_db_xlsx.grid(row=30, column=4)

btn_clear = Button(window, text="Clear", width=12, command=clear)
btn_clear.grid(row=30, column=5)

btn_find = Button(window, text="Find*", width=12, command=find_command)
btn_find.grid(row=31, column=4)

btn_close = Button(window, text="Close", width=12, command=window.destroy)
btn_close.grid(row=31, column=5)

btn_help = Button(window, text='Help', width=12, command=help_command)
btn_help.grid(row=27, column=5)

window.mainloop()
