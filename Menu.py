from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as con
from OrderSummary import *



def getMenu(restaurant_name, win3):
    win5 = Toplevel()

    win5.geometry("800x500+300+200")
    win5.title("FoodDash")
    win5.config(background="#FFFFFF")

    blankLbl = Label(win5, text="   ", font=("arial", 100), bg="#FFFFFF")
    blankLbl.grid(row=0, column=0)

    namelogo = Image.open("FoodDash_LogoWithName.png")
    logo = namelogo.resize((100, 100))
    logo1 = ImageTk.PhotoImage(logo)

    img1 = Label(win5, image=logo1, bg="#FFFFFF")
    img1.place(x=20, y=5)

    icon = PhotoImage(file="FoodDash_Icon.png")
    win5.iconphoto(True, icon)

    # Keep a reference to the logo image
    win5.logo1 = logo1

    title = Label(win5,
                  text="Menu",
                  font=("Elephant", 30, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404")
    title.place(x=340, y=30)

    # Connect to the MySQL database
    db_connection = con.connect(
        host="localhost",
        user="root",
        password="123456",
        database="FoodDashDB",
    )

    # Create a cursor object to execute SQL queries
    cursor = db_connection.cursor()

    # Fetch data based on the restaurant_name
    cursor.execute(f"SELECT * FROM {restaurant_name}")
    menu_data = cursor.fetchall()
    quantity_spinbox_list = []

    #the Order Button
    def logIn():
        selected_items = []
        for idx, row in enumerate(menu_data):
            item_quantity = quantity_spinbox_list[idx].get()
            print(f"Menu Item: {row[0]}, Spinbox Value: {item_quantity}")  #remove this later

            if item_quantity != '0':
                item_name, item_price = row[0], row[1]
                selected_items.append((item_name, item_price, int(item_quantity)))

        win5.destroy()
        orderSummary(selected_items)

    LogInB = Button(win5,
                    text="Order",
                    font=("Arial", 15, "bold"),
                    fg="#FFFFFF",
                    bg="#FF5404",
                    padx=50,
                    pady=0,
                    disabledforeground="light grey",
                    #disabledbackground="#F2AF79",
                    command=logIn)
    LogInB.place(x=420, y=370)

    def checkOrderButtonState():
        # Check if any quantity is greater than 0
        enable_order = any(int(quantity_spinbox.get()) > 0 for quantity_spinbox in quantity_spinbox_list)
        if enable_order:
            LogInB.config(state="normal")  # Enable the Order button
        else:
            LogInB.config(state="disabled")  # Disable the Order button


    #the Back Button
    def goBack():
        win5.destroy()
        win3.deiconify()

    BackB = Button(win5,
                    text="Back",
                    font=("Arial", 15, "bold"),
                    fg="#FFFFFF",
                    bg="#FF5404",
                    padx=50,
                    pady=0,
                    command=goBack)
    BackB.place(x=220, y=370)    
        


    ## Display the menu items with an option to select the quantity

    # Initial check for the Order button state
    checkOrderButtonState()

    # Your label and Spinbox creation code here
    count = 1
    for Row in menu_data:
        menu_label = Label(win5, text=f"{Row[0]}",
                           font=("Arial", 19, "bold"),
                           bg="#FFFFFF",
                           fg="#FF5404")
        menu_label.grid(row=count, column=1, sticky=W)

        price_label = Label(win5, text=f"   -  ₹{Row[1]}",
                            font=("Arial", 19, "bold"),
                            bg="#FFFFFF",
                            fg="#FF5404")
        price_label.grid(row=count, column=2, sticky=W)

        quantity_label = Label(win5, text="          Quantity: ",
                               font=("Arial", 19, "bold"),
                               bg="#FFFFFF",
                               fg="#FF5404")
        quantity_label.grid(row=count, column=3, sticky=E)

        quantity_var = IntVar()
        quantity_spinbox = Spinbox(win5, from_=0, to=5, textvariable=quantity_var)
        quantity_spinbox.grid(row=count, column=4, sticky=W)
        quantity_spinbox_list.append(quantity_spinbox)
        quantity_spinbox.config(command=checkOrderButtonState)  # Check button state on Spinbox change
        count += 1

    # Close the cursor and connection
    cursor.close()
    db_connection.close()

    win5.mainloop()
