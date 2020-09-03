#import openpyxl as op
#from openpyxl import workbook
#from openpyxl.utils import get_column_letter
import pandas as pd
import sqlite3

#con = sqlite3.connect('ELF_db.db')
##con=sqlite3.connect(filename+".db")
#file_loc = r'C:\Users\ao378d\Desktop\ELF.xlsx';
#wb = pd.read_excel(file_loc)
#
#df_melt = pd.DataFrame
##drop the unncessary columns
##wb.drop(columns = ['Req Id-Iteration','Req Id No','Request ID','Grand Total Cost','Grand Total Benefit','Total Cost'], inplace=True, axis=1)
#
##--------------------DESPERATELY NEED MELT----------------
#def df_melt_data():
#    global df_melt
#    df_melt = pd.melt(wb,
#                     id_vars=['Iteration',
#                              'Project/Program Type',
#                              'Project/Program Title',
#                              'Project/Program Description',
#                              'Business Unit',
#                              'Program Name',
#                              'Status',
#                              'Portfolio Alignment',
#                              'Customer',
#                              'Previous Request ID',
#                              'Notes',
#                              'Last Update Date',
#                              'Last Update User',
#                              'Receipt/Request Date',
#                              'Due Date',
#                              'ERB Review Date',
#                              'Manager Review Completion Date',
#                              'Integration with FinOps Completed',
#                              'BOE Date',
#                              'Date Cancelled or Lost',
#                              'Primary Estimator',
#                              'Secondary Estimator (Support)',
#                              'Project Manager',
#                              'Requestor',
#                              'Technical Focal',
#                              'FinOps Focal',
#                              'NR Cost Estimate ($ in Mil.)',
#                              'NPV ($ in Mil.)',
#                              'MIRR',
#                              'Payback (Discounted)',
#                              'BC Ratio',
#                              'Benefit Type',
#                              'Benefit Owner',
#                              'Date Completed'],
#                      value_vars=['2018 Cost',
#                                  '2019 Cost',
#                                  '2020 Cost',
#                                  '2021 Cost',
#                                  '2022 Cost',
#                                  '2023 Cost',
#                                  '2024 Cost',
#                                  '2025 Cost',
#                                  '2026 Cost',
#                                  '2027 Cost',
#                                  '2028 Cost',
#                                  '2029 Cost',
#                                  '2030 Cost',
#                                  '2031 Cost',
#                                  '2032 Cost',
#                                  '2018 Benefit',
#                                  '2019 Benefit',
#                                  '2020 Benefit',
#                                  '2021 Benefit',
#                                  '2022 Benefit',
#                                  '2023 Benefit',
#                                  '2024 Benefit',
#                                  '2025 Benefit',
#                                  '2026 Benefit',
#                                  '2027 Benefit',
#                                  '2028 Benefit',
#                                  '2029 Benefit',
#                                  '2030 Benefit',
#                                  '2031 Benefit',
#                                  '2032 Benefit'],
#                      var_name='Year')
#
##--------------SPLIT YEAR INTO YEAR AND TYPE------------------------
#def split_year():
#    df_melt[['Year','Type']] = df_melt.Year.str.split(' ',expand=True)
#
##--------------END------------------------
#
##-----------------NEED TO RENAME COLUMNS----------------------------
#def rename_fields():
#    df_melt.rename(columns={'Previous Request ID': 'Request ID'},inplace=True)
#    df_melt.rename(columns={'Integration with FinOps Completed': 'Integration FinOps Completed'},inplace=True)
#    df_melt.rename(columns={'value': '$Value'},inplace=True)
#    df_melt.rename(columns={'Manager Review Completion Date': 'Manager Review Date'},inplace=True)
#
##------------------------END----------------------------------------
#
##-----------------SQL table/.db-------------------------------------
##this will create a table with our db name and our table name!
#def create_sql_table():
#    try:
#        conn = sqlite3.connect('ELF_db.db')
#        #cur=conn.cursor()
#    except:
#        print('Failed to make connection!')
#    
#    try:
#        df_melt.to_sql('ELF', conn, if_exists='replace', index_label='id')
#    except:
#        print("Ooooops, couldn't convert to .db!")
#
##-------------------------END---------------------------------------
##-----------SUPER CRITICAL-----------to view sql table--------------
#
#conn = sqlite3.connect("ELF_test")
#cur=conn.cursor()
#cur.execute("SELECT name from sqlite_master WHERE type='table'")
##this will give you the name of the table which you need
#print(cur.fetchall())
#cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='#see result from last print'")
#print(cur.fetchone()[0])
##hopefully you will see a table that you're now ready to load
#
##--------------------------Testing scripts-----------------------------
    
conn = sqlite3.connect("ELF_db.db")
cur = conn.cursor()
#cur.execute('DROP TABLE ELF0')
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("CREATE TABLE IF NOT EXISTS ELF0 (pk0 INTEGER PRIMARY KEY AUTOINCREMENT, \
                                              'Iteration' INTEGER NOT NULL, \
                                              'Project/Program Type' TEXT NOT NULL, \
                                              'Project/Program Title' TEXT NULL, \
                                              'Project/Program Description' TEXT NULL, \
                                              'Business Unit' TEXT, \
                                              'Program Name' TEXT, \
                                              'Status' TEXT, \
                                              'Portfolio Alignment' TEXT, \
                                              'Customer' TEXT NULL, \
                                              'RequestID' TEXT NOT NULL, \
                                              'Notes' TEXT NULL, \
                                              'Last Update Date' TEXT NULL, \
                                              'Last Update User' TEXT NULL, \
                                              'Receipt/Request Date' TEXT NULL, \
                                              'Due Date' TEXT NULL, \
                                              'ERB Review Date' TEXT NULL, \
                                              'Manager Review Date' TEXT NULL, \
                                              'Integration FinOps Completed' TEXT NULL, \
                                              'BOE Date' TEXT NULL, \
                                              'Date Cancelled or Lost' TEXT NULL, \
                                              'Primary Estimator' TEXT, \
                                              'Secondary Estimator (Support)' TEXT NULL, \
                                              'Project Manager' TEXT NULL, \
                                              'Requestor' TEXT NULL, \
                                              'Technical Focal' TEXT NULL, \
                                              'FinOps Focal' TEXT NULL, \
                                              'NR Cost Estimate ($ in Mil.)' REAL NULL, \
                                              'NPV ($ in Mil.)' REAL NULL, \
                                              'MIRR' REAL, \
                                              'Payback (Discounted)' REAL NULL, \
                                              'BC Ratio' REAL NULL, \
                                              'Benefit Type' TEXT NULL, \
                                              'Benefit Owner' TEXT, \
                                              'Date Completed' TEXT NULL)")
conn.commit()
#conn.close()
#-----------------------------------------------$Value and Year table---------------------------------
#conn = sqlite3.connect("ELF_db.db")
#cur = conn.cursor()
#cur.execute('DROP TABLE ELF_data')
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("CREATE TABLE IF NOT EXISTS ELF_data (pk_data INTEGER PRIMARY KEY AUTOINCREMENT, \
                                                  pk0 INTEGER NOT NULL, \
                                                  'Iteration' INTEGER NOT NULL, \
                                                  'RequestID' TEXT NOT NULL, \
                                                  'Year' INTEGER NULL, \
                                                  'Value' REAL, \
                                                  'Type' TEXT, \
                                                  FOREIGN KEY (pk0) REFERENCES ELF0(pk0) \
                                                      ON UPDATE CASCADE \
                                                      ON DELETE CASCADE)")

conn.commit()
conn.close()

    
