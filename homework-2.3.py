import os


def search_path():
    target_dir = 'migrations'
    current_dir = os.getcwd()
    dir_dict = {}
    for dir_name in os.listdir():
        if dir_name.lower() == target_dir.lower():
            path_search = os.path.join(current_dir, target_dir)
    dir_list = os.listdir(path_search)
    for file_name in dir_list:
        dir_dict[file_name] = os.path.join(current_dir, target_dir, file_name)
    return dir_dict

def read_file(file_name):
    with open(file_name) as f:
        return f.read()

def filter_sql_files(dir_dict):
    file_sql = '.sql'
    dict_file_sql = {}
    for key, value in dir_dict.items():
        if file_sql in key:
            dict_file_sql[key] = value
    return dict_file_sql

def search_file(dir_dict):
    while True:
        filter_dict = {}
        user_input = input('Введите строку: ')
        for key, value in dir_dict.items():
            if user_input.lower() in read_file(value).lower():
                print(key)
                filter_dict[key] = value
        dir_dict = filter_dict

        print(f'Найдено {len(dir_dict)} совпадений')

search_file(filter_sql_files(search_path()))


def run_safary():
    os.system('open -a Safari')

run_safary()
