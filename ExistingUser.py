from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as con
from RestaurantOptions import *

def existingUserLogIn():
    win1 = Toplevel()

    win1.geometry("800x500+300+200")
    win1.title("FoodDash")
    win1.config(background="#FFFFFF")

    icon = PhotoImage(file="FoodDash_Icon.png")
    win1.iconphoto(True, icon)

    namelogo = Image.open("FoodDash_LogoWithName.png")
    logo = namelogo.resize((100,100))
    logo1 = ImageTk.PhotoImage(logo)

    img1 = Label(win1, image=logo1, bg="#FFFFFF")
    img1.place(x=20, y=5)

    # Keep a reference to the logo image
    win1.logo1 = logo1

    title = Label(win1,
                  text="Log In",
                  font=("Elephant", 30, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404")
    title.place(x=320, y=30)

    uname1 = Label(win1,
                  text="Username  :  ",
                  font=("Arial", 20, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404")
    uname1.place(x=150, y=180)
    untxt1 = Entry(win1,
                  font=("Arial", 20, "bold"),
                  bg="#FFFFFF")
    untxt1.place(x=350, y=180)    
    passwd1 = Label(win1,
                  text="Password  :  ",
                  font=("Arial", 20, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404")
    passwd1.place(x=150, y=230)    
    pwdtxt1 = Entry(win1,
                  font=("Arial", 20, "bold"),
                  show=str('*'),
                  bg="#FFFFFF")
    pwdtxt1.place(x=350, y=230)

    def logIn():
        # Retrieve values from the Entry widgets
        username = untxt1.get()
        password = pwdtxt1.get()

        # Connect to the MySQL database
        db_connection = con.connect(
            host="localhost",
            user="root",
            password="123456",
            database="FoodDashDB",
        )

        # Create a cursor object to execute SQL queries
        cursor = db_connection.cursor()

        # Check if the entered username and password match with data in 'CustomerData' table
        cursor.execute("""
            SELECT * FROM CustomerData
            WHERE uname = %s AND pass = %s
        """, (username, password))

        result = cursor.fetchone()

        if result:
            # If a matching record is found, open the next window (RestaurantOptions.py)
            restaurantOptions()
            win1.destroy()
        else:
            invalidL = Label(win1,
                  text="* invaid username or password",
                  font=("Arial", 15),
                  bg="#FFFFFF",
                  fg="red")
            invalidL.place(x=350, y=270)

        # Close the cursor and connection
        cursor.close()
        db_connection.close()

    LogInB = Button(win1,
                    text="Log In",
                    font=("Arial", 15, "bold"),
                    fg="#FFFFFF",
                    bg="#FF5404",
                    width=20,
                    command=logIn)
    LogInB.place(x=280, y=320)
