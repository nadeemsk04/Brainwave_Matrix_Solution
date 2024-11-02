# ------- All Functions -------


#         def signup(self):
#                 con = sqlite3.connect(database=r"inventory.db")
#                 c = con.cursor()

#                 try:
#                         # Check if all fields are filled
#                         if (self.user_id.get() == "" or self.user_name.get() == "" or self.user_dob.get() == "" or self.user_email.get() == "" or self.user_contact.get() == "" or self.user_gender.get() == "" or self.user_password.get() == "" or self.user_confirm_password.get() == "" or self.user_type.get() == ""):
#                                 messagebox.showerror("Error", "All Fields are Required.", parent=self.root)
                        
#                         # Check if password and confirm password match
#                         elif self.user_password.get() != self.user_confirm_password.get():
#                                 messagebox.showerror("Error", "Password and Confirm Password do not match.", parent=self.root)
                        
#                         else:
#                         # Check if user already exists
#                                 c.execute("SELECT * FROM users WHERE user_id = ? OR email = ?",(self.user_id.get(), self.user_email.get()))
#                                 existing_user = c.fetchone()

#                                 if existing_user:
#                                         messagebox.showerror("Error", "User already exists. Please login instead.", parent=self.root)
#                                 else:
#                                 # Insert new user into the database
#                                         c.execute("""INSERT INTO users (user_id, name, dob, email, contact, gender, password, type)
#                                         VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
#                                         (self.user_id.get(), self.user_name.get(), self.user_dob.get(), self.user_email.get(),self.user_contact.get(), self.user_gender.get(), self.user_password.get(), self.user_type.get()))
                                
#                                         con.commit()
#                                         messagebox.showinfo("Success", "Signup Successful. Please log in.", parent=self.root)
                                
#                 except Exception as ex:
#                         messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
                
#                 finally:
#                         con.close()

