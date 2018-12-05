import requests

API_KEY = 'trnsl.1.1.20181203T191747Z.5d2cfe998f0ff414.8000e3a64a41f942af7a2444f93566b86d8f280d'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def read_file(file_name):
    with open(file_name) as f:
        return f.read()


def translate(text, lang):
    response = requests.post(URL, data={'key': API_KEY, 'text': text, 'lang': lang})
    result = response.json()
    result_list = result['text']
    result_str = ''.join(result_list)
    return result_str

def write_file(file_name, text):
    with open(file_name, 'w') as f:
        f.write(text)

if __name__ == '__main__':
    read_file_name = input('Введите путь до файла, который необходимо перевести: ')
    write_file_name = input('Введите путь и имя файла, в который будет записан результ перевода: ')
    before_lang = input('Введите язык с которого необходимо перевести в виде кода,\n'
                        'например: анлгийский - en, русский - ru ')
    after_lang = input('Введите язык на который необходимо перевести в виде кода,\n'
                       'например: анлгийский - en, русский - ru ')
    lang = before_lang.lower() + '-' + after_lang.lower()
    text_tr = read_file(read_file_name)
    res_tr = translate(text_tr, lang)
    write_file(write_file_name, res_tr)