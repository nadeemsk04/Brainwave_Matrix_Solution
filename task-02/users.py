from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from tkinter import messagebox
import sqlite3


class usersClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+300+200")
        self.root.title("INVENTORY MANAGEMENT SYSTEM! Developed by Nadeem")
        self.root.config(bg="white")
        self.root.focus_force()


         # -----------------------------------------------------
        # ------- All variables --------
        self.var_search_by=StringVar()
        self.var_search_text=StringVar()
        


        self.var_users_id=StringVar()
        self.var_users_name=StringVar()
        self.var_users_dob=StringVar()
        self.var_users_email=StringVar()
        self.var_users_contact=StringVar()
        self.var_users_gender=StringVar()
        self.var_users_password=StringVar()
        self.var_users_confirm_password=StringVar()        
        self.var_users_type=StringVar()



        # ------ Search Frame -----
        searchFrame=LabelFrame(self.root, text="Search Users", font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchFrame.place(x=250,y=0,width=600,height=70)


        # ----- Options ------
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_search_by,values=("Seclect", "Name", "Email", "Contact","USER ID"), state="readonly", justify=CENTER, font=("goudy old style",12))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchFrame,textvariable=self.var_search_text,font=("goudy old style",15),bg="lightyellow").place(x=200, y=10)
        btn_search=Button(searchFrame,text="Search", command=self.search, font=("goudy old style",15),bg="#4caf50", fg="white", cursor="hand2").place(x=430, y=8,width=150, height=30)
        


        # ------ Title -----
        title=Label(self.root, text="User Details", bd=4, relief=RIDGE, font=("goudy old style",15), bg="green", fg="white").place(x=50, y=100, width=1000)


        # ------- Conatent ------
        # ------- Row 1 -------
        lbl_userid=Label(self.root, text="User ID", font=("goudy old style",10), bg="white").place(x=30, y=150)
        lbl_username=Label(self.root, text="Name", font=("goudy old style",10), bg="white").place(x=350, y=150)
        lbl_userdob=Label(self.root, text="Date of Birth", font=("goudy old style",10), bg="white").place(x=700, y=150)
       

        txt_userid=Entry(self.root, textvariable=self.var_users_id, font=("goudy old style",13), bg="lightblue").place(x=100, y=150, width=180)
        txt_username=Entry(self.root, textvariable=self.var_users_name, font=("goudy old style",13), bg="lightblue").place(x=450, y=150, width=180)
        txt_userdob=Entry(self.root, textvariable=self.var_users_dob, font=("goudy old style",13), bg="lightblue").place(x=850, y=150, width=180)

        # ------- Row 2 -------
        lbl_useremail=Label(self.root, text="Email", font=("goudy old style",10), bg="white").place(x=30, y=190)
        lbl_usercontact=Label(self.root, text="Conatct", font=("goudy old style",10), bg="white").place(x=350, y=190)
        lbl_usergender=Label(self.root, text="Gender", font=("goudy old style",10), bg="white").place(x=700, y=190)
       

        txt_useremail=Entry(self.root, textvariable=self.var_users_email, font=("goudy old style",13), bg="lightblue").place(x=100, y=190, width=180)
        txt_usercontact=Entry(self.root, textvariable=self.var_users_contact, font=("goudy old style",13), bg="lightblue").place(x=450, y=190, width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_users_gender,values=("Seclect", "Male", "Female", "Other"), state="readonly", justify=CENTER, font=("goudy old style",13))
        cmb_gender.place(x=850, y=190, width=180)
        cmb_gender.current(0)


        # ------- Row 3 -------
        lbl_userpaswword=Label(self.root, text="Password", font=("goudy old style",10), bg="white").place(x=30, y=230)
        lbl_userconfirmpassword=Label(self.root, text="Confirm\nPassword", font=("goudy old style",10), bg="white").place(x=350, y=230)
        lbl_usertype=Label(self.root, text="Type", font=("goudy old style",10), bg="white").place(x=700, y=230)
       

        txt_userpasword=Entry(self.root, textvariable=self.var_users_password, font=("goudy old style",13), bg="lightblue").place(x=100, y=230, width=180)
        txt_userconfirmpassword=Entry(self.root, textvariable=self.var_users_confirm_password,show="*", font=("goudy old style",13), bg="lightblue").place(x=450, y=230, width=180)
        cmb_type=ttk.Combobox(self.root,textvariable=self.var_users_type,values=("Seclect", "Admin", "User"), state="readonly", justify=CENTER, font=("goudy old style",13))
        cmb_type.place(x=850, y=230, width=180)
        cmb_type.current(0)


        # ------- Buttons -------
        btn_add = Button(self.root, text="ADD", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", activebackground="#2196f3", activeforeground="white", cursor="hand2").place(x=500, y=275, width=110, height=30)
        btn_update = Button(self.root, text="Update", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", activebackground="#4caf50", activeforeground="white", cursor="hand2").place(x=620, y=275, width=110, height=30)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", activebackground="#f44336", activeforeground="white", cursor="hand2").place(x=740, y=275, width=110, height=30)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", activebackground="#607d8b", activeforeground="white", cursor="hand2").place(x=860, y=275, width=110, height=30)




        # ------ User Details -------
        # Create a style for the Treeview
        style = ttk.Style()
        style.configure("Treeview.Heading",
                        background="lightblue",
                        foreground="black",
                        font=("goudy old style", 10, "bold"),
                        relief="solid",
                        borderwidth=1)
        

        user_frame=Frame(self.root,bd=4, relief=RIDGE)
        user_frame.place(x=0, y=312, relwidth=1, height=185)

        scrolly=Scrollbar(user_frame,orient=VERTICAL)
        scrollx=Scrollbar(user_frame,orient=HORIZONTAL)

        self.userTable=ttk.Treeview(user_frame,columns=("user_id", "name", "dob", "email", "contact", "gender", "password", "type"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.userTable.xview)
        scrolly.config(command=self.userTable.yview)


        self.userTable.heading("user_id",text="User ID")
        self.userTable.heading("name",text="Name")
        self.userTable.heading("dob",text="Date of Birth")
        self.userTable.heading("email",text="Email")
        self.userTable.heading("contact",text="Contact")
        self.userTable.heading("gender",text="Gender")
        self.userTable.heading("password",text="Password")
        self.userTable.heading("type",text="User Type")

        self.userTable["show"]="headings"

        self.userTable.column("user_id", width=150)
        self.userTable.column("name", width=150)
        self.userTable.column("dob", width=150)
        self.userTable.column("email", width=150)
        self.userTable.column("contact", width=150)
        self.userTable.column("gender", width=150)
        self.userTable.column("password", width=150)
        self.userTable.column("type", width=150)
        
        self.userTable.pack(fill=BOTH, expand=1)
        self.userTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()


   
# -----------------------------------------------------------------------
    def add(self):
        password = self.var_users_password.get()
        confirm_password = self.var_users_confirm_password.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!", parent=self.root)
            return

        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            if self.var_users_id.get() == "":
                messagebox.showerror("Error", "User ID must be required", parent=self.root)
            else:
                c.execute("Select * from users where user_id=?", (self.var_users_id.get(),))
                row = c.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "This User ID is already assigned, try different.", parent=self.root)
                else:
                    c.execute("Insert into users (user_id, name, dob, email, contact, gender, password, type) values(?, ?, ?, ?, ?, ?, ?, ?)", (
                        self.var_users_id.get(),
                        self.var_users_name.get(),
                        self.var_users_dob.get(),
                        self.var_users_email.get(),
                        self.var_users_contact.get(),
                        self.var_users_gender.get(),
                        self.var_users_password.get(),
                        self.var_users_type.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "User Added Successfully", parent=self.root)

                    self.show()

        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)




    def show(self):
        con=sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            c.execute("Select * from users")
            rows=c.fetchall()
            self.userTable.delete(*self.userTable.get_children())

            for row in rows:
                self.userTable.insert("", END, values=row)
            


        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)



    def get_data(self,ev):
        f=self.userTable.focus()
        content=(self.userTable.item(f))
        row=content["values"]
        self.var_users_id.set(row[0]),
        self.var_users_name.set(row[1]),
        self.var_users_dob.set(row[2]),
        self.var_users_email.set(row[3]),
        self.var_users_contact.set(row[4]),
        self.var_users_gender.set(row[5]),
        self.var_users_password.set(row[6]),
        self.var_users_confirm_password.set(row[6]),
        self.var_users_type.set(row[7])




    def update(self):
        password = self.var_users_password.get()
        confirm_password = self.var_users_confirm_password.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!", parent=self.root)
            return

        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            if self.var_users_id.get() == "":
                messagebox.showerror("Error", "User ID must be required", parent=self.root)
            else:
                c.execute("Select * from users where user_id=?", (self.var_users_id.get(),))
                row = c.fetchone()

                if row == None:
                    messagebox.showerror("Error", " Invalid User ID.", parent=self.root)
                else:
                    c.execute("Update users set name=?, dob=?, email=?, contact=?, gender=?, password=?, type=?  where user_id=?", (
                        self.var_users_name.get(),
                        self.var_users_dob.get(),
                        self.var_users_email.get(),
                        self.var_users_contact.get(),
                        self.var_users_gender.get(),
                        self.var_users_password.get(),
                        self.var_users_type.get(),
                        self.var_users_id.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success", "User Updated Successfully", parent=self.root)

                    self.show()

        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)





    def delete(self):
        password = self.var_users_password.get()
        confirm_password = self.var_users_confirm_password.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!", parent=self.root)
            return

        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            if self.var_users_id.get() == "":
                messagebox.showerror("Error", "User ID must be required", parent=self.root)
            else:
                c.execute("Select * from users where user_id=?", (self.var_users_id.get(),))
                row = c.fetchone()

                if row == None:
                    messagebox.showerror("Error", " Invalid User ID.", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you want to delete?", parent=self.root)
                    if op == True:

                        c.execute("delete from users where user_id=?",(self.var_users_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "User Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)



    def clear(self):
        self.var_users_id.set(""),
        self.var_users_name.set(""),
        self.var_users_dob.set(""),
        self.var_users_email.set(""),
        self.var_users_contact.set(""),
        self.var_users_gender.set("Select"),
        self.var_users_password.set(""),
        self.var_users_confirm_password.set(""),
        self.var_users_type.set("Select")
        self.show()



    def search(self):
        con=sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            if self.var_search_by.get()=="Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self.root)
            elif self.var_search_text.get()=="":
                messagebox.showerror("Error", "Search Input Should Be Required.", parent=self.root)
            else:
                c.execute("Select * from users where "+self.var_search_by.get()+" LIKE '%"+self.var_search_text.get()+"%'")
                rows=c.fetchall()
                if len(rows) != 0:
                    self.userTable.delete(*self.userTable.get_children())

                    for row in rows:
                        self.userTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "NO Record Found.", parent=self.root)

            


        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)









if __name__=="__main__":
    root = Tk()
    obj = usersClass(root)
    root.mainloop()




