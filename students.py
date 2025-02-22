class Student():
    def __init__(self, groop, name, surname, book, writing="Солнце светило", counting="5"):
        self.groop = groop
        self.name = name
        self.surname = surname
        self.book = book
        self.writing = writing
        self.counting = counting
    def write(self):
        print(f"{self.writing}")
    def count(self):
        print(f"{self.counting}")

student1 = Student("ИСП", "Вася", "Иванов", "Математика", "Мама мыла рамму", "2+2=4")
student2 = Student("АСС", "Ваня", "Иванов", "Физика")
student3 = Student("РЭУС", "Настя", "Иванов", "Химия")
student4 = Student("ИСП", "Петя", "Петров", "Русский")
print(student1.groop, student1.name, student1.surname, student1.book)
student1.write()
student1.count()
print(student2.groop, student2.name, student2.surname, student2.book)
student2.write()
student2.count()
print(student3.groop, student3.name, student3.surname, student3.book)
student3.write()
student3.count()
print(student4.groop, student4.name, student4.surname, student4.book)
student4.write()
student4.count()
