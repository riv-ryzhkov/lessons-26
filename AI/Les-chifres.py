import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from sklearn import datasets, svm
import random

# 1. Préparation des données et entraînement du modèle
digits = datasets.load_digits()
clf = svm.SVC(gamma=0.0001, C=100)
X_train, y_train = digits.data[:1700], digits.target[:1700]
clf.fit(X_train, y_train)

# 2. Configuration de l'interface graphique (GUI)
root = tk.Tk()
root.title("Reconnaissance de chiffres SVM")
root.geometry("1000x1000")

# Bloc 1 : Titre et résultat
label_title = tk.Label(root, text="Test de reconnaissance", font=("Arial", 18))
label_title.pack(pady=10)

label_result = tk.Label(root, text="Appuyez sur le bouton pour commencer", font=("Arial", 24, "bold"), fg="darkblue")
label_result.pack(pady=10)



# Bloc 3 : Texte explicatif
info_text_area = tk.Text(root, height=3, width=50, font=("Arial", 14),
                         bg=root.cget('bg'), relief="flat")
info_text_area.pack(pady=10)
# Configuration des tags pour le texte
info_text_area.tag_configure("center", justify="center")
info_text_area.tag_configure("highlight", foreground="red", font=("Arial", 16, "bold"), justify="center")

# Bloc 4 : Zone pour l'image
fig, ax = plt.subplots(figsize=(4.3, 4.3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Bloc 2 : Boutons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)


def show_prediction():
    idx = random.randint(1701, 1795)
    prediction = clf.predict([digits.data[idx]])[0]
    label_result.config(text=f"Identifié comme : {prediction}")

    info_text_area.config(state="normal")
    info_text_area.delete("1.0", tk.END)
    info_text_area.insert(tk.END, "Apprentissage effectué sur 1700 images (n°1 à n°1700).\n", "center")
    info_text_area.insert(tk.END, "Identification de l'image : ", "center")
    info_text_area.insert(tk.END, f"n°{idx + 1}", "highlight")
    info_text_area.config(state="disabled")

    ax.clear()
    ax.imshow(digits.images[idx], cmap=plt.cm.gray_r, interpolation="nearest")
    ax.axis('off')
    canvas.draw()


btn_next = tk.Button(frame_buttons, text="Chiffre suivant", command=show_prediction, font=("Arial", 12), bg="#e1e1e1",
                     width=15)
btn_next.pack(side="left", padx=10)

btn_exit = tk.Button(frame_buttons, text="Quitter", command=root.destroy, font=("Arial", 12), bg="#ffcccc", width=15)
btn_exit.pack(side="left", padx=10)

# Lancement de la boucle principale
root.mainloop()