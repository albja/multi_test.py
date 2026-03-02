while True:
    montant = input("Quel montant souhaitez vous emprunter ? ")
    taux = input("Quel est le taux d'emprunt annuel (en %) ? ")
    duree = input("Quelle est la durée souhaitée (en années) ? ")

    try:
        capital = int(montant)
        taux_mensuel = float(taux) / 100 / 12
        nb_mensualites = int(duree) * 12
        
        mensualite = capital * taux_mensuel / (1 - (1 + taux_mensuel) ** -nb_mensualites)
        total = mensualite * nb_mensualites
        cout_credit = total - capital
        
        print(f'Mensualité : {mensualite:.2f} euros')
        print(f'Coût total du crédit : {cout_credit:.2f} euros')
        print(f'Montant total à rembourser : {total:.2f} euros')
        break
    except ValueError:
        print("Renseigner que des chiffres pour le montant, le taux et la durée")