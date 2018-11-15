class Animal:

  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def feed(self):
    print(f'{self.name} накормлен(а)')

class Cattle:

  def milk(self):
    print(f'Вы подоили {self.name}')

class Bird:

  def collect_eggs(self):
    print(f'Вы собрали яйца у {self.name}')

class Cow(Animal, Cattle):

  def say(self):
    print('Муууу')

class Goat(Animal, Cattle):

  def say(self):
    print('Мееее')

class Sheep(Animal):

  def cut(self):
    print(f'Вы подстригли {self.name}')

  def say(self):
    print('Бееее')

class Chicken(Animal, Bird):

  def say(self):
    print('Ко-ко-ко')

class Duck(Animal, Bird):

  def say(self):
    print('Кря-кря')

class Duck(Animal, Bird):

  def say(self):
    print('Кря-кря')

class Goose(Animal, Bird):

  def say(self):
    print('Га-га-га')


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

goose_gray.collect_eggs()
goose_white.feed()
cow.milk()
sheep_1.cut()
sheep_2.say()
chicken_1.say()
chicken_2.collect_eggs()
goat_1.feed()
goat_2.milk()
duck.collect_eggs()

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