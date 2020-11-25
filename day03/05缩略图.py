from PIL import Image

# 打开图片
image1 = Image.open('../玫瑰.png')

# 设置尺寸
#thumbnail((宽,高))
image1.thumbnail((150,150))

# 显示
# image1.show()

#保存
image1.save('files/玫瑰_min.png')