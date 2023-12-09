class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def add_child(self, child):
        if self.age - child.age >= 16:
            self.children.append(child)
        else:
            print(f"Ошибка: Возраст ребенка {child.name} должен быть меньше возраста родителя {self.name} хотя бы на 16 лет.")

    def info(self):
        children_names = ', '.join(child.name for child in self.children)
        print(f"Имя: {self.name}, Возраст: {self.age}, Дети: {children_names}")

    def calm_child(self, child):
        if child in self.children:
            child.calm = True
            print(f"{self.name} успокаивает {child.name}.")
        else:
            print(f"{child.name} не является ребенком {self.name}.")

    def feed_child(self, child):
        if child in self.children:
            child.hungry = False
            print(f"{self.name} кормит {child.name}.")
        else:
            print(f"{child.name} не является ребенком {self.name}.")


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm = False
        self.hungry = True

    def info(self):
        calm_status = "спокоен" if self.calm else "неспокоен"
        hungry_status = "не голоден" if not self.hungry else "голоден"
        print(f"Имя: {self.name}, Возраст: {self.age}, Состояние спокойствия: {calm_status}, Состояние голода: {hungry_status}")


parent = Parent("Анна", 40)
child1 = Child("Иван", 10)
child2 = Child("Мария", 5)

parent.add_child(child1)
parent.add_child(child2)

parent.info()
child1.info()
child2.info()

parent.calm_child(child1)
parent.feed_child(child2)

child1.info()
child2.info()