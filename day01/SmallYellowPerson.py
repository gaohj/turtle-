import turtle

# 设置画布的大小
turtle.setup(800, 800)
turtle.speed(10)

# 1. 画身体轮廓
turtle.up()
turtle.goto(150, 150)
turtle.down()

turtle.fillcolor('#ffff00')
turtle.begin_fill()
# 顶部
turtle.left(90)
turtle.circle(150, 180)
# 中间
turtle.forward(300)
# 底部
turtle.circle(150, 180)
# 中间
turtle.forward(300)
turtle.end_fill()

# 2. 画眼睛
turtle.fillcolor('white')
turtle.begin_fill()
turtle.width(5)
turtle.up()
turtle.left(90)
turtle.fd(150)
turtle.right(90)
turtle.down()
turtle.circle(40)
turtle.left(180)
turtle.circle(40)
turtle.end_fill()

turtle.width(1)
turtle.up()
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.down()

turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()

turtle.up()
turtle.setx(50)
turtle.down()

turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()

turtle.up()
turtle.setx(80)
turtle.down()

turtle.width(20)
turtle.setx(150)

turtle.up()
turtle.setx(-80)
turtle.down()
turtle.setx(-150)


# 3. 画嘴
turtle.up()
turtle.goto(-50, 50)
turtle.left(220)
turtle.down()
turtle.pencolor('red')
turtle.width(3)
turtle.circle(80, 110)
turtle.up()


# 4. 画裤子
turtle.goto(-100, -100)
turtle.seth(0)
turtle.width(1)
turtle.pencolor('black')

turtle.fillcolor('#176185')
turtle.begin_fill()
turtle.down()
turtle.goto(100, -100)

turtle.right(90)
turtle.fd(60)
turtle.left(90)
turtle.fd(50)

turtle.up()
turtle.goto(-100, -100)
turtle.down()
turtle.right(90)
turtle.fd(60)
turtle.right(90)
turtle.fd(50)

turtle.left(90)
turtle.circle(150, 180)
turtle.end_fill()

# 5. 裤带
turtle.up()
turtle.goto(100, -110)   # 裤子端
turtle.down()
turtle.goto(150, -50)   # 肩膀端

turtle.begin_fill()
turtle.fd(15)
turtle.goto(90, -100)
turtle.goto(100, -110)
turtle.end_fill()

turtle.up()
turtle.begin_fill()
turtle.goto(-90, -100)
turtle.down()
turtle.goto(-150, -35)
turtle.back(15)
turtle.goto(-100, -113)
turtle.goto(-90, -100)
turtle.end_fill()

# 7. 画裤兜
turtle.width(4)
turtle.up()
turtle.goto(-50, -150)
turtle.down()
turtle.goto(50, -150)
turtle.back(30)
turtle.up()
turtle.goto(-50, -150)
turtle.down()
turtle.back(30)
turtle.left(180)
turtle.circle(50, 180)

# 8. 画手
# turtle.up()
# turtle.width(1)
# # turtle.pencolor('yellow')
# turtle.goto(-150, -35)
# turtle.down()
# turtle.fillcolor('yellow')
# turtle.begin_fill()
# turtle.goto(-250, -100)
# turtle.back(20)
# turtle.goto(-150, -55)
# turtle.end_fill()
#
# turtle.up()
# turtle.goto(-230, -110)
# turtle.down()
# turtle.begin_fill()
# turtle.circle(15)
# turtle.end_fill()

# 9. 画头发
turtle.up()
turtle.width(2)
turtle.goto(8, 300)
turtle.down()
turtle.goto(10, 360)

turtle.up()
turtle.goto(-8, 300)
turtle.down()
turtle.goto(-10, 370)

turtle.up()
turtle.goto(-20, 300)
turtle.down()
turtle.goto(-30, 380)

turtle.up()
turtle.goto(20, 295)
turtle.down()
turtle.goto(30, 376)

turtle.hideturtle()

# 让程序一直运行
turtle.mainloop()

