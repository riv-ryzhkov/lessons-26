# """
# Паттерн Strategy (стратегія) відноситься до паттернів проектування,
# які визначають сімейство алгоритмів, упаковують їх і роблять взаємозамінними.
# Цей паттерн дозволяє вибирати необхідний алгоритм в runtime,
# залежно від умови або потреби.
#
# Основна ідея використання паттерну Strategy -
# розділити функціональність на окремі класи,
# які реалізують конкретні алгоритми. Клас,
# який використовує ці алгоритми,
# має посилання на інтерфейс або абстрактний клас,
# що описує загальну поведінку.
# Потім в runtime можна обирати конкретну стратегію і передавати її в контекст.
# """

# # Абстрактний клас або інтерфейс стратегії
# class PaymentStrategy:
#     def pay(self, amount):
#         pass
#
#
# # Конкретні реалізації стратегій оплати
# class CreditCardPayment(PaymentStrategy):
#     def __init__(self, card_number, expiration_date):
#         self.card_number = card_number
#         self.expiration_date = expiration_date
#
#     def pay(self, amount):
#         print(f"Paid ${amount} with Credit Card {self.card_number}")
#
#
# class PayPalPayment(PaymentStrategy):
#     def __init__(self, email):
#         self.email = email
#
#     def pay(self, amount):
#         print(f"Paid ${amount} with PayPal ({self.email})")
#
#
# class CashPayment(PaymentStrategy):
#     def __init__(self, currency):
#         self.currency = currency
#
#     def pay(self, amount):
#         print(f"Paid ${amount} by cash in {self.currency}")
#
#
# # Клас контексту, який використовує стратегію
# class ShoppingCart:
#     def __init__(self):
#         self.items = []
#
#     def add_item(self, item):
#         self.items.append(item)
#
#     def checkout(self, payment_strategy):
#         total_amount = sum(item['price'] for item in self.items)
#         payment_strategy.pay(total_amount)
#
#
# # Приклад використання
# if __name__ == "__main__":
#     cart = ShoppingCart()
#     cart.add_item({'name': 'Apple', 'price': 20})
#     cart.add_item({'name': 'Banana', 'price': 30})
#     cart.add_item({'name': 'Orange', 'price': 70})
#     cart.add_item({'name': 'Lemon', 'price': 55})
#     print(cart.items)
#
#     # Оплата кредитною карткою
#     credit_card = CreditCardPayment('1234-5678-9876-5432', '12/26')
#     cart.checkout(credit_card)
#
#     # Оплата через PayPal
#     paypal = PayPalPayment('example@email.com')
#     cart.checkout(paypal)
#
#     cash = CashPayment('dollars')
#     cart.checkout(cash)
#
#
#
#     meth = input('<1> - credit_card, <2> - PayPal, <3> - Cash :')
#     if meth == '1':
#         pay_method = credit_card
#     elif meth == '2':
#         pay_method = paypal
#     else:
#         pay_method = cash
#
#
#     # payments = [credit_card, paypal, cash]
#     # for payment in payments:
#     #     cart.checkout(payment)
#
#     cart.checkout(pay_method)
"""
У цьому прикладі паттерн Strategy використовується 
для реалізації різних способів оплати товарів у кошику 
(кредитною карткою або через PayPal). 
Клас PaymentStrategy є абстрактним класом для стратегій оплати, 
а CreditCardPayment та PayPalPayment - 
конкретними реалізаціями стратегій.

Клас ShoppingCart представляє контекст, 
який може приймати різні стратегії оплати під час оформлення замовлення. 
Клас checkout приймає об'єкт стратегії оплати 
та виконує оплату відповідно до обраної стратегії.

Використовуючи паттерн Strategy, 
ми можемо додавати нові способи оплати, 
не змінюючи код контексту, 
що робить програму більш гнучкою та розширюваною.
"""

# # =============================================
# # Приклад калькулятора
# # =============================================
# #
# # Абстрактний клас або інтерфейс стратегії операцій
# class OperationStrategy:
#     def execute(self, a, b):
#         pass
#
#
# # Конкретні реалізації стратегій операцій
# class AdditionOperation(OperationStrategy):
#     def execute(self, a, b):
#         return a + b
#
#
# class SubtractionOperation(OperationStrategy):
#     def execute(self, a, b):
#         return a - b
#
#
# class MultiplicationOperation(OperationStrategy):
#     def execute(self, a, b):
#         return a * b
#
# class DivisionOperation(OperationStrategy):
#     def execute(self, a, b):
#         if b == 0:
#             return 'Division is impossible! b = 0!'
#         return a / b
#
#
# # Клас контексту для виконання операцій
# class Calculator:
#     def __init__(self, operation_strategy):
#         self.operation_strategy = operation_strategy
#
#     def perform_operation(self, a, b):
#         return self.operation_strategy.execute(a, b)
#
#
# # Приклад використання
# if __name__ == "__main__":
#     # Створюємо калькулятор та обираємо стратегію додавання
#     addition_strategy = AdditionOperation()
#     calculator = Calculator(addition_strategy)
#
#
#     result = calculator.perform_operation(10, 4)
#     print("Addition Result:", result)
#
#
#     # Змінюємо стратегію на віднімання
#     subtraction_strategy = SubtractionOperation()
#     calculator = Calculator(subtraction_strategy)
#
#     result = calculator.perform_operation(10, 4)
#     print("Subtraction Result:", result)
#
#     # Обираємо стратегію (все інше незмінне)
#     # a, b = 10, 4
#     a = int(input('Input first element :'))
#     b = int(input('Input second element :'))
#
#     print(f'For <{a}> and <{b}> choose action:')
#     action = int(input('Add - <1>, Sub - <2>, Div - <3>, Mult - <4>   Input action : '))
#
#     match action:
#         case 1:
#             strategy = AdditionOperation()
#         case 2:
#             strategy = SubtractionOperation()
#         case 3:
#             strategy = DivisionOperation()
#         case _:
#             strategy = MultiplicationOperation()
#
#
#     calculator.operation_strategy = strategy
#
#     result = calculator.perform_operation(a, b)
#     print('Result ->', result)