from customtkinter import *
from tkinter import ttk
from tkinter import *
import random as rd
import time

set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class UpdateDataClass:
    def __init__(self, root):
        self.update_window = root
        self.update_window.title("Cash Out")
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
        self.updateAction = ""

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

        self.CashOutButton = CTkButton(self.MainFrame, fg_color = "orange", text = "Update", font = ("Bookman Old Style", 22), corner_radius = 50, width = 100)
        self.CashOutButton.pack(pady = (15, 10))

        self.CashOutButton = CTkButton(self.MainFrame, fg_color = "red", text = "Delete", font = ("Bookman Old Style", 22), corner_radius = 50, width = 100)
        self.CashOutButton.pack(pady = (15, 10))

        self.ActionLabel = CTkLabel(self.MainFrame, text = "Action : ", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.ActionLabel.pack(pady = 10)

if __name__ == "__main__":
    root = CTk()
    obj = UpdateDataClass(root)
    root.mainloop()