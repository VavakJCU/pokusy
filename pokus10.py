def spocitej_frekvenci(polozky):
    vysledek = {}
    for vec in polozky:
        if vec in vysledek:
            vysledek[vec] += 1
        else:
            vysledek[vec] = 1
    return (vysledek)



if __name__ == "__main__":
    print (spocitej_frekvenci(["káva", "čaj", "káva", "džus", "káva"]))
