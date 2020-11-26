#验证码

#思路
#图片
#加干扰元素 背景
#图片上写入文字
from PIL import Image,ImageFont,ImageDraw,ImageFilter
import random
#创建空白图片
image1=Image.new('RGBA',(120,60),(255,255,255,200))

#创建一个画画对象
draw=ImageDraw.Draw(image1)
#渲染背景
#画点 循环->线->面
for x in range(0,120):
    for y in range(0,60):
        r=random.randint(60,255)
        g=random.randint(66,255)
        b=random.randint(88,255)
        draw.point((x,y),(r,g,b))
#给背景图 添加模糊效果
# image1=image1.filter(ImageFilter.BLUR)

#往背景图上写文字
font = ImageFont.truetype('../day03/files/font/bb.ttf',25)
#每次从数字里边 或者字母数字里边取一个 取4次
for x in range(4):
    y = random.randint(10,50)
    num = str(random.randint(0,9))
    r = random.randint(0, 120)
    g = random.randint(0, 120)
    b = random.randint(0, 200)
    draw.text((x*10,y),num,(r,g,b),font)
image1.show()