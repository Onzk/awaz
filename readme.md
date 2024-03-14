# Awaz : Module de fiscalité python
![fiscal logo image](https://github.com/Onzk/awaz/blob/master/awaz.png?raw=true)

[![pyversions](https://img.shields.io/pypi/pyversions/scrapy-playwright.svg)](https://pypi.python.org/pypi/scrapy-playwright)

## A propos

Awaz est un module proposant des fonctions pour effectuer des calculs fiscaux rapidement. Il a pour rôle de permettre à n'importe quel programmeur qui ne connaît pas grand chose au monde de la fiscalité, d'implémenter facilement des fonctionnalités, basées sur des calculs fiscaux.

Ce projet a été réalisé dans un cadre scolaire par des étudiants. 

* Université : Université Catholique de l'Afrique de l'Ouest - Unité Universitaire du Togo ([UCAO-UUT](https://ucao-uut.tg/)).

* Institu : Cycle Ingénieur - Année préparatoire

* Cours : Programmation python

* Parcours : Cybersécurité

* Année scolaire : 2023-2024 

* Professeur en charge : Mr APEKE

* Membres du Groupe 6 : 
    * DOSSOU Eugénie Dede
    * ASSIGNON Akofala Bénédicta
    * NGOMDJIBAYE David
    * KOUDOSSOU Messan Dhani Justin


## Système supporté

Le programme peut tout aussi bien fonctionner sous Windows comme sous un système Linux.


## Prérequis

Le module `awaz` utilise d'autres modules que sont : 

* Le module `math`

## Utilisation basique

Pour utiliser `awaz`, il suffit de l'importer comme tout autre module python.

```py
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
```
