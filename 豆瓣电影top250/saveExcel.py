import pickle
import xlwt

with open("dbData.txt","rb") as f:
    arr = pickle.load(f)


wb = xlwt.Workbook()  # 创建excel
ws = wb.add_sheet("豆瓣")

ws.write(0,0,"标题")
ws.write(0,1,"导演演员")
ws.write(0,2,"评分")
ws.write(0,3,"主题")
row = 1
for m in arr:
    ws.write(row,0,m[0])
    ws.write(row,1,m[1])
    ws.write(row,2,m[2])
    ws.write(row,3,m[3])
    row+=1

wb.save("dbData.xls")


