# Задание 1

list_1 = input('Введите выражение через пробел: ').split()

def notif(list):
    stack = []
    op = ''
    for i in list_1:
        if i.isdigit():
            stack.append(int(i))
            continue
        else:
            op = i
            continue
    a = stack.pop()
    b = stack.pop()
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    else:
        print(b // a)

notif(list_1)

# Задание 2

number = int(input('Введите число: '))
try:
    assert number > 0
except AssertionError:
    print('Введенное число меньше нуля')

# Задание № 3

documents = [
  {"type": "passport", "number": "2207 876234",},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]

# Расширить домашние задание из лекции 1.4 «Функции — использование встроенных и создание собственных» новой функцией,
#  выводящей имена всех владельцев документов.
# С помощью исключения KeyError проверяйте, если поле "name" и документа.

def get_name_owner_doc(documents):
  for document in documents:
    try:
      print(f'Владелец документа №{document["number"]} - {document["name"]}\n')
    except KeyError:
      print('Отсутствуют поле документа или поле с именем владельца документа')

get_name_owner_doc(documents)