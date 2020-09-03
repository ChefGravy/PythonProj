# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:50:36 2020

@author: ao378d
"""
import sqlite3

def data_dump():
    con = sqlite3.connect('ELF_db.db')
    cur=con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print("---------------------ELF0-------------")
    print(cur.fetchall())
    cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='ELF0'")
    print(cur.fetchall())
    print("-----------------ELF_data--------------")
    cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='ELF_data'")
    print(cur.fetchall())
    print("----------------ELF_data---------------")
    cur.execute("SELECT pk_data,pk0 FROM ELF_data")
    print(cur.fetchall())
    print("----------------ELF_0---------------")
    cur.execute("SELECT pk0 FROM ELF0")
    print(cur.fetchall())
    print("-------------------------ELF0 data-----------------")
    cur.execute("SELECT * FROM ELF0")
    print(cur.fetchall())
    con.commit()
    con.close()
            
data_dump()
#cur.execute("SELECT id_pk FROM ELF_data")
#print(cur.fetchall())