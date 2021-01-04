import json
import xml.etree.ElementTree as ET



def create_list_from_file_json(file_name):
    with open(file_name, encoding='utf-8') as f:
        json_data = json.load(f)
        news_list = json_data["rss"]["channel"]["items"]

    list_words = []
    for news in news_list:
        body = news["description"]
        list_words += (body.split(' '))
    return list_words

def create_list_from_file_xml(file_name):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_name, parser)
    root = tree.getroot()
    xml_news = root.findall("channel/item")

    list_words = []
    for news in xml_news:
        body = news.find("description").text
        list_words += (body.split(' '))
    return list_words


def create_top_10_words(list_words):
    list_words_big = []
    for word in list_words:
        if len(word) > 6:
            list_words_big.append(word)

    dict_words = {k: list_words_big.count(k) for k in list_words_big}
    sorted_dict = sorted(dict_words, key=dict_words.get, reverse=True)
    sorted_dict = sorted_dict[:10]

    dict_words_sorted = {}
    for k in sorted_dict:
        dict_words_sorted[k] = dict_words[k]
    for ke, ve in dict_words_sorted.items():
        print(f'{ke} - {ve} раз')
    print('')


create_top_10_words(create_list_from_file_json("files/newsafr.json"))

create_top_10_words(create_list_from_file_xml("files/newsafr.xml"))

