# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:25:12 2020

@author: Pepper
"""

import sqlite3
import tkinter as tk

def view():
    conn = sqlite3.connect('ELF_db.db')
    cur = conn.cursor()
    cur.execute("SELECT ELF_data.pk_data, ELF0.pk0, ELF_data.Iteration, ELF0.[Program Type], ELF0.[Program Title], \
                ELF0.[Program Description], ELF0.[Business Unit], ELF0.[Program Name], ELF0.Status, \
                ELF0.[Portfolio Alignment], ELF0.Customer, ELF_data.RequestID, ELF0.Notes, ELF0.[Last Update Date], \
                ELF0.[Last Update User], ELF0.[Request Date], ELF0.[Due Date], ELF0.[Review Date], \
                ELF0.[Manager Review Date], ELF0.[Finance Integration], ELF0.[BOE Date], \
                ELF0.[Date Cancelled], ELF0.[Primary Analyst], ELF0.[Secondary Analyst], \
                ELF0.[Project Manager], ELF0.Requester, ELF0.[Technical Focal], ELF0.[Finance Analyst], \
                ELF0.[Cost($M)], ELF0.[NPV($M)], ELF0.[MIRR], ELF0.[Payback], \
                ELF0.[B/C Ratio], ELF0.[Benefit Type], ELF0.[Benefit Owner], ELF0.[Date Completed], \
                ELF_data.Year, ELF_data.Type, ELF_data.Value \
                FROM ELF_data, ELF0 WHERE ELF_data.pk0=ELF0.pk0")
    rows = cur.fetchall()
    conn.close()
    return rows


def update_enmasse(data):
    try:
        # sets avoid duplicates
        primary_key = set()
        secondary_key = set()

        # populate keys ELF0 and ELF_data using sets to avoid duplicates
        for i in data.pk0:
            primary_key.add(i)
        for i in data.pk_data:
            secondary_key.add(i)
        tk.messagebox.showinfo("Update En Masse", "You're updating {} record(s).".format(len(primary_key) if len(primary_key) > len(secondary_key) else len(secondary_key)))
        # while loop for updates
        conn = sqlite3.connect('ELF_db.db')
        cur = conn.cursor()
        pk0_init = 0
        while pk0_init < len(primary_key):
            # update to ELF0
            cur.execute("UPDATE ELF0 SET Iteration=?, [Program Type]=?, [Program Title]=?,\
                        [Program Description]=?, [Business Unit]=?, [Program Name]=?, Status=?, \
                        [Portfolio Alignment]=?, Customer=?, [RequestID]=?, Notes=?,\
                        [Request Date]=?, [Due Date]=?, [Review Date]=?, \
                        [Manager Review Date]=?, [Finance Integration]=?, [BOE Date]=?, \
                        [Date Cancelled]=?, [Primary Analyst]=?, [Secondary Analyst]=?,\
                        [Project Manager]=?, Requester=?, [Technical Focal]=?, [Finance Analyst]=?,\
                        [Cost($M)]=?, [NPV($M)]=?, MIRR=?, [Payback]=?, \
                        [B/C Ratio]=?, [Benefit Type]=?,[Benefit Owner]=?, [Date Completed]=? WHERE pk0=?",
                        (str(data.iat[pk0_init, 2]), str(data.iat[pk0_init, 3]), str(data.iat[pk0_init, 4]), str(data.iat[pk0_init, 5]), str(data.iat[pk0_init, 6]),
                         str(data.iat[pk0_init, 7]), str(data.iat[pk0_init, 8]), str(data.iat[pk0_init, 9]), str(data.iat[pk0_init, 10]), str(data.iat[pk0_init, 11]), str(data.iat[pk0_init, 12]), str(data.iat[pk0_init, 13]),
                         str(data.iat[pk0_init, 16]), str(data.iat[pk0_init, 17]), str(data.iat[pk0_init, 18]), str(data.iat[pk0_init, 19]), str(data.iat[pk0_init, 20]),
                         str(data.iat[pk0_init, 21]), str(data.iat[pk0_init, 22]), str(data.iat[pk0_init, 23]), str(data.iat[pk0_init, 24]), str(data.iat[pk0_init, 25]), str(data.iat[pk0_init, 26]), str(data.iat[pk0_init, 27]),
                         str(data.iat[pk0_init, 28]), str(data.iat[pk0_init, 29]), str(data.iat[pk0_init, 30]), str(data.iat[pk0_init, 31]), str(data.iat[pk0_init, 32]), str(data.iat[pk0_init, 33]), str(data.iat[pk0_init, 34]),
                         str(data.iat[pk0_init, 35]), str(data.iat[pk0_init, 1])))
            pk0_init += 1
            # #update to ELF_data
            pk_data_init = 0
        while pk_data_init < len(secondary_key):
            cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                        (str(data.iat[pk_data_init, 38]), str(data.iat[pk_data_init, 39]), str(data.iat[pk_data_init, 40]), str(data.iat[pk_data_init, 41]), str(data.iat[pk_data_init, 42]),
                         str(data.iat[pk_data_init, 36])))
            pk_data_init += 1
        conn.commit()
        conn.close()
        tk.messagebox.showinfo("Success!, Update was a success!")
    except Exception as e:
        tk.messagebox.showerror(title='Ooops', message='Something went wrong {}'.format(e))


def search(iteration=None, request_id=None, prime_estimator=None, status=None):
    conn = sqlite3.connect("ELF_db.db")
    cur = conn.cursor()
    cur.execute("SELECT Iteration, [RequestID], [Primary Estimator],Status\
                FROM ELF0 \
                WHERE Iteration=? AND [RequestID]=? AND [Primary Estimator]=? AND Status=?",
                (iteration, request_id, prime_estimator, status))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(pk):
    conn = sqlite3.connect("ELF_db.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM ELF0 WHERE ELF0.pk0=?", (pk,))
    tk.messagebox.showinfo(title='Excellent!', message='You updated {} row(s)'.format(cur.rowcount))
    conn.commit()
    conn.close()


def update_ELF(primary_key_pk0, cost_year, cost_value, benefit_year, benefit_value, typo,
               iteration="", program_type="", proj_title="", proj_description="",
               business_unit="", program_name="", status="", portfolio_alignment="", customer="", request_id="",
               usr_notes="", last_update_date="", last_update_user="", receipt_date="", due_date="",
               erb_date="", manager_review_date="", finops_date="", boe_date="", date_cancelled="",
               primary_est="", secondary_est="", project_manager="", requester="", tech_focal="",
               finops_focal="", nr_estimate="", npv="", mirr="", pay_backdis="", b_c_ratio="",
               benefit_type="", benefit_owner="", date_completed=""):
    conn = sqlite3.connect("ELF_db.db")
    cur = conn.cursor()
    # min and max values for foreign keys
    cur.execute("SELECT MIN(pk_data) FROM ELF_data WHERE pk0 = ? and Type = 'Cost' ORDER BY pk_data ASC",
                [str(primary_key_pk0)])
    min_pk_cost = cur.fetchone()[0]
    cur.execute("SELECT MAX(pk_data) FROM ELF_data WHERE pk0 = ? and Type = 'Cost' ORDER BY pk_data ASC",
                [str(primary_key_pk0)])
    max_pk_cost = cur.fetchone()[0]
    cur.execute("SELECT MIN(pk_data) FROM ELF_data WHERE pk0 = ? and Type = 'Benefit' ORDER BY pk_data ASC",
                [str(primary_key_pk0)])
    min_pk_bene = cur.fetchone()[0]
    cur.execute("SELECT MAX(pk_data) FROM ELF_data WHERE pk0 = ? and Type = 'Benefit' ORDER BY pk_data ASC",
                [str(primary_key_pk0)])
    max_pk_bene = cur.fetchone()[0]

    cur.execute("UPDATE ELF0 SET Iteration=?, [Program Type]=?, [Program Title]=?,\
                        [Program Description]=?, [Business Unit]=?, [Program Name]=?, Status=?, \
                        [Portfolio Alignment]=?, Customer=?, [RequestID]=?, Notes=?, \
                        [Last Update Date]=?, [Last Update User]=?, [Request Date]=?, \
                        [Due Date]=?, [Review Date]=?, [Manager Review Date]=?, \
                        [Finance Integration]=?, [BOE Date]=?, \
                        [Date Cancelled]=?, [Primary Analyst]=?, [Secondary Analyst]=?,\
                        [Project Manager]=?, Requester=?, [Technical Focal]=?, [Finance Analyst]=?,\
                        [Cost($M)]=?, [NPV($M)]=?, MIRR=?, [Payback]=?, \
                        [B/C Ratio]=?, [Benefit Type]=?,[Benefit Owner]=?, [Date Completed]=? WHERE pk0=?",
                (iteration, program_type, proj_title, proj_description,
                 business_unit, program_name, status, portfolio_alignment, customer, request_id, usr_notes,
                 last_update_date, last_update_user, receipt_date, due_date, erb_date, manager_review_date,
                 finops_date, boe_date, date_cancelled, primary_est, secondary_est, project_manager,
                 requester, tech_focal, finops_focal, nr_estimate, npv, mirr, pay_backdis, b_c_ratio,
                 benefit_type, benefit_owner, date_completed, str(primary_key_pk0)))

    cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                (iteration, request_id, cost_year['year1'], cost_value['cost1'], typo.get('type1'), str(min_pk_cost)))
    cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                (iteration, request_id, benefit_year['year1'], benefit_value['bene1'], typo.get('type2'),
                 str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if ((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, cost_year['year2'], cost_value['cost2'], typo.get('type1'),
                     str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, benefit_year['year2'], benefit_value['bene2'], typo.get('type2'),
                     str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if ((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, cost_year['year3'], cost_value['cost3'], typo.get('type1'),
                     str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, benefit_year['year3'], benefit_value['bene3'], typo.get('type2'),
                     str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if ((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, cost_year['year4'], cost_value['cost4'], typo.get('type1'),
                     str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, benefit_year['year4'], benefit_value['bene4'], typo.get('type2'),
                     str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if ((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, cost_year['year5'], cost_value['cost5'], typo.get('type1'),
                     str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, benefit_year['year5'], benefit_value['bene5'], typo.get('type2'),
                     str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if ((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, cost_year['year6'], cost_value['cost6'], typo.get('type1'),
                     str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, benefit_year['year6'], benefit_value['bene6'], typo.get('type2'),
                     str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if ((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, cost_year['year7'], cost_value['cost7'], typo.get('type1'),
                     str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, benefit_year['year7'], benefit_value['bene7'], typo.get('type2'),
                     str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if ((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, cost_year['year8'], cost_value['cost8'], typo.get('type1'),
                     str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, benefit_year['year8'], benefit_value['bene8'], typo.get('type2'),
                     str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if ((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, cost_year['year9'], cost_value['cost9'], typo.get('type1'),
                     str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, benefit_year['year9'], benefit_value['bene9'], typo.get('type2'),
                     str(min_pk_bene)))
    min_pk_cost += 1
    min_pk_bene += 1
    if ((min_pk_cost <= max_pk_cost) and (min_pk_bene <= max_pk_bene)):
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, cost_year['year10'], cost_value['cost10'], typo.get('type1'),
                     str(min_pk_cost)))
        cur.execute("UPDATE ELF_data SET Iteration=?,RequestID=?,Year=?,Value=?,Type=? WHERE pk_data=?",
                    (iteration, request_id, benefit_year['year10'], benefit_value['bene10'], typo.get('type2'),
                     str(min_pk_bene)))
    conn.commit()
    tk.messagebox.showinfo(title='Excellent!', message='You updated {} row(s)'.format(cur.rowcount))
    cur.close()
    conn.close()

def insert_ELF(benefit_year, benefit_value, typo, cost_year, cost_value, iteration="", project_program_type="",
               project_program_title="", project_program_description="",
               business_unit="", program_name="", status="", portfolio_alignment="", customer="", request_id="",
               notes="", last_update_date="", last_update_user="", receipt_request_date="", due_date="",
               erb_review_date="", manager_review_date="", int_finops_date="", boe_date="", date_cancelled="",
               primary_estimator="", secondary_estimator="", project_manager="", requestor="", technical_focal="",
               finops_focal="", nr_cost_estimate="", npv="", mirr="", payback_discounted="", b_c_ratio="",
               benefit_type="", benefit_owner="", date_completed=""):
    try:
        conn = sqlite3.connect('ELF_db.db')
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
        cur.execute(
            "INSERT INTO ELF0 VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (iteration, project_program_type, project_program_title, project_program_description, business_unit,
             program_name, status, portfolio_alignment, customer, request_id, notes, last_update_date,
             last_update_user, receipt_request_date, due_date, erb_review_date, manager_review_date,
             int_finops_date, boe_date, date_cancelled, primary_estimator, secondary_estimator,
             project_manager, requestor, technical_focal, finops_focal, nr_cost_estimate, npv,
             mirr, payback_discounted, b_c_ratio, benefit_type, benefit_owner, date_completed))

        fk_pk0 = cur.lastrowid
        for key_value, key2_value in zip(cost_year.values(), cost_value.values()):
            if key_value != 0 and key2_value != 0:
                cur.execute("INSERT INTO ELF_data VALUES (NULL,?,?,?,?,?,?)",
                            (fk_pk0, iteration, request_id, str(key_value), str(key2_value), typo.get('type1')))
            else:
                continue

        for key_value, key2_value in zip(benefit_year.values(), benefit_value.values()):
            if key_value != 0 and key2_value != 0:
                cur.execute("INSERT INTO ELF_data VALUES (NULL,?,?,?,?,?,?)",
                            (fk_pk0, iteration, request_id, str(key_value), str(key2_value), typo.get('type2')))
            else:
                continue

        conn.commit()
        tk.messagebox.showinfo(title='Excellent!',
                               message='Total of {} record(s) were added successfully!'.format(cur.rowcount))
        cur.close()
        conn.close()
    except Exception as e:
        print(str(e))
