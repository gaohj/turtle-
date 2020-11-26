import xlrd

#打开excel 文件
workbook = xlrd.open_workbook('files/成绩表.xlsx')

#获取目标sheet对象
sheet = workbook.sheet_by_index(0)

#获取cell相关内容
# cell = sheet.cell(0,0) # 下标从0开始   也就是第一行 第一列
# print(cell)
# cell1 = sheet.row_slice(1,1,3) #包含 第1 不包含 第3
# print(cell1)[number:78.0, number:99.0]
# for x in cell1:
#     print(x.value)
# print(sum([x.value for x in cell1]))

# cell2 = sheet.col_slice(1,1,3) #包含 第1 不包含 第3
# print(cell2)
# for x in cell2:
#     print(x.value)
# print(len(cell2))
# print(sum([x.value for x in cell2])/len(cell2))

# print(sheet.cell_value(2,2)) #第二行 第二列 单元格的值


# print(sheet.row_values(3,1,3)) #第三行的第一列到第三列的值   包含第一列  不包含第三列

# print(sheet.nrows) #19
# print(sheet.col_values(1,1,sheet.nrows))#[78.0, 98.0, 94.0, 90.0, 95.0, 99.0, 96.0, 96.0, 93.0, 90.0, 95.0, 96.0, 92.0, 90.0, 96.0, 98.0, 92.0, 99.0]
#
# scores = sheet.col_values(1,1,sheet.nrows)
# result = sum(scores)/len(scores)
# print(result)

print(sheet.cell(0,1).ctype)  # 1   姓名
print(sheet.cell(2,2).ctype)  # 2  100