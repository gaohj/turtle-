import xlrd
import xlwt

rwb = xlrd.open_workbook('files/成绩表.xlsx')
mysheet = rwb.sheet_by_index(0)
#添加总分单元格
mysheet.put_cell(0,4,xlrd.XL_CELL_TEXT,'总分',None)
nrows = mysheet.nrows
for row in range(1,nrows):
    score = mysheet.row_values(row,1,4)
    mysheet.put_cell(row,4,xlrd.XL_CELL_NUMBER,sum(score),None)
    # mysheet.put_cell(2,4,xlrd.XL_CELL_NUMBER,sum(),None)
    # mysheet.put_cell(3,4,xlrd.XL_CELL_NUMBER,sum(),None)


mysheet.put_cell(19,0,xlrd.XL_CELL_TEXT,'平均分',None)

for col in range(1,mysheet.ncols):
    scores = mysheet.col_values(col,1,nrows)
    print(scores)
    avg = sum(scores)/len(scores)
    mysheet.put_cell(nrows,col,xlrd.XL_CELL_NUMBER,avg,None)


#编辑的实质是  读取 编辑  写入一个新的Excel文件

wwb = xlwt.Workbook(encoding='utf-8')

new_sheet = wwb.add_sheet('1班')
for row in range(mysheet.nrows):
    for col in range(mysheet.ncols):
        value = mysheet.cell_value(row,col)
        new_sheet.write(row,col,value)
wwb.save('files/新成绩表.xls')