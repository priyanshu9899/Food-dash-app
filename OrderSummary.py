from tkinter import *
from PIL import Image, ImageTk
from OrderPlaced import *


def orderSummary(selected_items):
    win6 = Toplevel()
    print("Selected items:", selected_items)  # remove this later

    win6.geometry("800x500+300+200")
    win6.title("Order Summary")
    win6.config(background="#FFFFFF")

    blankLbl = Label(win6, text="    ", font=("arial", 75), bg="#FFFFFF")
    blankLbl.grid(row=0, column=0)

    namelogo = Image.open("FoodDash_LogoWithName.png")
    logo = namelogo.resize((100, 100))
    logo1 = ImageTk.PhotoImage(logo)

    img1 = Label(win6, image=logo1, bg="#FFFFFF")
    img1.place(x=20, y=5)

    icon = PhotoImage(file="FoodDash_Icon.png")
    win6.iconphoto(True, icon)

    # Keep a reference to the logo image
    win6.logo1 = logo1

    title = Label(win6,
                  text="Order Summary",
                  font=("Elephant", 30, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404")
    title.place(x=250, y=30)


    # Display order summary
    total_price = 0

    #title Labels
    itemLbl = Label(win6, text="    ITEMS    ", font=("Arial", 15, "underline"),bg="#FFFFFF",fg="#000000")
    itemLbl.grid(row=1,column=1)
    qtyLbl = Label(win6, text=" QUANTITY ", font=("Arial", 15, "underline"),bg="#FFFFFF",fg="#000000", padx=4, pady=4)
    qtyLbl.grid(row=1,column=2)
    unitPriceLbl = Label(win6, text=" UNIT PRICE ", font=("Arial", 15, "underline"),bg="#FFFFFF",fg="#000000", padx=4, pady=4)
    unitPriceLbl.grid(row=1,column=3)
    priceLbl = Label(win6, text=" TOTAL PRICE ", font=("Arial", 15, "underline"),bg="#FFFFFF",fg="#000000", padx=4, pady=4)
    priceLbl.grid(row=1,column=4)

    count = 2
    if selected_items:  # Check if there are selected items
        for idx, item in enumerate(selected_items, start=0):
            item_name, item_price, item_quantity = item
            total_price += item_price * item_quantity

            item_label = Label(win6, text=f"{item_name}   ",
                               font=("Arial", 15),
                               bg="#FFFFFF",
                               fg="#000000")
            #item_label.place(x=50, y=100 + 30 * idx)
            item_label.grid(row=count,column=1, sticky=W)

            qty_label = Label(win6, text=f"   {item_quantity}   ",
                               font=("Arial", 15),
                               bg="#FFFFFF",
                               fg="#000000")
            #item_label.place(x=50, y=100 + 30 * idx)
            qty_label.grid(row=count,column=2)

            unitPrice_label = Label(win6, text=f"   ₹{item_price}   ",
                               font=("Arial", 15),
                               bg="#FFFFFF",
                               fg="#000000")
            #item_label.place(x=50, y=100 + 30 * idx)
            unitPrice_label.grid(row=count,column=3)

            price_label = Label(win6, text=f"   ₹{item_price * item_quantity}",
                               font=("Arial", 15),
                               bg="#FFFFFF",
                               fg="#000000")
            #item_label.place(x=50, y=100 + 30 * idx)
            price_label.grid(row=count,column=4)

            count += 2

    total_label = Label(win6, text=f" TOTAL:                                                            ₹{total_price}   ",
                        font=("Arial", 15, "underline"),bg="#FFFFFF",fg="#000000")
    total_label.place(x=120, y=250)

    def placeOrder():
        orderPlaced()
        win6.destroy()

    LogInB = Button(win6,
                    text="Confirm Order",
                    font=("Arial",15, "bold"),
                    fg="#FFFFFF",
                    bg="#FF5404",
                    padx=50,
                    pady=0,
                    command=placeOrder)
    LogInB.place(x=280,y=370)

    win6.mainloop()
