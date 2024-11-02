from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os

class loginClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+70+50")
        self.root.title("INVENTORY MANAGEMENT SYSTEM LOGIN PAGE! Developed by Nadeem")
        self.root.config(bg="white")
        self.root.focus_force()

        # ------ Variables -------
        self.var_users_id = StringVar()
        self.var_users_name = StringVar()
        self.var_users_dob = StringVar()
        self.var_users_email = StringVar()
        self.var_users_contact = StringVar()
        self.var_users_gender = StringVar()
        self.var_users_password = StringVar()
        self.var_users_confirm_password = StringVar()
        self.var_users_type = StringVar()

        # ------- Signup Frame ------
        signup_frame = Frame(self.root, bd=4, relief=RIDGE, bg="lightyellow")
        signup_frame.place(x=120, y=100, width=1100, height=500)

        lbl_title = Label(signup_frame, text="Signup Page", font=("times new roman", 30, "bold"), bg="lightyellow").place(x=0, y=15, relwidth=1)

        # ------- Row 1 -------
        Label(signup_frame, text="User ID", font=("goudy old style", 15), bg="lightyellow").place(x=10, y=150)
        Label(signup_frame, text="Name", font=("goudy old style", 15), bg="lightyellow").place(x=350, y=150)
        Label(signup_frame, text="Date of Birth", font=("goudy old style", 15), bg="lightyellow").place(x=700, y=150)

        Entry(signup_frame, textvariable=self.var_users_id, font=("goudy old style", 15), bg="lightblue").place(x=110, y=150, width=180)
        Entry(signup_frame, textvariable=self.var_users_name, font=("goudy old style", 15), bg="lightblue").place(x=450, y=150, width=180)
        Entry(signup_frame, textvariable=self.var_users_dob, font=("goudy old style", 15), bg="lightblue").place(x=850, y=150, width=180)

        # ------- Row 2 -------
        Label(signup_frame, text="Email", font=("goudy old style", 15), bg="lightyellow").place(x=10, y=220)
        Label(signup_frame, text="Contact", font=("goudy old style", 15), bg="lightyellow").place(x=350, y=220)
        Label(signup_frame, text="Gender", font=("goudy old style", 15), bg="lightyellow").place(x=700, y=220)

        Entry(signup_frame, textvariable=self.var_users_email, font=("goudy old style", 15), bg="lightblue").place(x=110, y=220, width=180)
        Entry(signup_frame, textvariable=self.var_users_contact, font=("goudy old style", 15), bg="lightblue").place(x=450, y=220, width=180)
        
        cmb_gender = ttk.Combobox(signup_frame, textvariable=self.var_users_gender, values=("Select", "Male", "Female", "Other"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_gender.place(x=850, y=220, width=180)
        cmb_gender.current(0)

        # ------- Row 3 -------
        Label(signup_frame, text="Password", font=("goudy old style", 15), bg="lightyellow").place(x=10, y=290)
        Label(signup_frame, text="Confirm \nPassword", font=("goudy old style", 15), bg="lightyellow").place(x=340, y=275)
        Label(signup_frame, text="Type", font=("goudy old style", 15), bg="lightyellow").place(x=700, y=290)

        Entry(signup_frame, textvariable=self.var_users_password, show="*", font=("goudy old style", 15), bg="lightblue").place(x=110, y=290, width=180)
        Entry(signup_frame, textvariable=self.var_users_confirm_password, show="*", font=("goudy old style", 15), bg="lightblue").place(x=450, y=290, width=180)
        
        cmb_type = ttk.Combobox(signup_frame, textvariable=self.var_users_type, values=("Select", "Admin", "User"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_type.place(x=850, y=290, width=180)
        cmb_type.current(0)

        Button(signup_frame, text="Sign Up", font=("goudy old style", 20), command=self.signup, bg="green", fg="white", bd=4, relief=RIDGE, cursor="hand2").place(x=450, y=400, width=120, height=40)
        Button(signup_frame, text="Login", font=("goudy old style", 20), command=self.login, bg="blue", fg="white", bd=4, relief=RIDGE, cursor="hand2").place(x=590, y=400, width=120, height=40)

    def signup(self):
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()
        
        try:
            if (self.var_users_id.get() == "" or self.var_users_name.get() == "" or self.var_users_dob.get() == "" or self.var_users_email.get() == "" or self.var_users_contact.get() == "" or self.var_users_gender.get() == "" or self.var_users_password.get() == "" or self.var_users_confirm_password.get() == "" or self.var_users_type.get() == ""):
                messagebox.showerror("Error", "All Fields are Required.", parent=self.root)
            
            elif self.var_users_password.get() != self.var_users_confirm_password.get():
                messagebox.showerror("Error", "Password and Confirm Password do not match.", parent=self.root)
            
            else:
                c.execute("SELECT * FROM users WHERE user_id = ? OR email = ?", 
                          (self.var_users_id.get(), self.var_users_email.get()))
                existing_user = c.fetchone()

                if existing_user:
                    messagebox.showerror("Error", "User already exists. Please login instead.", parent=self.root)
                else:
                    c.execute("""INSERT INTO users (user_id, name, dob, email, contact, gender, password, type)
                                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                              (self.var_users_id.get(), self.var_users_name.get(), self.var_users_dob.get(), self.var_users_email.get(), self.var_users_contact.get(), self.var_users_gender.get(), self.var_users_password.get(), self.var_users_type.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Signup Successful. Please log in.", parent=self.root)
                    
                    self.root.destroy()
                    os.system("python login.py")



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def login(self):
        self.root.destroy()
        os.system("python login.py")




if __name__ == "__main__":
    root = Tk()
    obj = loginClass(root)
    root.mainloop()
