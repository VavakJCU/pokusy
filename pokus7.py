def spocitej_drahe_polozky(ceny_zbozi, hranice):
    pocet = 0
    for ceny in ceny_zbozi:
        if ceny >= hranice:
            pocet += 1
        

    return (pocet)
    


if __name__ == "__main__":
    print (spocitej_drahe_polozky([50, 120, 300, 80, 500], 100))
