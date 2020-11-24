import turtle
# python 之所以入门简单 因为它有太多成熟的库 不需要我们重复造车

'''
#使用库 需要先安装 然后再 导入  
# pip install 库名  
'''

# 1创建 画布
turtle.setup(888,888)
# 2 设置笔
turtle.pencolor('orange') #默认是黑色
#设置线条的宽细
turtle.width(3)
# 控制笔移动的速度  1~10 由慢及快 递增  0 最快
turtle.speed(9)
#3 移动笔
#1）前进
# turtle.forward(100) #forward(100) 或者 fd(100)括号表示距离
turtle.fd(100) #forward(100) 或者 fd(100)括号表示距离
#3）后退
# turtle.back(200)
turtle.pencolor('green')
turtle.width(5)
turtle.bk(200) #后退200
# 3）移动到指定的位置
turtle.goto((100,100))
turtle.pencolor('red')
turtle.goto((-300,300))

# 修改坐标

turtle.setx(200) # y轴不变修改x轴
turtle.pencolor('yellow')
turtle.sety(-10)

#回到坐标原点

turtle.home()
#让程序一直运行
turtle.mainloop()

