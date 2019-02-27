#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
from tkinter import ttk
#----------------------------------------------------------------------------------
#Functions for handling gui and messages
#----------------------------------------------------------------------------------
def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")#recieve messages handled by server
            msg_list.insert(END, msg)#insert messages into messagebox client
            msg_list.yview(END)#autoscroll to the last inserted text in text box
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    msg = my_msg.get()#retreive user input from entry field
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))#send the user input to server for handling
    if msg == "{exit}":#typing {exit} will cause client to exit
        client_socket.close()#close the socket connection
        top.quit()#close application


def on_closing(event=None):
    my_msg.set("{exit}")
    send()

top = Tk()
top.title("UgoChat")
top.iconbitmap(r'Logo.ico')
top.geometry("500x500")

#------------------TESTING NEW CHUNK
"""style = ttk.Style()
style.theme_use('clam')

# list the options of the style
# (Argument should be an element of TScrollbar, eg. "thumb", "trough", ...)
print(style.element_options("Horizontal.TScrollbar.thumb"))

# configure the style
style.configure("Horizontal.TScrollbar", gripcount=0,
                background="Green", darkcolor="DarkGreen", lightcolor="LightGreen",
                troughcolor="gray", bordercolor="blue", arrowcolor="white")

hs = ttk.Scrollbar(top, orient="horizontal")
hs.place(x=12, y=400, width=150)
hs.set(0.2,0.3)"""
#--------------------END TESTING NEW CHUNK


messages_frame = Frame(top)
my_msg = StringVar()  # For the messages to be sent.
scrollbarY = Scrollbar(messages_frame)  # To navigate through past messages.
msg_list = Listbox(messages_frame, height=28, width=72, yscrollcommand=scrollbarY.set,bg="black",fg="#66ffff")
scrollbarY.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
messages_frame.pack()

sendPNG = PhotoImage(file = 'forward.png')
send_button = Button(top, text="Send", bg = "#6699ff", fg = "white", command=send)#button used to send text
#send_button = Button(top, image = sendPNG, command=send)#button used to send text
send_button.place(x=24, y=450, height = 19)#place the button at specified x and y
entry_field = Entry(top, bg = "#99ccff", textvariable=my_msg)#empty box to type and insert messages into chat
entry_field.bind("<Return>", send)#pressing enter performs send operation as does clicking send
entry_field.place(x=61, y=450, width=398, height =20)#place entry field at x and y


top.protocol("WM_DELETE_WINDOW", on_closing)

#-------------------------------------------------------------------------------------
#Connection to the server
#-------------------------------------------------------------------------------------
#print("\U0001F602")  prints out an emoji

host = '98.242.60.126'
port = 50000
BUFSIZ = 1024
ADDR = (host, port)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
top.mainloop()  # Starts GUI execution.


#credits for logo
#<div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" 		    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 		    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
