from tkinter import messagebox ,ttk
import customtkinter as ct
import mysql.connector
from configs import *
from khayyam import JalaliDatetime
from datetime import datetime


class ChequeFrame(ct.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cheqiueUi()

    def cheqiueUi(self):
        self.title('وارد کردن چک')
        self.geometry("700x450")
        self.configure(bg='#292e2e')
        darvajh_label = ct.CTkLabel(self, text='در وجه : ', font=(None, 20), )
        darvajh_label.pack(pady=20)

        darvajh = ct.CTkEntry(self, height=30, width=300,font=(None,20))
        darvajh.pack(pady=5)
        darvajh.focus_set()

        amount_label = ct.CTkLabel(self, text='مبلغ : ', font=(None, 20), )
        amount_label.pack(pady=20)

        amount = ct.CTkEntry(self, height=30, width=300,font=(None,20))
        amount.pack(pady=5)
        amount.focus_set()

        date_label = ct.CTkLabel(self, text='تاریخ با (-) جدا کنید : ', font=(None, 20), )
        date_label.pack(pady=20)

        Date = ct.CTkEntry(self, height=20, width=300, font=(None, 20))
        Date.pack(pady=5)
        Date.focus_set()

        submit_button = ct.CTkButton(self, text="submit",
                                     command= lambda : submit_logic(darvajh.get(), amount.get()),
                                     fg_color='lime', hover_color='red', text_color='black')
        submit_button.pack(pady = 20)

        exit_button = ct.CTkButton(self, text="exit",command=lambda : exit_logic(self),
                                     fg_color='red', hover_color='#7A0202', text_color='black')
        exit_button.pack(pady=20)

        def exit_logic(root):
            from main import MainPage
            root.destroy()
            MainPage().mainloop()

        def submit_logic(dar:str , price:int):
            if Date.get() and amount.get() and darvajh.get():
                cnx = self.connect_cursor()
                cursor = cnx.cursor()
                query = """INSERT INTO cheques (`date`, amount, target, `status`) 
                            VALUES (%s, %s, %s, N'در صف پرداخت');"""

                query2 = """INSERT INTO in_outs (ID ,`status` ,price ,date)
                            VALUES (UUID() ,%s, %s, %s);"""

                nowData = Date.get()
                amount_value = int(amount.get())
                target_value = darvajh.get()
                nowPersian = str(JalaliDatetime(datetime.now())).split()[0]

                values = (nowData, amount_value, target_value)
                values2 = ('پرداخت', amount_value ,nowPersian)

                cursor.execute(query, values)
                cursor.execute(query2 , values2)
                cnx.commit()

                messagebox.showinfo('submit','با موفقیت ثبت شد')
                cursor.close()
                cnx.close()
            else:
                messagebox.showinfo('error','لطفا تمام فیلد هارا پر کنید')
    @staticmethod
    def connect_cursor():
        cnx = mysql.connector.connect(
            host="localhost",
            user=User_c,
            password=Password_c,
            database=database_c
        )
        return cnx


class StoreFrame(ct.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.Inputs()
        self.index = 0

    def Inputs(self):
        self.title('افزایش موجودی')
        self.geometry("600x700")
        self.configure(bg='#292e2e')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0,weight=1)

        mainFrame = ct.CTkFrame(self , bg_color='#292e2e')
        phoneFrame = ct.CTkFrame(self, bg_color='#292e2e')
        otherFrame = ct.CTkFrame(self, bg_color='#292e2e')

        mainFrame.grid(row=0,column=0,sticky='nsew')
        phoneFrame.grid(row=0, column=0, sticky='nsew')
        otherFrame.grid(row=0, column=0, sticky='nsew')

        mainFrame.tkraise()
        tList = ttk.Combobox(mainFrame, values=['other','phone'], state="readonly", width=20,font="Verdana 16 bold")
        tList.pack(padx=10, pady=100,ipadx=10 , ipady=10)

        changeButton = ct.CTkButton(mainFrame,text="ENTER",command=lambda :show_frame(tList.get()),
                                     fg_color='#FA8128', hover_color='#FC6A03', text_color='black')
        changeButton.pack()

        exit_button = ct.CTkButton(mainFrame, text="EXIT", command=lambda: exit_logic(self),
                                   fg_color='red', hover_color='#7A0202', text_color='black')
        exit_button.pack(pady=20)

        def exit_logic(root):
            from main import MainPage
            root.destroy()
            MainPage().mainloop()

        def show_frame(choice):
            if choice == 'other':
                otherFrame.tkraise()
                mainFrame.forget()
            else:
                phoneFrame.tkraise()
                mainFrame.forget()

        id_label1 = ct.CTkLabel(otherFrame, text='ایدی : ', font=('Verdana', 20), )
        id_label2 = ct.CTkLabel(phoneFrame, text='ایدی : ', font=('Verdana', 20), )
        id_label1.grid(row=0,column=0,padx=20,pady=20)
        id_label2.grid(row=0,column=0,padx=20,pady=20)

        id_input1 = ct.CTkEntry(otherFrame, height=20, width=300, font=(None, 20))
        id_input2 = ct.CTkEntry(phoneFrame, height=20, width=300, font=(None, 20))
        id_input1.grid(row=0,column=1,)
        id_input2.grid(row=0,column=1,)

        brand_label = ct.CTkLabel(phoneFrame, text='برند : ', font=('Verdana', 20), )
        brand_label.grid(row=1, column=0, padx=20, pady=20)
        brand_input = ct.CTkEntry(phoneFrame, height=20, width=300, font=(None, 20))
        brand_input.grid(row=1, column=1, )

        category_label = ct.CTkLabel(otherFrame, text='بندی گروه : ', font=('Verdana', 20), )
        category_label.grid(row=1,column=0,padx=20,pady=20)

        category_input = ct.CTkEntry(otherFrame, height=20, width=300, font=(None, 20))
        category_input.grid(row=1,column=1,)

        model_label = ct.CTkLabel(otherFrame, text='مدل : ', font=('Verdana', 20), )
        model_label2 = ct.CTkLabel(phoneFrame, text='مدل : ', font=('Verdana', 20), )
        model_label.grid(row=2,column=0,padx=20,pady=20)
        model_label2.grid(row=3,column=0,padx=20,pady=20)

        model_input = ct.CTkEntry(otherFrame, height=20, width=300, font=(None, 20))
        model_input2 = ct.CTkEntry(phoneFrame, height=20, width=300, font=(None, 20))
        model_input.grid(row=2,column=1,)
        model_input2.grid(row=3,column=1,)

        quantity_label = ct.CTkLabel(otherFrame, text='تعداد : ', font=('Verdana', 20), )
        quantity_label2 = ct.CTkLabel(phoneFrame, text='تعداد : ', font=('Verdana', 20), )
        quantity_label.grid(row=3, column=0, padx=20, pady=20)
        quantity_label2.grid(row=4, column=0, padx=20, pady=20)

        quantity_input = ct.CTkEntry(otherFrame, height=20, width=300, font=(None, 20))
        quantity_input2 = ct.CTkEntry(phoneFrame, height=20, width=300, font=(None, 20))
        quantity_input.grid(row=3, column=1, )
        quantity_input2.grid(row=4, column=1, )

        buy_label = ct.CTkLabel(otherFrame, text=' خرید قیمت : ', font=('Verdana', 20), )
        buy_label2 = ct.CTkLabel(phoneFrame, text=' خرید قیمت : ', font=('Verdana', 20),)
        buy_label.grid(row=4, column=0, padx=20, pady=20)
        buy_label2.grid(row=5, column=0, padx=20, pady=20)

        buy_input = ct.CTkEntry(otherFrame, height=20, width=300, font=(None, 20))
        buy2_input = ct.CTkEntry(phoneFrame, height=20, width=300, font=(None, 20))
        buy_input.grid(row=4, column=1, )
        buy2_input.grid(row=5, column=1, )

        radioButtonValue = ct.IntVar()
        r1 = ct.CTkRadioButton(otherFrame,text='accessory',value=1,variable=radioButtonValue)
        r2 = ct.CTkRadioButton(otherFrame, text='watch', value=2, variable=radioButtonValue)
        r3 = ct.CTkRadioButton(otherFrame, text='airpod', value=3, variable=radioButtonValue)
        r4 = ct.CTkRadioButton(otherFrame, text='speaker', value=4, variable=radioButtonValue)
        r5 = ct.CTkRadioButton(otherFrame, text='cable', value=5,variable=radioButtonValue)
        r1.grid(row=6,column=0)
        r2.grid(row=6, column=1)
        r3.grid(row=7, column=0)
        r4.grid(row=7, column=1)
        r5.grid(row=8, column=0)

        def submit_logic1(db_number):
            if db_number != 0:
                db = dict(zip([1,2,3,4,5],['accessories','watchs','airpods','speaker_and_headsets','electrical_tools']))
                db = db[db_number]
                cnx = self.connect_cursor()
                if id_input1.get() and category_input.get() and model_input.get()and quantity_input.get() and buy_input.get():
                    cursor = cnx.cursor()
                    query =f"""INSERT INTO {db} (ID, category, model,quantity ,buy,`date`) 
                                                VALUES (%s, %s, %s, %s ,%s ,%s);"""

                    query2 = f"""INSERT INTO in_outs (ID, status, price , date) 
                                                VALUES (%s, %s, %s ,%s);"""

                    ID = id_input1.get()
                    category = category_input.get()
                    model = model_input.get()
                    quan = int(quantity_input.get())
                    buy = int(buy_input.get())
                    nowPersian = str(JalaliDatetime(datetime.now())).split()[0]

                    values = (ID,category,model,quan,buy,nowPersian)
                    cursor.execute(query, values)

                    values2 = (ID, 'پرداخت',buy ,nowPersian)
                    cursor.execute(query2, values2)

                    cnx.commit()

                    messagebox.showinfo('submit', 'با موفقیت ثبت شد')
                    cursor.close()
                    cnx.close()
                else:
                    messagebox.showerror('fileds','تمامی فیلد هارا پر کنید')
            else :messagebox.showerror('fileds','تمامی فیلد هارا پر کنید')

        def submit_logic2():
            cnx = self.connect_cursor()
            if id_input2.get()and brand_input.get() and model_input2.get()and quantity_input2.get() and buy2_input.get():
                cursor = cnx.cursor()
                query =f"""INSERT INTO phones (ID, brand ,model,quantity ,buy,`date`) 
                                            VALUES (%s, %s, %s, %s,%s ,%s);"""

                query2 = f"""INSERT INTO in_outs (ID, status, price , date) 
                                                                VALUES (%s, %s, %s ,%s);"""

                ID = id_input2.get()
                brand = brand_input.get()
                model = model_input2.get()
                quan = int(quantity_input2.get())
                buy = int(buy2_input.get())
                nowPersian = str(JalaliDatetime(datetime.now())).split()[0]

                values = (ID,brand,model,quan,buy,nowPersian)
                cursor.execute(query, values)

                cnx.commit()

                values2 = (ID, 'پرداخت', buy, nowPersian)
                cursor.execute(query2, values2)

                cnx.commit()

                messagebox.showinfo('submit', 'با موفقیت ثبت شد')
                cursor.close()
                cnx.close()
            else:
                messagebox.showerror('fileds','تمامی فیلد هارا پر کنید')


        submit_button = ct.CTkButton(otherFrame, text="submit",command=lambda : submit_logic1(radioButtonValue.get()),
                                     fg_color='lime', hover_color='red', text_color='black')
        submit_button2 = ct.CTkButton(phoneFrame, text="submit",command=lambda : submit_logic2(),
                                     fg_color='lime', hover_color='red', text_color='black')
        submit_button.grid(row=9,column=2)
        submit_button2.grid(row=6,column=2)

        def back_logic(frame_number):
            if frame_number == 2:
                mainFrame.tkraise()
                otherFrame.forget()
            else:
                mainFrame.tkraise()
                phoneFrame.forget()

        back_button = ct.CTkButton(otherFrame, text="back",command=lambda :back_logic(2),
                                     fg_color='lime', hover_color='red', text_color='black')
        back_button2 = ct.CTkButton(phoneFrame, text="back",command=lambda :back_logic(3),
                                   fg_color='lime', hover_color='red', text_color='black')
        back_button.grid(row=10,column=2,sticky='s',pady=20)
        back_button2.grid(row=7,column=2,sticky='s',pady=20)


    @staticmethod
    def connect_cursor():
        cnx = mysql.connector.connect(
            host="localhost",
            user=User_c,
            password=Password_c,
            database=database_c
        )
        return cnx


class AddSalesFrame(ct.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.addSalesUi()


    def addSalesUi(self):
        self.title('وارد کردن محصولات')
        self.geometry("600x700")
        self.configure(bg='#292e2e')

        def remove_zero_quantities(cn):
            db = ['accessories','watchs','airpods','speaker_and_headsets','electrical_tools','phones']
            cursor = cn.cursor()
            for db_name in db:
                query = f"""delete from applicationhesabdari.{db_name}
                            where quantity = %s"""
                values = (0,)
                cursor.execute(query,values)
                rows_deleted = cursor.rowcount
                if rows_deleted > 0:
                    messagebox.showinfo('db info', 'DataBase cleaned')
                cn.commit()
            else:
                cursor.close()
                cn.close()

        id_label1 = ct.CTkLabel(self, text='ایدی : ', font=('Verdana', 20), )
        id_label1.grid(row=0, column=0, padx=20, pady=20)

        id_input1 = ct.CTkEntry(self, height=20, width=300, font=(None, 20))
        id_input1.grid(row=0, column=1, )

        price_label = ct.CTkLabel(self, text='قیمت : ', font=('Verdana', 20), )
        price_label.grid(row=1, column=0, padx=20, pady=20)
        price_input = ct.CTkEntry(self, height=20, width=300, font=(None, 20))
        price_input.grid(row=1, column=1, )

        seller_label = ct.CTkLabel(self, text='فروشنده : ', font=('Verdana', 20), )
        seller_label.grid(row=2, column=0, padx=20, pady=20)
        seller_input = ct.CTkEntry(self, height=20, width=300, font=(None, 20))
        seller_input.grid(row=2, column=1, )




        radioButtonValue = ct.IntVar()
        r1 = ct.CTkRadioButton(self,text='accessory',value=1,variable=radioButtonValue)
        r2 = ct.CTkRadioButton(self, text='watch', value=2, variable=radioButtonValue)
        r3 = ct.CTkRadioButton(self, text='airpod', value=3, variable=radioButtonValue)
        r4 = ct.CTkRadioButton(self, text='speaker', value=4, variable=radioButtonValue)
        r5 = ct.CTkRadioButton(self, text='cable', value=5,variable=radioButtonValue)
        r6 = ct.CTkRadioButton(self, text='phone', value=6, variable=radioButtonValue)
        r1.grid(row=6,column=0,pady=10,padx=10)
        r2.grid(row=6, column=1,pady=10)
        r3.grid(row=7, column=0,pady=10,padx=10)
        r4.grid(row=7, column=1,pady=10)
        r5.grid(row=8, column=0,pady=10,padx=10)
        r6.grid(row=8, column=1,pady=10)

        submit_button = ct.CTkButton(self, text="submit", command=lambda: submit_logic1(radioButtonValue.get()),
                                     fg_color='lime', hover_color='red', text_color='black')
        submit_button.grid(row=11, column=1 ,pady=50 ,ipady=10,ipadx=50)

        exit_button = ct.CTkButton(self, text="EXIT", command=lambda: exit_logic(self),
                                   fg_color='red', hover_color='#7A0202', text_color='black')
        exit_button.grid(row=12, column=1 ,pady=20)

        def exit_logic(root):
            from main import MainPage
            root.destroy()
            MainPage().mainloop()

        def submit_logic1(db_number):

            if db_number != 0:

                db = dict(zip([1,2,3,4,5,6],['accessories','watchs','airpods','speaker_and_headsets','electrical_tools','phones']))
                db = db[db_number]
                cnx = self.connect_cursor()

                if id_input1.get() and price_input.get():
                    dbS = ['accessories', 'watchs', 'airpods', 'speaker_and_headsets', 'electrical_tools', 'phones']
                    cursor = cnx.cursor()
                    for db_name in dbS:
                        query = f"""delete from applicationhesabdari.{db_name}
                                    where quantity = %s"""
                        values = (0,)
                        cursor.execute(query, values)
                        rows_deleted = cursor.rowcount
                        if rows_deleted > 0:
                            messagebox.showinfo('db info', 'DataBase cleaned')
                        cnx.commit()
                    cursor.close()
                    cnx.close()

                    cnx = self.connect_cursor()
                    cursor = cnx.cursor()

                    ID = id_input1.get()
                    price = int(price_input.get())
                    nowPersian = str(JalaliDatetime(datetime.now())).split()[0]

                    query_select = f"""SELECT * FROM applicationhesabdari.{db}
                                    WHERE ID = %s"""
                    values_select = (ID,)
                    cursor.execute(query_select, values_select)
                    rows = cursor.fetchall()

                    if len(rows) > 0:
                        def minDate():
                            minDateQuery = f"select min(`date`) from applicationhesabdari.{db} where ID = %s"
                            cursor.execute(minDateQuery, (ID,))
                            minDateValue = str(cursor.fetchone()[0])
                            return minDateValue

                        q = f"select * from applicationhesabdari.{db} where `date` = %s;"

                        currentQuantityQuery = f"select quantity from applicationhesabdari.{db} where `date` = %s and ID = %s ;"
                        cursor.execute(currentQuantityQuery ,(minDate() , ID))
                        try :
                            currentQuantity = int(cursor.fetchone()[0])
                        except TypeError:
                            currentQuantity = 1
                        newQuantity = currentQuantity - 1

                        updateQuantityQuery = f"update applicationhesabdari.{db} set quantity = %s where `date` = %s and ID = %s ;"
                        cursor.execute(updateQuantityQuery, (newQuantity,minDate(), ID))
                        cnx.commit()

                        query2 = """INSERT INTO applicationhesabdari.sales (ID, price,`date`)
                                                                                                VALUES (%s, %s, %s);"""
                        values2 = (ID, price, nowPersian)
                        cursor.execute(query2, values2)
                        cnx.commit()

                        query4 = f"""INSERT INTO applicationhesabdari.in_outs (ID,status,price,date)
                                    VALUES (%s, %s, %s ,%s);"""
                        cursor.execute(query4 , (ID ,'دریافتی',price ,nowPersian))

                        cnx.commit()

                        query5 = """insert into applicationhesabdari.sellers_info (name,price,date)
                                    VALUES (%s ,%s ,%s);"""

                        cursor.execute(query5, (seller_input.get(), price, nowPersian))

                        cnx.commit()

                        messagebox.showinfo('submit', 'با موفقیت ثبت شد')
                        cursor.close()
                        cnx.close()
                    else:
                        messagebox.showerror('fileds', 'در انبار موجود نیست')
                else:
                    messagebox.showerror('fileds','تمامی فیلد هارا پر کنید')
            else :messagebox.showerror('fileds','تمامی فیلد هارا پر کنید')



    @staticmethod
    def connect_cursor():
        cnx = mysql.connector.connect(
            host="localhost",
            user=User_c,
            password=Password_c,
            database=database_c
        )
        return cnx


class ChangeDataFrame(ct.CTk):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.updateUi()

    @staticmethod
    def connect_cursor():
        cnx = mysql.connector.connect(
            host="localhost",
            user=User_c,
            password=Password_c,
            database=database_c
        )
        return cnx

    def updateUi(self):
        self.title('update price')
        self.geometry("500x600")
        self.configure(bg='#292e2e')

        mainFrame = ct.CTkFrame(self, fg_color='#323737', height=600)
        mainFrame.pack(side=ct.TOP, padx=10,pady=20 ,fill='both')
        mainFrame.pack_propagate(False)

        id_label1 = ct.CTkLabel(mainFrame, text='ایدی : ', font=('Verdana', 25),)
        id_label1.grid(row=0, column=0, padx=20, pady=20)

        id_input1 = ct.CTkEntry(mainFrame, height=20, width=300, font=(None, 20))
        id_input1.grid(row=0, column=1, )

        price_label = ct.CTkLabel(mainFrame, text='قیمت : ', font=('Verdana', 25),)
        price_label.grid(row=1, column=0, padx=20, pady=20)

        price_input = ct.CTkEntry(mainFrame, height=20, width=300, font=(None, 20),)
        price_input.grid(row=1, column=1, )

        quant_label = ct.CTkLabel(mainFrame, text='تعداد : ', font=('Verdana', 25),)
        quant_label.grid(row=2, column=0, padx=20, pady=20)

        quant_input = ct.CTkEntry(mainFrame, height=20, width=300, font=(None, 20))
        quant_input.grid(row=2, column=1, )

        radioButtonValue = ct.IntVar()
        r1 = ct.CTkRadioButton(mainFrame, text='accessory', value=1, variable=radioButtonValue)
        r2 = ct.CTkRadioButton(mainFrame, text='watch', value=2, variable=radioButtonValue)
        r3 = ct.CTkRadioButton(mainFrame, text='airpod', value=3, variable=radioButtonValue)
        r4 = ct.CTkRadioButton(mainFrame, text='speaker', value=4, variable=radioButtonValue)
        r5 = ct.CTkRadioButton(mainFrame, text='cable', value=5, variable=radioButtonValue)
        r6 = ct.CTkRadioButton(mainFrame, text='phone', value=6, variable=radioButtonValue)
        r1.grid(row=3, column=0, pady=5, padx=10)
        r2.grid(row=3, column=1, pady=5)
        r3.grid(row=4, column=0, pady=5, padx=10)
        r4.grid(row=4, column=1, pady=5)
        r5.grid(row=5, column=0, pady=5, padx=10)
        r6.grid(row=5, column=1, pady=5)

        checkButton = ct.CTkButton(mainFrame, text="check", font=(None, 20),command=lambda : checkLogic(),
                                 fg_color='#f6e0b5', hover_color='#0bff01', text_color='black')
        checkButton.grid(row=6,column=0,pady=20,padx=10)

        submitButton = ct.CTkButton(mainFrame, text="submit", font=(None, 20),command=lambda : submitLogic(radioButtonValue.get()),
                                    fg_color='#f6e0b5', hover_color='#0bff01', text_color='black')
        submitButton.grid(row=6, column=1, pady=20,sticky=ct.W)

        backButton = ct.CTkButton(mainFrame, text="back", font=(None, 20),command=lambda : exitLogic(),
                                   fg_color='#f6e0b5', hover_color='#0bff01', text_color='black')
        backButton.grid(row=6, column=1, pady=20, padx=10,sticky=ct.E)

        checkFrame = ct.CTkFrame(self, fg_color='#323737', )
        checkFrame.pack(side=ct.BOTTOM, padx=10, pady=10, fill='both')
        checkFrame.pack_propagate(False)

        def checkLogic():

            for widget in checkFrame.winfo_children():
                widget.destroy()

            tree = ttk.Treeview(checkFrame,height=10)
            tree['show'] = 'headings'
            cols = ('name', "model" ,"quantity" ,"price")
            persian_cols = ('ایدی', "مدل", "تعداد", "قیمت")
            tree['columns'] = cols
            for i, col in enumerate(cols):
                tree.column(col, width=150, minwidth=100, anchor=ct.CENTER)
                tree.heading(col, text=persian_cols[i], anchor=ct.CENTER)

            cn = self.connect_cursor()
            cursor = cn.cursor()

            query =  """select ID ,model ,quantity ,buy from (
                            select ID ,model ,quantity ,buy from accessories
                            union all
                            select ID ,model ,quantity ,buy from airpods
                            union all
                            select ID ,model ,quantity ,buy from electrical_tools
                            union all
                            select ID ,model ,quantity ,buy from speaker_and_headsets
                            union all
                            select ID ,model ,quantity ,buy from watchs
                            union all
                            select ID ,model ,quantity ,buy from phones) k
                        where k.ID = %s;           
                    """

            cursor.execute(query , (id_input1.get(),))
            rows = cursor.fetchall()

            i = 0
            for row in rows:
                if i % 2 == 0:
                    tree.insert('', index=i, text="", values=(row[0], row[1] ,row[2] ,row[3],), tags=('evenrow',))
                else:
                    tree.insert('', index=i, text="", values=(row[0], row[1] ,row[2] ,row[3],), tags=('oddrow',))
                i += 1
            styles = ttk.Style(tree)
            styles.theme_use("clam")
            styles.configure(".", font=("Helvetica", 12))
            styles.configure("Treeview.Heading", foreground='#292e2e', font=("Helvetica", 15, "bold"))

            tree.tag_configure('oddrow', background='white')
            tree.tag_configure('evenrow', background='#f6e0b5')
            tree.pack(padx=10, pady=10, fill='x')

            cursor.close()
            cn.close()

        def submitLogic(db_number):
            if db_number:
                db = dict(zip([1, 2, 3, 4, 5,6],
                              ['accessories', 'watchs', 'airpods',
                               'speaker_and_headsets', 'electrical_tools' ,'phones']))
                db = db[db_number]
                user_quantity = quant_input.get()
                user_price = price_input.get()

                cn = self.connect_cursor()
                cursor = cn.cursor()

                if user_quantity and user_price:
                    messagebox.showwarning('error', 'یک مقدار را انتخاب کنید')

                elif user_price:
                    query = f"""update applicationhesabdari.{db}
                                set buy = %s
                                where ID = %s;"""

                    values = (user_price,id_input1.get(),)
                    cursor.execute(query,values)
                    cn.commit()
                    messagebox.showinfo('', "با موفقیت ثبت شد")

                elif user_quantity:

                    cursor.execute('SELECT max(date) FROM applicationhesabdari.{} WHERE ID = %s'.format(db),
                                   (id_input1.get(),))
                    max_date = cursor.fetchone()[0]

                    query = f"""UPDATE applicationhesabdari.{db}
                            SET quantity = %s
                            WHERE ID = %s AND date = %s"""

                    values = (user_quantity, id_input1.get(), max_date)
                    cursor.execute(query, values)
                    cn.commit()
                    messagebox.showinfo('', "با موفقیت ثبت شد")

                else:
                    messagebox.showwarning('error', 'مقدار را انتخاب کنید')

            else:
                messagebox.showwarning('error', 'دیتابیس را انتخاب کنید')



        def exitLogic():
            from main import MainPage
            self.destroy()
            MainPage().mainloop()


class ReportFrame(ct.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.reportUi()

    @staticmethod
    def connect_cursor():
        cnx = mysql.connector.connect(
            host="localhost",
            user=User_c,
            password=Password_c,
            database=database_c
        )
        return cnx

    def reportUi(self):
        self.title('گزارشات')
        self.geometry("950x700")
        self.configure(bg='#292e2e')
        self.resizable(False,False)

        resultFrame = ct.CTkFrame(self,fg_color='#3c3c3c',height=650,width=700,)
        resultFrame.pack(side=ct.LEFT,padx=10)
        resultFrame.pack_propagate(False)

        buttonFrame = ct.CTkFrame(self, fg_color='#003e3e',height=650,width=200)
        buttonFrame.pack(side=ct.RIGHT,padx=10)
        buttonFrame.pack_propagate(False)


        def repLogic(phone_status:bool):

            for widget in resultFrame.winfo_children():
                widget.destroy()

            tree = ttk.Treeview(resultFrame ,height=20)
            tree['show'] = 'headings'
            if phone_status:
                tree['columns'] = ('ID', 'brand', 'model', 'quantity', 'buy', 'date')
            else:
                tree['columns'] = ('ID' , 'category' , 'model' , 'quantity' ,'buy' ,'date')
            tree.column('ID',width=100 ,minwidth=100 ,anchor=ct.CENTER)
            if phone_status:
                tree.column('brand', width=100, minwidth=100, anchor=ct.CENTER)
            else:
                tree.column('category', width=100, minwidth=100, anchor=ct.CENTER)
            tree.column('model', width=100, minwidth=100, anchor=ct.CENTER)
            tree.column('quantity', width=50, minwidth=100, anchor=ct.CENTER)
            tree.column('buy', width=150, minwidth=100, anchor=ct.CENTER)
            tree.column('date', width=100, minwidth=100, anchor=ct.CENTER)

            tree.heading('ID', text='ایدی', anchor=ct.CENTER)
            if phone_status:
                tree.heading('brand', text="برند", anchor=ct.CENTER)
            else:
                tree.heading('category', text="گروه",anchor=ct.CENTER)
            tree.heading('model', text="مدل", anchor=ct.CENTER)
            tree.heading('quantity', text="تعداد", anchor=ct.CENTER)
            tree.heading('buy', text="خرید",anchor=ct.CENTER)
            tree.heading('date', text="تاریخ", anchor=ct.CENTER)

            cn = self.connect_cursor()
            cursor = cn.cursor()
            d1 = beginDate.get()
            d2 = endDate.get()
            if d1 and d2:
                if phone_status:
                    query = f"select ID,brand,model,quantity,buy,date from phones where date BETWEEN %s and %s;"
                    cursor.execute(query,(d1,d2,))
                else:
                    query = f"""select ID,category,model,quantity,buy,date from accessories where date BETWEEN %s and %s
                            union all
                            select ID,category,model,quantity,buy,date from airpods where date BETWEEN %s and %s
                            union all
                            select ID,category,model,quantity,buy,date from electrical_tools where date BETWEEN %s and %s
                            union all
                            select ID,category,model,quantity,buy,date from speaker_and_headsets where date BETWEEN %s and %s
                            union all
                            select ID,category,model,quantity,buy,date from watchs where date BETWEEN %s and %s;;
                    """
                    cursor.execute(query,(d1,d2,d1,d2,d1,d2,d1,d2,d1,d2,))
                rows = cursor.fetchall()
            else:
                if phone_status:
                    query = "select ID,brand,model,quantity,buy,date from phones;"
                else:
                    query = """select ID,category,model,quantity,buy,date from accessories
                            union all
                            select ID,category,model,quantity,buy,date from airpods
                            union all
                            select ID,category,model,quantity,buy,date from electrical_tools
                            union all
                            select ID,category,model,quantity,buy,date from speaker_and_headsets
                            union all
                            select ID,category,model,quantity,buy,date from watchs;
                    """
                cursor.execute(query)
                rows = cursor.fetchall()

            i = 0
            for row in rows:
                if i % 2 == 0:
                    tree.insert('', index=i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5],),tags=('evenrow',))
                else:

                    tree.insert('', index=i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5],),tags=('oddrow',))
                i += 1

            styles = ttk.Style(tree)
            styles.theme_use("clam")
            styles.configure(".",font=("Helvetica",12))
            styles.configure("Treeview.Heading", foreground='#292e2e',font=("Helvetica", 15,"bold"))

            scroll = ct.CTkScrollbar(resultFrame,orientation='vertical',command=tree.yview)
            tree.configure(yscrollcommand=scroll.set)
            tree.tag_configure('oddrow', background='white')
            tree.tag_configure('evenrow', background='#f2e2cd')
            tree.pack(padx=10,pady=10,fill='x')

            # numericResultFrame = ct.CTkTextbox(resultFrame,fg_color="#f2e2cd",text_color='black',font=(None,20),)
            # numericResultFrame.pack(side=ct.BOTTOM, padx=10,pady=20 ,fill='both')
            # numericResultFrame.configure(state="disabled")

            numericResultFrame = ct.CTkFrame(resultFrame,fg_color="#f2e2cd",)
            numericResultFrame.pack(side=ct.BOTTOM, padx=10, pady=20, fill='both')

            if phone_status:
                if not d1 :
                    query = """
                            SELECT SUM(quantity) AS res FROM phones;
                            """
                    cursor.execute(query, )
                    report_quantity = cursor.fetchone()[0]

                    query = """
                            SELECT SUM(buy) AS res FROM phones;
                            """
                    cursor.execute(query, )
                    report_buy = cursor.fetchone()[0]
                else:
                    query = """
                            SELECT SUM(quantity) AS res FROM phones
                            where `date` between %s and %s;
                            """
                    values = (d1, d2,)
                    cursor.execute(query, values)
                    report_quantity = cursor.fetchone()[0]

                    query = """
                            SELECT SUM(buy) AS res FROM phones
                            where `date` between %s and %s;
                            """
                    values = (d1, d2,)
                    cursor.execute(query, values)
                    report_buy = cursor.fetchone()[0]
            else:
                if d1:
                    query = """
                            SELECT SUM(buy) AS result FROM (
                                SELECT buy FROM accessories where date between %s and %s
                                UNION ALL
                                SELECT buy FROM airpods where date between %s and %s
                                UNION ALL
                                SELECT buy FROM electrical_tools where date between %s and %s
                                UNION ALL
                                SELECT buy FROM speaker_and_headsets where date between %s and %s
                                UNION ALL
                                SELECT buy FROM watchs where date between %s and %s
                            ) k;
                            """
                    values = (d1,d2,d1,d2,d1,d2,d1,d2,d1,d2,)
                    cursor.execute(query, values)
                    report_buy = cursor.fetchone()[0]

                    query = """
                            SELECT SUM(quantity) AS result FROM (
                                SELECT quantity FROM accessories where date between %s and %s
                                UNION ALL
                                SELECT quantity FROM airpods where date between %s and %s
                                UNION ALL
                                SELECT quantity FROM electrical_tools where date between %s and %s
                                UNION ALL
                                SELECT quantity FROM speaker_and_headsets where date between %s and %s
                                UNION ALL
                                SELECT quantity FROM watchs where date between %s and %s
                            ) k;
                            """
                    cursor.execute(query, values)
                    report_quantity = cursor.fetchone()[0]
                else:
                    query = """
                            SELECT SUM(buy * quantity)  AS result FROM (
                                SELECT buy ,quantity FROM accessories 
                                UNION ALL
                                SELECT buy ,quantity FROM airpods 
                                UNION ALL
                                SELECT buy ,quantity FROM electrical_tools 
                                UNION ALL
                                SELECT buy ,quantity FROM speaker_and_headsets 
                                UNION ALL
                                SELECT buy ,quantity FROM watchs
                            ) k;
                            """
                    cursor.execute(query, )
                    report_buy = cursor.fetchone()[0]

                    query = """
                            SELECT SUM(quantity) AS result FROM (
                                SELECT quantity FROM accessories 
                                UNION ALL
                                SELECT quantity FROM airpods 
                                UNION ALL
                                SELECT quantity FROM electrical_tools 
                                UNION ALL
                                SELECT quantity FROM speaker_and_headsets 
                                UNION ALL
                                SELECT quantity FROM watchs
                            ) k;
                            """
                    cursor.execute(query, )
                    report_quantity = cursor.fetchone()[0]

            label1 = ct.CTkLabel(numericResultFrame, text = f'اجناس تعداد : {report_quantity}', font=('Verdana', 20),text_color='black' )
            label1.grid(row=0, column=0, padx=20, pady=20)

            label2 = ct.CTkLabel(numericResultFrame, text = f' خرید مجموع : {report_buy}', font=('Verdana', 20),text_color='black' )
            label2.grid(row=1, column=0, padx=20, pady=20)

            # numericResultFrame.insert(0.0,f" مجموع خرید : {report_buy}\n")
            # numericResultFrame.insert(0.0, f" تعداد خرید : {report_quantity}\n" )



        repositoryButton = ct.CTkButton(buttonFrame, text="گزارش انبار", font=(None, 20), command=lambda: repLogic(False),
                                       fg_color='#f6e0b5', hover_color='#0bff01', text_color='black')
        repositoryButton.pack(pady=10)

        phoneRepButton = ct.CTkButton(buttonFrame, text="گزارش انبار گوشی", font=(None, 20), command=lambda: repLogic(True),
                                       fg_color='#f6e0b5', hover_color='#0bff01', text_color='black')
        phoneRepButton.pack(pady=10)

        def chequeLogic():
            for widget in resultFrame.winfo_children():
                widget.destroy()

            tree = ttk.Treeview(resultFrame, height=20)
            tree['show'] = 'headings'
            cols = ('date', 'amount', 'target', 'status')
            persian_cols = ('تاریخ',"مقدار","در وجه","وضیعت")
            tree['columns'] = cols

            for i,col in enumerate(cols):
                tree.column(col,width=150,minwidth=100,anchor=ct.CENTER)
                tree.heading(col, text=persian_cols[i], anchor=ct.CENTER)


            cn = self.connect_cursor()
            cursor = cn.cursor()

            def cheq_cleaner():

                nowPersian = str(JalaliDatetime(datetime.now())).split()[0]
                query = """delete from applicationhesabdari.cheques
                            where date < %s;"""
                cursor.execute(query,(nowPersian,))
                cn.commit()

            cheq_cleaner()

            query = f"select date, amount, target, status from applicationhesabdari.cheques;"

            cursor.execute(query)
            rows = cursor.fetchall()
            i = 0
            for row in rows:
                if i % 2 == 0:
                    tree.insert('', index=i, text="", values=(row[0], row[1], row[2], row[3]),tags=('evenrow',))
                else:
                    tree.insert('', index=i, text="", values=(row[0], row[1], row[2], row[3]),tags=('oddrow',))
                i += 1

            styles = ttk.Style(tree)
            styles.theme_use("clam")
            styles.configure(".", font=("Helvetica", 12))
            styles.configure("Treeview.Heading", foreground='#292e2e', font=("Helvetica", 15, "bold"))

            tree.tag_configure('oddrow',background='white')
            tree.tag_configure('evenrow', background='#f6e0b5')
            tree.pack(padx=10, pady=10, fill='x')


        chequeButton = ct.CTkButton(buttonFrame, text="گزارش چک", font=(None, 20),command=lambda :chequeLogic(),
                                        fg_color='#f6e0b5', hover_color='#0bff01', text_color='black')
        chequeButton.pack(pady=10)

        def dailyLogic():
            for widget in resultFrame.winfo_children():
                widget.destroy()

            tree = ttk.Treeview(resultFrame, height=20)
            tree['show'] = 'headings'
            cols = ('ID', 'status', 'price', 'date')
            persian_cols = ('ایدی',"وصغیت","مقدار","تاریخ")
            tree['columns'] = cols
            for i,col in enumerate(cols):
                tree.column(col,width=150,minwidth=100,anchor=ct.CENTER)
                tree.heading(col, text=persian_cols[i], anchor=ct.CENTER)

            d1 = beginDate.get()
            d2 = endDate.get()

            cn = self.connect_cursor()
            cursor = cn.cursor()

            query = f"select ID,status, price, date from applicationhesabdari.in_outs where date between %s and %s;"
            nowPersian = str(JalaliDatetime(datetime.now())).split()[0]
            cursor.execute(query,(nowPersian,nowPersian))

            rows = cursor.fetchall()
            i = 0
            for row in rows:
                if i % 2 == 0:
                    tree.insert('', index=i, text="", values=(row[0], row[1], row[2], row[3]), tags=('evenrow',))
                else:
                    tree.insert('', index=i, text="", values=(row[0], row[1], row[2], row[3]), tags=('oddrow',))
                i += 1
            styles = ttk.Style(tree)
            styles.theme_use("clam")
            styles.configure(".", font=("Helvetica", 12))
            styles.configure("Treeview.Heading", foreground='#292e2e', font=("Helvetica", 15, "bold"))

            tree.tag_configure('oddrow', background='white')
            tree.tag_configure('evenrow', background='#f6e0b5')
            tree.pack(padx=10, pady=10, fill='x')

            numericResultFrame = ct.CTkFrame(resultFrame, fg_color="#f2e2cd", )
            numericResultFrame.pack(side=ct.BOTTOM, padx=10, pady=20, fill='both')

            query = """
                    SELECT SUM(price) as res FROM sales
                    where `date`= %s;
                    """
            values = (nowPersian,)
            cursor.execute(query, values)
            daily_sales = cursor.fetchone()[0]

            query = """
                    select sum(s.price - k.buy) AS res from sales as s
                    inner join (SELECT * FROM accessories 
                            UNION ALL
                            SELECT * FROM airpods 
                            UNION ALL
                            SELECT * FROM electrical_tools 
                            UNION ALL
                            SELECT * FROM speaker_and_headsets 
                            UNION ALL
                            SELECT * FROM watchs
                            UNION ALL 
                            select * from phones) as k on k.ID = s.ID
                    where s.date = %s;
                    """
            values = (nowPersian,)
            cursor.execute(query, values)

            daily_income = cursor.fetchone()[0]

            label1 = ct.CTkLabel(numericResultFrame, text=f'روزانه فروش : {daily_sales}', font=('Verdana', 20),
                                 text_color='black')
            label1.grid(row=0, column=0, padx=20, pady=20)

            label2 = ct.CTkLabel(numericResultFrame, text=f' روزانه سود : {daily_income}', font=('Verdana', 20),
                                 text_color='black')
            label2.grid(row=1, column=0, padx=20, pady=20)

            cursor.close()
            cn.close()


        dailyButton = ct.CTkButton(buttonFrame, text="گزارش روزانه", font=(None, 20),command=lambda :dailyLogic(),
                                        fg_color='#f6e0b5', hover_color='#0bff01', text_color='black')
        dailyButton.pack(pady=10)

        def monthlyLogic():
            for widget in resultFrame.winfo_children():
                widget.destroy()

            tree = ttk.Treeview(resultFrame, height=20)
            tree['show'] = 'headings'
            cols = ('ID', 'status', 'price', 'date')
            persian_cols = ('ایدی',"وصغیت","مقدار","تاریخ")
            tree['columns'] = cols
            for i,col in enumerate(cols):
                tree.column(col,width=150,minwidth=100,anchor=ct.CENTER)
                tree.heading(col, text=persian_cols[i], anchor=ct.CENTER)

            d1 = beginDate.get()
            d2 = endDate.get()

            cn = self.connect_cursor()
            cursor = cn.cursor()
            if d1 and d2 :
                query = "select ID, status, price, date from in_outs where `date` between %s and %s; "
                cursor.execute(query,(d1,d2,))
            else:
                query = "select ID, status, price, date from in_outs;"
                cursor.execute(query)


            rows = cursor.fetchall()
            i = 0
            for row in rows:
                if i % 2 == 0:
                    tree.insert('', index=i, text="", values=(row[0], row[1], row[2], row[3]), tags=('evenrow',))
                else:
                    tree.insert('', index=i, text="", values=(row[0], row[1], row[2], row[3]), tags=('oddrow',))
                i += 1
            styles = ttk.Style(tree)
            styles.theme_use("clam")
            styles.configure(".", font=("Helvetica", 12))
            styles.configure("Treeview.Heading", foreground='#292e2e', font=("Helvetica", 15, "bold"))

            tree.tag_configure('oddrow', background='white')
            tree.tag_configure('evenrow', background='#f6e0b5')
            tree.pack(padx=10, pady=10, fill='x')

            numericResultFrame = ct.CTkFrame(resultFrame, fg_color="#f2e2cd", )
            numericResultFrame.pack(side=ct.BOTTOM, padx=10, pady=20, fill='both')

            if d1 and d2:
                query = "SELECT SUM(price) as res FROM sales where `date` between %s and %s;"
                cursor.execute(query,(d1,d2,) )
                sales = cursor.fetchone()[0]

                query2 = """select sum(s.price - k.buy) as res from sales as s
                            inner join (SELECT * FROM accessories 
                            UNION ALL
                            SELECT * FROM airpods 
                            UNION ALL
                            SELECT * FROM electrical_tools 
                            UNION ALL
                            SELECT * FROM speaker_and_headsets 
                            UNION ALL
                            SELECT * FROM watchs
                            UNION ALL 
                            select * from phones) as k on k.ID = s.ID
                            where s.date between %s and %s;"""

                cursor.execute(query2,(d1,d2,))
                income = cursor.fetchone()[0]
            else:
                query = "SELECT SUM(price) as res FROM sales;"
                cursor.execute(query,)
                sales = cursor.fetchone()[0]

                query2 = """select sum(s.price - k.buy) as res from sales as s
                            inner join (SELECT * FROM accessories 
                            UNION ALL
                            SELECT * FROM airpods 
                            UNION ALL
                            SELECT * FROM electrical_tools 
                            UNION ALL
                            SELECT * FROM speaker_and_headsets 
                            UNION ALL
                            SELECT * FROM watchs
                            UNION ALL 
                            select * from phones) as k on k.ID = s.ID;"""

                cursor.execute(query2)
                income = cursor.fetchone()[0]


            label1 = ct.CTkLabel(numericResultFrame, text=f' فروش : {sales}', font=('Verdana', 20),
                                 text_color='black')
            label1.grid(row=0, column=0, padx=20, pady=20)

            label2 = ct.CTkLabel(numericResultFrame, text=f' سود : {income}', font=('Verdana', 20),
                                 text_color='black')
            label2.grid(row=1, column=0, padx=20, pady=20)

            cursor.close()
            cn.close()


        monthlyButton = ct.CTkButton(buttonFrame, text="گزارش ماهانه", font=(None, 20),command=lambda :monthlyLogic(),
                                        fg_color='#f6e0b5', hover_color='#0bff01', text_color='black')
        monthlyButton.pack(pady=10)

        yearlyButton = ct.CTkButton(buttonFrame, text="گزارش سالانه", font=(None, 20),command=lambda :monthlyLogic(),
                                        fg_color='#f6e0b5', hover_color='#0bff01', text_color='black')
        yearlyButton.pack(pady=10)

        def topLogic():
            for widget in resultFrame.winfo_children():
                widget.destroy()

            tree = ttk.Treeview(resultFrame, height=20)
            tree['show'] = 'headings'
            cols = ('ID', 'result')
            persian_cols = ('ایدی',"مقدار")
            tree['columns'] = cols
            for i,col in enumerate(cols):
                tree.column(col,width=150,minwidth=100,anchor=ct.CENTER)
                tree.heading(col, text=persian_cols[i], anchor=ct.CENTER)

            d1 = beginDate.get()
            d2 = endDate.get()

            cn = self.connect_cursor()
            cursor = cn.cursor()

            if d1 and d2:
                query = """SELECT ID, SUM(price) AS result
                        FROM sales
                        WHERE `date` between %s and %s
                        GROUP BY ID
                        ORDER BY result DESC;"""
                cursor.execute(query, (d1, d2,))
            else:
                query = """SELECT ID, SUM(price) AS result
                        FROM sales
                        GROUP BY ID
                        ORDER BY result DESC;"""
                cursor.execute(query,)
            rows = cursor.fetchall()
            i = 0
            for row in rows:
                if i % 2 == 0:
                    tree.insert('', index=i, text="", values=(row[0], row[1],), tags=('evenrow',))
                else:
                    tree.insert('', index=i, text="", values=(row[0], row[1],), tags=('oddrow',))
                i += 1
            styles = ttk.Style(tree)
            styles.theme_use("clam")
            styles.configure(".", font=("Helvetica", 12))
            styles.configure("Treeview.Heading", foreground='#292e2e', font=("Helvetica", 15, "bold"))

            tree.tag_configure('oddrow', background='white')
            tree.tag_configure('evenrow', background='#f6e0b5')
            tree.pack(padx=10, pady=10, fill='x')


        topButton = ct.CTkButton(buttonFrame, text="گزارش فروش برتر", font=(None, 20),command=lambda :topLogic(),
                                        fg_color='#f6e0b5', hover_color='#0bff01', text_color='black')
        topButton.pack(pady=10)

        def sellerLogic():
            for widget in resultFrame.winfo_children():
                widget.destroy()

            tree = ttk.Treeview(resultFrame, height=20)
            tree['show'] = 'headings'
            cols = ('name', 'price',)
            persian_cols = ('ایدی',"وصغیت","مقدار","تاریخ")
            tree['columns'] = cols
            for i,col in enumerate(cols):
                tree.column(col,width=150,minwidth=100,anchor=ct.CENTER)
                tree.heading(col, text=persian_cols[i], anchor=ct.CENTER)

            d1 = beginDate.get()
            d2 = endDate.get()

            cn = self.connect_cursor()
            cursor = cn.cursor()

            if d1 and d2 :
                query = """SELECT name, SUM(price) 
                        FROM sellers_info 
                        WHERE date between %s and %s
                        GROUP BY name;"""

                cursor.execute(query,(d1,d2,))
            else:
                query = "select * from sellers_info;"
                cursor.execute(query)

            rows = cursor.fetchall()
            i = 0
            for row in rows:
                if i % 2 == 0:
                    tree.insert('', index=i, text="", values=(row[0], row[1],), tags=('evenrow',))
                else:
                    tree.insert('', index=i, text="", values=(row[0], row[1],), tags=('oddrow',))
                i += 1
            styles = ttk.Style(tree)
            styles.theme_use("clam")
            styles.configure(".", font=("Helvetica", 12))
            styles.configure("Treeview.Heading", foreground='#292e2e', font=("Helvetica", 15, "bold"))

            tree.tag_configure('oddrow', background='white')
            tree.tag_configure('evenrow', background='#f6e0b5')
            tree.pack(padx=10, pady=10, fill='x')


        sellerButton = ct.CTkButton(buttonFrame, text="گزارش فروشنده", font=(None, 20),command=lambda :sellerLogic(),
                                        fg_color='#f6e0b5', hover_color='#0bff01', text_color='black')
        sellerButton.pack(pady=10)

        dateFilterFrame = ct.CTkScrollableFrame(buttonFrame,label_text='تاریخ',scrollbar_button_color="#292e2e")
        dateFilterFrame.pack(side=ct.BOTTOM, padx=10,pady=20)
        # dateFilterFrame.pack_propagate(False)

        beginDate = ct.CTkEntry(dateFilterFrame ,placeholder_text = ' مبدا تاریخ',height=30)
        beginDate.pack(side=ct.TOP, padx=5,pady=20)
        endDate = ct.CTkEntry(dateFilterFrame,placeholder_text = " مقصد تاریخ",height=30)
        endDate.pack(side=ct.TOP, padx=5, pady=10)

        def exitLogic():
            from main import MainPage
            self.destroy()
            MainPage().mainloop()

        exitButton = ct.CTkButton(dateFilterFrame,text='BACK',command=lambda :exitLogic(),
                                  fg_color='#f2e2cd',hover_color='red',text_color='black')
        exitButton.pack(side=ct.BOTTOM, padx=5, pady=10)
