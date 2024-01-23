import customtkinter as ct
# from tkinter import ttk ,Tk ,messagebox
from sys import exit
from frames import *
import mysql.connector

class MainPage(ct.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('صفحه اصلی')
        self.geometry('600x700')

        mainFrame = ct.CTkFrame(self ,width=500 ,height=600,)
        mainFrame.pack(side='top',fill='both',expand=True)
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)

        button1 = ct.CTkButton(mainFrame ,text='تعریف چک' ,command=lambda : self.changeFrame(1),
                               text_color='black',fg_color='lime',hover_color='red',
                               height=50,width=200,font=(None,20))
        button2 = ct.CTkButton(mainFrame, text='تعریف محصول',command=lambda : self.changeFrame(2),
                               text_color='black', fg_color='lime', hover_color='red',
                                height = 50, width=200,font = (None, 20))
        button3 = ct.CTkButton(mainFrame, text='قلم زدن',command=lambda : self.changeFrame(3),
                               text_color='black', fg_color='lime', hover_color='red',
                               height=50, width=200,font=(None, 20))
        button4 = ct.CTkButton(mainFrame, text='گزارشات',command=lambda : self.changeFrame(4),
                               text_color='black', fg_color='lime', hover_color='red',
                               height=50, width=200,font=(None, 20))
        button5 = ct.CTkButton(mainFrame, text='تغییر اطلاعات محصول',command=lambda : self.changeFrame(5),
                               text_color='black', fg_color='lime', hover_color='red',
                               height=50, width=200,font=(None, 20))
        def exitLogic():
            self.quit()
            self.destroy()
            exit(0)

        button6 = ct.CTkButton(mainFrame, text='خروج', command=lambda: exitLogic(),
                               text_color='black', fg_color='lime', hover_color='red',
                               height=50, width=200, font=(None, 20))

        button1.pack(pady=30)
        button2.pack(pady=30)
        button3.pack(pady=30)
        button4.pack(pady=30)
        button5.pack(pady=40)
        button6.pack(pady=40)

        self.pages = {1:ChequeFrame(),2:StoreFrame() ,3:AddSalesFrame(),4:ReportFrame(),5:ChangeDataFrame()}
        self.index = 0

    def changeFrame(self,frameNumber):
        self.index = frameNumber
        page = self.pages[self.index]
        self.destroy()
        page.mainloop()

    # ---------------------------------

def run():
    window = MainPage()
    window.mainloop()

if __name__ == "__main__":
    run()