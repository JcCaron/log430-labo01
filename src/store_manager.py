"""
Store manager application
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from views.user_view import UserView
from views.product_view import ProductView

def main_menu():
    while True:
        print("===== LE MAGASIN DU COIN =====")
        print("1. Gestion des produits")
        print("2. Gestion des utilisateurs")
        print("3. Quitter l'application")
        
        choice = input("Choisissez une option : ").strip()
        
        if choice == "1":
            ProductView().show_options()
        elif choice == "2":
            UserView().show_options()
        elif choice == "3":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.\n")
            
            
if __name__ == "__main__":
    main_menu()