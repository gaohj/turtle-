import turtle


# 设置画布大小
turtle.setup(800,800)
turtle.speed(0)

# 1画轮廓
#1-1 顶部
turtle.up()
turtle.goto((150,150))
turtle.down()
turtle.fillcolor('#ffff00')
turtle.begin_fill()
turtle.left(90)
turtle.circle(150,180)

#1-2中间
turtle.forward(300)
#1-3底部
turtle.circle(150,180)

turtle.forward(300)
turtle.end_fill()
# 画眼睛
turtle.fillcolor('white')
turtle.begin_fill()
turtle.width(5)
turtle.up() #抬笔
turtle.left(90)
turtle.fd(150)
turtle.right(90)
turtle.down()
turtle.circle(40)
turtle.left(180)
turtle.circle(40)
turtle.end_fill()
#上面画完两只大眼睛

#中号眼睛开始
#先左眼再右眼
turtle.width(1)
turtle.up()
turtle.right(90)
turtle.fd(30)
turtle.right(90)
turtle.down()
#中号眼睛开始
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
#中号眼睛结束
#小号眼睛开始
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()
#小号眼睛结束

#开始右眼黑眼圈
turtle.up()
turtle.setx(50)
turtle.down()
#中号眼睛开始
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
#中号眼睛结束
#小号眼睛开始
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()
#小号眼睛结束
#眼镜框
#右眼镜框
turtle.up()
turtle.setx(80)
turtle.down()

turtle.width(20)
turtle.setx(150)


turtle.up()
turtle.setx(-80)
turtle.down()

turtle.width(20)
turtle.setx(-150)










# 画嘴巴

turtle.up()
turtle.goto(-50, 50)
turtle.left(220)
turtle.down()
turtle.pencolor('red')
turtle.width(3)
turtle.circle(80, 110)
turtle.up()

# 画裤子
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


#画裤带
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

#画裤兜
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


#画头发
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

turtle.up()
turtle.goto((200,200))
turtle.down()
turtle.write("我是小黄人",align="center",font=("微软雅黑",16,"normal"))
#让程序一直运行
turtle.mainloop()