import json
import xml.etree.ElementTree as ET

def top_word_json():
    with open('files/newsafr.json') as json_file:
        json_data = json.load(json_file)

    desc_list = []

    for key, value in json_data['rss']['channel'].items():
        if key == 'items':
            for i in value:
                desc_list.append(i['description'])

    sort_list = []

    for news in desc_list:
        sort_list = news.split(' ')

    sort_list.sort()

    sort_len_list = []
    for word in sort_list:
        if len(word) > 6:
            sort_len_list.append(word)

    word_dict = {}
    for word in sort_len_list:
        word_dict[word] = 0
        for re_word in sort_len_list:
            if re_word == word:
                word_dict[word] += 1

    top_word = {}
    top_word = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)

    i = 0
    while i < 10:
        print(f'Слово: {top_word[i][0]} - количество повторов: {top_word[i][1]}')
        i += 1

top_word_json()

def top_word_xml():
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('files/newsafr.xml', parser=parser)
    xml_items = tree.findall("channel/item")

    desc_list = []
    for i in xml_items:
        desc_list.append(i.find('description').text)

    for news in desc_list:
        sort_list = news.split(' ')

    sort_list.sort()

    sort_len_list = []
    for word in sort_list:
        if len(word) > 6:
            sort_len_list.append(word)

    word_dict = {}
    for word in sort_len_list:
        word_dict[word] = 0
        for re_word in sort_len_list:
            if re_word == word:
                word_dict[word] += 1

    top_word = {}
    top_word = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)

    i = 0
    while i < 10:
        print(f'Слово: {top_word[i][0]} - количество повторов: {top_word[i][1]}')
        i += 1

print('-' * 60)

top_word_xml()