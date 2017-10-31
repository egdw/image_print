from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 二值化生成法

image_file = Image.open("/Users/hdy/Downloads/test/demo.jpg")  # open colour image

image_file = image_file.convert('L')  # convert image to black and white

threshold = 80
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

bim = image_file.point(table, '1')
bim.save('/Users/hdy/Downloads/test/demo2.jpg')
im = Image.open('/Users/hdy/Downloads/test/demo2.jpg')
pix = im.load()
width = im.size[0]
height = im.size[1]

image = Image.new('RGB', (bim.width, bim.height), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Arial.ttf', 1)
space = 0
space2 = 0
for x in range(width):
    space = 0
    space2 = space2 + 1
    if (space2 == 5):
        space2 = 0
        for y in range(height):
            color = pix[x, y]
            space = space + 1
            if (space == 5):
                if (color < 150):
                    draw.text((x, y), "&", fill=(0, 0, 0))
                else:
                    draw.text((x, y), ".", fill=(0, 0, 0))
                space = 0


image.save('/Users/hdy/Downloads/test/demo4.jpg', 'jpeg');
