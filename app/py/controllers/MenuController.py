class MenuController:
    def __init__(self):

        # Sablonok listája
        self.templates = [
            "0. - Exit",
            "1. - Ask Peternity to decide the meaning of a word based solely on its surrounding text (the context).",
            "2. - Hyphenate a Hungarian word",
            "3. - Privacy Policy & Data Handling.",
            "4. - View Chat History.",
            "5. - About Peternity.",
            "6. - Select AI Model.",
            "7. - Settings & Preferences.",
            "8. - User Profile Management.",
            "9. - Word Etymology Lookup.",
            "10. - Generate a Daily Random Word Challenge.",
            "11. - AI-Powered Grammar Check.",
            "12. - Fun Fact of the Day.",
            "13. - Generate a Short Story Based on a Prompt.",
            "14. - Help me write code",
        ]

    def display_menu(self):
        print("\nPlease choose from the following options:")

        # Sablonok megjelenítése
        for template in self.templates:
            print(template)

        print("\nEnter the number of the desired action (0-14): ")
