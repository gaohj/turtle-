import turtle

# turtle.circle(50)
# turtle.up()
# turtle.sety(-100)
#
# turtle.pencolor('yellow')


# turtle.dot(30)
turtle.speed(2)
#填充颜色
# 1. 设置填充颜色
turtle.fillcolor('pink')
#2.开始填充
turtle.begin_fill()
# turtle.circle(100)
turtle.fd(200)
turtle.left(100)
turtle.fd(200)
turtle.home()
#3.结束填充
turtle.end_fill()


turtle.up()
turtle.sety(-66)
turtle.down()
turtle.fillcolor('red')
turtle.begin_fill() #开始填充
turtle.fd(100)
turtle.right(130)
turtle.fd(150)
turtle.end_fill()



turtle.up()
turtle.sety(-88)
turtle.down()
turtle.fillcolor('#176185')
turtle.begin_fill() #开始填充
turtle.circle(50)
turtle.end_fill()

turtle.mainloop()