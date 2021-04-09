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
    #make root visible again
    root.iconify()
    root.deiconify()


#on clear button click
def clear():
    if(itemNameField.index(("end")) != 0):
        itemNameField.delete(0, END)
    if(itemPriceField.index(("end")) != 0):
        itemPriceField.delete(0, END)
    if(itemQTYfield.index(("end")) != 0):
        itemQTYfield.delete(0, END)


#on submit button click
def submit():
    #if all text fields are filled
    if(itemNameField.index(("end")) != 0 and itemPriceField.index(("end"))!= 0 and itemQTYfield.index(("end")) != 0 ):
        userEntryItemName = itemNameField.get()
        userEntryItemQTY = itemQTYfield.get()
        userEntryItemPrice = itemPriceField.get()
        insertNewRow(userEntryItemName, userEntryItemQTY, userEntryItemPrice)
        print(c.fetchall())
    else:
        print("ONE FIELD IS EMPTY")

def insertNewRow(itemm_name, item_qty, price):
    item_price = int(item_qty)* float(price)
    c.execute("INSERT INTO groceries (ITEM_NAME, ITEM_QUANTITY, ITEM_PRICE) values (?, ?, ?)",
            (itemm_name, item_qty, item_price))
    conn.commit()

    return c.lastrowid


root = tk.Tk()
canvas = tk.Canvas(root, heigh=380, width=400, bg="#263D42")
canvas.pack()

#Title Message To User Label
lbl=tk.Label(canvas, text="Enter Item Information Below:", fg='black', font=("Helvetica", 15,"bold"))
lbl.place(x=30, y=30)


#First Text Field Label
itemNamelbl=tk.Label(canvas, text="ITEM NAME:", fg='black', font=("Helvetica", 11))
itemNamelbl.place(x=30, y=80)
#Second Text Field Label
itemQTYlbl=tk.Label(canvas, text="ITEM QTY:", fg='black', font=("Helvetica", 11))
itemQTYlbl.place(x=30, y=120)
#Third Text Field Label
itemPricelbl=tk.Label(canvas, text="ITEM PRICE:", fg='black', font=("Helvetica", 11))
itemPricelbl.place(x=30, y=160)

#First Text Field
itemNameField=tk.Entry(canvas, textvariable='itemNameVar', bd=2)
itemNameField.place(x=240, y=80)
#Second Text Field
itemQTYfield=tk.Entry(canvas, textvariable='itemQTYeVar', bd=2)
itemQTYfield.place(x=240, y=120)
#Third Text Field 
itemPriceField=tk.Entry(canvas, textvariable='itemPriceVar', bd=2)
itemPriceField.place(x=240, y=160)

#Clear Button
clearButton = tk.Button(canvas, text ="CLEAR", height=3, width=20, command = clear)
clearButton.place(x=30, y=260)

#Submit Button
submitButton = tk.Button(canvas, text ="SUBMIT ORDER", height=3, width=20, command = submit)
submitButton.place(x=215, y=260)

#Submit Button
backToMainButton = tk.Button(canvas, text ="BACK TO MAIN MENU", height=2, width=30, command = backToMain)
backToMainButton.place(x=95, y=325)


#Button Frames where all buttons are located
# currentTotalFrame = tk.Frame(root, bg="gray")
# currentTotalFrame.place(relwidth = 0.8, relheight = 0.1, relx=0.1, rely = 0.88)


root.mainloop()

