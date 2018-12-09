from pprint import pprint

def get_cook_book(file_name):
    cook_book = {}
    dish_list = []
    with open(file_name) as f:
        for line in f:
            dish_name = line.strip()
            quantity_components = int(f.readline().strip())
            for component in range(quantity_components):
                components_dict = {'ingridient_name': None, 'quantity': None, 'measure': None}
                component = f.readline().strip().split('|')
                components_dict['ingridient_name'] =  component[0].strip()
                components_dict['quantity'] = int(component[1].strip())
                components_dict['measure'] = component[2].strip()
                dish_list.append(components_dict)
            f.readline()
            cook_book[dish_name] = dish_list
            dish_list = []
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for i in cook_book.get(dish):
                name_ingridient = i.get('ingridient_name')
                vol_ingridient = i.get('quantity')
                measure = i.get('measure')
                if name_ingridient in shop_list:
                    value = shop_list[name_ingridient]['quantity']
                    shop_list[name_ingridient]['quantity'] = value * 2
                else:
                    shop_list[name_ingridient] = {'measure': measure, 'quantity': vol_ingridient * person_count}
    return pprint(shop_list)


if __name__ == '__main__':
    file_name = input('Введите имя файла для чтения рецептов: ')
    cook_book = get_cook_book(file_name)
    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)