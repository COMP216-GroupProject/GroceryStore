import tkinter as tk
from sqlite3 import dbapi2 as sqlite
import sqlite3
from tkinter import PhotoImage, filedialog, Text
from tkinter.constants import END, NW

conn = sqlite3.connect("groceries.db")
c = conn.cursor()


def backToMain():
    root.destroy()
    import GroceryAppMainPage
    backToMainPage = GroceryAppMainPage.openAgain()
    openAgain()
    c.close()


def openAgain():
    # make root visible again
    root.iconify()
    root.deiconify()


# on clear button click
def clear():
    if (itemNameField.index(("end")) != 0):
        itemNameField.delete(0, END)
    if (itemPriceField.index(("end")) != 0):
        itemPriceField.delete(0, END)
    if (itemQTYfield.index(("end")) != 0):
        itemQTYfield.delete(0, END)


# on submit button click
def submit():
    # if all text fields are filled
    if itemNameField.index(("end")) != 0 and itemPriceField.index(("end")) != 0 and itemQTYfield.index(("end")) != 0:
        userEntryItemName = itemNameField.get()
        userEntryItemQTY = itemQTYfield.get()
        userEntryItemPrice = itemPriceField.get()
        print('lastrowid: ', insertNewRow(userEntryItemName, userEntryItemQTY, userEntryItemPrice))
        sqlite_select_query = """SELECT * from groceries"""

        c.execute(sqlite_select_query)
        records = c.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Name: ", row[0])
            print("Quantity: ", row[1])
            print("Price: ", row[2])
            print("\n")

    # if itemNameField.index(("end")) == itemNameField.index and itemPriceField.index(("end")) == itemPriceField and itemQTYfield.index(("end")) == itemQTYfield.index:
    #     userEntryItemName = itemNameField.get()
    #     userEntryItemQTY = itemQTYfield.get()
    #     userEntryItemPrice = itemPriceField.get()

    #     removeItem(userEntryItemName,userEntryItemQTY,userEntryItemPrice)

    else:
        print("ONE FIELD IS EMPTY")


def insertNewRow(itemm_name, item_qty, price):
    item_price = int(item_qty) * float(price)
    sql_insert_statement = "INSERT INTO groceries (ITEM_NAME, ITEM_QUANTITY, ITEM_PRICE) values (?, ?, ?)"
    data_tuple = (itemm_name, item_qty, item_price)
    c.execute(sql_insert_statement, data_tuple)
    conn.commit()

    return c.lastrowid

def remove():
    
    removeItem(itemNameField.get(),itemQTYfield.get(),itemPriceField.get())

def removeItem(itemm_name, item_qty, price):
    item_price = int(item_qty) * float(price)
    sql_insert_statement = "DELETE FROM groceries (ITEM_NAME, ITEM_QUANTITY, ITEM_PRICE) values (?, ?, ?)"
    data_tuple = (itemm_name, item_qty, item_price)
    c.execute(sql_insert_statement, data_tuple)
    conn.commit()
    
    return c.lastrowid


root = tk.Tk()
canvas = tk.Canvas(root, heigh=450, width=400, bg="#263D42")
canvas.pack()

# Title Message To User Label
lbl = tk.Label(canvas, text="Enter Item To Be Updated:", fg='black', font=("Helvetica", 15, "bold"))
lbl.place(x=30, y=30)

# First Text Field Label
itemNamelbl = tk.Label(canvas, text="ITEM NAME:", fg='black', font=("Helvetica", 11))
itemNamelbl.place(x=30, y=80)
# Second Text Field Label
itemQTYlbl = tk.Label(canvas, text="ITEM QTY:", fg='black', font=("Helvetica", 11))
itemQTYlbl.place(x=30, y=120)
# Third Text Field Label
itemPricelbl = tk.Label(canvas, text="ITEM PRICE:", fg='black', font=("Helvetica", 11))
itemPricelbl.place(x=30, y=160)

# First Text Field
itemNameField = tk.Entry(canvas, textvariable='itemNameVar', bd=2)
itemNameField.place(x=240, y=80)
# Second Text Field
itemQTYfield = tk.Entry(canvas, textvariable='itemQTYeVar', bd=2)
itemQTYfield.place(x=240, y=120)
# Third Text Field
itemPriceField = tk.Entry(canvas, textvariable='itemPriceVar', bd=2)
itemPriceField.place(x=240, y=160)

# Clear Button
clearButton = tk.Button(canvas, text="CLEAR", height=3, width=20, command=clear)
clearButton.place(x=30, y=260)

# Update Button
getBill = tk.Button(canvas, text="UPDATE ORDER", height=3, width=20, command=submit)
getBill.place(x=215, y=260)

# Main Page Button
backToMainButton = tk.Button(canvas, text="BACK TO MAIN MENU", height=3, width=20, command=backToMain)
backToMainButton.place(x=215, y=325)

# Remove Item Button
removeItemButton = tk.Button(canvas, text="REMOVE ITEM", height=3, width=20, command=remove)
removeItemButton.place(x=30, y=325)

# Button Frames where all buttons are located
# currentTotalFrame = tk.Frame(root, bg="gray")
# currentTotalFrame.place(relwidth = 0.8, relheight = 0.1, relx=0.1, rely = 0.88)


root.mainloop()
