import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

# Загружаем встроенный датасет рукописных цифр
digits = datasets.load_digits()

# Создаём классификатор SVM
clf = svm.SVC(gamma=0.0001, C=100)

# Количество изображений в датасете
print(len(digits.data))

# Формируем обучающую выборку
X = digits.data[:-10]
y = digits.target[:-10]

# Обучаем модель
clf.fit(X, y)

# Предсказываем цифру для одного изображения
# d_img = -1
#
# print("Prediction:", clf.predict([digits.data[d_img]]))

# Показываем изображение



for d_img in range(1796):
    plt.imshow(digits.images[d_img], cmap=plt.cm.gray_r, interpolation="nearest")
    print("Prediction:", clf.predict([digits.data[d_img]]))
    plt.show()


