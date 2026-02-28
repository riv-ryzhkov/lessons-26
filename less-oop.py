# import func
#
# # from func import pr2, pr1, pr3
# from func import *
#
# # from func import pr as my_print  # BS
#
#
# pr1('Hello, world!')
# pr2('Hello, world!')
# pr3('Hello, world!')
from lxml.html.builder import OBJECT


# f1('Hello!')


# print('run :', __name__)


# import math
# from math import sin, cos
# from math import sin as my_sin


# print(*dir(math), sep='\n')
# print(my_sin(3.14))
# print(cos(3.14))




##################################################################
############ Атрибуты и методы Class ##################################
#################################################################
################# Методы __init__, __str__, __repr__ ############
#################################################################

# class Human: #  StudentUniversity
#     hands = 2
#     foots = 2
#     head = 1
#
#     def __init__(self,  surname='NoSurname', age=18, sex='man', name='NoName'):
#         self.sex = sex
#         self.age = age
#         self.name = name
#         self.surname = surname
#
#
#     def __str__(self):  # print()
#         # return f'Hello, {self.name}!'
#         # return f'Human: {self.sex} {self.name} {str(self.age)} years old has {self.foots} foots'
#         return f'Human: {self.sex} {self.name} {self.surname} is {str(self.age)} years old.'
#         # return f'{self.name} {self.surname} {self.age}'
#
#
#     def __repr__(self):
#         return 'Human(' + self.name + ' ' + self.surname + ')'
#         # return 'Human(' + self.sex + ',' + self.name + ',' + self.surname + ',' + str(self.age) + ')'
#
#
# adam = Human(name = 'Adam', surname='Pupkin')
# print(adam)
# eva = Human(name = 'Eva', age=20, sex='girl', surname='Koval')
# print(eva)
# l1 = [adam, eva]
# print(l1)
#
#
#
# hum1 = Human(name='Olena', surname='Koval', age=25, sex='girl')
# hum2 = Human()
# hum3 = Human(name='Vasya')
# # print(*dir(hum1), sep='\n')
#
# print(hum1.name)
# hum1.name = 'Olga'
# print(hum1.name, hum1.surname, hum1.age, hum1.sex)
# print(hum1)
# print(hum2)
#
# my_list = [hum1, hum2]
# print(type(my_list))
# print(my_list)
# print(type(hum1.age))
# print(type(hum1.name))
# print(hum2.age + hum1.age)
# print(hum1.name[1:3])


# ######################################################################
# #   ПРИКЛАД  (з поліморфізмом та успадкуванням)   ####################
# # ####################################################################


#
# class Door:
#     colour = 'white'
#
#     def __init__(self, number=0, status='open'):
#         self.number = int(number)
#         self.status = status
#
#     def __str__(self):  # print()
#         return f'The {self.colour} door number {str(self.number)} is {self.status}'
#
#     def open(self):
#         self.status = 'open'
#
#     def close(self):
#         self.status = 'closed'
#
#     def colouring(self):
#         self.colour = input('input new colour = ')
#
#     def numbering(self):
#         num = int(input('input new number = '))
#         self.number = num
#
#     def nock(self):
#         print(f'Nock-Nock-Nock!!! in {self.number} door.')
#
#     def __add__(self, other):  # +
#         # return self.number + other.number
#         return str(self.number) + '+' + str(other.number) + '=' + str(self.number + other.number)
#
#     def __len__(self):
#         return len(str(self.number))
#
#
# door1 = Door(40)
# door2 = Door(123, 'closed')
# print(door1)
# print(door2)
#
# # door2.status = 'open'
# # print(door1)
# # print(door2)
#
# door2.open()
# print(door2)
#
# door2.close()
# print(door2)
#
# door1.nock()
# # door2.colouring()
# # door1.numbering()
# print(door1)
# print(door2)
# #
# # print(door1 + door2)
# #
# # # print(*dir(door2), sep='\n')
# #
# # print(len(door2))
# # door2.open()
# # print(door1)
# # print(door2)
# # door1.close()
# # door2.colouring()
# # door1.numbering()
# # print(door1)
# # print(door2)
# # # print(*dir(door1), sep='\n')
# # door2.nock()
# # print(len(door1))
# # print(door1 + door2)
#
#
#
# class SecurityDoor(Door):
#     colour = 'grey'
#
#     def __init__(self, number=0, status='closed', locked=True):
#         Door.__init__(self, number, status)
#         self.locked = locked
#
#     def __str__(self):
#         # return Door.__str__(self)
#         lock = 'locked' if self.locked else 'unlocked'
#         return f'The door {str(self.number)} is {self.colour}, {self.status} and {lock}'
#         # return f'the door {str(self.number)} is {self.colour}, {self.status} and {self.locked}'
#
#     def open(self):
#         if self.locked == False:
#             self.status = 'open'
#
#     def close(self):
#         self.status = 'close'
#         self.locked = True
#
#     def unlock(self):
#         self.locked = False
#
#     def lock(self):
#         self.status = 'close'
#         self.locked = True
#
#
# door5 = SecurityDoor()
# print(door5)
# door5.open()
# print(door5)
# door5.unlock()
# door5.open()
# print(door5)
# door5.lock()
# door5.colouring()
# print(door5)
# print(door5 + door2)





#
#
#
#
# d1 = SecurityDoor()
# d2 = Door()
#
# print(*dir(d2), sep='\n')

# print(type(d1), d1)
# print(type(d2), d2)
#
# d1.unlock()
# d1.open()
#
# print(d1)
#
# d1.lock()
# print(d1)
#
# d1.colouring()
# d1.numbering()
# d2.numbering()
# print(d1)
# print(d2)
#
# print(d1 + d2)

# d1.locked = False
# d1.open()
# d2.open()
# print(d1)
# print(d2)
# d1.close()
# d2.close()
# d1.numbering()
# d2.numbering()
# print(d1)
# print(d2)
# print(len(d1))
# print(d1 + d2)

# print(*dir(d1), sep='\n')


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#                УСПАДКУВАННЯ (Inheritance)
#############################################
#
# class Human:
#
#     def __init__(self, name='NoName', surname='NoSurname', age=0):
#         self.age = age
#         self.name = name
#         self.surname = surname
#
#     def __repr__(self):  # representation
#         return '=repr=' + self.name + ' ' + self.surname + ' ' + str(self.age)
#
#     def __str__(self):  # print()
#         # return '=str=   ' + self.name + ' ' + self.surname + ' ' + str(self.age)
#         return f'=str=   {self.name} {self.surname} {str(self.age)}.'
#
#
# class Student(Human):
#
#     def __init__(self, name='NoName', surname='NoSurname', age=0, group=0):
#         Human.__init__(self, name, surname, age)
#         self.group = group
#
#     def __str__(self):
#         return f'group {self.group} includs student {self.name} {self.surname}, {self.age} years old.'
#         # return '==new-str==' + super.__str__(self) + ' group ' + str(self.group)
#
#
# n1 = Human()
# n2 = Student()
# n3 = Student(age=21, name='Petya', group=555, surname="Pupkin")
# # print(n1)
# # print(n2)
# # print(n3)
#
# print(isinstance(n3, Human), type(n3))
# print(type(n3) == Human)
#
# # print(n2.group, n2.name, n2.surname, n2.age)
# # print('!!!', n2)
# # print(n3.group, n3.name, n3.surname, n3.age)
# # print(n3)
# # print(n1)
############################################################


######################################################
############ Stack (LIFO) ############################
######################################################


# class Stack:
#
#     def __init__(self):
#         self.number = None
#
#     def inp(self, x):
#         self.number = [x, self.number]
#
#     def pop(self):
#         # assert self.number is not None, 'Stack is empty'
#         if self.number == None:
#             return 'Stack is empty'
#         x = self.number[0]
#         self.number = self.number[1]
#         return x
#
#
# a = Stack()
# a.inp(input('Input element : '))
# a.inp(input('Input element : '))
# a.inp(input('Input element : '))
# a.inp(input('Input element : '))
#
# print(type(a))
# print(a.number)
#
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())



# class Stack:
#
#     def __init__(self):
#         self.number = []
#
#     def inp(self, x):
#         if self.number:
#             self.number = [x] + self.number
#         else:
#             self.number = [x]
#         # self.number.append(x)
#
#     def pop(self):
#         if not self.number:
#             return 'Stack is empty'
#         x = self.number[0]
#         self.number = self.number[1:]
#         return x
#
#
#
#
# a = Stack()
# b = Stack()
# c = Stack()
# # print(*dir(a), sep='\n')
# a.inp(input('Input element a : '))
# b.inp(input('Input element b : '))
# a.inp(input('Input element a : '))
# c.inp(input('Input element c : '))
# c.inp(input('Input element c : '))
# c.inp(input('Input element c : '))
# a.inp(input('Input element a : '))
#
#
# print(type(a))
# print(a.number)
# print(b.number)
#
# print(b.pop())
# print(b.pop())
# print(b.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(c.pop())
# print(c.pop())
# print(c.pop())
# print(c.pop())

######################################################################
###################### __del__() #################################

# class Car:
#
#     def __init__(self, model='BMW'):
#         self.model = model
#
#     def __str__(self):
#         return self.model
#
#     def __del__(self):
#         print(f'{self.model} was deleted...')
#
#
# car1 = Car('Toyota')
# car2 = Car('Honda')
# car3 = Car()
# my_car = Car('Lada')
#
#
# print(car1, 'is the best!')
# print(car2, 'is the best!')
# del car3
# # print(car3)
#
# print('\nEND of the Program!!!!!!!!!!!!\n\n')

######################################################################
###### method / @classmethod / @staticmethod #########################
######################################################################

# class ToyClass:
#     colour = 'red'
#
#     def __init__(self, name='Toy'):
#         self.name = name
#
#     def i_method(self):
#         return f'instance method called. Name of instance = {self.name}'
#
#     @classmethod
#     def c_method(cls):
#         cls.colour = 'green'
#         return f'class method called. Name of class = {cls.__name__}.'
#
#     @staticmethod
#     def s_method():
#         return 'static method called. Hello, world!'
#
#
#
# obj = ToyClass('Ball')
#
# print(obj.i_method())
# print(obj.c_method())
# print(obj.s_method())
#
# print(ToyClass.c_method())
# print(ToyClass.s_method())
#
# print(obj.colour)
#
# obj.colour = 'grey'
# print(ToyClass.c_method())
# print(ToyClass.s_method())
#
# print(obj.colour)

###################
#######################################################################
#############     ІНКАПСУЛЯЦІЯ (Encapsulation)     ####################
#######################################################################


# class StudentUniver:
#     animal = 'Human'
#
#     def __init__(self, height=170, age=18):
#         self.height = height
#         self.age = age
#         self.health = '50x50'
#
#     def __str__(self):  # PRINT
#         return f'{self.animal} Student {self.age} years old {self.height} cm fills {self.health}.'
#
#
#     def _health_change(self, health='good'):
#         self.health = health
#         return self.health
#
#     def __ill(self, health='bed'):
#         self.health = health
#         return self.health
#
#     def fill_bed(self, state):
#         self.__ill(state)
#
#     def __average__(obj1, obj2):
#         return (obj1.height + obj2.height)/2
#
#     @classmethod
#     def anim(cls, anim):
#         cls.animal = anim
#
#     @staticmethod
#     def get_hello():
#         print('Hello, world!')
#
#
# s1 = StudentUniver(200, 18)
# s2 = StudentUniver(180, 20)
# print(s1)
# print(s2)
# s1._health_change('Very nice!')
# print(s1)
# # s1.__ill('so bed!')
# s1.fill_bed('very bed!')
# print(s1)
#
# # print(*dir(s2), sep='\n')
#
# s1._StudentUniver__ill('bed!!!!')
# #
# print(s1)
# s1.animal = 'Got'
# print(StudentUniver.__average__(s1, s2))
# StudentUniver.anim('Robot')
# print(s1)
# print(s2)
#
# StudentUniver.get_hello()
# s1.get_hello()


######################################################
### School ###########################################
###     ПОЛІМОРФІЗМ (Polymorphism)    ################
######################################################

# class SchoolMember:
#     count_members = 0
#
#     def __init__(self, name='Noname', age=18, surname='NoSurname'):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         SchoolMember.count_members += 1
#         print(f'(Created SchoolMember: {self.name}). We are {SchoolMember.count_members}.', end=' ')
#
#
#     def tell(self):
#         # print(f'Name:"{self.name}" Surname:"{self.surname}" Age:"{self.age}"')
#         print(f'Name:"{self.name}" Surname:"{self.surname}" Age:"{self.age}"', end=" ")
#
#     # def __del__(self):
#     #     print(self.name, 'Deleted!!!!!!!!!!!!!')
#
#
#
# # s1 = SchoolMember()
# # s2 = SchoolMember('Jon', 19)
# # s3 = SchoolMember('Ann', 21)
# # print(s1)
# # print(s2)
# # print(s3)
# # s1.tell()
# # s2.tell()
# # s3.tell()
#
# class Teacher(SchoolMember):
#     status = '<teacher>'
#
#     def __init__(self, name='Noname', age=25, surname='NoSurname', salary=1000):
#         SchoolMember.__init__(self, name, age, surname)
#         self.salary = salary
#         print(f'(Created Teacher: {self.name}).')
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print(self.status, 'Salary: "{0:d}" grn.'.format(self.salary))
#
#
# # t1 = Teacher(name='Ben', age=45, salary=1000)
# # t2 = Teacher(name='Nick', surname='Koval', salary=5500, age=35)
# # t1.tell()
# # t2.tell()
#
#
#
# class Student(SchoolMember):
#     status = '<student>'
#
#     def __init__(self, name, age, surname='NoSurname', marks='100'):
#         SchoolMember.__init__(self, name, age, surname)
#         self.marks = marks
#         print(f'(Created Student: {self.name})')
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print(self.status, 'Mark: "{0:d}"'.format(self.marks))
#
#     def __eq__(self, other):  # ==
#         return self.marks == other.marks
#
#
#
#
#
# t1 = Teacher(name='Vasiliy', surname='Mr. Shevchenko', age=35, salary=20000)
# print(SchoolMember.count_members)
# t2 = Teacher(name='Oleg', surname='Dr. Koval', age=40, salary=30000)
# print(SchoolMember.count_members)
# s1 = Student(name='Mykola', surname='Petrov', age=20, marks=100)
# print(SchoolMember.count_members)
# s2 = Student(surname='Hmara', name='Petro', marks=90, age=19)
#
# # s2 = s1
# print(id(s1))
# print(id(s2))
# t1.tell()
# t2.tell()
# s1.tell()
# s2.tell()
# # s1.name = 'MAX'
# # print(id(s1))
# # print(id(s2))
# # s1.tell()
# # s2.tell()
#
# #
# print(SchoolMember.count_members)
#
# sm1 = SchoolMember(name='Olena', surname='Grineva', age=17)
# print(SchoolMember.count_members)
#
#
# print()
# print('='*80)
#
# members = [t1, s2, s1, t2, sm1]
#
# for member in members:
#     member.tell()
#     print('.'*80)
#
#
# # s1=s2
# # print(*dir(s1), sep='\n')
# print(s1==s2)
# print(id(s1))
# print(id(s2))

####################################### END







# a = [4, 5]
# t = ['Hello, ', 'Vasya']
# b = ['-34.56', '88.23']
# t1 = ['How do You', ' Do!']
#
# list1 = [a, b, t, t1]
#
# for el in list1:
#     print(el[0]+el[1])


# class A:
#     def __init__(self, num=0):
#         self.num = num
#
#     def add(self, num=1):
#         self.num += num
#
#
# class B(A):
#     def __init__(self, num=0):
#         A.__init__(self, num)
#         super().add(num)
#
#     def add(self, num=1):
#         self.num += 2 * num
#
#
# a = A(2)
# print(a.num)
# a.add(3)
# print(a.num)
# b = B(4)
# print(a.num, b.num)
# b.add(5)
# print(a.num, b.num)
# print(a.num + b.num)
