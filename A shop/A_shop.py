import tkinter as tk
import pymysql

class ShopLogin():
    def __init__(self, root):
        self.root = root
        self.root.title("Shop Application")
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
        self.enterPass = tk.Entry(self.frame)
        self.enterPass.grid(row=1, column=1, padx=(5, 10))

        self.signIn_bt = tk.Button(self.frame, text="Sign In", command=self.signIn, width=10)
        self.signIn_bt.grid(row=3, column=0, padx=10, pady=20)

        self.reg_bt = tk.Button(self.frame, text="Register", command=self.register, width=10)
        self.reg_bt.grid(row=3, column=1, padx=10, pady=20)

    def signIn(self):
        userName = self.enterName.get()
        password = self.password.get()

        signedIn = False
        pass

    def register(self):
        pass

    def logMessage(self, message, color):
        pass
root = tk.Tk()
obj = ShopLogin(root)
root.mainloop()

