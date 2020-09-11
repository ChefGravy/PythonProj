# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:28:51 2020

@author: Pepper
"""

import sqlite3

def connect():
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS elfy ('id' INTEGER PRIMARY KEY, \
                                                  'prog_title' TEXT,\
                                                  'analyst' TEXT,\
                                                  'notes' TEXT, \
                                                  'pid_aid' TEXT)")
    conn.commit()
    conn.close()
    
def insert(prog_title, analyst, notes, pid_aid):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO elfy VALUES (NULL, ?,?,?,?)", (prog_title, analyst, notes, pid_aid))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM elfy")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(prog_title="", analyst="", notes="", pid_aid=""):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM elfy WHERE prog_title=? OR analyst=? OR notes=? OR pid_aid=?", (prog_title, analyst, notes, pid_aid))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM elfy WHERE id=?",(id,))
    conn.commit()
    conn.close()
    
def update(id,prog_title, analyst, notes, pid_aid):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE elfy SET prog_title=?, analyst=?, notes=?, pid_aid=? WHERE id=?", (prog_title, analyst, notes, pid_aid,id))
    conn.commit()
    conn.close()
