import datetime
from contextlib import contextmanager
import xml.etree.ElementTree as ET

@contextmanager
def manager_time():
    try:
        start_time = datetime.datetime.now()
        print(start_time)
        yield
    except:
        print('что-то пошло не так')
    else:
        stop_time = datetime.datetime.now()
        print(stop_time)
        res = start_time - stop_time
        print(f'На выполнение кода было потрачено {res.seconds} секунд')


def top_word_xml():
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('files/newsafr.xml', parser=parser)
    xml_items = tree.findall("channel/item")

    desc_list = []
    for i in xml_items:
        desc_list.append(i.find('description').text)

    sort_list = []
    for news in desc_list:
        for word in news.lower().split(' '):
            if len(word) > 6:
                sort_list.append(word)

    word_dict = {}
    for word in sort_list:
        word_dict[word] = 0
        for re_word in sort_list:
            if re_word == word:
                word_dict[word] += 1
    return word_dict

def search_top_word(word_dict):
    top_word = {}
    top_word = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)

    i = 0
    while i < 10:
        print(f'Слово: {top_word[i][0]} - количество повторов: {top_word[i][1]}')
        i += 1


with manager_time() as f:
    search_top_word(top_word_xml())