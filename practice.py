import requests

with open ('DE.txt') as a:
    text_1 = a.read()
with open ('ES.txt') as b:
    text_2 = b.read()
with open ('FR.txt') as c:
    text_3 = c.read()

all_text = [text_1, text_2, text_3]

def translate_it(*all_text):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    for i in all_text:

        if i == text_1:
            params = {
            'key': key,
            'lang': 'de-ru',
            'text': text_1,
             }
            response_1 = requests.get(url, params=params).json()

        elif i == text_2:
            params = {
            'key': key,
            'lang': 'es-ru',
            'text': text_2,
             }
            response_2 = requests.get(url, params=params).json()

        elif i == text_3:
            params = {
            'key': key,
            'lang': 'fr-ru',
            'text': text_3,
            }
            response_3 = requests.get(url, params=params).json()


    print_all = ' '.join(response_1.get('text', [])), ' '.join(response_2.get('text', [])) , ' '.join(response_3.get('text', []))
    with open ('texts_done.txt', 'w') as f:
        f.write(str(print_all))

#a = translate_it('Привет')
#print(a)

print(translate_it(*all_text))