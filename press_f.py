import discord
from random import randint


def rand_pic_f():
    number = randint(1, 3)

    str_file = "forbot/press" + str(number) + ".png"

    file = discord.File(str_file, filename=str_file)

    return file