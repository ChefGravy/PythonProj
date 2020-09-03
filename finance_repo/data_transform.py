import pandas as pd
import sqlite3
import frontend
from frontend import get_selected_row

conn = sqlite3.connect('ELF_db.db')
sql_query = pd.read_sql_query("SELECT * FROM ELF_data \
                              WHERE primary_key_pk0=?",(get_selected_row.primary_key_pk0), conn)
df1 = pd.DataFrame(sql_query, columns=['Iteration','RequestID','Year', 'Value', 'Type'])
#print (df)
df1_transposed = df1.T

print(df1)
#print(df1_transposed)
#print(len(df1))
#for i in range(len(df1)):
#    print(i)
#    print(df1_transposed[i][2])
#    print(df1_transposed[i][3])
#    print(df1_transposed[i][4])

