# %% [markdown]
# # Awaz : Module de fiscalité python
# ![fiscal logo image](https://github.com/Onzk/awaz/blob/master/awaz.png?raw=true)

# %% [markdown]
# ### Importation du module

# %%
import awaz

# %% [markdown]
# ## Démonstrations pratiques avec des exercices

# %% [markdown]
# ### Description de la fonction augmentation en pourcentage
# La fonction augmentation en pourcentage calcule la croissance 
# proportionnelle d'un montant depuis sa valeur initiale jusqu'à sa nouvelle 
# valeur supérieure. Elle est couramment utilisée pour mesurer le changement 
# relatif dans une quantité et s'exprime en pourcentage.
# 
# #### Exemple
# Vous analysez la croissance des ventes d'une entreprise au fil des années.
# Dans la première année, les ventes étaient de 200 000 euros.
# Dans la deuxième année, les ventes ont atteint 250 000 euros.

# %%
augmentation_percent: float = awaz.augmentation_percent(200_000, 50_000)

print(f"""Les ventes ont connu une augmentation de {augmentation_percent}% de la première à la 
deuxième année. Ce pourcentage d'augmentation offre une mesure claire 
de la croissance relative des ventes de l'entreprise sur la période spécifiée.""")

# %% [markdown]
# ### Description de la fonction diminution en pourcentage
# La fonction diminution en pourcentage calcule la diminution proportionnelle 
# d'un montant depuis sa valeur initiale jusqu'à sa nouvelle valeur inférieure. Elle 
# est couramment utilisée pour mesurer le changement relatif dans une 
# quantité et s'exprime en pourcentage. Cette fonction est essentielle dans 
# divers contextes financiers et analytiques, offrant une méthode normalisée 
# pour quantifier l'ampleur des changements négatifs, tels que les réductions 
# de coûts, la baisse des ventes ou d'autres métriques de performance.
# 
# #### Exemple
# Vous analysez la croissance des ventes d'une entreprise au fil des années.
# - Dans la première année, les ventes ont atteint 250 000 euros.
# - Dans la deuxième année, les ventes n'étaient que 200 000 euros.

# %%
diminution_percent: float = awaz.diminution_percent(250_000, 50_000)

print(f"""Les ventes ont connu une diminution de {diminution_percent}% de la première à la deuxième 
année. Ce pourcentage de diminution offre une mesure claire de la 
réduction relative des ventes de l'entreprise sur la période spécifiée.""")

# %% [markdown]
# ### Description et utilisation de l'interpolation linéaire
# La fonction ci-dessous montre comment calculer une valeur par interpolation 
# linéaire. L'interpolation linéaire est un procédé mathématique qui permet 
# d'estimer une valeur en calculant la moyenne de deux valeurs environnantes 
# connues. L'interpolation linéaire est fréquemment utilisée en finance, par 
# exemple, pour estimer le rendement ou le prix d'instruments financiers, 
# notamment lorsqu'on travaille avec des intervalles de temps irréguliers ou 
# avec des points de données manquants dans une série temporelle.
# 
# #### Exemple
# Une courbe de taux affiche, pour des maturités de 3 ans (x1) et de 5 ans (x2) 
# respectivement, des taux de rendement de 2.5% (y1) et de 3.5% (y2).
# Le taux recherché (yi) est celui de l'échéance de 4 ans (xi).

# %%
rate: float = awaz.linear_interpolation(4, 3, 5, 0.025, 0.035)

print(f"""Le taux recherché {round(rate * 100, 3)}% est celui de l'échéance de 4 ans.""")

# %% [markdown]
# ### Calcul du terme taux d'intérêt réel
# Le taux d'intérêt réel est le taux d'intérêt nominal corrigé des effets de 
# l'inflation.
# 
# #### Exemple
# Si le taux d'intérêt nominal annuel d'un investissement (inom) est de 5%, et le 
# taux d'inflation estimé pour l'année à venir (restinf) est de 1.5%, le taux d'intérêt 
# réel pour un placement d'un an ressort à combien ?

# %%
real_interest_rate: float = awaz.fisher_real_interest(0.05, 0.015)

print(f"""Le taux d'intérêt réel pour un placement d'un an ressort à {round(real_interest_rate * 100, 3)}%""")

# %% [markdown]
# ### Calcul de la valeur future d'un capital (périodes de capitalisation inférieures à un an)
# Fonction permettant de calculer la valeur d'un capital au bout de N années, 
# avec m capitalisations par an.
# 
# #### Exemple
# Prenons l'exemple d'un capital de 100 000 (C) placé à un taux d'intérêt 
# annuel de 3% (i) pendant 5 ans (N) et avec une capitalisation d'intérêts 
# mensuelle (m = 12). Au bout des cinq années, ce capital vaudra combien ?

# %%
future_capital: float = awaz.one_year_less_future_capital_value(100_000, 0.03, 12, 5)

print(f"""Au bout des cinq années, ce capital vaudra {round(future_capital, 2)}""")

# %% [markdown]
# ### Calcul de la valeur future d'une série d'annuités égales placées en début de période et pendant n périodes
# Cette fonction permet de déterminer la valeur d'un capital Cn, constitué par 
# le placement d'une série d'annuités égales a en début de période, et ce 
# pendant un nombre n de périodes.
# 
# #### Exemple
# Calcul de la valeur du capital constitué par des versements de 200 euros tous 
# les débuts de mois pendant 5 ans et sur un compte rémunéré à 3.5% p. a, 
# avec capitalisation des intérêts à chaque fin de mois. Afin de connaître la 
# réponse à cette question, il convient d'abord de transformer le taux d'intérêt
# annuel en taux d'intérêt proportionnel mensuel. Le résultat est de 3.5% / 12 = 0.291666667%.
# En appliquant ce taux, déterminez une valeur du capital, au bout de 5 ans.

# %%
value: float = awaz.period_start_future_annuity_value(200, 0.00291666667, 5)

print(f"""Au bout des cinq années, ce capital vaudra {round(value, 2)} euros""")

# %% [markdown]
# ### Calcul de la valeur future d'une série d'annuités égales placées en fin de période et pendant n périodes
# Cette fonction permet de déterminer la valeur d'un capital Cn constitué par le 
# placement d'une série d'annuités a, en fin de période, pendant un 
# nombre n de périodes.
# 
# #### Exemple
# Calcul de la valeur du capital constitué par des versements de 200 euros 
# toutes les fins de mois pendant 5 ans et sur un compte rémunéré à 3.5% p. a, 
# avec capitalisation des intérêts à chaque fin de mois. Afin de connaître la 
# réponse à cette question, il convient d'abord de transformer le taux d'intérêt 
# annuel en taux d'intérêt proportionnel mensuel. Le résultat est de 3.5% / 12 = 
# 0.291666667%. En appliquant ce taux, déterminez une valeur du capital, au bout de 5 ans.

# %%
value: float = awaz.period_end_future_annuity_value(200, 0.00291666667, 5)

print(f"""Au bout des cinq années, ce capital vaudra {round(value, 2)} euros""")

# %% [markdown]
# ### Calcul de la mensualité de crédit avec un taux et un capital donné
# Cette fonction permet de calculer la mensualité à payer pour rembourser un 
# crédit de montant C avec un taux d'intérêt r et une durée de N périodes. Elle 
# permet donc de répondre à la question suivante : Combien dois-je débourser 
# chaque période si je veux emprunter le montant C à un taux d'intérêt r, en 
# remboursant sur N périodes.
# 
# #### Exemple
# Prenons l'exemple d'un crédit d'un montant de 50 000 euros, avec un taux 
# d'intérêt de 2.4% par an et une durée de 6 ans (72 mois).
# En utilisant la fonction adéquate, calculez la mensualité du crédit aux conditions 
# énoncées.

# %%
value: float = awaz.mensuality_credit(50_000 , 0.024, 12, 6 * 12)

print(f"""La mensualité du crédit s'élève à {round(value, 2)} euros""")

# %% [markdown]
# ### Calcul du capital d'un crédit avec un taux et une mensualité donnée
# Cette fonction permet de déterminer le montant (maximum) C qui peut être 
# emprunté avec les conditions de durée N, de taux d'intérêt r et de capacité 
# de remboursement par période m données.
# Elle permet donc de répondre à la question suivante : Combien peut-on 
# emprunter, avec un taux d'intérêt de r, sur une durée de N périodes et en 
# payant une mensualité de m ?
# 
# #### Exemple
# Prenons les conditions d'emprunt suivantes : un taux d'intérêt de 2.4% par an, 
# une durée souhaitée de 6 ans (72 mois), et une capacité de remboursement 
# mensuelle de 750 euros.
# En utilisant la fonction adéquate, calculez la somme qui peut être empruntée.

# %%
capital: float = awaz.credit_capital(0.024, 12, 6 * 12, 750)

print(f"""La somme qui peut être empruntée s'élève à {round(capital, 2)} euros""")

# %% [markdown]
# ### Calcul de la durée d'un crédit en nombre de périodes à partir de montant, taux et mensualité
# Cette fonction permet de calculer durée d'un crédit lorsque le montant, le 
# taux d'intérêt et de la mensualité sont connus.
# 
# #### Exemple
# Considérons un crédit d'un montant de 50 000 euros, avec un taux d'intérêt 
# de 2.4% par an et une mensualité de 800 euros.
# En appliquant la fonction appropriée, calculez la durée du crédit aux conditions 
# énoncées.

# %%
duration: float = awaz.credit_duration(50_000,800, 0.024, 12)

print(f"""La durée du crédit sera de {duration} mois (soit {round(duration)} mois).""")

# %% [markdown]
# # Merci !


