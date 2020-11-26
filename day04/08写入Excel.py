#导入 xlwt
import xlwt
import random
#创建 workbook对象
workbook = xlwt.Workbook(encoding='utf-8')

#创建一个sheet对象
sheet = workbook.add_sheet('成绩表')

#添加表头
sheet.write(0,0,'姓名')
sheet.write(0,1,'语文')
sheet.write(0,2,'数学')
sheet.write(0,3,'英语')
for row in range(1,11):
    for col in range(4):
        sheet.write(row,col,random.randint(50,100))

#保存成Excel文件
workbook.save('files/scores.xls')