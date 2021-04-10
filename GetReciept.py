import tkinter as tk
from sqlite3 import dbapi2 as sqlite
import sqlite3
from tkinter import PhotoImage, filedialog, Text
from tkinter.constants import END, NW
from tkinter import Entry

conn = sqlite3.connect("groceries.db")
c = conn.cursor()


def backToMain():
    root.destroy()
    # import GroceryAppMainPage
    # backToMainPage = GroceryAppMainPage.openAgain()
    openAgain()
    c.close()


def openAgain():
    # make root visible again
    root.iconify()
    root.deiconify()


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
            print("Id: ", row[0])
            print("Name: ", row[1])
            print("Email: ", row[2])
            print("\n")
    else:
        print("ONE FIELD IS EMPTY")


def showOrderSummmary(canvas):
    sqlite_select_query = """SELECT * from groceries"""
    total = 0
    c.execute(sqlite_select_query)
    records = c.fetchall()
    x = 30
    y = 80
    for row in records:
        #print("Item: ", row[0], " | Quantity: ", row[1], " | Price: ", row[2])
        rowData = "Item: " + row[0] + " |   Quantity: " + str(row[1]) + " |     Price: " + str(row[2])
        rowDataString = str(rowData)
        print(rowDataString)
        itemNamelbl = tk.Label(canvas, text=(rowDataString),
                               fg='black', font=("Helvetica", 11))
        itemNamelbl.place(x=x, y=y)
        y += 40
        total += int(float(row[2]))

    y += 40
    x += 280
    itemNamelbl = tk.Label(canvas, text=("Order Total : $" + str(total)), fg='red',
                           font=("Helvetica", 14))
    itemNamelbl.place(x=x, y=y)

    print("Order Total : ", total)


def insertNewRow(itemm_name, item_qty, price):
    item_price = int(item_qty) * float(price)
    sql_insert_statement = "INSERT INTO groceries (ITEM_NAME, ITEM_QUANTITY, ITEM_PRICE) values (?, ?, ?)"
    data_tuple = (itemm_name, item_qty, item_price)
    c.execute(sql_insert_statement, data_tuple)
    conn.commit()
    return c.lastrowid



root = tk.Tk()
canvas = tk.Canvas(root, heigh=680, width=500, bg="#263D42")
showOrderSummmary(canvas)

# Title Message To User Label
lbl = tk.Label(canvas, text="Order Summary", fg='black', font=("Helvetica", 15, "bold"))
lbl.place(x=180, y=30)

backToMainButton = tk.Button(canvas, text="BACK TO MAIN MENU", height=2, width=30, command=backToMain)
backToMainButton.place(x=95, y=625)

canvas.pack()
root.mainloop()
