"""
Паттерн "Visitor" (Відвідувач) - це паттерн проектування,
який дозволяє додавати нові операції до об'єктів без зміни їхньої структури.
Він розділяє алгоритми від структури об'єкту,
дозволяючи створювати нові операції, не змінюючи класи об'єктів,
які підлягають обробці.

Основна ідея полягає в тому, що ми маємо два основних компоненти:

Елементи (Elements):
Це класи об'єктів, які можуть бути відвідані (піддані операції).
Вони повинні визначити метод accept,
який приймає об'єкт відвідувача і дозволяє відвідувачу взаємодіяти з цим об'єктом.

Відвідувачі (Visitors):
Це класи, які реалізують конкретні операції або алгоритми,
які мають бути виконані над об'єктами.
Вони повинні визначити методи для обробки кожного типу елементів,
які вони відвідують.

Припустимо, ми маємо ієрархію геометричних фігур (коло, квадрат, трикутник)
і хочемо реалізувати функціональність обчислення площі кожної фігури
без зміни їхніх класів.
"""


# # Базовий клас елементу (фігури)
# class Shape:
#     def accept(self, visitor):
#         pass
#
#
# # Конкретні класи елементів (фігур)
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def accept(self, visitor):
#         visitor.visit_circle(self)
#
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def accept(self, visitor):
#         visitor.visit_square(self)
#
#
# class Quatro(Shape):
#     def __init__(self, side_1, side_2):
#         self.side_1 = side_1
#         self.side_2 = side_2
#
#     def accept(self, visitor):
#         visitor.visit_quatro(self)
#
#
#
# # Базовий клас відвідувача
# class Visitor:
#     def visit_circle(self, circle):
#         pass
#
#     def visit_square(self, square):
#         pass
#
#     def visit_quatro(self, quatro):
#         pass
#
#     def get_result(self):
#         pass
#
#
#
# # Конкретний відвідувач для обчислення площі
# class AreaCalculator(Visitor):
#     def __init__(self):
#         self.total_area = 0
#
#     def visit_circle(self, circle):
#         area = 3.14 * circle.radius * circle.radius
#         self.total_area += area
#
#     def visit_square(self, square):
#         area = square.side ** 2
#         self.total_area += area
#
#     def visit_quatro(self, quatro):
#         area = quatro.side_1 * quatro.side_2
#         self.total_area += area
#
#
#     def get_result(self):
#         return self.total_area
#
#
# class PerimeterCalculator(Visitor):
#     def __init__(self):
#         self.total_area = 0
#
#     def visit_circle(self, circle):
#         area = 2 * 3.14 * circle.radius
#         self.total_area += area
#
#     def visit_square(self, square):
#         area = square.side * 4
#         self.total_area += area
#
#     def visit_quatro(self, quatro):
#         area = quatro.side_1 * quatro.side_2
#         self.total_area += area
#
#
#     def get_result(self):
#         return self.total_area
#
#
# # Приклад використання
# if __name__ == "__main__":
#     shapes = [
#         Circle(5),
#         Square(4),
#         Circle(6.56),
#         Square(100),
#         Quatro(2, 3),
#         Quatro(20, 7),
#     ]
#
#     calculator = AreaCalculator()
#     calculator_1 = PerimeterCalculator()
#
#     for shape in shapes:
#         shape.accept(calculator)
#         shape.accept(calculator_1)
#
#     # print("Total Area:", calculator.total_area)
#     print("Total Area:", calculator.get_result())
#     print("Total Perimeter:", calculator_1.get_result())
