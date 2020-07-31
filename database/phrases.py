import sqlite3
from datetime import datetime
from random import randint
from random import choice

def add_phrases(phrase) -> object:

    # подключаемся к базе
    conn = sqlite3.connect("database/discbase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    # разобъём входную фразу на слова
    lst = phrase.split()
    i = 0
    while i < len(lst):
        el = lst[i]
        words_count = 0
        if len(lst) > 3:

            # соберём слова обратно во фразы, но со случайным количеством слов (от 1 до 7)
            words_count = randint(1, 6)
            for j in range(words_count):
                try:
                    el = el + " " + lst[i + j + 1]
                except:
                    el = el + ""
                j = j + 1

        # запишем данные в базу
        today = datetime.now()
        dt = today.strftime("%Y.%m.%d %H:%M:%S")
        phr_str = (el, str(dt))
        cursor.execute("DELETE FROM phrases WHERE phrase =?", [phr_str[0]])
        cursor.execute("INSERT INTO phrases (phrase, date) VALUES (?,?)", phr_str)
        conn.commit()
        i = i + 1 + words_count

def create_phrase(user_phr):
    """

    :rtype: object
    """
    count_find = 0
    count_table = 0

    # подкючаемся к базе
    conn = sqlite3.connect("database/discbase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    # найдём общее количество записей в таблице фраз, для того чтобы определить зону поиска
    cursor.execute('SELECT COUNT(*) FROM phrases')
    count_table = cursor.fetchone()

    len_new_phr = randint(1, 10)    # длина генерируемого ответа

    # разобьём входную фразу на слова, что провести поиск
    lst = user_phr.split()

    new_phrase = ""
    old_result = ""

    # сделаем поиск по случаному слову из сообщения
    fword = choice(lst)

    finded = False


    # и установим переключатель использования этой фразы
    fword_used = False

    # определим есть ли в базе фразы с данным словом
    cursor.execute('SELECT COUNT(*) FROM phrases WHERE phrase LIKE ?', ['%' + fword + '%'])
    count_find = cursor.fetchone()

    # если фразы есть, выгрузим их в results и выберем случайную, которую в дальнейшем и используем
    if count_find[0] != 0:
        cursor.execute('SELECT phrase FROM phrases WHERE phrase LIKE ?', ['%' + fword + '%'])
        results = cursor.fetchall()
        fresult = choice(results)[0]
        finded = True

    for i in range(len_new_phr):

        if finded == True:
            # определим вероятность использования фразы с этим словом в генерируемом сообщении
            rand_use_fword = randint(0, 10)

            # Если условия удовлетворяют, прибавим к нашему генерируемому сообщению
            if rand_use_fword > 1 and fword_used == False:
                new_phrase = new_phrase + " " + fresult
                fword_used = True

        int_id = (randint(1, count_table[0]))
        cursor.execute('SELECT phrase FROM phrases WHERE Id=?', [int_id])
        result = cursor.fetchone()
        if result != old_result:
            old_result = cursor.fetchone()
            try:
                new_phrase = new_phrase + " " + result[0]
            except Exception:
                new_phrase = new_phrase + "."

    return new_phrase
