import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm
import random

# Charger le jeu de données intégré de chiffres manuscrits
digits = datasets.load_digits()

# Créer le classificateur SVM
clf = svm.SVC(gamma=0.0001, C=100)

# Nombre d'images dans le jeu de données
print(len(digits.data))

# Former l'échantillon d'apprentissage (training set)
X = digits.data[:1700]
y = digits.target[:1700]

# Entraîner le modèle
clf.fit(X, y)

# pour d_img dans range(1796):
#     plt.imshow(digits.images[d_img], cmap=plt.cm.gray_r, interpolation="nearest")
#     print("Prediction:", clf.predict([digits.data[d_img]]))
#     plt.show()


for i in range(20):
    clf.predict(digits.data[-96:])
    # Prédire le chiffre pour une seule image
    d_img = random.randint(-96,-1)

    print("Prediction:", clf.predict([digits.data[d_img]]))

    # Afficher l'image
    plt.imshow(digits.images[d_img], cmap=plt.cm.gray_r, interpolation="nearest")
    plt.show()