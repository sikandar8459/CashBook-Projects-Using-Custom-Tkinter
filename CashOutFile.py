from customtkinter import *
from tkinter import ttk
from tkinter import *
import random as rd
import time

set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class CashInClass:
    def __init__(self, root):
        self.window2 = root
        self.window2.title("Cash Out")
        self.window2.geometry("600x600+50+0")
        self.window2.focus_force()
        self.window2.grab_set()
        # print(time.strftime("%d/%m/%Y"))

        self.HeaderLabel = CTkLabel(self.window2, text = "Cash Out", font = ("Bookman Old Style", 34), fg_color = "transparent")
        self.HeaderLabel.pack(fill = X)
        
        self.MainFrame = CTkFrame(self.window2, bg_color = "transparent")
        self.MainFrame.pack(fill = BOTH, expand = 1)

        self.DateLabel = CTkLabel(self.MainFrame, text = "Date", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.DateLabel.pack(pady = (20, 10))
        self.DateEntry = CTkEntry(self.MainFrame, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.DateEntry.pack(fill = X, padx = 150, pady = 5)

        self.CashbookIDLabel = CTkLabel(self.MainFrame, text = "ID", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.CashbookIDLabel.pack(pady = 10)
        self.CashbookIDEntry = CTkEntry(self.MainFrame, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.CashbookIDEntry.pack(fill = X, padx = 150, pady = 5)

        self.AmountLabel = CTkLabel(self.MainFrame, text = "Amount", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.AmountLabel.pack(pady = 10)
        self.AmountEntry = CTkEntry(self.MainFrame, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.AmountEntry.pack(fill = X, padx = 150, pady = 5)

        self.RemarksLabel = CTkLabel(self.MainFrame, text = "Remarks", font = ("Bookman Old Style", 20), fg_color = "transparent")
        self.RemarksLabel.pack(pady = 10)
        self.RemarksEntry = CTkEntry(self.MainFrame, justify = "center", font = ("Bookman Old Style", 20), corner_radius = 50)
        self.RemarksEntry.pack(fill = X, padx = 150, pady = 5)

        self.CashOutButton = CTkButton(self.MainFrame, fg_color = "red", text = "Cash Out", font = ("Bookman Old Style", 22), corner_radius = 50, width = 100)
        self.CashOutButton.pack(pady = (15, 10))

if __name__ == "__main__":
    root = CTk()
    obj = CashOutClass(root)
    root.mainloop()