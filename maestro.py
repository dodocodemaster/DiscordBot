import numpy as np
from PIL import Image, ImageDraw, ImageFont
import discord

# создадим белое изображение
# или можно считать изобрежние с помощью cv2.imread("path_to_file")

# для простоты и совместимости возьмем пустое изображение из первого примера
# Чтобы не использовать opencv, а только PIL используйте функцию Image.open()
def put_text_pil(txt: str):
    try:
        print(txt[0])
        mnum = int(txt[0])

    except Exception:
        return False
    if mnum < 1:
        return False
    if mnum > 10:
        return False
    txt = txt[2:]


    font_size = 40
    font = ImageFont.truetype('Arialbd.ttf', size=font_size)

    imag = Image.open('maestro_pics/maestro'+str(mnum)+'.png')


    # здесь узнаем размеры сгенерированного блока текста

    y_pos = 340
    draw = ImageDraw.Draw(imag)
    w, h = draw.textsize(txt, font=font)

    # теперь можно центрировать текст
    draw.text((int((imag.size[1] - w)/2), y_pos), txt, fill='rgb(255, 255, 250)', font=font)
    imag.save('temp/img001.png')
    file = discord.File('temp/img001.png', filename='temp/img001.png')

    return file
