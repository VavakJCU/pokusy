def spocitej_vstupentku(vek, je_vikend):
    if vek <= 12:
        cena = 100
    elif vek >= 13 and vek <= 64:
        cena = 200
    else:
        cena = 120

    if je_vikend == True:
        vysledek = cena + 30
    else:
        vysledek = cena

    return (vysledek)

if __name__ == "__main__":
    x = spocitej_vstupentku(25, False)
    print(x)