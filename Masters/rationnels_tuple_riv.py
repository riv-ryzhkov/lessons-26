""" création d'un type rationnel avec un tuple """

def pgcd(a: int, b: int) -> int:
    """ calcule le pgcd de a et b """
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def ppcm(a: int, b: int) -> int:   # Plus Petit Commun Multiple
    """ calcule le ppcm de a et b """
    return a * (b // pgcd(a, b))


def normalise(r: tuple[int, int]) -> tuple[int, int]:
    """ normalise un rationnel """
    num, den = r
    if den < 0:
        num, den = -num, -den
    d = pgcd(num, den)
    return (num // d, den // d)


def cree(num: int, den: int) -> tuple[int, int]:
    """ crée un rationnel sous forme de tuple (num, den) """
    if den == 0:
        raise ValueError("Le dénominateur ne peut pas être nul.")
    r = (num, den)
    return normalise(r)


def entree(message: str = "Entrez un rationnel : ") -> tuple[int, int]:
    """ demande à l'utilisateur de saisir un rationnel """
    print(message, end="")
    num = int(input("Entrez le numérateur : "))
    den = int(input("Entrez le dénominateur : "))
    return cree(num, den)


def text(r: tuple[int, int]) -> str:
    """ retourne une représentation sous forme de chaîne du rationnel """
    return f"{r[0]}/{r[1]}"


def test1() -> None:
    """ test de la fonction cree """
    r = cree(2, 4)
    assert r == (1, 2), f"Erreur : {r} != (1, 2)"
    r = cree(-2, 4)
    assert r == (-1, 42), f"Erreur : {r} != (-1, 2)"
    r = cree(2, -4)
    assert r == (-1, 2), f"Erreur : {r} != (-1, 2)"
    r = cree(-2, -4)
    assert r == (1, 2), f"Erreur : {r} != (1, 2)"
    n = int(input("Entrez un numérateur pour le test : "))
    d = int(input("Entrez un dénominateur pour le test : "))
    r = cree(n, d)
    print(f"Le rationnel saisi (normalisé) est : {text(r)}")


def plus(r1: tuple[int, int], r2: tuple[int, int]) -> tuple[int, int]:
    """ additionne deux rationnels avec simplification par pgcd et ppcm """
    pg = pgcd(r1[1], r2[1])
    pp = (r1[1] // pg) * r2[1]
    num = r1[0] * (r2[1] // pg) + r2[0] * (r1[1] // pg)
    den = pp
    return cree(num, den)


def plus1(r1: tuple[int, int], r2: tuple[int, int]) -> tuple[int, int]:
    """ additionne deux rationnels directement sans simplification """
    num = r1[0] * r2[1] + r2[0] * r1[1]
    den = r1[1] * r2[1]
    return cree(num, den)


def test2() -> None:
    """ test de la fonction plus """
    r1 = cree(1, 2)
    r2 = cree(1, 3)
    r3 = plus(r1, r2)
    assert r3 == (5, 6), f"Erreur : {r3} != (5, 6)"
    r4 = plus1(r1, r2)
    assert r4 == (5, 6), f"Erreur : {r4} != (5, 6)"
    print("test de la fonction plus")
    r1 = entree("Entrez le premier rationnel : ")
    r2 = entree("Entrez le second rationnel : ")
    r3 = plus(r1, r2)
    print(f"{text(r1)} + {text(r2)} = {text(r3)}")


def opp(r: tuple[int, int]) -> tuple[int, int]:
    """ retourne l'opposé d'un rationnel """
    return cree(-r[0], r[1])


def moins(r1: tuple[int, int], r2: tuple[int, int]) -> tuple[int, int]:
    """ soustrait deux rationnels """
    return plus(r1, opp(r2))


def mult(r1: tuple[int, int], r2: tuple[int, int]) -> tuple[int, int]:
    """ multiplie deux rationnels avec simplification par pgcd """
    pg1 = pgcd(r1[0], r2[1])
    pg2 = pgcd(r2[0], r1[1])
    num = (r1[0] // pg1) * (r2[0] // pg2)
    den = (r1[1] // pg2) * (r2[1] // pg1)
    return cree(num, den)

def mult1(r1: tuple[int, int], r2: tuple[int, int]) -> tuple[int, int]:
    """ multiplie deux rationnels """
    num = r1[0] * r2[0]
    den = r1[1] * r2[1]
    return cree(num, den)


def inv(r: tuple[int, int]) -> tuple[int, int]:
    """ retourne l'inverse d'un rationnel """
    if r[0] == 0:
        raise ValueError("Le numérateur ne peut pas être nul pour l'inverse.")
    return cree(r[1], r[0])


def div(r1: tuple[int, int], r2: tuple[int, int]) -> tuple[int, int]:
    """ divise deux rationnels """
    return mult(r1, inv(r2))


def menu() -> None:
    """ affiche le menu et demande à l'utilisateur de choisir une opération """
    choix = -1
    while choix != 0:
        print("\nMenu :")
        print("1 : Addition de deux rationnels")
        print("2 : Opposé d'un rationnel")
        print("3 : Soustraction de deux rationnels")
        print("4 : Multiplication de deux rationnels")
        print("5 : Inverse d'un rationnel")
        print("6 : Division de deux rationnels")
        print("0 : Quitter")
        
        choix = int(input("Entrez votre choix : "))
        
        if choix == 1:
            r1 = entree("Entrez le premier rationnel : ")
            r2 = entree("Entrez le second rationnel : ")
            print(f"{text(r1)} + {text(r2)} = {text(plus(r1, r2))}")
        elif choix == 2:
            r = entree("Entrez un rationnel : ")
            print(f"L'opposé de {text(r)} est {text(opp(r))}")
        elif choix == 3:
            r1 = entree("Entrez le premier rationnel : ")
            r2 = entree("Entrez le second rationnel : ")
            print(f"{text(r1)} - {text(r2)} = {text(moins(r1, r2))}")
        elif choix == 4:
            r1 = entree("Entrez le premier rationnel : ")
            r2 = entree("Entrez le second rationnel : ")
            print(f"{text(r1)} * {text(r2)} = {text(mult(r1, r2))}")
        elif choix == 5:
            r = entree("Entrez un rationnel : ")
            try:
                print(f"L'inverse de {text(r)} est {text(inv(r))}")
            except ValueError as e:
                print(f"Erreur : {e}")
        elif choix == 6:
            r1 = entree("Entrez le premier rationnel : ")
            r2 = entree("Entrez le second rationnel : ")
            try:
                print(f"{text(r1)} / {text(r2)} = {text(div(r1, r2))}")
            except ValueError as e:
                print(f"Erreur : {e}")


def determinant(a1: tuple[int, int], a2: tuple[int, int], b1: tuple[int, int], b2: tuple[int, int]) -> tuple[int, int]:
    """ calcule le déterminant d'une matrice 2x2 de rationnels """
    return moins(mult(a1, b2), mult(a2, b1))


def est_nul(r: tuple[int, int]) -> bool:
    """ teste si un rationnel est nul """
    return r[0] == 0


def resoud_systeme() -> None:
    """ résout un système de deux équations à deux inconnues """
    print("Résolution d'un système :")
    print("a1 * x + b1 * y = c1")
    print("a2 * x + b2 * y = c2")
    
    a1 = entree("a1 : ")
    b1 = entree("b1 : ")
    c1 = entree("c1 : ")
    a2 = entree("a2 : ")
    b2 = entree("b2 : ")
    c2 = entree("c2 : ")

    det = determinant(a1, b1, a2, b2)
    if est_nul(det):
        print("Le système n'a pas de solution unique.")
        return

    x_num = determinant(c1, b1, c2, b2)
    y_num = determinant(a1, c1, a2, c2)

    x = div(x_num, det)
    y = div(y_num, det)

    print(f"Solution : x = {text(x)}, y = {text(y)}")
    
    

if __name__ == "__main__":
    # test1()
    # test2()
    # menu()
    resoud_systeme()