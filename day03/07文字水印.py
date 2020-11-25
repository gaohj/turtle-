from PIL import Image,ImageFont,ImageDraw

#打开图片
image1 = Image.open('../玫瑰.png')
# image1.show()

# 创建字体truetype(字体文件,字号)
font = ImageFont.truetype('files/font/青呱石头体.ttf',100)

# 创建一个将文字写到图片上的对象            Draw(目标图片)
draw = ImageDraw.Draw(image1)

#渲染文字   text(坐标,文字内容,文字颜色,字体类型 ) 这种写法 顺序不能错
#渲染文字   text(坐标,文字内容,font=字体类型,fill=文字颜色) # 这种写法后两个可以调换位置
draw.text((66,66),'耗子尾汁',font=font,fill=(255,0,0,100)) #100透明读  255 完全不透明 0 完全透明

# 显示保存
image1.show()
image1.save('files/new_image1.png')