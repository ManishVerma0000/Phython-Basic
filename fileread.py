import xlrd

loc = "CoC_CD423240188.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
print(sheet.cell_value(0, 0))
