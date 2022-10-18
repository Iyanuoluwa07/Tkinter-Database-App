# Database with Tkinter

from tkinter import *
import sqlite3

root = Tk()
root.title('A Simple Database')
root.iconbitmap('fire.ico')
root.geometry('335x500')

# connecting to database
conn = sqlite3.connect('address_book.db')
# create cursor
c = conn.cursor()


def update_new_record():
    global editor, conn, c

    # create or connect to a database
    conn = sqlite3.connect('address_book.db')
    # cursor
    c = conn.cursor()

    record_id = delete.get()
    delete.delete(0, END)

    # add record
    c.execute('''UPDATE  addresses SET
              first_name = :first_name,
              last_name = :last_name,
              address = :address,
              city = :city,
              state = :state,
              zipcode = :zipcode

              WHERE oid = :oid''',
              {
                  'first_name': first_name_editor.get(),
                  'last_name': last_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'oid': record_id
              })

    # commit
    conn.commit()
    # close database
    conn.close()

    editor.destroy()


first_name_editor = Entry()
last_name_editor = Entry()
address_editor = Entry()
city_editor = Entry()
state_editor = Entry()
zipcode_editor = Entry()


def edit_record():
    global editor, conn, c

    editor = Tk()
    editor.title('Update Record')
    editor.iconbitmap('fire.ico')
    editor.geometry('335x250')

    # connecting to database
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()

    query_label.grid_forget()

    record_id = delete.get()
    # query records
    c.execute('SELECT * FROM addresses WHERE oid = ' + record_id)
    records = c.fetchall()

    global first_name_editor, last_name_editor, address_editor, city_editor, state_editor, zipcode_editor

    # create entry boxes
    first_name_editor = Entry(editor, width=40)
    first_name_editor.grid(row=0, column=1, padx=20, pady=(15, 0))
    last_name_editor = Entry(editor, width=40)
    last_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=40)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=40)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=40)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=40)
    zipcode_editor.grid(row=5, column=1, padx=20)

    # create text boxes labels
    first_name_la = Label(editor, text='First Name')
    first_name_la.grid(row=0, column=0, pady=(15, 0))
    last_name_la = Label(editor, text='Last Name')
    last_name_la.grid(row=1, column=0)
    address_la = Label(editor, text='Address')
    address_la.grid(row=2, column=0)
    city_la = Label(editor, text='City')
    city_la.grid(row=3, column=0)
    state_la = Label(editor, text='State')
    state_la.grid(row=4, column=0)
    zipcode_la = Label(editor, text='Zipcode')
    zipcode_la.grid(row=5, column=0)

    # loop thru result
    for record in records:
        first_name_editor.insert(0, record[0])
        last_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # create edit button
    update_btn = Button(editor, text='Update Record', command=update_new_record, background='Grey')
    update_btn.grid(row=6, column=0, pady=10, padx=(50, 0), ipadx=40, columnspan=2)

    # commit
    conn.commit()
    # close database
    conn.close()


# create add record button
def add_record():
    global conn, c, query_label

    # create or connect to a database
    conn = sqlite3.connect('address_book.db')
    # cursor
    c = conn.cursor()

    # add record
    c.execute('INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)',
              {
                 'first_name': first_name.get(),
                 'last_name': last_name.get(),
                 'address': address.get(),
                 'city': city.get(),
                 'state': state.get(),
                 'zipcode': zipcode.get()
              })

    # commit
    conn.commit()
    # close database
    conn.close()

    query_label.grid_forget()

    # delete old entry for new entry
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


query_label = Label()


def show_record():
    global conn, c, query_label

    # create or connect to a database
    conn = sqlite3.connect('address_book.db')
    # cursor
    c = conn.cursor()

    # query records
    c.execute('SELECT *, oid FROM addresses')
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    # commit
    conn.commit()
    # close database
    conn.close()


def delete_record():
    global conn, c, query_label
    # create or connect to a database
    conn = sqlite3.connect('address_book.db')
    # cursor
    c = conn.cursor()

    # query records
    c.execute('DELETE from addresses WHERE oid=' + delete.get())

    delete.delete(0, END)

    query_label.grid_forget()

    # commit
    conn.commit()
    # close database
    conn.close()


# create entry boxes
first_name = Entry(root, width=40)
first_name.grid(row=0, column=1, padx=20, pady=(15, 0))
last_name = Entry(root, width=40)
last_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=40)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=40)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=40)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=40)
zipcode.grid(row=5, column=1, padx=20)
delete = Entry(root, width=40)
delete.grid(row=8, column=1, padx=20, pady=5)

# create text boxes labels
first_name_label = Label(root, text='First Name')
first_name_label.grid(row=0, column=0, pady=(15, 0))
last_name_label = Label(root, text='Last Name')
last_name_label.grid(row=1, column=0)
address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(root, text='City')
city_label.grid(row=3, column=0)
state_label = Label(root, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)
delete_label = Label(root, text='Record ID')
delete_label.grid(row=8, column=0)

# create add record button
add_record_btn = Button(root, text='Add Record', command=add_record, background='Yellow')
add_record_btn.grid(row=6, column=0, pady=10, padx=(50, 0), ipadx=46, columnspan=2)

# create show record button
show_record_btn = Button(root, text='Show Records', command=show_record, background='Grey')
show_record_btn.grid(row=7, column=0, pady=10, padx=(50, 0), ipadx=40, columnspan=2)

# delete record button
delete_record_btn = Button(root, text='Delete Record', command=delete_record, background='Grey')
delete_record_btn.grid(row=9, column=0, pady=10, padx=(50, 0), ipadx=40, columnspan=2)

# create edit button
edit_btn = Button(root, text='Edit Record', command=edit_record, background='Yellow')
edit_btn.grid(row=10, column=0, pady=10, padx=(50, 0), ipadx=46, columnspan=2)

# commit
conn.commit()
# close database
conn.close()

root.mainloop()
