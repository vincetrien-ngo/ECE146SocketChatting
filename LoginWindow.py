from tkinter import *
import os

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


def userRegistration():
    usernameInfo = username.get()  # acquire user input for username on registration page
    passwordInfo = password.get()  # acquire user input for password on registration page

    file = open(usernameInfo, "w")  # open a username file with writing privilages
    file.write(usernameInfo+"\n")  # store username into file
    file.write(passwordInfo)  # store password into file
    file.close()  # close the file

    usernameEntry.delete(0, END)  # Clear the text from the username textbox
    passwordEntry.delete(0, END)  # Clear the text from the password textbox

    Label(screen1, text = "Registration Successful!", fg = "green", font = ("Calibri", 11)).pack()

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


def register():
    global screen1  # Made global for use in userRegistration() function
    screen1 = Toplevel(screen)  # make this screen the currently used screen
    screen1.title("Registration")  # window title
    screen1.geometry("400x300")  # size of the screen

    global username  # globalize for use in userRegistration() function
    global password  # globalize for use in userRegistration() function
    global usernameEntry  # Made global for use in userRegistration() function
    global passwordEntry  # Made global for use in userRegistration() function

    username = StringVar()  # create as StringVar type
    password = StringVar()  # create as StringVar type

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()

    Label(screen1, text="Username: ", justify=LEFT, width="300", height="2").pack()
    Label(text="").pack()
    usernameEntry = Entry(screen1, textvariable=username, width="30")  # textbox for username
    usernameEntry.pack()

    Label(screen1, text="Password: ", justify=LEFT).pack()
    passwordEntry = Entry(screen1, textvariable=password, width="30")  # textbox for password
    passwordEntry.pack()

    Label(screen1, text="").pack()

    Button(screen1, text="Confirm Registration", height="2", width="30", bg="grey", command=userRegistration).pack()

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x300")
    Label(screen2, text="Please enter details below to login").pack()

    global userVerification
    global passVerification
    global userEntry
    global passEntry

    userVerification = StringVar()
    passVerification = StringVar()

    Label(screen2, text="Username: ").pack()
    userEntry = Entry(screen2, textvariable=userVerification)
    userEntry.pack()

    Label(screen2, text="Password: ").pack()
    passEntry = Entry(screen2, textvariable=passVerification)
    passEntry.pack()

    Label(text="").pack()
    Button(screen2, text="Login", width="30", height="2", bg="gray", command=verifyLogin).pack()

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------


def verifyLogin():
    username1 = userEntry.get()
    password1 = passEntry.get()
    userEntry.delete(0,END)
    passEntry.delete(0,END)

    fileList = os.listdir(os.curdir)
    if username1 in fileList:
        userFile = open(username1, "r")
        verify = userFile.read().splitlines()
        if password1 in verify:
            successfulLogin()
        else:
            failedLogin()
    else:
        userNotFound()


def successfulLogin():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login success").pack()
    Button(screen3, text="OK", command=destroy3).pack()


def failedLogin():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Failed Login")
    screen3.geometry("150x100")
    Label(screen3, text="Login Failure").pack()
    Button(screen3, text="OK", command=destroy3).pack()


def userNotFound():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("User Error")
    screen3.geometry("150x100")
    Label(screen3, text="User not found").pack()
    Button(screen3, text="OK", command=destroy3).pack()


def destroy3():
    screen3.destroy()

# ***************************************************************************************
# mainScreen is the screen in charge of choosing register or login
# ***************************************************************************************


def mainScreen():
    global screen
    screen = Tk()  # main login screen
    screen.geometry("400x300")  # size of screen
    screen.title("Login Authenticator")#window title
    Label(text="Ugo Chat", bg="grey", width="300", height="2", font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()  # login button
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()  # register button

    screen.mainloop()  # continuously check for events

# ----------------------------------------
# program start
# ----------------------------------------


mainScreen()  # run mainScreen function
