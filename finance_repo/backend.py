# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:25:12 2020

@author: ruslan polyak
"""

import sqlite3
import tkinter as tk
import pandas as pd

#need this for the textbox/NOTES

def view():
    conn=sqlite3.connect('ELF_db.db')
    cur=conn.cursor()
    cur.execute("SELECT ELF_data.pk_data, ELF0.pk0, ELF_data.Iteration, ELF0.[Project/Program Type], ELF0.[Project/Program Title], \
                ELF0.[Project/Program Description], ELF0.[Business Unit], ELF0.[Program Name], ELF0.Status, \
                ELF0.[Portfolio Alignment], ELF0.Customer, ELF_data.RequestID, ELF0.Notes, ELF0.[Last Update Date], \
                ELF0.[Last Update User], ELF0.[Receipt/Request Date], ELF0.[Due Date], ELF0.[ERB Review Date], \
                ELF0.[Manager Review Date], ELF0.[Integration FinOps Completed], ELF0.[BOE Date], \
                ELF0.[Date Cancelled or Lost], ELF0.[Primary Estimator], ELF0.[Secondary Estimator (Support)], \
                ELF0.[Project Manager], ELF0.Requestor, ELF0.[Technical Focal], ELF0.[FinOps Focal], \
                ELF0.[NR Cost Estimate ($ in Mil.)], ELF0.[NPV ($ in Mil.)], ELF0.[MIRR], ELF0.[Payback (Discounted)], \
                ELF0.[BC Ratio], ELF0.[Benefit Type], ELF0.[Benefit Owner], ELF0.[Date Completed], \
                ELF_data.Year, ELF_data.Type, ELF_data.Value \
                FROM ELF_data, ELF0 WHERE ELF_data.pk0=ELF0.pk0")
    #Iteration, [Project/Program Type],[Project/Program Title],[Business Unit],[Program Name],Status,[Request ID],[Due Date],[Primary Estimator],Notes  FROM ELF1 GROUP BY Iteration, [Project/Program Type],[Project/Program Title],[Business Unit],[Program Name],Status,[Request ID],[Due Date],[Primary Estimator], Notes 
    rows = cur.fetchall()
    conn.close()
    return rows

def search(iteration=None, request_id=None, prime_estimator=None, status=None):
    conn=sqlite3.connect("ELF_db.db")
    cur=conn.cursor()
    cur.execute("SELECT Iteration, [RequestID], [Primary Estimator],Status\
                FROM ELF0 \
                WHERE Iteration=? AND [RequestID]=? AND [Primary Estimator]=? AND Status=?", (iteration,request_id,prime_estimator,status))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(pk):
    conn=sqlite3.connect("ELF_db.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM ELF0 WHERE ELF0.pk0=?",(pk,))
    tk.messagebox.showinfo(title='Excellent!', message='You updated {} row(s)'.format(cur.rowcount))
    conn.commit()
    conn.close()

def update_ELF(primary_key_pk0, primary_key_pk_data,cost_year,cost_value,benefit_year,benefit_value, typo, iteration="", project_program_type="", project_program_title="", project_program_description="",
                business_unit="", program_name="", status="", portfolio_alignment="", customer="", request_id="", 
                notes="", last_update_date="", last_update_user="", receipt_request_date="", due_date="", 
                erb_review_date="", manager_review_date="", int_finops_date="", boe_date="", date_cancelled="", 
                primary_estimator="", secondary_estimator="", project_manager="", requestor="", technical_focal="", 
                finops_focal="", nr_cost_estimate="", npv="", mirr="", payback_discounted="", b_c_ratio="", 
                benefit_type="", benefit_owner="", date_completed=""):
    conn=sqlite3.connect("ELF_db.db")
    cur=conn.cursor()
    #min and max values for foreign keys
    cur.execute("SELECT MIN(pk_data) FROM ELF_data WHERE pk0 = ? and Type = 'Cost' ORDER BY pk_data ASC", [str(primary_key_pk0)])
    min_pk_cost = cur.fetchone()[0]
    cur.execute("SELECT MAX(pk_data) FROM ELF_data WHERE pk0 = ? and Type = 'Cost' ORDER BY pk_data ASC", [str(primary_key_pk0)])
    max_pk_cost = cur.fetchone()[0]
    cur.execute("SELECT MIN(pk_data) FROM ELF_data WHERE pk0 = ? and Type = 'Benefit' ORDER BY pk_data ASC", [str(primary_key_pk0)])
    min_pk_bene = cur.fetchone()[0]
    cur.execute("SELECT MAX(pk_data) FROM ELF_data WHERE pk0 = ? and Type = 'Benefit' ORDER BY pk_data ASC", [str(primary_key_pk0)])
    max_pk_bene = cur.fetchone()[0]
    
    cur.execute("UPDATE ELF0 SET Iteration=?, Customer=?, [Project/Program Type]=?, [Project/Program Title]=?,\
                [Project/Program Description]=?, [Business Unit]=?, [Program Name]=?, Status=?, \
                [Portfolio Alignment]=?, Customer=?, [RequestID]=?, Notes=?, [Last Update Date]=?,\
                [Last Update User]=?, [Receipt/Request Date]=?, [Due Date]=?, [ERB Review Date]=?, \
                [Manager Review Date]=?, [Integration FinOps Completed]=?, [BOE Date]=?, \
                [Date Cancelled or Lost]=?, [Primary Estimator]=?, [Secondary Estimator (Support)]=?,\
                [Project Manager]=?, Requestor=?, [Technical Focal]=?, [FinOps Focal]=?,\
                [NR Cost Estimate ($ in Mil.)]=?, [NPV ($ in Mil.)]=?, MIRR=?, [Payback (Discounted)]=?, \
                [BC Ratio]=?, [Benefit Type]=?,[Benefit Owner]=?, [Date Completed]=? WHERE pk0=?",
                (iteration, customer, project_program_type, project_program_title, project_program_description, 
                business_unit, program_name, status, portfolio_alignment, customer, request_id, notes, last_update_date, 
                last_update_user, receipt_request_date, due_date, erb_review_date, manager_review_date, int_finops_date, 
                boe_date, date_cancelled, primary_estimator, secondary_estimator, project_manager, requestor, 
                technical_focal, finops_focal, nr_cost_estimate, npv, mirr, payback_discounted, b_c_ratio,
                benefit_type, benefit_owner, date_completed, str(primary_key_pk0)))

    cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                       (iteration, request_id, cost_year['year1'], cost_value['cost1'], typo.get('type1'),str(min_pk_cost)))
    cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                       (iteration, request_id, benefit_year['year1'], benefit_value['bene1'], typo.get('type2'),str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, cost_year['year2'], cost_value['cost2'], typo.get('type1'),str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, benefit_year['year2'], benefit_value['bene2'], typo.get('type2'),str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, cost_year['year3'], cost_value['cost3'], typo.get('type1'),str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, benefit_year['year3'], benefit_value['bene3'], typo.get('type2'),str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, cost_year['year4'], cost_value['cost4'], typo.get('type1'),str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, benefit_year['year4'], benefit_value['bene4'], typo.get('type2'),str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, cost_year['year5'], cost_value['cost5'], typo.get('type1'),str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, benefit_year['year5'], benefit_value['bene5'], typo.get('type2'),str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, cost_year['year6'], cost_value['cost6'], typo.get('type1'),str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, benefit_year['year6'], benefit_value['bene6'], typo.get('type2'),str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, cost_year['year7'], cost_value['cost7'], typo.get('type1'),str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, benefit_year['year7'], benefit_value['bene7'], typo.get('type2'),str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, cost_year['year8'], cost_value['cost8'], typo.get('type1'),str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, benefit_year['year8'], benefit_value['bene8'], typo.get('type2'),str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, cost_year['year9'], cost_value['cost9'], typo.get('type1'),str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, benefit_year['year9'], benefit_value['bene9'], typo.get('type2'),str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, cost_year['year10'], cost_value['cost10'], typo.get('type1'),str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                           (iteration, request_id, benefit_year['year10'], benefit_value['bene10'], typo.get('type2'),str(min_pk_bene)))
    conn.commit()
    tk.messagebox.showinfo(title='Excellent!', message='You updated {} row(s)'.format(cur.rowcount))
    cur.close()
    conn.close()
#------------------------INSERT--------------------------------------     
def insert_ELF(benefit_year,benefit_value,typo,cost_year,cost_value,iteration="", project_program_type="", project_program_title="", project_program_description="",
                business_unit="", program_name="", status="", portfolio_alignment="", customer="", request_id="", 
                notes="", last_update_date="", last_update_user="", receipt_request_date="", due_date="", 
                erb_review_date="", manager_review_date="", int_finops_date="", boe_date="", date_cancelled="", 
                primary_estimator="", secondary_estimator="", project_manager="", requestor="", technical_focal="", 
                finops_focal="", nr_cost_estimate="", npv="", mirr="", payback_discounted="", b_c_ratio="", 
                benefit_type="", benefit_owner="", date_completed=""):
    try:
        conn=sqlite3.connect('ELF_db.db')
        cur=conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")

        cur.execute("INSERT INTO ELF0 VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
               (iteration, project_program_type, project_program_title, project_program_description, business_unit,
                program_name, status, portfolio_alignment, customer, request_id, notes, last_update_date,
                last_update_user, receipt_request_date, due_date, erb_review_date, manager_review_date,
                int_finops_date, boe_date, date_cancelled, primary_estimator, secondary_estimator,
                project_manager, requestor, technical_focal, finops_focal, nr_cost_estimate, npv,
                mirr, payback_discounted, b_c_ratio, benefit_type, benefit_owner, date_completed))

        fk_pk0=cur.lastrowid
        for key_value,key2_value in zip(cost_year.values(), cost_value.values()):
            if key_value != 0 and key2_value != 0:
                cur.execute("INSERT INTO ELF_data VALUES (NULL,?,?,?,?,?,?)",
                            (fk_pk0,iteration, request_id, str(key_value), str(key2_value), typo.get('type1')))
            else:
                continue

        for key_value,key2_value in zip(benefit_year.values(), benefit_value.values()):
            if key_value != 0 and key2_value != 0:
                cur.execute("INSERT INTO ELF_data VALUES (NULL,?,?,?,?,?,?)",
                            (fk_pk0,iteration, request_id, str(key_value), str(key2_value), typo.get('type2')))
            else:
                continue

        conn.commit()
        tk.messagebox.showinfo(title='Excellent!', message='Total of {} record(s) were added succesfully!'.format(cur.rowcount))
        cur.close()
        conn.close()
    except Exception as e:
        print(str(e))
