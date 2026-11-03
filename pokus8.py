def vyfiltruj_drahe(ceny_zbozi, hranice):
    drahe_polozky = []
    for ceny in ceny_zbozi:
        if ceny > hranice:
            drahe_polozky.append(ceny)
    return (drahe_polozky)

if __name__ == "__main__":
    print(vyfiltruj_drahe([50, 120, 300, 80, 500], 100))
