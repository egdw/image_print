# -*- coding: utf-8 -*-
#灰度化生成法
from PIL import Image, ImageDraw, ImageFont, ImageFilter
# 输入的文件地址
image_file = Image.open("/Users/hdy/Downloads/test/3.jpg")  # open colour image

image_file = image_file.convert('L')
# 获取像素
im = image_file.load()

image = Image.new('RGB', (image_file.width, image_file.height), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Arial.ttf', 1)
# y轴间隔像素点
space = 0
# x轴间隔像素点
space2 = 0
for x in range(image_file.width):
    space = 0
    space2 += 1
    if (space2 == 6):
        space2 = 0
        for y in range(image_file.height):
            space += 1
            if (space == 12):
                color = im[x, y]
                print(color)
                if (color < 20):
                    draw.text((x, y), '$', fill=(0, 0, 0))
                elif (color < 40):
                    draw.text((x, y), "&", fill=(0, 0, 0))
                elif (color < 60):
                    draw.text((x, y), "*", fill=(0, 0, 0))
                elif (color < 80):
                    draw.text((x, y), "M", fill=(0, 0, 0))
                elif (color < 100):
                    draw.text((x, y), "A", fill=(0, 0, 0))
                elif (color < 120):
                    draw.text((x, y), "X", fill=(0, 0, 0))
                elif (color < 140):
                    draw.text((x, y), "I", fill=(0, 0, 0))
                else:
                    draw.text((x, y), ".", fill=(0, 0, 0))
                space = 0


#输出的文件地址
image.save('/Users/hdy/Downloads/test/3.png', 'png');
