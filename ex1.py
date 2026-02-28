def time_from_angle(alpha):
    # Знаходимо кількість повних годин
    hours = alpha // 30

    # Залишок у градусах, який буде переведений у хвилини
    remaining_degrees = alpha % 30

    # Перетворюємо залишок градусів на хвилини
    minutes = remaining_degrees * 2

    # Цілі хвилини
    full_minutes = int(minutes)

    # Залишок у хвилинах перетворюємо на секунди
    seconds = (minutes - full_minutes) * 60

    # Округлюємо кількість секунд
    full_seconds = int(seconds)

    return int(hours), full_minutes, full_seconds


# Приклад
alpha = 90  # Кут у градусах
hours, minutes, seconds = time_from_angle(alpha)

print(f"Пройшло {hours} годин, {minutes} хвилин і {seconds} секунд.")
