#图片拼接

from PIL import Image

#第一步  创建一个空白图  new(模式,大小,颜色)
# 模式  RGB/RGBA   r red 红色   g  green 绿色  b blue 蓝色   a 透明度
# (红,绿,蓝) (255,0,0) 红色  (0,255,0) 绿色  (0,0,255) 蓝色 (0,0,0) 黑色
#(255,255,255) 白色
empty = Image.new('RGB',(1500,600),(123,125,120))
# empty.show()

#第二步  打开两张图片
image1 = Image.open('../自我介绍/img/4.jpeg')
image2 = Image.open('../自我介绍/img/5.jpeg')


#第三步   把两张图片粘贴到空白图上
empty.paste(image1,(0,0))
empty.paste(image2,(700,0))

empty.show()