import sqlite3
from datetime import datetime
from random import randint
from random import choice

def add_phrases(phrase) -> object:

    # подключаемся к базе
    conn = sqlite3.connect("database/mcbase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    # разобъём входную фразу на слова
    lst = phrase.split()
    for i in range(len(lst) - 1):

        pair = (lst[i], lst[i + 1])

        # определим есть ли в базе это слово
        cursor.execute('SELECT COUNT(*) FROM pairs WHERE word1 LIKE ? AND word2 LIKE ?', pair)
        count_find = cursor.fetchone()
        if count_find[0] == 0:
            cursor.execute("INSERT INTO pairs (word1, word2) VALUES (?,?)", pair)
            conn.commit()


def create_phrase(user_phr):

    # подкючаемся к базе
    conn = sqlite3.connect("database/mcbase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    # найдём общее количество записей в таблице фраз, для того чтобы определить зону поиска
    cursor.execute('SELECT COUNT(*) FROM pairs')
    count_table = cursor.fetchone()

    len_new_phr = randint(1, 30)    # длина генерируемого ответа

    # разобьём входную фразу на слова, что провести поиск
    lst = user_phr.split()

    new_phrase = ""
    old_result = ""
    fresult = ""

    # сделаем поиск по случаному слову из сообщения
    fword = choice(lst)

    finded = False

    # определим есть ли в базе записи с данным словом
    cursor.execute('SELECT COUNT(*) FROM pairs WHERE word1 LIKE ?', [fword])
    count_find = cursor.fetchone()

    # если запись есть, выгрузим их в results
    if count_find[0] != 0:
        cursor.execute('SELECT word1,word2 FROM pairs WHERE word1 LIKE ?', [fword])
        results = cursor.fetchall()

        finded = True

    # определим вероятность использования этой пары слов в генерируемом сообщении
    rand_use_fword = randint(0, 10)

    # Если условия соблюдены, первую пару слов берём случайно из results
    # Иначе берём просто случайную пару слов из базы
    if finded == True and rand_use_fword > 4:
        fresult = choice(results)
    else:
        int_id = (randint(1, count_table[0]))
        cursor.execute('SELECT word1,word2 FROM pairs WHERE Id=?', [int_id])
        fresult = cursor.fetchone()

    new_phrase = fresult[0] + " " + fresult[1]

    # запомним последнее слово
    last_word = fresult[1]

    for i in range(len_new_phr):
        cursor.execute('SELECT word1,word2 FROM pairs WHERE word1 LIKE ?', [last_word])
        results = cursor.fetchall()
        try:
            fresult = choice(results)
            new_phrase = new_phrase + " " + fresult[1]
            last_word = fresult[1]
        except Exception:
            new_phrase = new_phrase + "."

    return new_phrase
