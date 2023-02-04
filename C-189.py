import hashlib
from tkinter import *
from tkinter import messagebox
from firebase import firebase

_firebase = firebase.FirebaseApplication(
    "https://encryptedchat-2-default-rtdb.asia-southeast1.firebasedatabase.app/", None)

registration_window = Tk()
registration_window.geometry("400x400")
__bullet_utf_8 = "\u2022"
_bg_ = "purple"
_fg_ = "white"
registration_window.config(bg=_bg_)


def login():
    print("login function")
    login_username_entry
    login_password_entry
    username = login_username_entry.get()
    password = login_password_entry.get()
    password_encode = password.encode()
    encrypted_password = hashlib.md5(password_encode)
    hexadecimal_password = encrypted_password.hexdigest()
    print(hexadecimal_password)
    get_password = _firebase.get("/users/", username)
    if password != None:
        print(get_password)
        print(password)
        if get_password == hexadecimal_password:
            messagebox.showinfo("Info", "Logged In User!")
    else:
        messagebox.showwarning("Warning", "Password Should Not Be Empty")


def register():
    print("register function")
    username = username_entry.get()
    password = password_entry.get()
    passmd5 = hashlib.md5(password.encode())
    hexedpassmd5 = passmd5.hexdigest()
    print(hexedpassmd5)
    _firebase.put(url=("/users/"), name=(username), data=(hexedpassmd5))
    messagebox.showinfo("Notification", "Registered Successfully!")


def login_window():
    login_window = Tk()
    login_window.geometry("400x400")
    login_window.config(bg=_bg_)
    log_heading_label = Label(
        login_window, text="Log In", font='arial 18 bold', fg=_fg_, bg=_bg_)
    log_heading_label.place(relx=0.5, rely=0.2, anchor=CENTER)

    login_username_label = Label(
        login_window, text="Username : ", font='arial 13', fg=_fg_, bg=_bg_)
    login_username_label.place(relx=0.3, rely=0.4, anchor=CENTER)

    global login_username_entry
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

    login_password_label = Label(
        login_window, text="Password : ", font='arial 13', fg=_fg_, bg=_bg_)
    login_password_label.place(relx=0.3, rely=0.5, anchor=CENTER)

    global login_password_entry
    login_password_entry = Entry(login_window, show=__bullet_utf_8)
    login_password_entry.place(relx=0.6, rely=0.5, anchor=CENTER)

    btn_login = Button(login_window, text="Log In", font='arial 13 bold',
                       fg=_fg_, bg=_bg_, command=login, relief=FLAT)
    btn_login.place(relx=0.5, rely=0.65, anchor=CENTER)

    registration_window.destroy()
    login_window.mainloop()


heading_label = Label(registration_window, text="Register",
                      font='arial 18 bold', bg=_bg_, fg=_fg_)
heading_label.place(relx=0.5, rely=0.2, anchor=CENTER)

username_label = Label(registration_window,
                       text="Username : ", font='arial 13', bg=_bg_, fg=_fg_)
username_label.place(relx=0.3, rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

password_label = Label(registration_window,
                       text="Password :  ", font='arial 13', bg=_bg_, fg=_fg_)
password_label.place(relx=0.3, rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window, show=__bullet_utf_8)
password_entry.place(relx=0.6, rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up", font='arial 13 bold',
                 command=register, relief=FLAT, padx=10, bg=_bg_, fg=_fg_)
btn_reg.place(relx=0.5, rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In",
                          font='arial 10 bold',  command=login_window, relief=FLAT, bg=_bg_, fg=_fg_)

btn_login_window.place(relx=0.9, rely=0.06, anchor=CENTER)
registration_window.mainloop()
