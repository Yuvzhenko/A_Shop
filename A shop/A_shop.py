import tkinter as tk
from tkinter import messagebox
import pymysql

class ShopLogin():
    def __init__(self, root):
        self.root = root
        self.root.title("Shop Login")
        self.root.geometry("600x400")
        self.root.configure(bg="#111111")

        self.is_logged_in = False
        self.currentID = None
        self.tries = 3

        self.frame = tk.Frame(self.root, bg="#141414", bd=0)
        self.frame.pack(expand=True)

        self.name = tk.Label(self.frame, text="UserName:", bg="#141414", fg="white", width=10, height=2)
        self.name.grid(row=0, column=0)
        self.enterName = tk.Entry(self.frame, bg="#141414", fg="#f3951d", insertbackground="#f3951d", bd=2)
        self.enterName.grid(row=0, column=1, padx=(5, 10))

        self.password = tk.Label(self.frame, text="Password:", bg="#141414", fg="white", width=10, height=2)
        self.password.grid(row=1, column=0)
        self.enterPass = tk.Entry(self.frame, show='*', bg="#141414", fg="#f3951d", insertbackground="#f3951d", bd=2)
        self.enterPass.grid(row=1, column=1, padx=(5, 10))

        self.signIn_bt = tk.Button(self.frame, text="Sign In", bg="#f3951d", activebackground="#f3951d", command=self.signIn, width=10)
        self.signIn_bt.grid(row=3, column=0, padx=10, pady=20)

        self.reg_bt = tk.Button(self.frame, text="Register", bg="#f3951d", activebackground="#f3951d", command=self.register, width=10)
        self.reg_bt.grid(row=3, column=1, padx=10, pady=20)

    def signIn(self):
        if self.tries < 1:
            messagebox.showerror("Error", "You are out of tries\nTry again later")
            return

        userName = self.enterName.get()
        password = self.enterPass.get()

        con = pymysql.connect(host="localhost", user="root", password="", database="shop")
        cur = con.cursor()

        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cur.execute(query, (userName, password))

        user_data = cur.fetchone()

        if user_data:
            messagebox.showinfo("Success", "You successfuly entered your account")
            self.currentID = user_data[0]
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
            con = pymysql.connect(host="localhost", user="root", password="", database="shop")
            cur = con.cursor()

            query = "INSERT INTO users(username, password) VALUES(%s, %s)"
            cur.execute(query, (userName, password))
            con.commit()

            cur.execute("SELECT LAST_INSERT_ID()")
            self.currentID = cur.fetchone()[0]

            messagebox.showinfo("Success", "You successfuly registered!")
            self.tries = 3
            
        except pymysql.err.IntegrityError:
            messagebox.showerror("Error", "The password is already in use")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")
        finally:
            if 'con' in locals() and con.open:
                con.close()

class ShopMenu():
    def __init__(self, root, currentID):
        self.root = root
        self.root.title("Shop")
        self.root.geometry("800x400")
        self.root.configure(bg="#141414")

        self.cart = {}
        self.purchase_costs = 0
        
        con = pymysql.connect(host="localhost", user="root", password="", database="shop")
        cur = con.cursor()

        query = "SELECT balance FROM users WHERE ID = %s"
        cur.execute(query, (currentID,))
        
        result = cur.fetchone()
        self.balance_amount = result[0]

        cur.execute("SELECT DISTINCT category FROM products")
        self.categories = [row[0] for row in cur.fetchall()]

        con.close()

        self.products_frame = tk.Frame(self.root, bg="#141414")
        self.products_frame.place(anchor="center", x=400, y=160)

        self.logo_frame = tk.Frame(self.root, bg="#141414")
        self.logo_frame.place(x=100, y=50, anchor="center")

        self.logo = tk.Label(self.logo_frame, text="DELIVERY", bg="#141414", fg="white", font=("Arial black", 24))
        self.logo.pack()

        self.categories_frame = tk.Frame(self.root, bg="#141414")
        self.categories_frame.place(anchor="center", x=100, y=230)

        self.column_count = 2

        for index, name in enumerate(self.categories):
            lambda name=name:self.open_category(name)
            btn = tk.Button(self.categories_frame, text=name, bg="#141414", fg="white",
                             activebackground="#141414", activeforeground="white", bd=0, font=("Arial", 11),
                             command=lambda n= name: self.open_category(n))

            r = index // self.column_count
            c = index % self.column_count

            btn.grid(row=r, column=c, padx=10, pady=10, sticky="ew")
        
        self.cartFrame = tk.Frame(self.root, bg="#141414")
        self.cartFrame.place(anchor="center", x=730, y=50)

        self.cartButton = tk.Button(self.cartFrame, text="cart", bg="#141414", fg="#f3951d",
                                    activebackground="#141414", activeforeground="#f3951d",
                                    font=("Arial", 15, "bold"), bd=0, command=self.cartFunc)
        self.cartButton.pack()

        self.balance_lable = tk.Label(self.cartFrame, text=f"Balance: ${self.balance_amount}", font=("Arial", 12),
                                      bg="#141414", fg="#f3951d")
        self.balance_lable.pack(pady=10)

        self.replenishment_button = tk.Button(self.cartFrame, text="+", font=("Arial", 10), bd=0, bg="#141414", fg="#f3951d",
                                              activebackground="#141414", activeforeground="#f3951d",
                                              command=self.replenish_balance)
        self.replenishment_button.pack()


    def open_category(self, category_name):

        for widget in self.products_frame.winfo_children():
            widget.destroy()

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="shop")
            cur = con.cursor()

            query = "SELECT name, price, remains, category FROM products WHERE category = %s"
            cur.execute(query, category_name)

            products = cur.fetchall()

            con.close()

            tk.Label(self.products_frame, text=f"Category: {category_name}", fg="white", bg="#141414",
                      font=("Arial", 14, "bold")).grid(row=0, column=0)
            if not products:
                tk.Label(self.products_frame, text="No products avalible", bg="#141414", fg="white").grid(row=1, column=0)
                return
            r = 2
            for product in products:
                p_name = product[0]
                p_price = product[1]
                p_remains = product[2]

                item_lable = tk.Label(self.products_frame, text=p_name, font=("Arial", 15),
                                      bg="#141414", fg="white", anchor="w")
                item_lable.grid(row= r, column=0, padx=100, pady=2)
                if p_remains > 0:
                    item_addToCart_button = tk.Button(self.products_frame, text=f"Buy for {p_price}$", bg="#f3951d", activebackground="#f3951d",
                                               command=lambda p=product: self.addToCart_button_func(p))
                    item_addToCart_button.grid(row=r, column=1)
                else:
                    item_addToCart_button = tk.Button(self.products_frame, text=f"ran out", bg="gray", state="disabled")
                    item_addToCart_button.grid(row=r, column=1)
                r += 1

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:{e}")

    def cartFunc(self):
        for widget in self.products_frame.winfo_children():
            widget.destroy()

        if not self.cart:
            tk.Label(self.products_frame, text="Cart is empty", bg="#141414", fg="white",
                      font=("Arial", 15)).grid(row=1, column=0)
            return

        r = 2
        for product, info in self.cart.items():
            amount = info['qty']
            price = info['price']

            item_lable = tk.Label(self.products_frame, text=f"{product} | Price: {price * amount}$ | Amount: {amount}",
                                   font=("Arial", 12), bg="#141414", fg="white", anchor="w")
            item_lable.grid(row= r, column=0, padx=100, pady=2)

            item_minus_button = tk.Button(self.products_frame, text="—", font=("Arial", 12, "bold"),
                                         bg="#800807", fg="white", activebackground="#800807", activeforeground="white", bd=0,
                                         command=lambda p=product: self.modify_cart(p, -1))
            item_minus_button.grid(row=r, column=1, pady=2)

            r += 1

        self.buyButton = tk.Button(self.products_frame, text=f"Buy for {self.purchase_costs}$", bg="#f3951d", activebackground="#f3951d",
                                    font=("Arial black", 12), command=self.buy_button_function)
        self.buyButton.grid(row=r, column=0, pady=15)

    def modify_cart(self, product, change):
        if product not in self.cart:
            return

        current_qty = self.cart[product]['qty']
        p_price = self.cart[product]['price']

        new_qty = current_qty + change

        if new_qty <= 0:
            self.purchase_costs -= p_price * current_qty
            del self.cart[product]
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="shop")
            cur = con.cursor()

            query = "SELECT remains FROM products WHERE name = %s"
            cur.execute(query, (product,))
            result = cur.fetchone()
            con.close()

            if result and new_qty > result[0]:
                messagebox.showerror("Error", "No more items of this product are available")
                return

            self.cart[product]['qty'] = new_qty
            self.purchase_costs += p_price * change

        self.cartFunc()

    def buy_button_function(self):
        if self.purchase_costs > self.balance_amount:
            messagebox.showerror("Error", "You don't have enough money to make this purchase")
            return
        self.balance_amount -= self.purchase_costs
        self.balance_lable.config(text=f"Balance: ${self.balance_amount}")

        con = pymysql.connect(host="localhost", user="root", password="", database="shop")
        cur = con.cursor()
        for product, info in self.cart.items():
            p_name = product
            p_qty = info['qty']

            query = "UPDATE products SET remains = remains - %s WHERE name = %s"
            cur.execute(query, (p_qty, p_name))

        query = "UPDATE users SET balance = %s WHERE ID = %s"
        cur.execute(query, (self.balance_amount, currentID))
        con.commit()

        query = "INSERT INTO sellingHystory(customerID, productName, quantity, categoryName, price) VALUES(%s, %s, %s, %s, %s)"
        for product, info in self.cart.items():
            p_name = product
            p_qty = info['qty']
            p_category = info['category']
            p_price = info['price']

            cur.execute(query, (currentID, p_name, p_qty, p_category, p_price * p_qty))
        con.commit()

        con.close()

        self.purchase_costs = 0
        self.cart.clear()
        self.cartFunc()

    def addToCart_button_func(self, product):
        p_name = product[0]
        p_price = product[1]
        p_remains = product[2]
        p_category = product[3]

        qnt_in_cart = 0
        if p_name in self.cart:
            qnt_in_cart = self.cart[p_name]['qty']

        if qnt_in_cart + 1 > p_remains:
            messagebox.showerror("Error", "No more items of this product are available")
            return

        if p_name in self.cart:
            self.cart[p_name]['qty'] += 1
        else:
            self.cart[p_name] = {'price': p_price, 'category': p_category, 'qty': 1}
        
        self.purchase_costs += p_price

    def replenish_balance(self):
        def add_balance():
            try:
                amount = int(entry.get())
                if amount <= 0:
                    raise ValueError("Amount must be positive")
                self.balance_amount += amount
                self.balance_lable.config(text=f"Balance: ${self.balance_amount}")
                try:
                    con = pymysql.connect(host="localhost", user="root", password="", database="shop")
                    cur = con.cursor()

                    query = "UPDATE users SET balance = %s WHERE ID = %s"
                    cur.execute(query, (self.balance_amount, currentID))
                    con.commit()
                    con.close()

                    top.destroy()
                    
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to update balance in database: {e}")
            except ValueError as ve:
                messagebox.showerror("Error", f"Invalid amount: {ve}")

        top = tk.Toplevel(self.root)
        top.title("Replenish Balance")
        top.geometry("300x150")
        top.configure(bg="#141414")

        label = tk.Label(top, text="Enter amount to add:", bg="#141414", fg="white")
        label.pack(pady=10)

        entry = tk.Entry(top, bg="#141414", fg="#f3951d", insertbackground="#f3951d", bd=2)
        entry.pack(pady=5)

        add_button = tk.Button(top, text="Add", bg="#f3951d", activebackground="#f3951d", bd=0, command=add_balance)
        add_button.pack(pady=10)
        

if __name__ == "__main__":
    root = tk.Tk()
    logging_window = ShopLogin(root)
    root.mainloop()
    del root

    if logging_window.is_logged_in:
        currentID = logging_window.currentID

        root = tk.Tk()
        shop_window = ShopMenu(root, currentID)
        root.mainloop()
        
    
