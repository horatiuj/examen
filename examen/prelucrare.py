import pandas as pd
import sqlite3



with sqlite3.connect('db.sqlite3') as conn:
    df= pd.read_sql('select * from usermodel',conn)
    df['full_name'] =df['first_nume'] + ' ' + df['last_nume']

df.to_excel('rezultat.xlsx')

df1= df["number_of_login"].mean()
df2= df["number_of_login"].std()
print(df1)
print(df2)
