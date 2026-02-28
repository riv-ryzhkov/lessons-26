# class Vector:
#     """
#     Класс Вектор!
#     """
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):   # representation
#         return f"Vector({self.x}, {self.y})"
#
#     def __str__(self):    # print()
#         return f"({self.x}, {self.y})"
#
#
#     def __eq__(obj1, obj2): #  ==
#         # if obj1.x == obj2.x and obj1.y == obj2.y:
#         #     return True
#         # else:
#         #     return False
#
#         # return True if obj1.x == obj2.x and obj1.y == obj2.y else False
#         return obj1.x == obj2.x and obj1.y == obj2.y
#
#
#     def the_same(obj1, obj2): #  is
#         return id(obj1) == id(obj2)
#
#
#     def __add__(self, other): #   +
#         return Vector(self.x + other.x, self.y + other.y)
#
#
#     def __sub__(self, other):   # -
#         return Vector(self.x - other.x, self.y - other.y)
#
#
#     def len(self):   # довжина
#         return (self.x**2 + self.y**2)**(1/2)
#
#
#     def __gt__(self, other):  # >
#         return self.len() > other.len()
#
#
#     def __ge__(self, other): #  >=
#         return self.len() >= other.len()
#
#
#     def __lt__(self, other):  # <
#         return self.len() < other.len()
#
#
#     def __le__(self, other): #  <=
#         return self.len() <= other.len()
#
#
#
#
# v1 = Vector(2, 4)
#
# # print(*dir(v1), sep='\n')
# print(v1.__doc__)
# print(v1)
# print(f"vector v1 = {v1}")
#
# v2 = Vector(3, 5)
# # v2 = v1
# print(f"vector v2 = {v2}")
# print([v1, v2])
#
# print(f"v1 == v2 ->", v1 == v2)
# print(v1.the_same(v2))
# print(v1 is v2)
#
# print(f"v1 + v2 = {v1 + v2}")
# v3 = v1 + v2
# print('v3 =', v3)
#
# print(f"v2 - v1 = {v2 - v1}")
# v4 = v2 - v1
# print('v4 =', v4)
#
#
# print(f"|v1| = {v1.len()}")
#
# # print(*dir(v1), sep='\n')
# print(type(v1))
# print(v1.__class__)
# print(v1.__str__())
# print('v1 > v2', v1 > v2)
# print('v1 < v2', v1 < v2)
# print('v1 >= v2', v1 >= v2)
# print('v1 <= v2', v1 <= v2)
#
# print(v1.the_same(v2))
# print(v1 == v2)


# '''
# __eq__  ->  ==
# __ge__  ->  >=
# __gt__  ->  >
# __le__  ->  <=
# __lt__  ->  <
# __ne__  ->  NOT
# '''
#


# ===============================================================
# class UserLevel:
#     us_dict = {"Admin": 4, "Operator": 3, "Dispatcher": 2, "User": 1, "Guest": 0}
#
#     def __init__(self, user_level):
#         if user_level in self.us_dict:
#             self.u_level = user_level
#         else:
#             print("Wrong user type! ---> Guest")
#             self.u_level = "Guest"
#
#     def diff(self, level1, level2):
#         return self.us_dict[level1] - self.us_dict[level2]
#
#
#
#     def __lt__(self, user):
#         return self.diff(self.u_level, user.u_level) < 0
#
#     def __le__(self, user):
#         return self.diff(self.u_level, user.u_level) <= 0
#
#     def __eq__(self, user):
#         return self.diff(self.u_level, user.u_level) == 0
#
#     def __ge__(self, user):
#         return self.diff(self.u_level, user.u_level) >= 0
#
#     def __gt__(self, user):
#         return self.diff(self.u_level, user.u_level) > 0
#
#     def __repr__(self):
#         return f"UserLevel({self.u_level})"
#
#     def __str__(self):
#         return self.u_level
#
#     def __sub__(self, other):  # -
#         return self.diff(self.u_level, other.u_level)
#
#
# a1 = UserLevel('Operator')
# a2 = UserLevel('User')
# a3 = UserLevel('Admin')
# a4 = UserLevel('Got')
#
# print('a1 =', a1)
# print('a2(рівень доступу) =', a2)
# print('a3 =', a3)
# print('a4 =', a4)
#
# print('='*80)
# print(a1.diff('Admin', 'Guest'))
# print(a1 - a2)
# print(a1 == a2)
# print(a1 < a2)
# print(a1 > a2)
# print(a1 <= a2)
# print(a1 >= a2)
#
# users = [a1, a2, a3, a4]
#
# for user in users:
#     if user >= a1:
#         print(user, ':  Доступ надано!')
#     else:
#         print(user, ':  У доступі відмовлено!')
#
# print('*'*80)
# # # # .....................................................
#
# if __name__ == "__main__":
#
#     need = "Operator"
#     # need = "Admin"
#
#     need_level = UserLevel(need)
#     print(f"need level: {need_level.us_dict[need]}  {need}")
#
#     # user = "Dispatcher"
#     user = input('User level = ')
#     if user not in UserLevel.us_dict:
#         user = "Guest"
#     user_level = UserLevel(user)
#     print(f"user level: {user_level.us_dict.get(user)}  {user}")
#
#     if user_level.us_dict.get(user) >= need_level.us_dict.get(need):
#     # if user_level.us_dict.[user] >= need_level.us_dict[need]:
#         print("Access enabled!")
#     else:
#         print("Access denied!")