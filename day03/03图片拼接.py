from PIL import Image

#准备图片
image1 = Image.open('files/beauty.jpeg')
image2 = Image.open('files/tel.png')

# image1.show()
# image2.show()

#粘贴 图片1.paste(图片2,位置)
image1.paste(image2,(200,200))
image1.show()