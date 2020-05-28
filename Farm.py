class Animals():

    def __init__(self, name, weight : float, voice):
      self.name = name
      self.weight = weight
      self.voice = voice
      Animals.farm.append(self)
      Animals.weight.append(weight)

    farm = []
    weight = []
    # max_weight = 0
    # for maximum in weight:
    #     if maximum > max_weight:
    #         max_weight = maximum


    def get_name(self):
      return self.name

    def get_weight(self):
      return self.weight

    def get_voice(self):
      return self.voice


class Geese(Animals):
  def pic_up_eggs(self):
    self.state = "Собрать яйца"


class Hen(Geese, Animals):
  pass


class Cow(Animals):
  def get_milk(self):
    self.state = "Доить"


class Goat(Cow, Animals):
  pass


class Sheep(Animals):
  def shave(self):
    self.state = "Стричь"


class Duck(Geese, Animals):
  pass

class SomeAnimal(Animals):
    def put_eat(self, value: int):
      self.weight += value
      return (f'Покормил {self.name} и но теперь весит {self.weight}')

goose_grey = SomeAnimal('гусь Серый',20,'гага')
goose_white = SomeAnimal('гусь Белый',20,'гага')
cow = SomeAnimal('корова Манька', 1000, 'мууу')
sheep_lamb = SomeAnimal('овца Барашек', 200, 'бее')
sheep_curly = SomeAnimal('овца Кудрявый', 200, 'бее')
chicken_ko= SomeAnimal('курица Ко-Ко', 10, 'ко-ко-ко')
chicken_ku = SomeAnimal('курица Кукареку', 10, 'ко-ко-ко')
Goat_Horns = SomeAnimal('коза Рога', 150, 'Меее')
Goat_Hooves = SomeAnimal('коза Копыта', 150, 'Меее')
duck = SomeAnimal('утка Кряква', 15, 'Кря-кря')


animals = [goose_grey, goose_white, cow, sheep_lamb, sheep_curly, chicken_ko, chicken_ku, Goat_Horns,Goat_Hooves, duck]

for animal in animals:
  print(f'Это {animal.get_name()} и оно весит {animal.get_weight()}')
  print(animal.put_eat(2))

# for animal in animals:
#   print(f'{animal.name} - {animal.weight}')

# for animal in animals:
#    print(animal.__class__.__name__  , animal.__dict__)

for animal in animals:
  print(f'{animal.name} - {animal.voice}')

summ_weight = 0
for animal in animals:
    summ_weight += int(animal.get_weight())
print(f'Общий вес животных после кормления: {summ_weight} кг')

print(f'Общий вес до кормления {sum(Animals.weight)}кг')

# for animal in Animals.farm:
#     if max(Animals.weight) == SomeAnimal.weight:
#        print(f"Самый тяжелый житель фермы - {animal.name}")

for animal in animals:
    if max(Animals.weight) == int(animal.get_weight()):
       print(f"Самый тяжелый житель фермы - {animal.name}")










