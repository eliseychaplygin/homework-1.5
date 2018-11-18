import random

class Animal:

  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def feed(self):
    print(f'{self.name} накормлен(а)')

  def collect(self):
    res_collect = random.randint(1, 10)
    print('Вы произвели действие с животным')
    return res_collect

  def get_hungry(self):
    if random.randint(1, 11) % 2 == 0:
      hungry = True
    else:
      hungry = False
    return hungry


class Cow(Animal):

  def say(self):
    print('Муууу')

  def collect(self):
    vol_milk = random.randint(1, 10)
    print(f'Вы подоили {self.name}')
    return vol_milk

class Goat(Animal):

  def say(self):
    print('Мееее')

  def collect(self):
    vol_milk = random.randint(1, 10)
    print(f'Вы подоили {self.name}')
    return vol_milk

class Sheep(Animal):

  def cut(self):
    vol_wool = random.randint(1, 10)
    print(f'Вы подстригли {self.name}')
    return vol_wool

  def say(self):
    print('Бееее')

  def collect(self):
    pass

class Chicken(Animal):

  def say(self):
    print('Ко-ко-ко')

  def collect(self):
    vol_egg = random.randint(1, 10)
    print(f'Вы собрали яйца у {self.name}')
    return vol_egg

class Duck(Animal):

  def say(self):
    print('Кря-кря')

  def collect(self):
    vol_egg = random.randint(1, 10)
    print(f'Вы собрали яйца у {self.name}')
    return vol_egg

class Goose(Animal):

  def say(self):
    print('Га-га-га')

  def collect(self):
    vol_egg = random.randint(1, 10)
    print(f'Вы собрали яйца у {self.name}')
    return vol_egg


goose_1 = Goose('Серый', 5)
goose_2 = Goose('Белый', 6)
cow = Cow('Манька', 35)
sheep_1 = Sheep('Барашек', 15)
sheep_2 = Sheep('Кудрявый', 13)
chicken_1 = Chicken('Ко-ко', 1)
chicken_2 = Chicken('Кукареку', 2)
goat_1 = Goat('Рога', 11)
goat_2 = Goat('Копыта', 10)
duck = Duck('Кряква', 4)
animal_list = [goose_1, goose_2, cow, sheep_1, sheep_2, chicken_1, chicken_2, goat_1, goat_2, duck]

def action_animals(animal_list):
  for animal in animal_list:
    if animal.get_hungry() == False:
      animal.feed()
    animal.collect()

def total_weight(animal_list):
  total_weight = 0
  heaviest = None
  for i in animal_list:
    total_weight += i.weight
    if heaviest == None:
      heaviest = i
    elif i.weight > heaviest.weight:
      heaviest = i
  return print(f'Общий вес животных: {total_weight}, самое тяжелое животное {heaviest.name}')

total_weight(animal_list)
action_animals(animal_list)