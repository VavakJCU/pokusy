def najdi_spolecne_zajmy(zajmy_osoba1, zajmy_osoba2):

    prvni = {}
    druhy = {}

    prvni = set(zajmy_osoba1)
    druhy = set(zajmy_osoba2)

    prusecik = prvni & druhy

    vysledek = list(prusecik)

    return (vysledek)

if __name__ == "__main__":
    print(najdi_spolecne_zajmy(["rybaření", "fotbal", "plavání"], ["čtení", "fotbal", "rybaření"]))
