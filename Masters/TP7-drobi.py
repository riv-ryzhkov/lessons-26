# 1) Функція НСД (Алгоритм Евкліда)
def pgcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


# 2) Функція НСК з використанням формули pgcd(u,v) * ppcm(u,v) = u * v
def ppcm(u, v):
    if u == 0 or v == 0:
        return 0
    return abs(u * v) // pgcd(u, v)


# 3) Створення раціонального числа (кортежу)
def cree(num, den):
    if den == 0:
        raise ValueError("Знаменник не може дорівнювати нулю.")
    return (num, den)


# 4) Введення раціонального числа користувачем
def entre():
    num = int(input("Введіть чисельник: "))
    den = int(input("Введіть знаменник: "))
    return cree(num, den)


# 5) Рядкове представлення раціонального числа
def text(r):
    return f"{r[0]}/{r[1]}"


# 6) Нормалізація раціонального числа
def normalise(r):
    num, den = r
    # Якщо знаменник від'ємний, змінюємо знаки
    if den < 0:
        num, den = -num, -den

    # Скорочуємо дріб, ділячи на НСД
    g = pgcd(num, den)
    return cree(num // g, den // g)


# 7) Тест нормалізації
def test_normalisation():
    print("--- Тест нормалізації ---")
    r = entre()
    print("Нормалізована форма:", text(normalise(r)))


# 8) Додавання і тест додавання
def plus(r1, r2):
    num1, den1 = r1
    num2, den2 = r2
    # a/b + c/d = (ad + cb) / bd
    res_num = num1 * den2 + num2 * den1
    res_den = den1 * den2
    return normalise(cree(res_num, res_den))


def test_plus():
    print("--- Тест додавання ---")
    print("Дріб 1:")
    r1 = entre()
    print("Дріб 2:")
    r2 = entre()
    print("Сума:", text(plus(r1, r2)))


# 9) Інші математичні операції
def opp(r):
    # Протилежне: -(a/b) = (-a)/b
    return normalise(cree(-r[0], r[1]))


def moins(r1, r2):
    # a - b = a + (-b)
    return plus(r1, opp(r2))


def mult(r1, r2):
    # Множення: (a/b) * (c/d) = (ac) / (bd)
    return normalise(cree(r1[0] * r2[0], r1[1] * r2[1]))


def inv(r):
    # Обернене число: 1 / (a/b) = b/a
    if r[0] == 0:
        raise ValueError("Неможливо знайти обернене число для нуля.")
    return normalise(cree(r[1], r[0]))


def div(r1, r2):
    # Ділення: a / b = a * (1/b)
    return mult(r1, inv(r2))


# 10) Меню користувача
def menu():
    while True:
        print("\n=== МЕНЮ РАЦІОНАЛЬНИХ ЧИСЕЛ ===")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Протилежне число")
        print("6. Обернене число")
        print("0. Вихід")

        choix = input("Виберіть операцію: ")

        if choix == '0':
            break
        elif choix in ['1', '2', '3', '4']:
            print("Перший дріб:")
            r1 = entre()
            print("Другий дріб:")
            r2 = entre()

            if choix == '1':
                print("Результат:", text(plus(r1, r2)))
            elif choix == '2':
                print("Результат:", text(moins(r1, r2)))
            elif choix == '3':
                print("Результат:", text(mult(r1, r2)))
            elif choix == '4':
                print("Результат:", text(div(r1, r2)))
        elif choix in ['5', '6']:
            print("Введіть дріб:")
            r = entre()
            if choix == '5':
                print("Результат:", text(opp(r)))
            elif choix == '6':
                print("Результат:", text(inv(r)))


# 11) Метод Крамера для системи рівнянь
def cramer(a1, b1, c1, a2, b2, c2):
    """
    Розв'язує систему вигляду:
    a1*x + b1*y = c1
    a2*x + b2*y = c2
    Усі аргументи — це раціональні числа (кортежі).
    """
    # det = a1*b2 - a2*b1
    det = moins(mult(a1, b2), mult(a2, b1))

    if det[0] == 0:
        return "Система не має єдиного розв'язку (визначник дорівнює нулю)"

    # detX = c1*b2 - c2*b1
    det_x = moins(mult(c1, b2), mult(c2, b1))
    # detY = a1*c2 - a2*c1
    det_y = moins(mult(a1, c2), mult(a2, c1))

    # x = detX / det
    x = div(det_x, det)
    # y = detY / det
    y = div(det_y, det)

    return text(x), text(y)

# Приклад використання методу Крамера:
# Якщо розкоментувати рядки нижче, можна протестувати рішення
# print("Рішення системи Крамера:")
# a1, b1, c1 = cree(1, 1), cree(2, 1), cree(5, 1) # 1x + 2y = 5
# a2, b2, c2 = cree(3, 1), cree(4, 1), cree(11, 1) # 3x + 4y = 11
# res_x, res_y = cramer(a1, b1, c1, a2, b2, c2)
# print(f"x = {res_x}, y = {res_y}")