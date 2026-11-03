def spocitej_kosik(ceny_zbozi, je_vip):
    
    vysledek = sum(ceny_zbozi)

    if je_vip is True:
        vysledekkk = vysledek * 0.85
    else:
        vysledekkk = vysledek

    return (vysledekkk)


if __name__ == "__main__":
    vysledek = spocitej_kosik(ceny_zbozi = [100, 50, 50.5, 300], je_vip = True)

    print(vysledek)