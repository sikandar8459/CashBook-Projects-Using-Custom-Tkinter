from customtkinter import *
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as msg
import random as rd
import time
import sqlite3

from SaveDataToExcel import DataToExcel

conn = sqlite3.connect("CashBook.db")
cur = conn.cursor()

set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class CashBookCustomTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Cashbook Project using Custom Tkinter | sikandarsingh2210@gmail.com")
        self.root.geometry("1200x600+50+0")
        # self.root._set_appearance_mode("Light")
        
        self.HeaderLabel = CTkLabel(self.root, text = "CashBook", font = ("Bookman Old Style", 34), fg_color = "transparent")
        self.HeaderLabel.pack(fill = X)
        
        self.MainFrame = CTkFrame(self.root, bg_color = "transparent")
        self.MainFrame.pack(fill = BOTH, expand = 1)

        #Search Frame Starts Here
        self.SearchFrame = CTkFrame(self.MainFrame, height = 60, bg_color = "transparent", corner_radius = 0)
        self.SearchFrame.pack(fill = X, padx = 20, pady = 10)
        
        self.SearchLabel = CTkLabel(self.SearchFrame, text = "Search by Remarks", font = ("Bookman Old Style", 20))
        self.SearchLabel.grid(row = 0, column = 0, padx = 20, pady = 10)
        
        self.Search_Var = StringVar()
        self.SearchEntry = CTkEntry(self.SearchFrame, textvariable = self.Search_Var, font = ("Bookman Old Style", 20), width = 300, corner_radius = 50)
        self.SearchEntry.grid(row = 0, column = 1, padx = 20, pady = 10)
        
        self.SearchButton = CTkButton(self.SearchFrame, command = self.Search_Data, text = "Search", cursor = "hand2", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.SearchButton.grid(row = 0, column = 2, padx = 20, pady = 10)

        #Appearance Mode Starts Here
        self.appearance_mode_label = CTkLabel(self.SearchFrame, text = "Appearance Mode:", font = ("Bookman Old Style", 20))
        self.appearance_mode_label.grid(row = 0, column = 3, padx = 20, pady = 10)
        self.appearance_mode_optionemenu = CTkOptionMenu(self.SearchFrame, font = ("Bookman Old Style", 20), values=["Dark", "Light", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row = 0, column = 4, padx = 20, pady = 10)
        #Appearance Mode Ends Here
        #Search Frame Ends Here

        #Value Frame Starts Here
        self.ValueFrame = CTkFrame(self.MainFrame, height = 100, bg_color = "transparent", corner_radius = 0)
        self.ValueFrame.pack(fill = X, padx = 20, pady = (10, 20))
        
        # self.CashInFrame = CTkFrame(self.ValueFrame, height = 80, corner_radius = 0)
        # self.CashInFrame.pack(side = LEFT, padx = (10, 5), pady = 10, fill = BOTH, expand = 1)
        
        self.CashInLabel = CTkLabel(self.ValueFrame, font = ("Bookman Old Style", 25), fg_color = "green", corner_radius = 100, text = f"Cash In\n{rd.randint(1111, 9999)}")
        self.CashInLabel.pack(fill = BOTH, expand = 1, side = LEFT, padx = 10, pady = 10)

        # self.CashOutFrame = CTkFrame(self.ValueFrame, height = 80, corner_radius = 0)
        # self.CashOutFrame.pack(side = LEFT, padx = (10, 5), pady = 10, fill = BOTH, expand = 1)

        self.CashOutLabel = CTkLabel(self.ValueFrame, font = ("Bookman Old Style", 25), fg_color = "red", corner_radius =  100, text = f"Cash Out\n{rd.randint(1111, 9999)}")
        self.CashOutLabel.pack(fill = BOTH, expand = 1, side = LEFT, padx = 10, pady = 10)

        # self.BalanceFrame = CTkFrame(self.ValueFrame, height = 0, corner_radius = 50)
        # self.BalanceFrame.pack(side = LEFT, padx = 10, pady = 10, fill = BOTH, expand = 1)

        self.BalanceLabel = CTkLabel(self.ValueFrame, font = ("Bookman Old Style", 25), fg_color = "blue", corner_radius = 100, text = f"Balance\n{rd.randint(1111, 9999)}")
        self.BalanceLabel.pack(fill = BOTH, expand = 1, side = LEFT, padx = 10, pady = 10) 
        #Value Frame Ends Here

        #Button Frame Starts Here
        self.ButtonFrame = CTkFrame(self.MainFrame, height = 0, bg_color = "transparent")
        self.ButtonFrame.pack(fill = X, padx = 20, pady = 5)
        
        self.CashInButton = CTkButton(self.ButtonFrame, text = "Cash In", command = self.CashInFunction, cursor = "hand2", width = 560, font = ("Bookman Old Style", 26), fg_color = "green", corner_radius = 50)
        self.CashInButton.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.CashOutButton = CTkButton(self.ButtonFrame, text = "Cash Out", command = self.CashOutFunction, cursor = "hand2", width = 560, font = ("Bookman Old Style", 26), fg_color = "red", corner_radius = 50)
        self.CashOutButton.grid(row = 0, column = 1, padx = 10, pady = 10)
        #Button Frame Ends Here
        
        #Data Table Frame Starts Here
        self.DataFrame = CTkFrame(self.MainFrame, corner_radius = 0, bg_color = "transparent")
        self.DataFrame.pack(fill = BOTH, expand = 1, padx = 20, pady = 10)
        
        self.DataLabel = CTkLabel(self.DataFrame, text = "All Data is Here", fg_color = "blue", corner_radius = 50, font = ("Bookman Old Style", 20))
        self.DataLabel.pack(fill = X, padx = 5, pady = 5)
        
        # self.DataTable = CTkScrollableFrame(self.DataFrame, )
        self.DFrame = CTkFrame(self.DataFrame, corner_radius = 0)
        self.DFrame.pack(fill = BOTH, expand = 1, padx = 5, pady = 5)
        
        self.y_scroll = Scrollbar(self.DFrame, orient = VERTICAL)
        self.DataTable = ttk.Treeview(self.DFrame, style="mystyle.Treeview", columns = ["date","cashbook_id","amount","remarks","action"], yscrollcommand = self.y_scroll.set)
        self.y_scroll.pack(fill = Y, side = RIGHT, padx = 5, pady = 5)
        self.y_scroll.config(command = self.DataTable.yview)
        self.DataTable.pack(fill = BOTH, expand = 1, padx = 5, pady = 5)
        
        self.DataTable.column("date", width = 100)
        self.DataTable.column("cashbook_id", width = 50)
        self.DataTable.column("amount", width = 50)
        self.DataTable.column("remarks", width = 300)
        self.DataTable.column("action", width = 100)
        
        self.DataTable["show"] = "headings"
        
        self.DataTable.heading("date", text = "Date", anchor = "w")
        self.DataTable.heading("cashbook_id", text = "Cashbook ID", anchor = "w")
        self.DataTable.heading("amount", text = "Amount", anchor = "w")
        self.DataTable.heading("remarks", text = "Remarks", anchor = "w")
        self.DataTable.heading("action", text = "Action", anchor = "w")
        self.DataTable.bind("<ButtonRelease-1>", self.UpdateWindow)
        
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Bookman Old Style', 14)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Bookman Old Style', 20, 'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'news'})])
        # style.configure("mystyle.Treeview", rows = 'odd', background='red')
        # style.configure("mystyle.Treeview", rows = 'even', background='green')
        self.ShowData()
        self.UpdateLabels()
        #Data Table Frame Ends Here

        self.DownloadExcelBtn = CTkButton(self.DataFrame, text = "Download Excel File", command = self.DownloadExcelFile, cursor = "hand2", font = ("Bookman Old Style", 15), fg_color = "red", corner_radius = 50)
        self.DownloadExcelBtn.pack(fill = X, padx = 5, pady = 5)

        self.FooterLabel = CTkLabel(self.root, text = "** CashBook | Developed by Sikandar Singh | You can Contact me on sikandarsingh2210@gmail.com for more Projects **", font = ("Bookman Old Style", 11), fg_color = "transparent")
        self.FooterLabel.pack(fill = X, side = BOTTOM)
    
    def UpdateWindow(self, event):
        self.update_window = CTkToplevel(self.root)
        self.update_window.title("Update or Delete Your CashBook")
        self.update_window.geometry("600x600+50+0")
        self.update_window.focus_force()
        self.update_window.grab_set()
        # print(time.strftime("%d/%m/%Y"))

        self.HeaderLabel = CTkLabel(self.update_window, text = "Update/Delete Your CashBook", font = ("Bookman Old Style", 34), fg_color = "transparent")
        self.HeaderLabel.pack(fill = X)
        
        self.MainFrame = CTkFrame(self.update_window, bg_color = "transparent")
        self.MainFrame.pack(fill = BOTH, expand = 1)
        
        self.updateDate = StringVar()
        self.updateID = StringVar()
        self.updateAmount = StringVar()
        self.updateRemarks = StringVar()

        self.DateLabel = CTkLabel(self.MainFrame, text = "Date", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.DateLabel.pack(pady = (20, 10))
        self.DateEntry = CTkEntry(self.MainFrame, textvariable = self.updateDate, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.DateEntry.pack(fill = X, padx = 150, pady = 5)

        self.CashbookIDLabel = CTkLabel(self.MainFrame, text = "ID", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.CashbookIDLabel.pack(pady = 10)
        self.CashbookIDEntry = CTkEntry(self.MainFrame, textvariable = self.updateID, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.CashbookIDEntry.pack(fill = X, padx = 150, pady = 5)

        self.AmountLabel = CTkLabel(self.MainFrame, text = "Amount", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.AmountLabel.pack(pady = 10)
        self.AmountEntry = CTkEntry(self.MainFrame, textvariable = self.updateAmount, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.AmountEntry.pack(fill = X, padx = 150, pady = 5)

        self.RemarksLabel = CTkLabel(self.MainFrame, text = "Remarks", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.RemarksLabel.pack(pady = 10)
        self.RemarksEntry = CTkEntry(self.MainFrame, textvariable = self.updateRemarks, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.RemarksEntry.pack(fill = X, padx = 150, pady = 5)

        self.UpdateButton = CTkButton(self.MainFrame, fg_color = "orange", command = self.UpdateSelected, text = "Update", font = ("Bookman Old Style", 22), corner_radius = 50, width = 100)
        self.UpdateButton.pack(pady = (15, 10))

        self.DeleteButton = CTkButton(self.MainFrame, fg_color = "red", command = self.DeleteSelected, text = "Delete", font = ("Bookman Old Style", 22), corner_radius = 50, width = 100)
        self.DeleteButton.pack(pady = (15, 10))

        self.ActionLabel = CTkLabel(self.MainFrame, text = f"Action : ", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.ActionLabel.pack(pady = 10)
        
        self.GetUpdateData()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        set_appearance_mode(new_appearance_mode)
        
    def CashInFunction(self):
        self.window1 = CTkToplevel(self.root)
        self.window1.title("Cash In")
        self.window1.geometry("600x600+50+0")
        self.window1.focus_force()
        self.window1.grab_set()
        # print(time.strftime("%d/%m/%Y"))
        
        self.inData_Var = StringVar()
        self.inID_Var = StringVar()
        self.inAmount_Var = StringVar()
        self.inRemarks_Var = StringVar()

        self.HeaderLabel = CTkLabel(self.window1, text = "Cash In", font = ("Bookman Old Style", 34), fg_color = "transparent")
        self.HeaderLabel.pack(fill = X)
        
        self.MainFrame = CTkFrame(self.window1, bg_color = "transparent")
        self.MainFrame.pack(fill = BOTH, expand = 1)

        self.DateLabel = CTkLabel(self.MainFrame, text = "Date", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.DateLabel.pack(pady = (20, 10))
        self.DateEntry = CTkEntry(self.MainFrame, textvariable = self.inData_Var, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.DateEntry.pack(fill = X, padx = 150, pady = 5)
        self.inData_Var.set(time.strftime("%d/%m/%Y"))

        self.CashbookIDLabel = CTkLabel(self.MainFrame, text = "ID", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.CashbookIDLabel.pack(pady = 10)
        self.CashbookIDEntry = CTkEntry(self.MainFrame, textvariable = self.inID_Var, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.CashbookIDEntry.pack(fill = X, padx = 150, pady = 5)
        self.inID_Var.set(rd.randint(1, 9999))

        self.AmountLabel = CTkLabel(self.MainFrame, text = "Amount", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.AmountLabel.pack(pady = 10)
        self.AmountEntry = CTkEntry(self.MainFrame, textvariable = self.inAmount_Var, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.AmountEntry.pack(fill = X, padx = 150, pady = 5)

        self.RemarksLabel = CTkLabel(self.MainFrame, text = "Remarks", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.RemarksLabel.pack(pady = 10)
        self.RemarksEntry = CTkEntry(self.MainFrame, textvariable = self.inRemarks_Var, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.RemarksEntry.pack(fill = X, padx = 150, pady = 5)

        self.CashInButton = CTkButton(self.MainFrame, command = self.InFunction, fg_color = "green", text = "Cash In", font = ("Bookman Old Style", 22), corner_radius = 50, width = 100)
        self.CashInButton.pack(pady = (15, 10))
        # self.ShowData()
        
    def InFunction(self):
        try:
            if self.inID_Var.get() == "" or self.inAmount_Var.get() == "" or self.inRemarks_Var.get() == "":
                msg.showerror("Error", "All fields are required", parent = self.window1)
            else:
                cur.execute("insert into CashBook_Table values (?,?,?,?,?)",(
                    self.inData_Var.get(),
                    self.inID_Var.get(),
                    self.inAmount_Var.get(),
                    self.inRemarks_Var.get(),
                    "Cash_In",
                ))
                conn.commit()
                msg.showinfo("Success", f"{self.inID_Var.get()} as been Added Successfully...", parent = self.window1)
                self.ShowData()
                self.ClearIn()
                self.UpdateLabels()
        except Exception as ex:
            msg.showerror("Error",f"Error due to {ex}", parent = self.window1)
            print(ex)

    def OutFunction(self):
        try:
            if self.outID_Var.get() == "" or self.outAmount_Var.get() == "" or self.outRemarks_Var.get() == "":
                msg.showerror("Error", "All fields are required", parent = self.window2)
            else:
                cur.execute("insert into CashBook_Table values (?,?,?,?,?)",(
                    self.outData_Var.get(),
                    self.outID_Var.get(),
                    "-"+self.outAmount_Var.get(),
                    self.outRemarks_Var.get(),
                    "Cash_Out",
                ))
                conn.commit()
                msg.showinfo("Success", f"{self.outID_Var.get()} as been Added Successfully...", parent = self.window2)
                self.ShowData()
                self.ClearOut()
                self.UpdateLabels()
        except Exception as ex:
            msg.showerror("Error",f"Error due to {ex}", parent = self.window2)
            print(ex)

    def CashOutFunction(self):
        self.window2 = CTkToplevel(self.root)
        self.window2.title("Cash Out")
        self.window2.geometry("600x600+50+0")
        self.window2.focus_force()
        self.window2.grab_set()
        # print(time.strftime("%d/%m/%Y"))

        self.outData_Var = StringVar()
        self.outID_Var = StringVar()
        self.outAmount_Var = StringVar()
        self.outRemarks_Var = StringVar()

        self.HeaderLabel = CTkLabel(self.window2, text = "Cash Out", font = ("Bookman Old Style", 34), fg_color = "transparent")
        self.HeaderLabel.pack(fill = X)
        
        self.MainFrame = CTkFrame(self.window2, bg_color = "transparent")
        self.MainFrame.pack(fill = BOTH, expand = 1)

        self.DateLabel = CTkLabel(self.MainFrame, text = "Date", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.DateLabel.pack(pady = (20, 10))
        self.DateEntry = CTkEntry(self.MainFrame, textvariable = self.outData_Var, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.DateEntry.pack(fill = X, padx = 150, pady = 5)
        self.outData_Var.set(time.strftime("%d/%m/%Y"))

        self.CashbookIDLabel = CTkLabel(self.MainFrame, text = "ID", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.CashbookIDLabel.pack(pady = 10)
        self.CashbookIDEntry = CTkEntry(self.MainFrame, textvariable = self.outID_Var, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.CashbookIDEntry.pack(fill = X, padx = 150, pady = 5)
        self.outID_Var.set(rd.randint(1, 9999))

        self.AmountLabel = CTkLabel(self.MainFrame, text = "Amount", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.AmountLabel.pack(pady = 10)
        self.AmountEntry = CTkEntry(self.MainFrame, textvariable = self.outAmount_Var, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.AmountEntry.pack(fill = X, padx = 150, pady = 5)

        self.RemarksLabel = CTkLabel(self.MainFrame, text = "Remarks", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.RemarksLabel.pack(pady = 10)
        self.RemarksEntry = CTkEntry(self.MainFrame, textvariable = self.outRemarks_Var, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.RemarksEntry.pack(fill = X, padx = 150, pady = 5)

        self.CashOutButton = CTkButton(self.MainFrame, command = self.OutFunction, fg_color = "red", text = "Cash Out", font = ("Bookman Old Style", 22), corner_radius = 50, width = 100)
        self.CashOutButton.pack(pady = (15, 10))
        
    def Search_Data(self):
        try:
            if self.Search_Var.get() == "":
                msg.showerror("Fields Error","All fields are required..", parent = self.root)
            else:
                cur.execute("select * from CashBook_Table where remarks=?",(self.Search_Var.get(),))
                result = cur.fetchall()
                self.DataTable.delete(*self.DataTable.get_children())
                for row in result:
                    self.DataTable.insert("", END, values = row)
        except Exception as ex:
            msg,showerror("Exception Error",f"Error due to {ex}", parent = self.root)


    def ShowData(self):
        try:
            cur.execute("select * from CashBook_Table")
            result = cur.fetchall()
            self.DataTable.delete(*self.DataTable.get_children())
            for row in result:
                self.DataTable.insert("", END, values = row)
        except Exception as ex:
            print(ex)

    def ClearIn(self):
        self.inData_Var.set(time.strftime("%d/%m/%Y"))
        self.inID_Var.set(rd.randint(1, 9999))
        self.inAmount_Var.set("")
        self.inRemarks_Var.set("")

    def ClearOut(self):
        self.outData_Var.set(time.strftime("%d/%m/%Y"))
        self.outID_Var.set(rd.randint(1, 9999))
        self.outAmount_Var.set("")
        self.outRemarks_Var.set("")

    def UpdateLabels(self):
        inValue = 0
        outValue = 0
        
        cur.execute("select amount from CashBook_Table where action = ?",("Cash_In",))
        InAmount = cur.fetchall()
        for i in InAmount:
            inValue += i[0]
        self.CashInLabel.configure(text = f"Cash In\n{inValue}")

        cur.execute("select amount from CashBook_Table where action = ?",("Cash_Out",))
        OutAmount = cur.fetchall()
        for a in OutAmount:
            outValue += a[0]
        self.CashOutLabel.configure(text = f"Cash Out\n{outValue}")
        
        balanceValue = inValue + outValue
        self.BalanceLabel.configure(text = f"Balance\n{balanceValue}")
        
    def DownloadExcelFile(self):
        download = msg.askyesno("Download file","Do you really want to Download File", parent = self.root)
        if download == 1:
            obj = DataToExcel()
            msg.showinfo("Download Progress", "File downloaded successfully...", parent = self.root)
        else:
            pass

    def GetUpdateData(self):
        r = self.DataTable.focus()
        content = self.DataTable.item(r)
        i = content["values"]
        
        self.updateDate.set(i[0])
        self.updateID.set(i[1])
        self.updateAmount.set(i[2])
        self.updateRemarks.set(i[3])
        self.ActionLBL = i[4]
        self.ActionLabel.configure(text = f"Action : {self.ActionLBL}")

    def UpdateSelected(self):
        try:
            if self.updateDate.get() == "" or self.updateID.get() == "" or self.updateAmount.get() == "" or self.updateRemarks.get() == "":
                msg.showerror("Error", "All fields are required..", parent = self.update_window)
            else:
                updateVal = msg.askyesno("Update","Do you really want to Update CashBook", parent = self.update_window)
                if updateVal == 1:
                    cur.execute("update CashBook_Table set date = ?, amount = ?, remarks = ? where cb_id = ?",(
                            self.updateDate.get(),
                            self.updateAmount.get(),
                            self.updateRemarks.get(),
                            self.updateID.get(),
                    ))
                    conn.commit()
                    msg.showinfo("Update", "Data has been Updated Successfull", parent = self.update_window)
                    self.ShowData()
                    self.UpdateClear()
                else:
                    pass                
        except Exception as ex:
            msg.showerror("Error", f"Error due to {ex}", parent = self.update_window)
            print(ex)
    
    def DeleteSelected(self):
        try:
            if self.updateDate.get() == "" or self.updateID.get() == "" or self.updateAmount.get() == "" or self.updateRemarks.get() == "":
                msg.showerror("Error", "All fields are required..", parent = self.update_window)
            else:
                updateVal = msg.askyesno("Delete","Do you really want to Delete CashBook", parent = self.update_window)
                if updateVal == 1:
                    cur.execute("delete from CashBook_Table where cb_id = ?",(
                            self.updateID.get(),
                    ))
                    conn.commit()
                    msg.showinfo("Delete", "Data has been Deleted Successful..", parent = self.update_window)
                    self.ShowData()
                    self.UpdateClear()
                else:
                    pass                
        except Exception as ex:
            msg.showerror("Error", f"Error due to {ex}", parent = self.update_window)
            print(ex)
            
    def UpdateClear(self):
        self.updateDate.set("")
        self.updateID.set("")
        self.updateAmount.set("")
        self.updateRemarks.set("")
        self.ActionLabel.configure(text = f"Action : ")


if __name__ == "__main__":
    root = CTk()
    obj = CashBookCustomTkinter(root)
    root.mainloop()