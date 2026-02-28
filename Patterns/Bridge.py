# # Абстракція, яка визначає інтерфейс для реалізації
# class Abstraction:
#     def __init__(self, implementation):
#         self._implementation = implementation
#
#     def operation(self):
#         pass
#
#
# # Конкретна абстракція
# class ConcreteAbstraction(Abstraction):
#     def operation(self):
#         return f"ConcreteAbstraction: {self._implementation.operation_implementation()}"
#
#
# # Реалізація, яка визначає інтерфейс для реалізації певного способу
# class Implementation:
#     def operation_implementation(self):
#         pass
#
#
# # Конкретна реалізація
# class ConcreteImplementationA(Implementation):
#     def operation_implementation(self):
#         return "ConcreteImplementationA"
#
#
# class ConcreteImplementationB(Implementation):
#     def operation_implementation(self):
#         return "ConcreteImplementationB"
#
#
# # Приклад використання
# if __name__ == "__main__":
#     implementation_a = ConcreteImplementationA()
#     abstraction_a = ConcreteAbstraction(implementation_a)
#     print(abstraction_a.operation())
#
#     implementation_b = ConcreteImplementationB()
#     abstraction_b = ConcreteAbstraction(implementation_b)
#     print(abstraction_b.operation())


# # ============ Квадрат та трикутник (зелені або сині) ==========
# #
# # Абстрактна Реалізація - колір
# class Color:
#     def fill_color(self):
#         pass
#
#
# # Конкретні реалізації - зелений та синій
# class GreenColor(Color):
#     def fill_color(self):
#         return "Green"
#
#
# class BlueColor(Color):
#     def fill_color(self):
#         return "Blue"
#
#
# class RedColor(Color):
#     def fill_color(self):
#         return "Red"
#
#
# # Абстракція - фігура
# class Shape:
#     def __init__(self, color):
#         self._color = color
#
#     def draw(self):
#         pass
#
#
# # Конкретні абстракції - квадрат та трикутник
# class Square(Shape):
#     def draw(self):
#         return f"Drawing a {self._color.fill_color()} square"
#
#
# class Triangle(Shape):
#     def draw(self):
#         return f"Drawing a {self._color.fill_color()} triangle"
#
# class Circle(Shape):
#     def draw(self):
#         return f"Drawing a {self._color.fill_color()} circle"
#
# # Приклад використання
# if __name__ == "__main__":
#     green_color = GreenColor()
#     blue_color = BlueColor()
#     red_color = RedColor()
#
#     green_square = Square(green_color)
#     blue_triangle = Triangle(blue_color)
#     blue_square = Square(blue_color)
#     green_triangle = Triangle(green_color)
#     red_circle = Circle(red_color)
#     red_square = Square(red_color)
#
#
#
#     # print(green_square.draw())
#     # print(blue_triangle.draw())
#     # print(blue_square.draw())
#     # print(green_triangle.draw())
#
#     shapes = [
#         blue_triangle,
#         blue_square,
#         green_square,
#         green_triangle,
#         red_square,
#         red_circle
#     ]
#
#     for sh in shapes:
#         print(sh.draw())

"""
У цьому прикладі маємо реалізацію Color, яка визначає метод fill_color, 
а також конкретні реалізації GreenColor та BlueColor, 
які успадковуються від Color і реалізують метод fill_color.

Shape є абстракцією, яка має змінну для зберігання кольору та метод draw, 
який буде реалізований в підкласах.

Square та Triangle - це конкретні абстракції, 
які успадковуються від Shape і реалізують метод draw. 
Кожна з них приймає об'єкт кольору (зелений або синій) у конструкторі.

У прикладі використання ми створюємо об'єкти GreenColor та BlueColor 
для визначення кольору. Потім створюємо об'єкт Square зі зеленим кольором 
та об'єкт Triangle з синім кольором і викликаємо їх методи draw, 
щоб отримати повідомлення про малювання квадрата та трикутника 
відповідного кольору.

Цей приклад демонструє використання патерну Міст 
для відокремлення абстракції фігур від реалізації кольорів.
"""

