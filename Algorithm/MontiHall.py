import random


def play_game(switch_choice):
    doors = [0, 1, 2]

    # де знаходиться приз
    prize = random.choice(doors)

    # вибір гравця
    choice = random.choice(doors)

    # ведучий відкриває двері без призу і не вибрані гравцем
    remaining_doors = [d for d in doors if d != choice and d != prize]
    opened = random.choice(remaining_doors)

    # якщо гравець змінює вибір
    if switch_choice:
        choice = [d for d in doors if d != choice and d != opened][0]

    # повертає True, якщо гравець виграв
    return choice == prize


def simulate(n=10000):
    stay_wins = 0
    switch_wins = 0

    for _ in range(n):
        # гра без зміни вибору
        if play_game(False):
            stay_wins += 1

        # гра зі зміною вибору
        if play_game(True):
            switch_wins += 1

    # виводимо ймовірності виграшу
    print(f"Не змінювати: {stay_wins / n:.3f}")
    print(f"Змінювати:    {switch_wins / n:.3f}")


simulate()