def spocitej_cenu_kosiku(kosik, cenik):
    celkova_cena = 0
    for polozka in kosik:
        cena = cenik[polozka]
        celkova_cena += cena
    return celkova_cena


if __name__ == "__main__":
    print(spocitej_cenu_kosiku(["káva", "čaj", "káva"], {"káva": 60, "čaj": 40, "džus": 50}))