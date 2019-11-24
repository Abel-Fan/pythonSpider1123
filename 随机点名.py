import xlrd,random

book = xlrd.open_workbook("python课程名单.xlsx")
sh = book.sheet_by_index(0)

arr = []

for i in range(2,40):
    arr.append(sh.cell_value(rowx=i,colx=1))
    if i<=38:
        arr.append(sh.cell_value(rowx=i,colx=3))


print(random.choice(arr))



