import discord
from random import choice
from random import randint
from database import phrases

import config
import weather
import bvid
import ozstat
import press_f
import maestro

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        channel = message.channel
        if message.author.bot == False:
            mess = '{0.content}'.format(message)
            phrases.add_phrases(mess)
            if mess.lower() == 'сукабот!':
                await channel.send("Привет! Я СукаБот. Могу рассказать какая сейчас \
                погода в интересующем вас городе. Если спросите меня Кто, я вам отвечу. Ещё ты можешь\
                попросить у меня рандомное видео с youtube.Больше я нихуя не умею.")
            elif mess.find('Погода ') == 0:
                city = mess.replace("Погода ", "")
                w_st = weather.weather_status(city)
                await channel.send(w_st)
            elif mess.find('Кто ') == 0:
                phrase = mess.replace("Кто ", "")
                phrase = phrase.replace("?", "")
                user = choice(message.channel.guild.members)
                start_phrase = ['', 'Конечно же, ', 'Несомненно, ', 'Сто пудов, ', 'Невероятно, но ', 'Да, ']
                phrase = choice(start_phrase) + user.mention + " " + phrase
                await channel.send(phrase)
            elif mess.find('Сука ютуб ') == 0:
                search_word = mess.replace("Сука ютуб ", "")
                id_yt = bvid.youtube_search(search_word)
                await channel.send(id_yt)
            elif mess.find('Жиза ') == 0:
                nick = mess.replace("Жиза ", "")
                lna_stat = ozstat.LNA(nick)
                await channel.send(lna_stat)
            elif mess.lower().find('бл') > -1 or mess.lower().find('пиз') > -1:
                phrase_kek = ['Мда', 'Ты пидр', 'Пизда', 'Ору!', 'Ди нах', 'Хуй саси', 'Ну ты и петушара', 'лох', 'Хуй', 'Букашка','Вы думаете что я вас не переиграю, что я вас не уничтожу?','Я вас уничтожу', 'Подвергнуть казни РАССТРЕЛЯНИЕМ']
                pon_phr = choice(phrase_kek)
                phr = phrases.create_phrase(pon_phr)
                await channel.send(phr)
            elif mess.lower().find('f') == 0 and len(mess) == 1:
                file = press_f.rand_pic_f()
                await message.channel.send("", file=file)
            elif mess.find('Маэстро ') == 0:
                maes = mess.replace("Маэстро ", "")
                file = maestro.put_text_pil(maes)
                if file != False:
                    await message.channel.send("", file=file)
            elif mess.find('Понас') == 0:
                pon_phr = mess.replace("Понас ", "")
                phr = phrases.create_phrase(pon_phr)
                await channel.send(phr)
            else:
                send_chance = randint(1, 10)
                if send_chance > 6:
                    phr = phrases.create_phrase(mess)
                    await channel.send(phr)

client = MyClient()
client.run(config.TOKEN)
