# # Объектно-ориентированное программирование (ООП)
# # шаблон класса
# class Car():
#     # свойства или атрибуты класса
#     color = "Red"
#     speed = 250
    
#     # способности или методы класса
#     def beep(self):
#         print("Биииииип!")

# # создание объектов
# bmw = Car()
# audi = Car()

# print(bmw.color, bmw.speed)
# bmw.beep()

# print(audi.color, audi.speed)
# audi.beep()

class Car():
    # конструктор класса
    def __init__(self, color, speed, gudok):
        self.color = color
        self.speed = speed
        self.gudok = gudok
        # print("Сработал конструктор")
    def beep(self):
        print(f'{self.gudok}')
      
bmw = Car('Black', 360, 'Bep-bep-beeep!')
audi = Car('White', 270, 'Beeeeeeep!')
print(bmw.color, bmw.speed)
bmw.beep()
print(audi.color, audi.speed)
audi.beep()

