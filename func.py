def pr1(text):
    print('pr1 :', __name__)
    print(text.upper())
    print('=' * 30)


def pr2(text):
    print('pr2 :', __name__)
    # print('Вы только что уcпешно ввели следующий текст:', text)
    # print('Длина Вашего текста составляет ', len(text), 'символов')
    print('len =', len(text))
    print('=' * 30)


def pr3(text):
    print('pr3 :', __name__)
    # print('А вот квадрат длины Вашего текста составляет:')
    print('len**2 =', len(text)**2)
    print('='*40)


# pr1('Hello   ')
# print(__name__)

if __name__ == '__main__':
    pr1('hello')
    pr2('world')
    pr3('world')