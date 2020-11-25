from PIL import Image

#加载图片
image1 = Image.open('../表白.png')
# image1 = Image.open('../玫瑰.png')

#左右镜像
image_lr=image1.transpose(Image.FLIP_LEFT_RIGHT) #左右反转
image_lr.show()
# image_lr.save('files/image_lr.png')

# image_tb=image1.transpose(Image.FLIP_TOP_BOTTOM) # 上下反转
#
# #显示 保存
# image_tb.show()
# image_tb.save('files/image_tb.png')


image_lr_tb=image_lr.transpose(Image.FLIP_TOP_BOTTOM)
image_lr_tb.show()