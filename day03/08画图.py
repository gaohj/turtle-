from PIL import Image,ImageDraw
import random


#创建画布
image1 = Image.new('RGB',(800,800),(255,255,255))
# image1.show()

#创建一个画画的人
draw = ImageDraw.Draw(image1)

#画颜色  point((坐标),(颜色))
# draw.point((100,100),(255,0,0))
# draw.point((100,101),(0,255,0))


#画一条线
# for x in range(100,601): 由点汇成线
#     draw.point((100, x), (255, 0, 0))
#     draw.point((101, x), (255, 0, 0))
#     draw.point((102, x), (255, 0, 0))

#由线汇成面
# for x in range(100,601):
#     for y in range(100,301):
#         draw.point((x,y),(255, 0, 0))
# print(random.randint(1,33)) #1到 33 随机取一个数

def rand_color():
    return random.randint(1,255),random.randint(1,255),random.randint(1,255)


# print(rand_color())

for x in range(100,601): #线汇成面
    for y in range(100,301): #点汇成线
        draw.point((x,y),rand_color())
        # print(x,y)
image1.show()