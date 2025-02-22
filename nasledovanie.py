# 3 постулата ООП: инкапсуляция, наследование, полимарфизм
# Наследование

# class Transport():
#     def __init__(self, speed, color, wheel):
#         self.speed = speed
#         self.color = color
#         self.wheel = wheel

#     def beep(self):
#         print("Beep!")

# class Car(Transport):
#     def __init__(self, speed, color, wheel, owner):
#         super().__init__(speed, color, wheel)
#         self.owner = owner
    
#     def beep(self):
#         super().beep()
#         print("Beeeeeeep!")
        
#     def get_owner(self):
#         print(f"Владелец автомобиля bmw - {self.owner}.")
    
# bmw = Car(250, "Black", 4, "Иван")
# # bmw.beep()
# bmw.get_owner()

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, school, _class):
        super().__init__(name, age)
        self.school = school
        self._class = _class
    def say_school(self):
        print(f"Моя школа - {self.school}")
    def say_class(self):
        print(f"Мой класс - {self._class}")

student1 = Student("Алексей", 14, "Гимназия №1", 7)
student1.say_school()
student1.say_class()