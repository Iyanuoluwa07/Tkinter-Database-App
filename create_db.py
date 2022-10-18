# Database

from tkinter import *
import sqlite3

root = Tk()

root.title('Database')
root.iconbitmap('fire.ico')
root.geometry('480x480')

# create or connect to a database
conn = sqlite3.connect('address_book.db')

# cursor
c = conn.cursor()

# create table
c.execute(''' CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
    )''')

# commit
conn.commit()

# close database
conn.close()

root.mainloop()
