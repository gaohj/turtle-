from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#创建 空画布
image1 = Image.new('RGBA',(120,60),(255,255,255,100))
#创建一个画画的对象
draw = ImageDraw.Draw(image1)

#生成三个随机数  用来表示 颜色 r g  b
def rand_color():
    return random.randint(1,255),random.randint(1,255),random.randint(1,255)

#渲染背景
for x in range(0,120): #线汇成面
    for y in range(0,60): #点汇成线
        draw.point((x,y),rand_color())
#加一个渲染效果
# image1 = image1.filter(ImageFilter.BLUR)
# image1.show()
#渲染文字
#创建一个字体对象
font = ImageFont.truetype('files/font/aa.ttf',25)

#将0-9之间任意数字    4次 写入上面背景上
for x in range(4):
    y = random.randint(10,40)
    num = str(random.randint(0,9)) #由数值转成字符串  str()
    draw.text((x*30,y), num, font=font, fill=rand_color())
#显示保存

image1.show()