#原理
#前进的过程中不管改变笔的方向

# 不断  在程序中 体现出来的就是循环

#python严格区分缩进
# for x in range(10): # 10的话表示 0到10 包含 0 但是不包含10
#     print(x)    #相当于(0,10)
#
#
# for x in range(1,11):
#     print(x)

import turtle
turtle.pencolor('orange')
turtle.speed(5)
for x in range(9):
    turtle.fd(10)
    turtle.left(10)

for x in range(9):
    turtle.fd(10)
    turtle.right(10)
turtle.mainloop()