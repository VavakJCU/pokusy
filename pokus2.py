def spocitej_ucet(cena_jidla = 200, cena_piti = 50):
    x = int(cena_jidla + cena_piti)
    y = x * 1.1
    return (y)

if __name__ == "__main__":
    vysledek = spocitej_ucet()
    print(f"celková cena je {vysledek}")
