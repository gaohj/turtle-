# Python操作 Excel   

## 安装  

>  读取 Excel   pip install xlrd   read 
>
>  写入Excel   pip install xlwt    write 





## 读取 Excel   

```python
import xlrd

myexcel = xlrd.open_workbook('files/test.xlsx')
mysheetname = myexcel.sheet_names()
print(mysheetname)

```



## 获取 sheet  

一个`Excel `可以有多个 `sheet`

1. `sheet_names()`: 获取所有sheet的名字  
2. `sheet_by_index`:根据所在的下标获取sheet          张三  李四  王五  张三排在第一位 因为下标从0开始 所以张三的下标是0 
3. `sheet_by_name`:根据名字获取sheet  
4. `sheets`：获取一个Excel文件中所有的sheet表格  
5. `nrows`: 获取表格的行数  
6. `ncols`:获取表格的列数  

```python
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

```



## Cell 相关操作 

> 先获取 sheet 表格  然后再获取其中的单元格

1. `sheet.cell(row,col)`: 获取指定行 row 和 列 col的 cell对象 
2. `sheet.row_slice(row,start_col,end_col)`:指定 行的 某几列的  cell对象 
3. `sheet.col_slice(col,start_row,end_row)`:获取指定列的 某几行cell对象
4. `sheet.cell_value(row,col)`:获取指定行和列的值  
5. `sheet.row_values(row,start_col,end_col)`:获取指定行的某几列的值 
6. `sheet.col_values(col,start_row,end_row)`:获取指定列的某几行的值  

```python
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

print(sheet.nrows) #19
print(sheet.col_values(1,1,sheet.nrows))#[78.0, 98.0, 94.0, 90.0, 95.0, 99.0, 96.0, 96.0, 93.0, 90.0, 95.0, 96.0, 92.0, 90.0, 96.0, 98.0, 92.0, 99.0]

scores = sheet.col_values(1,1,sheet.nrows)
result = sum(scores)/len(scores)
print(result)
```



 ps: 

​	cell.value:这个单元格中的值  

   cell.ctype:这个单元格的数据类型 

```
print(sheet.cell(0,1).ctype)  # 1   姓名    文本
print(sheet.cell(2,2).ctype)  # 2  100    数字 
```



## Cell数据类型 

1. `xlrd.XL_CELL_TEXT` 文本类型
2. `xlrd.XL_CELL_NUMBER` 数值类型
3. `xlrd.XL_CELL_DATE` 日期类型
4. `xlrd.XL_CELL_BOOLEAN` 布尔类型
5. `xlrd.XL_CELL_BLANK` 空白类型



## 写入Excel  

1. 导入 xlwt模块 
2. 创建一个workbook对象  
3. 创建有一个sheet对象 
4. 使用sheet.write(行,列,数据)方法写入到 sheet下指定的行和列中  如果想要添加新的单元格 那么就用put_cell()
5. 保存成Excel文件  

```

```

