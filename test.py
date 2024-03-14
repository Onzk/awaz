import awaz

# La formule augmentation en pourcentage calcule la croissance
# proportionnelle d'un montant depuis sa valeur initiale jusqu'à sa nouvelle
# valeur supérieure. Elle est couramment utilisée pour mesurer le changement
# relatif dans une quantité et s'exprime en pourcentage.
# EXEMPLE
# Vous analysez la croissance des ventes d'une entreprise au fil des années.
# Dans la première année, les ventes étaient de 200 000 euros.
# Dans la deuxième année, les ventes ont atteint 250 000 euros.
# Calcul à l'aide de la formule d'augmentation en pourcentage

augmentation_percent: float = awaz.augmentation_percent(200_000, 50_000)

print(augmentation_percent)
