from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os
import email_pass
import smtplib
import time


class loginClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+70+50")
        self.root.title("INVENTORY MANAGEMENT SYSTEM LOGIN PAGE! Developed by Nadeem")
        self.root.config(bg="white")
        self.root.focus_force()

        self.user_id = StringVar()
        self.user_password = StringVar()

        self.otp=""

        # ------- Login Frame ------
        login_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        login_frame.place(x=500, y=80, width=380, height=450)

        lbl_title = Label(login_frame, text="Login Page", font=("Elephant", 30, "bold"), bg="white").place(x=0, y=30, relwidth=1)

        lbl_userid = Label(login_frame, text="Enter Username", font=("Andalus", 15), bg="white").place(x=30, y=100)
        txt_userid = Entry(login_frame, textvariable=self.user_id, font=("goudy old style", 18), bd=4, relief=RIDGE, bg="lightblue").place(x=30, y=130, width=300)

        lbl_password = Label(login_frame, text="Enter Password", font=("Andalus", 15), bg="white").place(x=30, y=180)
        txt_password = Entry(login_frame, textvariable=self.user_password, font=("goudy old style", 18), bd=4, relief=RIDGE, bg="lightblue", show='*').place(x=30, y=210, width=300)


        btn_login = Button(login_frame, text="LOGIN", font=("goudy old style", 18, "bold"),command=self.login, bg="green", activebackground="green", activeforeground="white", fg="white", bd=4, relief=RIDGE, cursor="hand2").place(x=30, y=280, width=300, height=40)


        hr=Label(login_frame,bg="lightgray").place(x=30, y=340, width=300, height=5)
        oR=Label(login_frame, text="OR", bg="white", font=("old goudy style", 15, "bold")).place(x=150, y=330)


        btn_forget_password=Button(login_frame,text="Forget Password", command=self.forget_password, font=("times new roman", 15), bg="white", fg="blue", bd=0, activebackground="white", activeforeground="blue", cursor="hand2").place(x=100, y=360)


        # ------ SignUp Frame -------
        signup_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        signup_frame.place(x=500, y=540, width=380, height=60)

        lbl_dont_account=Label(signup_frame, text="Don't have an Account?", font=("times new roman", 15), bg="white", fg="red").place(x=50, y=15)
        btn_signup=Button(signup_frame, text="SignUp", command=self.signup, font=("times new roman", 16), bg="white", fg="green", activebackground="white", activeforeground="green", cursor="hand2", bd=0).place(x=238, y=11)

    # ------- All Functions -------

    def login(self):
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            if self.user_id.get()=="" or self.user_password.get()=="":
                messagebox.showerror("Error", "All Fields are Required.", parent=self.root)
            else:
                c.execute("select type from users where user_id=? AND password=?",(self.user_id.get(), self.user_password.get()))
                user=c.fetchone()
                if user == None:
                        messagebox.showerror("Error", "Invalid User ID / Password.", parent=self.root)
                else:
                    if user[0] =="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
                    
        
        
        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)



    def forget_password(self):
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            if self.user_id.get()=="":
                messagebox.showerror("Error", "User ID must be required", parent=self.root)
            else:
                c.execute("select email from users where user_id=? ",(self.user_id.get(),))
                email=c.fetchone()
                if email == None:
                        messagebox.showerror("Error", "Invalid User ID. TRY Again!", parent=self.root)
                else:
                    # ------ Forget Window -------
                    self.var_otp=StringVar()
                    self.var_new_password=StringVar()
                    self.var_confirmed_password=StringVar()

                    # call send_email_function()
                    chk = self.send_email(email[0])
                    if chk == "f":
                        messagebox.showerror("Error", "Connection Error, Try Again!",parent=self.root)
                    else:

                        self.forget_pass=Toplevel(self.root)
                        self.forget_pass.title("RESET PASSWORD")
                        self.forget_pass.geometry("550x480+450+120")
                        self.forget_pass.focus_force()

                        lbl_title=Label(self.forget_pass, text="RESET PASSWORD", font=("times new roman", 20, "bold"), bg="#3f51b5", fg="white").pack(side=TOP, fill=X)


                        lbl_reset=Label(self.forget_pass, text="Enter OTP. Sent on Regisered Email", font=("times new roman", 15)).place(x=20, y=60)
                        txt_reset=Entry(self.forget_pass, textvariable=self.var_otp, font=("times new roman", 15), bg="lightblue").place(x=20, y=100, width=250,height=28)

                        lbl_line=Label(self.forget_pass, text="-"*100, font=("times new roman",15)).pack(pady=150, fill=X)



                        lbl_new_password=Label(self.forget_pass, text="NEW Password:", font=("times new roman", 15)).place(x=20, y=250)
                        txt_reset=Entry(self.forget_pass, textvariable=self.var_new_password, font=("times new roman", 15), bg="lightblue").place(x=20, y=280, width=250, height=28)


                        lbl_confirmed_password=Label(self.forget_pass, text="Confirm Password:", font=("times new roman", 15)).place(x=20, y=320)
                        txt_confirmed_password=Entry(self.forget_pass, textvariable=self.var_confirmed_password, font=("times new roman", 15), bg="lightblue").place(x=20, y=350, width=250, height=28)


                        self.btn_reset=Button(self.forget_pass, command=self.verify_otp, text="SUBMIT", font=("times new roman", 15), bg="red", fg="white", activebackground="red", activeforeground="white", cursor="hand2")
                        self.btn_reset.place(x=400, y=100, width=100, height=28)

                        self.btn_update=Button(self.forget_pass, command=self.update_password, text="Update", font=("times new roman", 15), state=DISABLED, bg="green", fg="white", activebackground="green", activeforeground="white", cursor="hand2")
                        self.btn_update.place(x=400, y=400, width=100, height=28)


        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)



    def verify_otp(self):
        # Check if the OTP entry is empty
        otp_entered = self.var_otp.get()
        if not otp_entered:
            messagebox.showerror("Error", "Please enter the OTP.", parent=self.forget_pass)
            return

        # Compare the entered OTP with the generated one
        try:
            if int(self.otp) == int(otp_entered):
                self.btn_update.config(state=NORMAL)
                self.btn_reset.config(state=DISABLED)
                messagebox.showinfo("Success", "OTP verified successfully!", parent=self.forget_pass)
            else:
                messagebox.showerror("Error", "Invalid OTP. Try Again!", parent=self.forget_pass)
        except ValueError:
            messagebox.showerror("Error", "Invalid OTP format. Please enter numeric OTP.", parent=self.forget_pass)


    def update_password(self):
        if self.var_new_password.get()=="" or self.var_confirmed_password.get()=="":
            messagebox.showerror("Error", "All Fields are Required", parent=self.forget_pass)
        elif self.var_new_password.get() != self.var_confirmed_password.get():
            messagebox.showerror("Error", "Password & Confirm Password Does Not Mch", parent=self.forget_pass)
        else:
            con = sqlite3.connect(database=r"inventory.db")
            c = con.cursor()

            try:
                c.execute("Update users SET password=? where user_id=?", (self.var_new_password.get(), self.user_id.get()))
                con.commit()
                messagebox.showinfo("Success", "Your Password Changed Successfully.")
                
                self.forget_pass.destroy()

            except Exception as ex:
                messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.forget_pass)


            

    




    def send_email(self, to_):
        try:
            # Initialize the SMTP connection
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
            
            # Login with credentials
            email_ = email_pass.email_
            pass_ = email_pass.pass_
            s.login(email_, pass_)
            
            # Generate OTP
            self.otp = int(time.strftime("%H%S%M")) + int(time.strftime("%S"))
            
            # Compose the message
            subject = "IMS-Reset Password OTP"
            msg = f"Dear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nWith Regards,\nIMS Developer Nadeem"
            msg = "Subject:{}\n\n{}".format(subject, msg)
            
            # Send the email
            s.sendmail(email_, to_, msg)
            
            # Close the connection
            s.quit()
            
            return "s"  # Success
        except smtplib.SMTPException as e:
            return "f"  # Failure

    






    def signup(self):
        self.root.destroy()
        os.system("python signup.py")










if __name__ == "__main__":
    root = Tk()
    obj = loginClass(root)
    root.mainloop()

