import random
import time

class Fish():
    def __init__(self, name, kalorii):
        self.name = name
        self.kalorii = kalorii
        print(f"{self.name} лежит, её пищевая ценность: {self.kalorii}")
    
class Cat():
    def __init__(self, name, health, life):
        self.name = name
        self.health = health
        self.life = life
        print(f"Появилась новая кошка с именем {self.name}")
        
    def eating(self, fish):
        print(f"{self.name} кушает")
        self.health += fish.kalorii
        if self.health>35:
            print(f"{self.name} наелась. Её колличество жизней увеличилось")
            self.life += 1
            self.health = 20
        elif self.health<0:
            print(f"{self.name} отравилась и голодает")
            self.life -= 1
        print(f"Здоровье: {self.health}, жизней: {self.life}")

fish1 = Fish("Форель", 20)
fish2 = Fish("Треска", 2)
fish3 = Fish("Испорченный карась", -15)

fishes = [fish1, fish2, fish3]

cat1 = Cat("Персик", 10, 1)

for i in range(10):
    f = random.choice(fishes)
    print(f"Попалась рыбка {f.name}")
    cat1.eating(f)
    time.sleep(4)
print(f"{cat1.name} устал от рыбок и уходит.")
