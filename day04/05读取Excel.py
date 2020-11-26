import xlrd

myexcel = xlrd.open_workbook('files/test.xlsx')
# mysheetname = myexcel.sheet_names()
# mysheetname = myexcel.sheet_by_index(6) #返回的是一个整体
# mysheetname = myexcel.sheet_by_name('试题模板') #返回的依然是一个整体
# mysheet = myexcel.sheets() #返回所有的表格
# # print(mysheet)
# for x in mysheet: #挨个把表格从列表 （可以理解挨个为从箱子里边拿出酒）
#     print(x.name)  #打印该sheet的名字
# print(mysheetname.name) #打印这个整体的名字

sheet0 = myexcel.sheet_by_index(6)
print("行数:%d" % sheet0.nrows) #test.xlsx 表格1的行数
print("列数:%d" % sheet0.ncols)# test.xlsx 表格1的列数
