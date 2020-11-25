# 安装  pip install  pillow

from PIL import Image,ImageFilter

# 1 加载图片  打开图片
# image1 = Image.open('C:/Users/neyo/Desktop/yk03/自我介绍/img/xx.jpg') #绝对路径
image1 = Image.open('../自我介绍/img/xx.jpg') #相对路径
# ../ 上一级
# ../../ 上二级
#./ 当前文件夹下面


#相对路径 和绝对路径
# # 2.显示图片
# image1.show()
#
# # 3.保存图片
# image1.save('files/canglaoshi.jpeg')
#========打开的图片.filter(滤镜效果)   返回给你一个新的图片
#浮雕效果
# image2 = image1.filter(ImageFilter.EMBOSS) #把步骤1打开的图片进行处理 放到image2里
# image2.show() #显示image2
# image2.save('files/beauty_fudiao.jpeg')

#铅笔画
# image3 = image1.filter(ImageFilter.CONTOUR) #把步骤1打开的图片进行处理 放到image3里
# image3.show() #显示image3
# image3.save('files/beauty_qianbi.jpeg')

#模糊效果
# image4 = image1.filter(ImageFilter.BLUR) #把步骤1打开的图片进行处理 放到image4里
# image4.show() #显示image4
# image4.save('files/beauty_mohu1.jpeg')


# image5 = image1.filter(ImageFilter.EDGE_ENHANCE) #把步骤1打开的图片进行处理 放到image4里
# image5.show() #显示image5
# image5.save('files/beauty_EDGE_ENHANCE.jpeg')


# image6 = image1.filter(ImageFilter.SHARPEN) #把步骤1打开的图片进行处理 放到image4里
# image6.show() #显示image5
# image6.save('files/beauty_SHARPEN.jpeg')

# 自定义效果
class WH_PYTHON(ImageFilter.BuiltinFilter):
    name = "WH_Python"
    filterargs = (3, 3), 5, 0, (
        -1, -1, -1,
        -1, 10, -1,
        -1, -1, -1,
    )

image7 = image1.filter(WH_PYTHON)
image7.show()
