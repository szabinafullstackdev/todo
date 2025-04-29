def megjelenit_udvozlo_uzenet():
    """Megjeleníti az üdvözlő üzenetet a felhasználónak."""
    print("Üdvözöllek a teendő alkalmazásban!")
    print("Kérlek, válassz a menüpontok közül:")
    print("1. Új teendő hozzáadása")
    print("2. Teendők listázása")
    print("3. Teendő törlése")
    print("4. Kilépés")

def uj_teendo_hozzaadasa(teendok):
    """Hozzáad egy új teendőt a listához."""
    teendo = input("Add meg az új teendőt: ")
    teendok.append(teendo)
    print(f"'{teendo}' hozzáadva a teendők listájához.")

def teendok_listazasa(teendok):
    """Listázza a teendők tartalmát."""
    if not teendok:
        print("Nincsenek teendők a listában.")
    else:
        print("A teendők listája:")
        for i, teendo in enumerate(teendok):
            print(f"{i + 1}. {teendo}")

def teendo_torlese(teendok):
    """Töröl egy teendőt a listából."""
    teendok_listazasa(teendok)
    if not teendok:
        return
    try:
        torlendo_index = int(input("Add meg a törlendő teendő sorszámát: ")) - 1
        if 0 <= torlendo_index < len(teendok):
            torolt_teendo = teendok.pop(torlendo_index)
            print(f"'{torolt_teendo}' törölve a teendők listájából.")
        else:
            print("Érvénytelen sorszám!")
    except ValueError:
        print("Érvénytelen bemenet! Számot kell megadni.")

def main():
    """A fő alkalmazás logikája."""
    teendok = []  # A teendők tárolására szolgáló lista
    megjelenit_udvozlo_uzenet()

    while True:
        valasztas = input("Válassz egy menüpontot (1-4): ")

        if valasztas == "1":
            uj_teendo_hozzaadasa(teendok)
        elif valasztas == "2":
            teendok_listazasa(teendok)
        elif valasztas == "3":
            teendo_torlese(teendok)
        elif valasztas == "4":
            print("Kilépés az alkalmazásból...")
            break
        else:
            print("Érvénytelen választás. Kérlek, válassz a menüpontok közül (1-4).")

if __name__ == "__main__":
    main()
