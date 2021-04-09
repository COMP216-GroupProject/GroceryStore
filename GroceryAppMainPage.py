import sqlite3
import tkinter as tk 
from tkinter import PhotoImage, filedialog, Text
from tkinter.constants import END, NUMERIC, NW


conn = sqlite3.connect("groceries.db")
c = conn.cursor()
#If table doesnt exist it creates it
try:
   c.execute("""CREATE TABLE groceries (
   ITEM_NAME TEXT,
   ITEM_QUANTITY INTEGER,
   ITEM_PRICE REAL
   )""")
except:
   #If table exits then do nothing all previous values for new order
   print("Table Already Exits")
conn.commit()

def newOrder():
   setCurrentValue(0)
   c.execute('DELETE FROM groceries;')
   conn.commit()

#method for setting Current Total Value
def setCurrentValue(newTotalPrice):
    currentTotalValue.set(str(newTotalPrice))
    return

def openAgain():
    #make root visible again
    root.iconify()
    root.deiconify()

#on addToOrder button click
def addToOrder():  
   root.destroy()
   import AddToOrderPage
   addOrderPage = AddToOrderPage.openAgain()
   openAgain()
   c.close()


#on updateOrderButton button click
def updateOrder():
   tk.messagebox.showinfo( "Add To Existing Order", "Order")

#on getBillButton button click
def getBill():
   tk.messagebox.showinfo( "Add To Existing Order", "Order")

root = tk.Tk()
root.title("GROCERY STORE BILL CALCULATOR")
canvas1 = tk.Canvas(root, heigh=700, width=683, bg="#263D42")
canvas1.pack()




# #Welcome frame to add welcome Image to (the farme at the top)
# welcomeFrame = tk.Frame(root, bg="white")
# welcomeFrame.place(relwidth = 0.8, relheight = 0.3, relx=0.1, rely = 0.05)

img = PhotoImage(file="./Images/WelcomeImage2.png")
canvas1.create_image(20,20, anchor=NW, image=img)  

#Button Frames where all buttons are located
buttonFrame = tk.Frame(root, bg="gray")
buttonFrame.place(relwidth = 0.8, relheight = 0.2, relx=0.1, rely = 0.65)

#Button Frames where all buttons are located
currentTotalFrame = tk.Frame(root, bg="gray")
currentTotalFrame.place(relwidth = 0.8, relheight = 0.1, relx=0.1, rely = 0.88)

#"Current Total" Label
lbl=tk.Label(currentTotalFrame, text="Current Total:", fg='red', font=("Helvetica", 14,"bold"))
lbl.place(x=30, y=30)

label = tk.Label(currentTotalFrame, text='$', fg="black", font=("Helvetica", 13,"bold"))
label.place(x=397, y=30)


# "Current Total" TextField 
currentTotalValue = tk.StringVar()
currentTotalTxtFld=tk.Entry(currentTotalFrame, textvariable=currentTotalValue, bd=5)
currentTotalTxtFld.place(x=410, y=30)
currentTotalTxtFld.configure(state="disabled")



  

c.execute("SELECT SUM(ITEM_PRICE) FROM groceries")
[(totalPricesOfItems,)] = c.fetchall()
#Set The price of the current item
if(totalPricesOfItems == None):
      setCurrentValue(0)
else:
   setCurrentValue(totalPricesOfItems)

newOrderButton = tk.Button(buttonFrame, text ="New Order?", height=2, width=20, command = newOrder)
newOrderButton.place(x=200, y=20)

addToOrderButton = tk.Button(buttonFrame, text ="Add To Order",  height=2, width=12,command = addToOrder)
addToOrderButton.place(x=30, y=80)

updateOrderButton= tk.Button(buttonFrame, text ="Update Order", height=2, width=12, command = updateOrder)
updateOrderButton.place(x=230, y=80)

getBillButton = tk.Button(buttonFrame, text ="Get Receipt",  height=2, width=12,command = getBill)
getBillButton.place(x=430, y=80)



root.mainloop()
