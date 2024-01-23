import customtkinter as ct
from tkinter import ttk ,Tk ,messagebox ,PhotoImage
import json
from configs import icon_path
#
#
class Login(ct.CTk):
    with open('pass.json', mode='r') as f:
        user_pass = f.read()
        user_pass = json.loads(user_pass)

    def __init__(self):
        super().__init__()
        self.login_ui()

    def login_ui(self):
        self.title("اپلیکیشن حسابداری")
        self.geometry("700x300+100+50")
        self.resizable(False, False)
        self.configure(bg='#292e2e')
        self.iconbitmap(fr"{icon_path}")


        def login_logic(user, pas):
            from main import MainPage

            if user in Login.user_pass.keys():
                if Login.user_pass[user] == pas:
                    self.destroy()
                    MainPage().mainloop()
                    #****************************************
                else:
                    messagebox.showerror('error', 'رمز اشتباه است')

            else:
                messagebox.showerror('error', 'نام کاربری اشتباه است')

        username_label = ct.CTkLabel(self , text='Username : ',font=(None,15),)
        username_label.pack(pady=20)

        username = ct.CTkEntry(self ,height=20 ,width=200)
        username.pack(pady=5)
        username.focus_set()

        password_label = ct.CTkLabel(self, text='Password : ', font=(None, 15),)
        password_label.pack(pady=20)

        password = ct.CTkEntry(self, height=20, width=200,show='*')
        password.pack(pady=5)
        password.focus_set()

        submit_button = ct.CTkButton(self ,text="submit" ,
                                     command= lambda : login_logic(username.get() ,password.get()),
                                     fg_color='lime' ,hover_color='red' ,text_color='black')
        submit_button.pack(pady = 20)

if __name__ == "__main__":
    app = Login()
    app.mainloop()

# pip install -r requirements.txt
