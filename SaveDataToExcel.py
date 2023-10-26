import sqlite3
import pandas.io.sql as sql
import xlwt
from time import gmtime, strftime

class DataToExcel:
	def __init__(self):
		self.date = strftime("%d %b %Y")

		conn = sqlite3.connect("CashBook.db")
		cur = conn.cursor()

		df = sql.read_sql("select * from CashBook_Table", conn)

		# print(df)
		# print("\n")
		# print(f"All Excel File/CashBook Details {strftime('%Y%d')} at {strftime('%H%M%S')}.xls")

		df.to_excel(f"CashBook Details{strftime('%b-%d-%Y')}.xls")

if __name__ == '__main__':
	obj = DataToExcel()