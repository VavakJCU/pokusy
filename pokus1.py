def kava():

    cena_za_kus = int(input("Cena za kus je: "))
        
    pocet_kusu = int(input("Počet kusů je: "))
    
    celkova_cena = cena_za_kus * pocet_kusu

    return (celkova_cena)

if __name__ == "__main__":
    vysledek = kava()
    print(vysledek)