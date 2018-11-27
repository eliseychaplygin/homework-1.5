def get_components():
    file_name = input('Введите имя файла для чтения рецептов: ')
    cook_book = {}
    dish_list = []
    components_dict = {'ingridient_name': None, 'quantity': None, 'measure': None}
    with open(file_name) as f:
        for line in f:
            dish_name = line.strip()
            quantity_components = int(f.readline().strip())
            for component in range(1, quantity_components + 1):
                component = f.readline().strip().split('|')
                components_dict['ingridient_name'] =  component[0]
                components_dict['quantity'] = component[1]
                components_dict['measure'] = component[2]
                dish_list.append(components_dict.copy())
            f.readline()
            cook_book[dish_name] = dish_list
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = dishes
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for i in cook_book.get(dish):
                name_ingridient = i.get('ingridient_name')
                vol_ingridient = i.get('quantity')
                measure = i.get('measure')
                shop_list[name_ingridient] = {measure: vol_ingridient * person_count}
    return print(shop_list)

get_shop_list_by_dishes(get_components(), 2)