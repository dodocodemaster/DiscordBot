#import re
import discord
#from discord import utils
from random import choice

import config
import weather
import bvid
import ozstat
import press_f

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))

	async def on_message(self, message):
		print('Message from {0.author}: {0.content}'.format(message))
		channel = message.channel
		mess = '{0.content}'.format(message)
		if mess == 'СукаБот!':
			await channel.send("Привет! Я СукаБот. Могу рассказать какая сейчас \
погода в интересующем вас городе. Если спросите меня Кто, я вам отвечу. Ещё ты можешь\
попросить у меня рандомное видео с youtube.Больше я нихуя не умею.")
		if mess.find('Погода ') == 0:
			city = mess.replace("Погода ", "")
			w_st = weather.weather_status(city)
			await channel.send(w_st)
		if mess.find('Кто ') == 0:
			phrase = mess.replace("Кто ", "")
			phrase = phrase.replace("?", "")
			user = choice(message.channel.guild.members)
			start_phrase = ['', 'Конечно же, ', 'Несомненно, ', 'Сто пудов, ', 'Невероятно, но ', 'Да, ']
			phrase = choice(start_phrase) + user.mention + " " + phrase
			await channel.send(phrase)
		if mess.find('Рандом видос') == 0:
			id_yt = bvid.youtube_search()
			await channel.send('https://www.youtube.com/watch?v='+ id_yt)	
		if mess.find('Жиза ') == 0:
			nick = mess.replace("Жиза ", "")
			lna_stat = ozstat.LNA(nick)
			await channel.send(lna_stat)
		if mess.find('бля') > -1:
			phrase_kek = ['Мда', 'Ты пидр', 'Пизда', 'Ору!', 'Ди нах', 'Хуй саси', 'Ну ты и петушара', 'Я напоминаю, что Виталька лох', 'Хуй']
			kekich = choice(phrase_kek)
			await channel.send(kekich)
		if mess.find('F') == 0 and len(mess) == 1:
			file = press_f.rand_pic_f()
			await message.channel.send("", file=file)


client = MyClient()
client.run(config.TOKEN)
