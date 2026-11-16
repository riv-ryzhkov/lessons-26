import random


def main():
    n_jeux = int(input("Введіть кількість ігор : "))

    # Створюємо масиви для зберігання результатів
    user = [0] * n_jeux
    ord_scores = [0] * n_jeux

    user_count = 0
    ord_count = 0

    jeux = int(input("\nОберіть гру (1-комп/користувач; 2-користувач/комп) : "))

    if jeux == 1:
        for i in range(n_jeux):
            user[i] = ord_sage()
            ord_scores[i] = user_sage()
    elif jeux == 2:
        for i in range(n_jeux):
            ord_scores[i] = user_sage()
            user[i] = ord_sage()
    else:
        print("GAME OVER! (((")

    for i in range(n_jeux):
        user_count += user[i]
        ord_count += ord_scores[i]

    result(user, user_count, ord_scores, ord_count, n_jeux)


def affiche(T, n):
    print(T[0], end="")
    for i in range(1, n):
        print(f" + {T[i]}", end="")


def user_choisir():
    return int(input("\nВведіть число (1...100) : "))


def usr_verifier():
    return input("\nвведіть відповідь ('=', '<', '>') : ").strip()


# комп'ютер - мудрець, а ви - провидець.
def ord_sage():
    secret_num = random.randint(1, 99)
    num = user_choisir()
    count = 1

    while num != secret_num:
        if secret_num > num:
            print("загадане число більше, ніж запропоноване >>>>>")
        else:
            print("загадане число менше, ніж запропоноване <<<<<")

        num = user_choisir()
        count += 1

    print("число відгадано!")
    print(f"кількість спроб = {count}")
    return count


# ви - мудрець, а комп'ютер - провидець.
def user_sage():
    count = 0
    print("\nзагадайте число, яке провидець має відгадати (1...100)!")
    gauche = 1  # Лівий індекс
    droite = 100  # Правий індекс
    target = '<'

    while gauche <= droite and target != '=':
        milieu = gauche + (droite - gauche) // 2  # Обчислення середнього індексу

        # Перевірка, чи шукане значення знаходиться на середньому індексі
        print(f"Комп'ютер обирає число : {milieu}")
        count += 1
        target = usr_verifier()

        if target == '<':
            droite = milieu - 1
        elif target == '>':
            gauche = milieu + 1
        elif target == '=':
            print(f"Ваше число = {milieu}")
        else:
            print("Ваша відповідь некоректна!")

    print("\nчисло відгадано!")
    print(f"кількість спроб = {count}")
    return count


def result(user, user_count, ord_scores, ord_count, n_jeux):
    print("-----------------------------------------")
    print("\n\nРЕЗУЛЬТАТ:")
    print("\nКористувач : ", end="")
    affiche(user, n_jeux)
    print(f" --> {user_count}", end="")

    print("\nКомп'ютер : ", end="")
    affiche(ord_scores, n_jeux)
    print(f" --> {ord_count}")
    print("\n==========================================")

    if user_count <= ord_count:
        print("Користувач переміг ! БРАВО!!!!!!!")
    else:
        print("Комп'ютер переміг ! На жаль...")


if __name__ == "__main__":
    main()