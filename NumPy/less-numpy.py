import numpy as np

b = np.array([[1.5, 2, 3], [4, 5, 6]], dtype=np.complex64)
print('b.ndim=', b.ndim)
print('b.shape=', b.shape)
print('b.size=', b.size)
print('b.dtype=', b.dtype)
print('b.itemsize=', b.itemsize)
print('b.data=', b.data)
print('type(b)=', type(b))

print(np.zeros((3, 5)))
print(np.ones((2, 2, 2)))
print(np.eye(5))
print(np.empty((3, 3)))
print(np.linspace(0, 2, 9))

print('='*80)
def f1(i, j):
    return i + j


print(np.fromfunction(f1, (3, 4)))
print('='*80)
print(np.arange(0, 30, 1))
print('='*80)
# np.set_printoptions(threshold=np.nan)
print('='*80)

a = np.array([20, 30, 40, 50])
b = np.arange(1, 5)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)

print('='*80)
print(a+1)
print('='*80)
print(a*2)
print('='*80)
print(a%3==0)
print('='*80)
print(np.sin(a))
print('='*80)
print(np.sum(a))
print('='*80)
print(np.min(a))
print('='*80)
b = np.array([[1.5, 2, 3], [4, 5, 6]])
print(b.max(axis=0)) # по колонкам
print('='*80)
print(b.min(axis=1)) # по рядам
print('='*80)
b = np.array([[  0, 1, 2, 3],
              [10, 11, 12, 13],
              [20, 21, 22, 23],
              [30, 31, 32, 33],
              [40, 41, 42, 43]])
print(b)
print('='*80)
print(b[2, 3])
print(b[(2,3)])
print(b[2][3])
print(b[:,2]) # колонка 2
print(b[:2]) # строки 0 и 1
print(b[1:3, : :]) # 2 и 3 строка
print('='*80)
print(b[-1])
print(b[-1, :])
print(b[-1, ...])
print('='*80)

a = np.array(([[0, 1, 2], [10, 12, 13]], [[100, 101, 102], [110, 112, 113]]))
print(a.shape)
print(a[1])
print('='*80)
for row in a:
    print(row)
    print('-'*80)
print('='*80)
for el in a.flat:
    print(el)
print('='*80)
a.ravel()  # Делает массив плоским
print(a)
print('.'*80)
a.shape = (6, 2)  # Изменение формы
print(a)
print('.'*80)
a = a.transpose()  # Транспонирование
print(a)
print('.'*80)
a = a.reshape((3, 4), order='F')  # Изменение формы
print(a)
print('.'*80)
a.resize((2, 6))
print(a)
print('='*80)
a = a.reshape((3, -1))
print(a)
print('='*80)


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.vstack((a, b))
d = np.hstack((a, b))
print(c)
print('='*80)
print(d)
print('='*80)
a1 = np.column_stack((a, b))
print(a1)
print('='*80)
a2 = np.vstack((a, b))
print(a2)
print('='*80)
a = np.arange(12).reshape((2, 6))
print(a)
print('.'*80)
a3 = np.hsplit(a, 3)
print(a3)
print('='*80)
a4 = np.hsplit(a, (3, 4))
print(a4)
print('='*80)
print('='*80)