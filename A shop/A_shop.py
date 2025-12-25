import tkinter as tk
from tkinter import messagebox
import pymysql

class ShopLogin():
    def __init__(self, root):
        self.root = root
        self.is_logged_in = False
        self.root.title("Shop Login")
        self.root.geometry("600x400")

        self.tries = 3

        self.frame = tk.Frame(self.root, bg="light grey", bd=0)
        self.frame.pack(expand=True)

        self.name = tk.Label(self.frame, text="UserName:", bg="light grey", width=10, height=2)
        self.name.grid(row=0, column=0)
        self.enterName = tk.Entry(self.frame, bd= 1)
        self.enterName.grid(row=0, column=1, padx=(5, 10))

        self.password = tk.Label(self.frame, text="Password:", bg="light grey", width=10, height=2)
        self.password.grid(row=1, column=0)
        self.enterPass = tk.Entry(self.frame, show='*')
        self.enterPass.grid(row=1, column=1, padx=(5, 10))

        self.signIn_bt = tk.Button(self.frame, text="Sign In", command=self.signIn, width=10)
        self.signIn_bt.grid(row=3, column=0, padx=10, pady=20)

        self.reg_bt = tk.Button(self.frame, text="Register", command=self.register, width=10)
        self.reg_bt.grid(row=3, column=1, padx=10, pady=20)

    def signIn(self):
        if self.tries < 1:
            messagebox.showerror("Error", "You are out of tries\nTry again later")
            return

        userName = self.enterName.get()
        password = self.enterPass.get()

        con = pymysql.connect(host="localhost", user="root", password="", database="shop users")
        cur = con.cursor()

        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cur.execute(query, (userName, password))

        if cur.fetchone():
            messagebox.showinfo("Success", "You successfuly entered your account")
            con.close()
            self.is_logged_in = True
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Incorrect Username or Password.\nTry again")
            self.tries -= 1

        con.close()

        

    def register(self):
        userName = self.enterName.get()
        password = self.enterPass.get()

        if not userName or not password:
            messagebox.showerror("Error", "You must fill both username and password")
            return
        
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="shop users")
            cur = con.cursor()

            query = "INSERT INTO users(username, password) VALUES(%s, %s)"
            cur.execute(query, (userName, password))
            con.commit()

            messagebox.showinfo("Success", "You successfuly registered!")
            self.tries = 3
            
        except pymysql.err.IntegrityError:
            messagebox.showerror("Error", "The password is already in use")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")
        finally:
            if 'con' in locals() and con.open:
                con.close()

        con.close()

class ShopMenu():
    def __init__(self, root):
        self.root = root
        self.root.title("Shop")
        self.root.geometry("600x400")

        self.logo_frame = tk.Frame(self.root)
        self.logo_frame.place(x=100, y=50, anchor="center")

        self.logo = tk.Label(self.logo_frame, text="DELIVERY", font=("Arial black", 24))
        self.logo.pack()

        self.categories_frame = tk.Frame(self.root)
        self.categories_frame.place(anchor="center", x=100, y=230)
        
        self.categories = [
            "Drinks", "Snacks", "Alcohol", 
            "Cigarette", "Ice Cream", "Papers", 
            "AutoChem", "Hats", "Glasses", 
            "Plush toys", "Donuts", "Toys"
        ]
        self.column_count = 2

        for index, name in enumerate(self.categories):
            lambda name=name:self.open_category(name)
            btn = tk.Button(self.categories_frame, text=name, bd=0, font=("Arial", 11),
                             command=lambda n= name: self.open_category(n))

            r = index // self.column_count
            c = index % self.column_count

            btn.grid(row=r, column=c, padx=10, pady=10, sticky="ew")

    def open_category(self, category_name):
        pass

        
if __name__ == "__main__":
    '''root = tk.Tk()
    logging_window = ShopLogin(root)
    root.mainloop()
    del root

    if logging_window.is_logged_in:
        root = tk.Tk()
        shop_window = ShopMenu(root)
        root.mainloop()
    '''
    root = tk.Tk()
    shop_window = ShopMenu(root)
    root.mainloop()
