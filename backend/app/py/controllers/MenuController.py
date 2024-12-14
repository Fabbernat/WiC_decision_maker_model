class MenuController:
    def __init__(self):

        # Sablonok listája
        self.templates = [
            "0. - Mégse",
            "1. - Fizetési felszólítás",
            "2. - Tájékoztató az új szabályokról",
            '3. - Ellenőrzési értesítés',
            "4. - Adóbevallási emlékeztető",
            "5. - Egyéni lekérdezés válasz, megadott id alapján"
        ]

    def display_menu(self):
        print("\nKérjük, válasszon az alábbi műveletek közül:");

        # Sablonok megjelenítése
        for template in self.templates:
            print(template)

        print("\nAdja meg a választott művelet számát (0-5): ")
