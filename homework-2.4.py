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


search_top_word(top_word_json())
print('-' * 60)
search_top_word(top_word_xml())