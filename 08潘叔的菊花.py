#向前100像素  画笔旋转 90度 再向前 100像素  形成第二条边   这样四次形成一个正方形


import turtle

turtle.speed(6) #控制速度
turtle.pencolor('red') # 画笔颜色
turtle.fillcolor('yellow') #填充颜色
turtle.begin_fill() #开始填充
for x in range(36): #需要36个正方形
    for y in range(4): #一条线画完 转化角度  4次之后形成正方形
        turtle.fd(100)
        turtle.left(90)
    turtle.right(10) #每个正方形画完以后 调整角度
turtle.end_fill() #结束填充

turtle.mainloop()