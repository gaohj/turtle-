from PIL import Image

#打开图片

image1 = Image.open('files/beauty.jpeg')

#剪切图片
# crop((范围))  范围:左上右下
#
image2=image1.crop((0,20,1500,800))
image2.show()
image2.save('files/cut_demo.png')