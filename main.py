import os
from PIL import Image, ImageDraw, ImageFont

FILE_DIRECTORY = r'C:\Users\User\PycharmProjects\watermarking\Test'
FONT_FAMILY = 'Roboto.ttf'
COLOR = (255, 0, 0, 100)


def walk(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            add_watermark(root, os.path.join(root, name))


def add_watermark(root, file):
    watermark_text = 'My watermark'
    name = os.path.basename(file)

    image = Image.open(file)

    image_type = 'RGB' if image.format == 'JPEG' else 'RGBA'
    image = image.convert('RGBA')
    image_watermarker = Image.new('RGBA', image.size)

    draw = ImageDraw.Draw(image_watermarker)
    width, height = image.size
    font = ImageFont.truetype(FONT_FAMILY, int(height / 10))
    text_width, text_height = draw.textsize(watermark_text, font)
    print(text_width, text_height)
    text_x = width - text_width
    text_y = height - text_height

    draw.text((text_x, text_y), watermark_text, COLOR, font)
    result = Image.alpha_composite(image, image_watermarker)

    result.convert(image_type).save('watermark' + name)


if __name__ == '__main__':
    walk(FILE_DIRECTORY)
