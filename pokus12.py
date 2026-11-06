import sys
def spocitej_prumer(studenti_znamky, jmeno_studenta):

    seznam_znamek = studenti_znamky[jmeno_studenta]

    prumer = [0]

    a = sum(seznam_znamek)
    b = len(seznam_znamek)
    prumer = a / b
    return (prumer)

if __name__ == "__main__":
    jmena = ["Petr", "Jana"]
    
    x = input("Vložte jméno s prvním velkým písmenem: ")
    if x in jmena:
        pass
    else:
        print ("Jméno není v seznamu")
        sys.exit()

    

    y = {"Petr": [1, 2, 3], "Jana": [1, 2, 2]}
    print(spocitej_prumer(y, x))
    