import turtle

turtle.circle(80)

# 模拟了一个抬起来的效果
# turtle.pencolor('white') #更改笔的颜色 白色
# turtle.setx(-100)  #更改坐标
#
# turtle.pencolor('green') #笔的颜色 绿色
# turtle.fd(150)  # 向前 150
#

# 方法二   
# up()   抬起笔   turtle.up()
turtle.up()
turtle.sety(-100)

# down() 放下笔   turtle.down()
turtle.down()
turtle.fd(150)


turtle.mainloop()