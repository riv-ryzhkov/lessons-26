"""
Поле чудес (Wheel of Fortune) - графическая версия на Python + tkinter

Файл: Поле_чудес.py
Требования: Python 3 (tkinter входит в стандартную библиотеку), запустить: python3 Поле_чудес.py

Описание:
- Игра выбирает слово/фразу из списка (русские слова/фразы).
- Игрок может крутить барабан (spin) и получать очки, банкрот или пропуск хода.
- Игрок называет букву или угадывает слово целиком.
- При угадывании буквы открываются все вхождения и начисляются очки.
- Есть счет текущего игрока (один игрок vs компьютер можно расширить).

Комментарии в коде — на русском, поясняющие логику.
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import sys

# --- Настройки игры ---
WORDS = [
    "ПРИВЕТ МИР",
    "ПОЛЕ ЧУДЕС",
    "ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ",
    "МАШИННОЕ ОБУЧЕНИЕ",
    "ПРОГРАММИРОВАНИЕ",
    "ТЕСТОВОЕ ПРЕДЛОЖЕНИЕ",
    "НОВЫЙ ГОД",
    "КОМПЬЮТЕР",
]

WHEEL = [100, 200, 300, 400, 500, 600, 700, 800, 900, 'Банкрот', 'Пропуск']
VOWELS = set('АЕЁИОУЫЭЮЯ')

class PoleChudesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Поле чудес')
        self.geometry('700x420')
        self.resizable(False, False)

        # Переменные игры
        self.word = ''              # текущее загаданное слово (строка)
        self.display = []           # список символов для отображения (буквы или '_')
        self.revealed = set()       # набор открытых букв
        self.score = 0              # очки игрока
        self.current_spin = None    # текущее значение кручения
        self.guessed_letters = set()

        # Построение интерфейса
        self.create_widgets()
        self.new_round()

    def create_widgets(self):
        # Поле со словом (большой Label)
        self.word_label = tk.Label(self, text='', font=('Arial', 28), wraplength=650, justify='center')
        self.word_label.pack(pady=20)

        # Панель управления
        control_frame = tk.Frame(self)
        control_frame.pack(pady=10)

        # Кнопка крутить барабан
        self.spin_button = tk.Button(control_frame, text='Крутить барабан', font=('Arial', 14), command=self.spin_wheel)
        self.spin_button.grid(row=0, column=0, padx=8)

        # Отображение результата кручения
        self.spin_label = tk.Label(control_frame, text='Сделайте кручение', font=('Arial', 12))
        self.spin_label.grid(row=0, column=1, padx=8)

        # Ввод буквы
        letter_frame = tk.Frame(self)
        letter_frame.pack(pady=8)

        tk.Label(letter_frame, text='Буква:', font=('Arial', 12)).grid(row=0, column=0)
        self.letter_entry = tk.Entry(letter_frame, width=5, font=('Arial', 16), justify='center')
        self.letter_entry.grid(row=0, column=1, padx=6)

        self.guess_letter_btn = tk.Button(letter_frame, text='Угадать букву', command=self.guess_letter)
        self.guess_letter_btn.grid(row=0, column=2, padx=6)

        # Кнопка угадать слово целиком
        self.guess_word_btn = tk.Button(self, text='Угадать слово целиком', font=('Arial', 12), command=self.guess_word)
        self.guess_word_btn.pack(pady=6)

        # Информация о счёте и отгаданных буквах
        info_frame = tk.Frame(self)
        info_frame.pack(pady=6)

        self.score_label = tk.Label(info_frame, text=f'Очки: {self.score}', font=('Arial', 12))
        self.score_label.grid(row=0, column=0, padx=12)

        self.guessed_label = tk.Label(info_frame, text='Отгаданные буквы: —', font=('Arial', 12))
        self.guessed_label.grid(row=0, column=1, padx=12)

        # Кнопки помощь / новая игра / выход
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(pady=12)

        self.hint_btn = tk.Button(bottom_frame, text='Подсказка (платно: -200)', command=self.hint)
        self.hint_btn.grid(row=0, column=0, padx=8)

        self.new_game_btn = tk.Button(bottom_frame, text='Новая игра', command=self.new_round)
        self.new_game_btn.grid(row=0, column=1, padx=8)

        self.exit_btn = tk.Button(bottom_frame, text='Выход', command=self.quit_game)
        self.exit_btn.grid(row=0, column=2, padx=8)

    def new_round(self):
        """Запуск нового раунда: выбрать слово, сбросить переменные"""
        self.word = random.choice(WORDS).upper()
        # Создаем отображение: буквы заменяются на '_' (пробелы остаются)
        self.display = [ch if ch == ' ' else '_' for ch in self.word]
        self.revealed = set()
        self.score = 0
        self.current_spin = None
        self.guessed_letters = set()
        self.update_display()
        self.update_info()
        self.spin_label.config(text='Сделайте кручение')

    def update_display(self):
        """Обновить текст на экране со словом"""
        # Собираем строку для отображения: пробелы и открытые буквы показываются
        shown = ' '.join(self.display)
        self.word_label.config(text=shown)

    def update_info(self):
        """Обновить метки очков и отгаданных букв"""
        self.score_label.config(text=f'Очки: {self.score}')
        guessed = ', '.join(sorted(self.guessed_letters)) if self.guessed_letters else '—'
        self.guessed_label.config(text=f'Отгаданные буквы: {guessed}')

    def spin_wheel(self):
        """Симуляция кручения барабана"""
        result = random.choice(WHEEL)
        self.current_spin = result
        # Выводим результат
        self.spin_label.config(text=f'Выпало: {result}')

        if result == 'Банкрот':
            # Обнуление очков
            self.score = 0
            self.update_info()
            messagebox.showinfo('Банкрот', 'Увы — банкрот! Ваши очки обнуляются.')
            # В версии для одного игрока просто продолжаем
            self.current_spin = None
            self.spin_label.config(text='Сделайте кручение')
        elif result == 'Пропуск':
            messagebox.showinfo('Пропуск', 'Пропуск хода — вы теряете текущую возможность назвать букву.')
            self.current_spin = None
            self.spin_label.config(text='Сделайте кручение')
        else:
            # Игрок может назвать букву — даём возможность
            # В этой простой версии мы не реализуем очередей игроков
            pass

    def guess_letter(self):
        """Обработка угадывания буквы"""
        raw = self.letter_entry.get().strip().upper()
        self.letter_entry.delete(0, tk.END)

        if not raw:
            messagebox.showwarning('Ошибка', 'Введите букву.')
            return
        if len(raw) != 1 or not raw.isalpha():
            messagebox.showwarning('Ошибка', 'Введите одну букву (русскую).')
            return

        letter = raw
        # Не позволяйте называть одну и ту же букву дважды
        if letter in self.guessed_letters:
            messagebox.showinfo('Уже называли', f'Буква "{letter}" уже называлась.')
            return

        # Проверка был ли кручение (если результат числа) — если нет, требуем кручение
        if self.current_spin is None or self.current_spin in ('Банкрот', 'Пропуск'):
            messagebox.showinfo('Сделайте кручение', 'Сначала крутите барабан.')
            return

        self.guessed_letters.add(letter)

        if letter in self.word:
            # Открываем все вхождения буквы
            count = 0
            for i, ch in enumerate(self.word):
                if ch == letter:
                    self.display[i] = letter
                    count += 1
            # Начисляем очки: стоимость умножаем на количество вхождений
            if isinstance(self.current_spin, int):
                gained = self.current_spin * count
                self.score += gained
                messagebox.showinfo('Правильно', f'Буква "{letter}" найдена {count} раз(а). +{gained} очков')
            else:
                messagebox.showinfo('Правильно', f'Буква "{letter}" найдена {count} раз(а).')

            self.current_spin = None
            self.update_display()
            self.update_info()

            # Проверяем, угадано ли всё слово
            if '_' not in self.display:
                self.win_round()
        else:
            # Буквы нет — теряется возможность (в реальной игре меняется ход)
            messagebox.showinfo('Неправильно', f'Буквы "{letter}" нет в слове.')
            self.current_spin = None
            self.update_info()

    def guess_word(self):
        """Позволяет игроку попытаться угадать слово целиком"""
        # Спрашиваем у пользователя ввод слова через диалог
        answer = simpledialog.askstring('Угадать слово', 'Введите слово целиком:')
        if answer is None:
            return
        guess = answer.strip().upper()
        if not guess:
            return

        if guess == self.word:
            # Успех — начисляем бонус (например, 1000 очков)
            bonus = 1000
            self.score += bonus
            # раскрываем все буквы
            for i, ch in enumerate(self.word):
                self.display[i] = ch
            self.update_display()
            self.update_info()
            messagebox.showinfo('Победа', f'Вы угадали слово! +{bonus} очков')
            self.win_round()
        else:
            messagebox.showinfo('Неправильно', 'Это не то слово. Ход считается использованным.')
            # В стандартной игре ход передается — в этой одиночной версии просто сбрасываем кручение
            self.current_spin = None
            self.spin_label.config(text='Сделайте кручение')

    def win_round(self):
        """Обработка выигрыша раунда"""
        # Показать поздравление и спросить — новая игра?
        messagebox.showinfo('Раунд завершён', f'Слово было: {self.word}\nВаши очки: {self.score}')
        if messagebox.askyesno('Новая игра', 'Хотите сыграть ещё раз?'):
            self.new_round()
        else:
            self.quit_game()

    def hint(self):
        """Подсказка: открывает одну букву за плату"""
        cost = 200
        if self.score < cost:
            messagebox.showwarning('Недостаточно очков', f'Для подсказки нужно {cost} очков.')
            return

        # Выбираем случайную закрытую букву
        closed_indices = [i for i, ch in enumerate(self.display) if ch == '_']
        if not closed_indices:
            messagebox.showinfo('Нет подсказок', 'Все буквы уже открыты.')
            return

        # Находим случайную букву, которой ещё нет в revealed
        i = random.choice(closed_indices)
        letter = self.word[i]
        # Открываем все вхождения этой буквы
        for j, ch in enumerate(self.word):
            if ch == letter:
                self.display[j] = letter
        self.score -= cost
        self.update_display()
        self.update_info()
        messagebox.showinfo('Подсказка', f'Открыта буква: {letter} (стоимость {cost} очков)')

        # Проверка победы
        if '_' not in self.display:
            self.win_round()

    def quit_game(self):
        """Выход из программы"""
        if messagebox.askokcancel('Выход', 'Вы действительно хотите выйти?'):
            self.destroy()
            sys.exit()


if __name__ == '__main__':
    app = PoleChudesApp()
    app.mainloop()

# --- Пояснения (короткие) ---
# В этом коде:
# - Используется tkinter для GUI: метки, кнопки, диалоги.
# - Список WORDS содержит русские фразы; пробелы сохраняются как есть.
# - При кручении барабана назначается текущая стоимость (или спец.слово), и только
#   после кручения игрок может назвать букву.
# - Есть простая подсказка, стоящая очки, и возможность угадать слово целиком.
# - Код легко расширить: добавить нескольких игроков, подсчёт раундов, улучшенную механику очередности.
