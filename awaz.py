# %% [markdown]
# # Awaz : Module de fiscalité python
# ![fiscal logo image](https://github.com/Onzk/awaz/blob/master/awaz.png?raw=true)
# 
# [![pyversions](https://img.shields.io/pypi/pyversions/scrapy-playwright.svg)](https://pypi.python.org/pypi/scrapy-playwright)

# %% [markdown]
# ---

# %% [markdown]
# ## Readme
# 
# ### A propos
# 
# Awaz est un module proposant des fonctions pour effectuer des calculs fiscaux rapidement. Il a pour rôle de permettre à n'importe quel programmeur qui ne connaît pas grand chose au monde de la fiscalité, d'implémenter facilement des fonctionnalités, basées sur des calculs fiscaux.
# 
# Ce projet a été réalisé dans un cadre scolaire par des étudiants. 
# 
# * Université : Université Catholique de l'Afrique de l'Ouest - Unité Universitaire du Togo ([UCAO-UUT](https://ucao-uut.tg/)).
# 
# * Institut : Cycle Ingénieur - Année préparatoire
# 
# * Cours : Programmation python
# 
# * Parcours : Cybersécurité
# 
# * Année scolaire : 2023-2024 
# 
# * Professeur en charge : Dr APEKE Kodjo
# 
# * Membres du Groupe 6 : 
#     * DOSSOU Eugénie Dede
#     * ASSIGNON Akofala Bénédicta
#     * NGOMDJIBAYE David
#     * KOUDOSSOU Messan Dhani Justin
# 
# 
# ### Système supporté
# 
# Le programme peut tout aussi bien fonctionner sous Windows comme sous un système Linux.
# 
# 
# ### Prérequis
# 
# Le module `awaz` utilise d'autres modules que sont : 
# 
# * Le module `math`
# 
# ### Utilisation basique
# 
# Pour utiliser `awaz`, il suffit de l'importer comme tout autre module python.
# 
# ```py
#     import awaz
# 
#     # La formule augmentation en pourcentage calcule la croissance
#     # proportionnelle d'un montant depuis sa valeur initiale jusqu'à sa nouvelle
#     # valeur supérieure. Elle est couramment utilisée pour mesurer le changement
#     # relatif dans une quantité et s'exprime en pourcentage.
#     # EXEMPLE
#     # Vous analysez la croissance des ventes d'une entreprise au fil des années.
#     # Dans la première année, les ventes étaient de 200 000 euros.
#     # Dans la deuxième année, les ventes ont atteint 250 000 euros.
#     # Calcul à l'aide de la formule d'augmentation en pourcentage
# 
#     augmentation_percent: float = awaz.augmentation_percent(200_000, 50_000)
# 
#     print(augmentation_percent)
# ```

# %% [markdown]
# ---

# %% [markdown]
# ## Sommaire du corps du projet
# - Introducion
# - Importation des dépendances
# - Les outils du module
#     - La classe FinancialError
#     - La fonction de validation
# - Arithmétique
#     - Calcul de pourcentages
#         * Différence entre deux montants en pourcent (changement en pourcentage)
#         * Augmentation en pourcentage
#         * Diminution en pourcentage
# - Analyse numérique et statistiques 
#     - Interpolation
#         * Interpolation linéaire
#     - Mesure de tendance centrale
#         * Moyenne arithmétique
#         * Moyenne pondérée
# - La valeur temps de l'argent 
#     - Calculs d'intérêts
#         * Intérêts simples, période inférieure à un an
#         * Intérêts simples, périodes d'années pleines
#         * Calcul d'un taux d'intérêt réel (relation de Fisher)
#         * Calcul d'un taux forward
#     - Valeur actuelle
#         * Valeur actuelle d'un paiement (périodes de capitalisation inférieures à un an)
#         * Valeur actuelle d'un paiement (capitalisation annuelle)
#         * Valeur actuelle d'une série de paiements annuels de montants égaux
#         * Valeur actuelle d'une série de paiements annuels de montants variés
#     - Valeur future
#         * Valeur future d'un capital (périodes de capitalisation inférieures à un an)
#         * Valeur future d'un paiement (capitalisation annuelle)
#         * Valeur future d'un capital (capitalisation continue)
#         * Valeur future d'une série d'annuités égales placées en début de période et pendant n périodes
#         * Valeur future d'une série d'annuités égales placées en fin de période et pendant n périodes
#         * Montant de l'annuité requise pour constitution d'un capital à une durée et un taux donnés
#     - Intérêts composés - Taux d'intérêt 
#         * Taux d'intérêt qui donne la valeur future KN pour un capital K0 placé pour une durée de N
#     - Taux de rendement
#         * Calcul du taux zero coupon à partir du facteur d'actualisation
#         * Taux de rendement actuariel (périodes annuelles)
#     - Facteur d'actualisation
#         * Calcul du facteur d'actualisation à partir de la valeur actuelle et de la valeur future
#         * Calcul du facteur d'actualisation à partir du taux périodique et du nombre de périodes
#     - Conversions et comparaisons de taux
#         * Taux d'intérêt périodique proportionnel équivalent à un taux d'intérêt annuel simple
#         * Taux d'intérêt actuariel périodique équivalent à un taux d'intérêt actuariel annuel
#         * Conversion d'un taux d'intérêt périodique proportionnel en un taux d'intérêt annuel simple équivalent
#         * Conversion d'un taux d'intérêt périodique actuariel en un taux d'intérêt annuel actuariel équivalent
#         * Conversion taux d'intérêt nominal en taux d'intérêt effectif
# - Crédits
#     - Mensualité du crédit
#         * Mensualité de crédit avec un taux et un capital donnés
#     - Montant du crédit
#         * Capital d'un crédit avec un taux et une mensualité donnés
#         * Calcul du capital remboursé au terme de n périodes
#         * Calcul du capital restant à rembourser au terme de n périodes
#     - Durée du crédit
#         * Calcul de la durée d'un crédit en nombre de périodes à partir de montant, taux et mensualité
# - Démonstrations pratiques avec des exercices
# - Exemples de cas d'utilisation
# - Conclusion

# %% [markdown]
# ## Introduction
# Dans le monde fiscal, il existe toute une collection exhaustive des formules et ratios essentiels qui guident l'analyse financière et la prise de décision. Que vous soyez étudiant, professionnel ou passionné, ce module vous aidera à implémenter des calculs complexes et à renforcer votre compétence financière. Dans la suite, nous verrons des fonctions de calculs financiers organisées par sections.

# %% [markdown]
# ## Importation des dépendances

# %%
import math

# %% [markdown]
# ## Les outils du module
# Avant toute chose, nous devons créer une classe pour gérer les exceptions du module et une fonction pour valider les données reçues. Il s'agit là, des outils du module.
# 
# ### Classe FinancialError

# %%
# Définition de la classe qui étend Exception
class FinancialError(Exception) :
    """La classe FinancialError gère les erreurs de calculs financiers.
    """    
    
    # Constructeur de la classe se basant sur 
    # sa classe mère Exception
    def __init__(self, *args: object) -> None:
        # Intialisation de la classe mère
        super().__init__(*args)

# %% [markdown]
# ### La fonction de validation

# %%
def ___(to_check:dict) -> None:
    """Cette fonction valide les données pour les calculs financiers,
    et lève une FinancialError en cas de problème.
    
    Elle prend en entrée, un dictionnaire dont les clés sont des 
    conditions et qui lève une FinancialError si l'une d'elles est vraie, 
    avec le message d'erreur qui est la valeur correspondante dans le dictionnaire.
    
    Args:
        to_check (dict): dictionnaire de validations (condition:message)

    Raises:
        FinancialError: si une condition est vraie dans le dictionnaire
    """
    
    # Parcours du dictionnaire des vérifications à faire.
    for condition, message in to_check.items():
        # Si la condition est vérifiée,
        if condition :
        # une FinancialError est levée.
            raise FinancialError(message)

# %% [markdown]
# ## Section arithmétique
# 
# ### Calcul de pourcentages

# %%
# Différence entre deux montants en pourcent (changement en pourcentage).
def diff_percent(ca: float, cn: float) -> float:
    """Cette fonction calcule la différence entre deux nombres en pourcentage.
    Ceci est souvent important dans le monde des affaires et de la finance, 
    où les changements dans les bénéfices, les marges et les pertes sont exprimés en pourcentages.
    
    Ref:
        Différence entre deux montants en pourcent (changement en pourcentage).

    Args:
        ca (float): le premier montant
        cn (float): le second montant

    Returns:
        float: la différence en pourcentage
    """
    
    # Validaton des montants
    ___(
        {
            ca == 0 or ca < 0: "Le premier montant n'est pas strictement supérieur à 0.",
            cn < 0 : "Le second montant n'est pas supérieur à 0.",
        }
    )
    
    # Opération du calcul
    return (cn - ca) / ca

# %%
# Augmentation en pourcentage.
def augmentation_percent(old_amount: float, amount_augmentation: float) -> float:
    """Cette fonction sert à calculer la croissance proportionnelle d'un montant depuis
    sa valeur initiale jusqu'à sa nouvelle valeur supérieure.
    Ce caclul est couramment utilisé pour mesurer le changement relatif dans une quantité
    et s'exprime en pourcentage.

    Ref:
        Augmentation en pourcentage.

    Args:
        old_amount (float): l'ancien montant
        amount_augmentation (float): l'augmentation du montant

    Returns:
        float: l'augmentation en pourcentage
    """

    # Validaton des montants
    ___(
        {
            old_amount == 0
            or old_amount < 0: "L'ancien montant n'est pas strictement supérieur à 0.",
            amount_augmentation < 0: "L'augmentation du montant n'est pas supérieur à 0.",
        }
    )

    # Opération de calcul
    return amount_augmentation / old_amount * 100

# %%
# Diminution en pourcentage. 
def diminution_percent(old_amount: float, amount_diminution:float) -> float:
    """Cette fonction sert à calculer la diminution proportionnelle d'un montant
    depuis sa valeur initiale jusqu'à sa nouvelle valeur inférieure.
    Elle se repose sur une formule couramment utilisée pour mesurer le changement relatif
    dans une quantité et s'exprime en pourcentage. La formule en question est essentielle dans
    divers contextes financiers et analytiques, offrant une méthode normalisée pour quantifier
    l'ampleur des changements négatifs, tels que les réductions de coûts,
    la baisse des ventes ou d'autres métriques de performance.

    Ref:
        Diminution en pourcentage.

    Args:
        old_amount (float): l'ancien montant
        amount_diminution (float): la diminution du montant

    Returns:
        float: la diminution en pourcentage
    """

    # Validaton des montants
    ___(
        {
            old_amount == 0 or old_amount < 0: "L'ancien montant n'est pas strictement supérieur à 0.",
            amount_diminution < 0 : "La diminution du montant n'est pas supérieur à 0.",
        }
    )

    # Opération de calcul
    return (amount_diminution / old_amount) * 100

# %% [markdown]
# ## Section analyse numérique et statistiques
# 
# ### Interpolation

# %%
# Interpolation linéaire.
def linear_interpolation(
    xi: float, x1: float, x2: float, y1: float, y2: float
) -> float:
    """Cette fonction sert à calculer une valeur par interpolation linéaire.
    L'interpolation linéaire est un procédé mathématique qui permet d'estimer une valeur
    en calculant la moyenne de deux valeurs environnantes connues.
    L'interpolation linéaire est fréquemment utilisée en finance, par exemple,
    pour estimer le rendement ou le prix d'instruments financiers,
    notamment lorsqu'on travaille avec des intervalles de temps irréguliers ou
    avec des points de données manquants dans une série temporelle.

    Ref:
        Interpolation linéaire.

    Args:
        xi (float): point sur l'abscisse à interpoler
        x1 (float): point inférieur sur l'abscisse
        x2 (float): point supérieur sur l'abscisse
        y1 (float): point inférieur sur l'ordonnée
        y2 (float): point supérieur sur l'ordonnée

    Returns:
        float: valeur trouvée après l'interpolation
    """

    # Vérification des entrées
    ___(
        {
            not (
                x1 < xi < x2
            ): "La valeur à interpoler n'est pas comprise entre le point inférieur et supérieur de l'abscisse.",
            x1
            > x2: "Le point inférieur sur l'abscisse ne doit pas être inférieur au point supérieur sur l'abscisse.",
            y1
            > y2: "Le point inférieur sur l'ordonnée ne doit pas être inférieur au point supérieur sur l'ordonnée.",
        }
    )
    # Opération de calcul
    return y1 + (y2 - y1) * (xi - x1) / (x2 - x1)

# %% [markdown]
# ### Mesures de tendance centrale

# %%
# Moyenne arithmétique.
def arithmetic_mean(values: list) -> float:
    """Cette fonction permet de calculer la moyenne arithmétique d'une série de points
    de données. La moyenne arithmétique est obtenue en divisant la somme
    des valeurs de la liste par leur nombre total.
    Elle représente le point central de la série.
    
    Ref:
        Moyenne arithmétique.

    Args:
        values (list): série de données

    Returns:
        float: moyenne de la série
    """

    # Vérification des entrées
    ___(
        {
            # Vérifie si la série n'est pas vide.
            len(values) == 0: "La série ne doit pas être vide.",
            
            # Vérifie s'il y a autre chose que des nombres dans la série.
            not len([i for i in values if not isinstance(i, (float, int))])
            == 0: "La série ne doit contenir que des nombres.",
        }
    )
    
    # Opération de calcul
    return sum(values) / len(values)

# %%
#Moyenne pondérée.
def ponderous_mean(values: list, factors:list) -> float:
    """Cette fonction permet de calculer la moyenne pondérée 
    d'une série de points de données.
    
    Ref:
        Moyenne pondérée.

    Args:
        values (list): série de points de données
        factors (list): série de points de données

    Returns:
        float: moyenne de la série
    """
    
    # Vérification des entrées
    ___(
        {
            # Vérifie si la série n'est pas vide.
            len(values) == 0: "La série de points ne doit pas être vide.",
            
            # Vérifie s'il y a autre chose que des nombres dans la série des points.
            not len([i for i in values if not isinstance(i, (float, int))])
            == 0: "La série de points ne doit contenir que des nombres.",
            
            # Vérifie si la série de facteurs de pondération n'est pas vide.
            len(factors) == 0: "La série de facteurs de pondération ne doit pas être vide.",
            
            # Vérifie s'il y a autre chose que des nombres dans la série 
            # des facteurs de pondération.
            not len([i for i in values if not isinstance(i, (float, int))])
            == 0: "La série ne doit contenir que des nombres.",
            
            # Vérifie si les deux séries sont de mêmes tailles.
            not len(factors) == len(values): "Les deux séries doivent avoir la même taille.",
        }
    )
    
    # Opération de calcul
    return sum([value * factor for value, factor in zip(values, factors)]) / sum(factors)

# %% [markdown]
# ## Section valeur temps de l'argent
# 
# ### Calculs d'intérêts

# %%
# Intérêts simples, période inférieure à un an.
def one_year_less_interest(capital:float, days:int, year_days:int, annual_nominal_interest:float) -> float:
    """Cette fonction permet de calculer des intérêts simples, 
    avec des périodes d'intérêts inférieures à un an.

    Ref:
        Intérêts simples, période inférieure à un an.

    Args:
        capital (float): capital initial
        days (int): nombre de jours
        year_days (int): nombre de jours dans l'année (360,365, 366 selon convention)
        annual_nominal_interest (float): Taux d'intérêt nominal annuel

    Returns:
        float: l'intérêt
    """
    
    # Vérification des entrées
    ___(
        {
            days < 0 : "Le nombre de jour n'est pas positif.",
            days > 366 : "Le nombre de jour ne doit pas dépasser un an.",
            not year_days in [360, 365, 366] : "Le nombre de jour dans l'année doit être dans la liste (360,355,366).",
        }
    )
    
    # Opération de calcul
    return capital * annual_nominal_interest * days / year_days

# %%
# Intérêts simples, périodes d'années pleines.
def full_years_interest(capital: float, years: int, annual_nominal_interest: float) -> float:
    """Cette fonction permet de calculer des intérêts simples,
    avec périodes d'intérêts en années pleines.
    
    Ref:
        Intérêts simples, périodes d'années pleines.

    Args:
        capital (float): capital initial
        years (int): Nombre de périodes (années)
        annual_nominal_interest (float): Taux d'intérêt nominal annuel

    Returns:
        float: l'intérêt
    """

    # Vérification des entrées
    ___({years < 0: "Le nombre d'années n'est pas positif."})

    # Opération de calcul
    return capital * annual_nominal_interest * years

# %%
# Calcul d'un taux d'intérêt réel (relation de Fisher).
def fisher_real_interest(nominal_interest: float, estimated_inflation: float) -> float:
    """Cette fonction permet de calculer le taux d'intérêt réel pour une période
    à partir d'un taux d'intérêt réel et d'un taux d'inflation estimé.
    Elle se base sur une formule également connue sous le nom de relation de Fisher.

    Ref:
        Calcul d'un taux d'intérêt réel (relation de Fisher).

    Args:
        nominal_interest (float): taux d'intérêt nominal
        estimated_inflation (float): taux d'inflation estimé

    Returns:
        float: l'intérêt
    """

    # Vérification des entrées
    ___(
        {estimated_inflation == -1: "Le taux d'inflation estimé ne peut pas être égal à -1."}
    )

    # Opération de calcul
    return (1 + nominal_interest) / (1 + estimated_inflation) - 1

# %%
# Calcul d'un taux forward.
def forward_interest(
    dbase: int, n01: int, n02: int, n12: int, r01: float, r02: float
) -> float:
    """Cette fonction permet de calculer un taux d'intérêt forward pour une période
    située entre les deux dates t1 et t2.

    Ref:
        Calcul d'un taux forward.
    
    Args:
        dbase (int): nombre de jours d'une année (selon la convention : 360 ou 365[366])
        n01 (int): nombre de jours de la période entre la date de calcul t0 et t1
        n02 (int): nombre de jours de la période entre la date de calcul t0 et t2
        n12 (int): nombre de jours de la période entre la date t1 et la date t2
        r01 (float): taux d'intérêt pour la période entre la date de calcul t0 et t1
        r02 (float): taux d'intérêt pour la période entre la date de calcul t0 et t2

    Returns:
        float: l'intérêt
    """

    # Vérification des entrées
    ___(
        {
            not dbase
            in [
                360,
                365,
                366,
            ]: "Le nombre de jours dans l'année doit être dans la liste (360,355,366)."
        }
    )

    # Opération de calcul
    return ((1 + r02 * n02 / dbase) / (1 + r01 * n01 / dbase) - 1) * (dbase / n12)

# %% [markdown]
# ### Valeur actuelle

# %%
# Valeur actuelle d'un paiement (périodes de capitalisation inférieures à un an).
def one_year_less_actual_payment_value(
    future_value: float,
    annual_interest_rate: float,
    per_year_actualisations: int,
    years: int,
) -> float:
    """Cette fonction permet de calculer la valeur actuelle d'un paiement avec
    des périodes de capitalisation inférieures à un an.
    
    Ref:
        Valeur actuelle d'un paiement (périodes de capitalisation inférieures à un an).

    Args:
        future_value (float): valeur future
        annual_interest_rate (float): taux d'intérêt annuel
        per_year_actualisations (float): nombre de périodes d'actualisation par an
        years (int): nombre d'années

    Returns:
        float: la valeur actuelle du paiment
    """

    # Vérification des entrées
    ___(
        {
            per_year_actualisations
            <= 0: "Le nombre de périodes d'actualisation par an doit être strictement supérieur à 0.",
            years < 0: "Le nombre d'années doit être positif.",
        }
    )

    # Opération de calcul
    return (
        future_value
        * years
        * pow(
            (1 + annual_interest_rate / per_year_actualisations),
            -per_year_actualisations * years,
        )
    )

# %%
# Valeur actuelle d'un paiement (capitalisation annuelle).
def actual_payment_value(
    future_value: float,
    annual_interest_rate: float,
    years: int,
) -> float:
    """Cette fonction sert à calculer de la valeur actuelle d'un paiement
    avec capitalisation annuelle.
    
    Ref:
        Valeur actuelle d'un paiement (capitalisation annuelle).
        
    Args:
        future_value (float): valeur future
        annual_interest_rate (float): taux d'intérêt annuel
        years (int): nombre d'années

    Returns:
        float: la valeur actuelle du paiment

    """

    # Vérification des entrées
    ___(
        {
            years < 0: "Le nombre d'années doit être positif.",
            annual_interest_rate
            == -1: "Le taux d'intérêt annuel doit être différent de -1.",
        }
    )

    # Opération de calcul
    return future_value * years * pow((1 + annual_interest_rate), -years)

# %%
# Valeur actuelle d'une série de paiements annuels de montants égaux.
def actual_payment_value_annual_equal_amounts(
    flux: float,
    annual_interest_rate: float,
    years: int,
) -> float:
    """Cette fonction permet de déterminer la valeur actuelle (ou valeur présente)
    d'une série de flux de montants égaux versés annuellement.
    
    Ref:
        Valeur actuelle d'une série de paiements annuels de montants égaux.

    Args:
        flux (float): flux de paiement récurrent
        annual_interest_rate (float): taux d'intérêt annuel
        years (int): nombre de périodes (années)

    Returns:
        float: la valeur actuelle de la série de paiments

    """

    # Vérification des entrées
    ___(
        {
            years < 0: "Le nombre de périodes (années) doit être positif.",
            annual_interest_rate
            == -1: "Le taux d'intérêt annuel doit être différent de -1.",
        }
    )

    # Opération de calcul
    return sum([flux / pow(1 + annual_interest_rate, n) for n in range(1, years + 1)])

# %%
# Valeur actuelle d'une série de paiements annuels de montants variés.
def actual_payment_value_annual_various_amounts(
    flux: list,
    annual_interest_rate: float,
) -> float:
    """Cette fonction permet de déterminer la valeur actuelle (ou valeur présente) 
    d'une série de flux de montants variés versés annuellement.
    
    Ref:
        Valeur actuelle d'une série de paiements annuels de montants variés.

    Args:
        flux (list): liste de flux de paiements récurrents
        annual_interest_rate (float): taux d'intérêt annuel

    Returns:
        float: la valeur actuelle de la série de paiements
    """
    
    # Vérification des entrées
    ___({annual_interest_rate == -1: "Le taux d'intérêt annuel doit être différent de -1."})
    
    # Opération de calcul
    return sum([flux[n + 1] / pow(1+annual_interest_rate, n + 1) for n in range(0, len(flux))])

# %% [markdown]
# ### Valeur future

# %%
# Valeur future d'un capital (périodes de capitalisation inférieures à un an).
def one_year_less_future_capital_value(
    captial: float,
    annual_interest_rate: float,
    per_year_actualisations: int,
    years: int,
) -> float:
    """Cette fonction permet de calculer la valeur d'un capital au bout de certain nombre
    d'années, avec un nombre de capitalisations par an.
    
    Ref:
        Valeur future d'un capital (périodes de capitalisation inférieures à un an).

    Args:
        captial (float): capital initial
        annual_interest_rate (float): taux d'intérêt annuel
        per_year_actualisations (float): nombre de périodes d'actualisation par an
        years (int): nombre d'années

    Returns:
        float: la valeur future du capital
    """

    # Vérification des entrées
    ___(
        {
            per_year_actualisations
            <= 0: "Le nombre de périodes d'actualisation par an doit être strictement supérieur à 0.",
            years < 0: "Le nombre d'années doit être positif.",
        }
    )

    # Opération de calcul
    return (
        captial
        * pow(
            (1 + annual_interest_rate / per_year_actualisations),
            per_year_actualisations * years,
        )
    )

# %%
# Valeur future d'un paiement (capitalisation annuelle).
def annual_future_paiment_value(
    actual_value: float,
    annual_interest_rate: float,
    years: int,
) -> float:
    """Cette fonction permet de calculer valeur future d'un paiement
    avec capitalisation annuelle.

    Ref:
        Valeur future d'un paiement (capitalisation annuelle).

    Args:
        actual_value (float): capital initial
        annual_interest_rate (float): taux d'intérêt annuel
        years (int): nombre d'années

    Returns:
        float: la valeur future du paiement
    """

    # Vérification des entrées
    ___({years < 0: "Le nombre d'années doit être positif."})

    # Opération de calcul
    return actual_value * pow((1 + annual_interest_rate), years)

# %%
# Valeur future d'un capital (capitalisation continue).
def continue_capitalisation_future_capital_value(
    capital: float,
    annual_interest_rate: float,
    years: int,
) -> float:
    """Cette fonction permet de calculer valeur d'un capital au bout d'un nombre 
    d'années, en capitalisation continue.

    Ref:
        Valeur future d'un capital (capitalisation continue).

    Args:
        capital (float): capital initial
        annual_interest_rate (float): taux d'intérêt annuel
        years (int): nombre d'années

    Returns:
        float: la valeur future d'un capital
    """

    # Vérification des entrées
    ___({years < 0: "Le nombre d'années doit être positif."})

    # Opération de calcul
    return capital * math.exp(annual_interest_rate * years) 

# %%
# Valeur future d'une série d'annuités égales placées
# en début de période et pendant n périodes.
def period_start_future_annuity_value(
    annuity: float,
    periodic_rate: float,
    periods: int,
) -> float:
    """Cette fonction permet de déterminer la valeur d'un capital,
    constitué par le placement d'une série d'annuités égales en début de période,
    et ce pendant un nombre de périodes.

    Ref:
        Valeur future d'une série d'annuités égales placées
        en début de période et pendant n périodes.

    Args:
        annuity (float): annuité
        periodic_rate (float): taux périodique équivalent
        periods (int): nombre de périodes

    Returns:
        float: la valeur future de la série d'annuités
    """

    # Vérification des entrées
    ___(
        {
            periods < 0: "Le nombre d'années doit être positif.",
            periodic_rate
            <= 0: "Le taux périodique équivalent doit être strictement positif.",
        }
    )

    # Opération de calcul
    return (
        annuity
        * (1 + periodic_rate)
        * (pow(1 + periodic_rate, periods * 12) - 1)
        / (periodic_rate)
    )

# %%
# Valeur future d'une série d'annuités égales placées
# en fin de période et pendant n périodes.
def period_end_future_annuity_value(
    annuity: float, periodic_rate: float, periods: int
) -> float:
    """Cette fonction permet de déterminer la valeur d'un capital constitué
    par le placement d'une série d'annuités, en fin de période,
    pendant un nombre de périodes.

    Ref:
        Valeur future d'une série d'annuités égales placées
        en fin de période et pendant n périodes.

    Args:
        annuity (float): annuité
        periodic_rate (float): taux périodique équivalent
        periods (int): nombre de périodes

    Returns:
        float: la valeur future de la série d'annuités
    """

    # Vérification des entrées
    ___(
        {
            periods < 0: "Le nombre de périodes doit être positif.",
            periodic_rate
            <= 0: "Le taux périodique équivalent doit être strictement positif.",
        }
    )

    # Opération de calcul
    return annuity * (pow(1 + periodic_rate, periods * 12) - 1) / periodic_rate

# %%
# Montant de l'annuité requise pour constitution d'un
# capital à une durée et un taux donnés.
def required_annuity_amount_for_capital(
    capital: float,
    annual_interest_rate: float,
    years: int,
) -> float:
    """Cette fonction permet de calculer le montant de l'annuité a nécessaire
    pour constituer, avec une durée de placement d'années et un taux
    d'intérêt donnés, avec paiement annuel des intérêts, un capital de montant.

    Ref:
        Montant de l'annuité requise pour constitution d'un
        capital à une durée et un taux donnés.

    Args:
        capital (float): capital à constituer
        annual_interest_rate (float): taux d'intérêt annuel
        years (int): nombre de périodes (années)

    Returns:
        float: le montant de l'annuité requise pour constitution du capital
    """

    # Vérification des entrées
    ___({years < 0: "Le nombre d'années doit être positif."})

    # Opération de calcul
    return capital * annual_interest_rate / ((pow(1 + annual_interest_rate), years) - 1)

# %% [markdown]
# ### Intérêts composés - Taux d'intérêt

# %%
# Taux d'intérêt qui donne la valeur future pour un
# capital placé pour une durée d'années.
def future_capital_interest(
    future_capital: float,
    actual_capital: float,
    years: int,
) -> float:
    """Cette fonction permet de calculer le taux d'intérêt qui
    donne la valeur future pour un capital placé pour une durée d'années.

    Ref:
        Taux d'intérêt qui donne la valeur future pour un
        capital placé pour une durée d'années.

    Args:
        future_capital (float): capital à constituer
        actual_capital (float): taux d'intérêt annuel
        years (int): nombre de périodes (années)

    Returns:
        float: le taux d'intérêt qui donne la valeur future du capital
    """

    # Vérification des entrées
    ___(
        {
            years < 0: "Le nombre d'années doit être positif.",
            actual_capital == 0 : "Le capital actuel ne peut pas être égal à 0."
        }
    )

    # Opération de calcul
    return 100 * (pow(future_capital / actual_capital, 1 / years) - 1)

# %% [markdown]
# ### Taux de rendement

# %%
# Calcul du taux zero coupon à partir du facteur d'actualisation.
def zero_coupon_rate(
    actualisation_factor: float,
    years: int,
) -> float:
    """Cette fonction permet de calculer le taux zero coupon pour une maturité
    à partir du facteur d'actualisation pour cette maturité.

    Ref:
        Calcul du taux zero coupon à partir du facteur d'actualisation.

    Args:
        actualisation_factor (float): facteur d'actualisation pour la maturité
        years (int): nombre de périodes (années)

    Returns:
        float: le taux zero coupon
    """

    # Vérification des entrées
    ___(
        {
            years < 0: "Le nombre d'années doit être positif.",
            actualisation_factor == 0 : "Le facteur d'actualisation pour la maturité ne peut pas être égal à 0."
        }
    )

    # Opération de calcul
    return pow(1 / actualisation_factor, 1 / years)

# %%
# Taux de rendement actuariel (périodes annuelles).
def actuarial_rate_of_return(
    actual_value: float,
    future_value: float,
    years: int,
) -> float:
    """Cette fonction permet de calculer le taux de rendement actuariel 
    avec périodes de calcul d'intérêts annuelles.

    Ref:
        Taux de rendement actuariel (périodes annuelles).

    Args:
        actual_value (float): la valeur actuelle
        future_value (float): la valeur future
        years (int): nombre de périodes (années)

    Returns:
        float: le taux de rendement actuariel
    """

    # Vérification des entrées
    ___(
        {
            years < 0: "Le nombre d'années doit être positif.",
            actual_value == 0 : "La valeur actuelle ne peut pas être égale à 0."
        }
    )

    # Opération de calcul
    return pow(future_value / actual_value, 1 / years) - 1

# %% [markdown]
# ### Facteur d'actualisation

# %%
# Calcul du facteur d'actualisation à partir de la valeur 
# actuelle et de la valeur future.
def calculate_actualisation_value_factor(
    actual_value: float,
    future_value: float,
) -> float:
    """Cette fonction permet de calculer le facteur d'actualisation 
    à partir de la valeur future et de la valeur présente d'un flux financier.

    Ref:
        Calcul du facteur d'actualisation à partir de la valeur 
        actuelle et de la valeur future.

    Args:
        actual_value (float): la valeur actuelle
        future_value (float): la valeur future

    Returns:
        float: le facteur d'actualisation
    """

    # Vérification des entrées
    ___(
        {
            future_value == 0 : "La valeur future ne peut pas être égale à 0."
        }
    )

    # Opération de calcul
    return actual_value / future_value

# %%
# Calcul du facteur d'actualisation à partir du
# taux périodique et du nombre de périodes.
def calculate_actualisation_periodic_factor(
    periodic_interest_rate: float,
    periods: int,
) -> float:
    """Cette fonction permet de calculer le facteur d'actualisation pour
    un flux futur avec un taux périodique et un nombre de périodes donnés.

    Ref:
        Calcul du facteur d'actualisation à partir du
        taux périodique et du nombre de périodes.

    Args:
        periodic_interest_rate (float): le taux d'intérêt périodique
        periods (int): le nombre de périodes

    Returns:
        float: le facteur d'actualisation
    """

    # Vérification des entrées
    ___(
        {
            periods <= 0: "Le nombre de périodes doit être strictement positif.",
            periodic_interest_rate
            == -1: "Le taux d'intérêt périodique doit être différent de -1.",
        }
    )

    # Opération de calcul
    return 1 / pow(1 + periodic_interest_rate, periods)

# %% [markdown]
# ### Conversions et comparaisons de taux

# %%
# Taux d'intérêt périodique proportionnel équivalent
# à un taux d'intérêt annuel simple.
def simple_periodic_interest_rate(annual_interest_rate: float, periods: int) -> float:
    """Cette fonction permet de déterminer le taux d'intérêt périodique
    proportionnel équivalent à un taux d'intérêt annuel simple.

    Ref:
        Taux d'intérêt périodique proportionnel équivalent
        à un taux d'intérêt annuel simple.

    Args:
        annual_interest_rate (float): le taux d'intérêt annuel
        periods (int): le nombre de périodes par an

    Returns:
        float: le taux d'intérêt périodique
    """

    # Vérification des entrées
    ___(
        {
            periods <= 0: "Le nombre de périodes doit être strictement positif.",
        }
    )

    # Opération de calcul
    return annual_interest_rate / periods

# %%
# Taux d'intérêt actuariel périodique équivalent
# à un taux d'intérêt actuariel annuel.
def actuarial_periodic_interest_rate(
    annual_interest_rate: float,
    actualisation_periods: int,
) -> float:
    """Cette fonction permet de déterminer le taux d'intérêt actuariel
    périodique équivalent à un taux d'intérêt actuariel annuel.

    Ref:
        Taux d'intérêt actuariel périodique équivalent
        à un taux d'intérêt actuariel annuel.

    Args:
        annual_interest_rate (float): le taux d'intérêt annuel
        actualisation_periods (int): le nombre de périodes d'actualisation par an

    Returns:
        float: le taux d'intérêt actuariel périodique
    """

    # Vérification des entrées
    ___(
        {
            actualisation_periods
            <= 0: "Le nombre de périodes d'actualisation par an doit être strictement positif.",
        }
    )

    # Opération de calcul
    return pow(1 + annual_interest_rate, 1 / actualisation_periods) - 1

# %%
# Conversion d'un taux d'intérêt périodique proportionnel
# en un taux d'intérêt annuel simple équivalent.
def simple_periodic_interest_rate_conversion(
    proportionnal_periodic_rate: float, periods_per_year: int
) -> float:
    """Cette fonction permet la conversion d'un taux d'intérêt périodique
    proportionnel en un taux d'intérêt annuel simple équivalent.

    Ref:
        Conversion d'un taux d'intérêt périodique proportionnel
        en un taux d'intérêt annuel simple équivalent.

    Args:
        proportionnal_periodic_rate (float): le taux périodique proportionnel
        periods_per_year (int): le nombre de périodes par an

    Returns:
        float: la conversion du taux d'intérêt périodique
    """

    # Vérification des entrées
    ___(
        {
            periods_per_year
            <= 0: "Le nombre de périodes par an doit être strictement positif.",
        }
    )

    # Opération de calcul
    return proportionnal_periodic_rate * periods_per_year

# %%
# Conversion d'un taux d'intérêt périodique actuariel
# en un taux d'intérêt annuel actuariel équivalent.
def actuarial_periodic_interest_rate_conversion(
    periodic_interest_rate: float, actualisation_period_per_year: int
) -> float:
    """Cette fonction permet la conversion d'un taux d'intérêt périodique
    actuariel en un taux d'intérêt annuel actuariel équivalent.

    Ref:
        Conversion d'un taux d'intérêt périodique actuariel
        en un taux d'intérêt annuel actuariel équivalent.

    Args:
        periodic_interest_rate (float): le taux d'intérêt périodique actuariel pour une période de 1/m années
        actualisation_period_per_year (int): le nombre de périodes d'actualisation par an

    Returns:
        float: la conversion du taux d'intérêt périodique
    """
    
    # Vérification des entrées
    ___(
        {
            actualisation_period_per_year
            <= 0: "Le nombre de périodes d'actualisation par an doit être strictement positif.",
        }
    )

    # Opération de calcul
    return pow(1 + periodic_interest_rate, actualisation_period_per_year) - 1

# %%
# Conversion taux d'intérêt nominal en taux d'intérêt effectif.
def nominal_interest_rate_conversion(
    nominal_interest_rate: float,
    payments_per_year: int,
) -> float:
    """Cette fonction permet la conversion d'un taux d'intérêt 
    nominal en un taux d'intérêt effectif.

    Ref:
        Conversion taux d'intérêt nominal en taux d'intérêt effectif.

    Args:
        nominal_interest_rate (float): le taux d'intérêt nominal annuel
        payments_per_year (int): le nombre de paiements par an

    Returns:
        float: la taux d'intérêt effectif
    """

    # Vérification des entrées
    ___(
        {
            payments_per_year
            <= 0: "Le nombre de paiements par an doit être strictement supérieur à 0.",
        }
    )

    # Opération de calcul
    return pow(1 + nominal_interest_rate / payments_per_year, payments_per_year) - 1

# %% [markdown]
# ## Crédits
# 
# ### Mensualité du crédit

# %%
# Mensualité de crédit avec un taux et un capital donnés.
def mensuality_credit(
    capital: float,
    annual_nominal_interest_rate: float,
    payments_per_year: int,
    total_annuity_count: int,
) -> float:
    """Cette fonction permet de calculer la mensualité à payer pour rembourser un crédit
    de montant C avec un taux d'intérêt r et une durée de N périodes.
    Elle permet donc de répondre à la question suivante: Combien dois-je débourser
    chaque période si je veux emprunter le montant C à un taux d'intérêt r, en remboursant sur N périodes.

    Ref:
        Mensualité de crédit avec un taux et un capital donnés.

    Args:
        capital (float): le capital initial
        annual_nominal_interest_rate (float): le taux d'intérêt nominal annuel
        payments_per_year (int): le nombre de paiements par an
        total_annuity_count (int): le nombre total d'annuités (nombre d'années x remboursements par an)

    Returns:
        float: la mensualité
    """

    # Vérification des entrées
    ___(
        {
            payments_per_year
            <= 0: "Le nombre de paiements par an doit être strictement supérieur à 0.",
            total_annuity_count
            < 0: "Le nombre total d'annuités doit être strictement supérieur à 0.",
        }
    )

    # Opération de calcul
    return (
        capital
        * (annual_nominal_interest_rate / payments_per_year)
        / (1 - pow(1 + annual_nominal_interest_rate / payments_per_year, -total_annuity_count))
    )

# %% [markdown]
# ### Montant du crédit

# %%
# Capital d'un crédit avec un taux et une mensualité donnés.
def credit_capital(
    annual_nominal_interest_rate: float,
    payments_per_year: int,
    total_annuity_count: int,
    mensuality: float,
) -> float:
    """Cette fonction permet de déterminer le montant (maximum) C  qui peut être
    emprunté avec les conditions de durée N, de taux d'intérêt r et de capacité de
    remboursement par période m données. Elle permet donc de répondre à la question
    suivante : Combien peut-on emprunter, avec un taux d'intérêt de r, une durée de N périodes
    et en payant une mensualité de m ?

    Ref:
        Capital d'un crédit avec un taux et une mensualité donnés.

    Args:
        annual_nominal_interest_rate (float): le taux d'intérêt nominal annuel
        payments_per_year (int): le nombre de paiements par an
        total_annuity_count (int): le nombre total d'annuités (nombre d'années x remboursements par an)
        mensualité (float): la mensualité

    Returns:
        float: le capital du crédit
    """

    # Vérification des entrées
    ___(
        {
            payments_per_year
            <= 0: "Le nombre de paiements par an doit être strictement supérieur à 0.",
            total_annuity_count
            < 0: "Le nombre total d'annuités doit être strictement supérieur à 0.",
        }
    )

    # Opération de calcul
    return (
        mensuality
        * (
            1
            - pow(
                1 + annual_nominal_interest_rate / payments_per_year,
                -total_annuity_count,
            )
        )
        / (annual_nominal_interest_rate / payments_per_year)
    )

# %%
# Calcul du capital remboursé au terme de n périodes.
def capital_repaid(
    capital: float,
    proportionnal_periodic_rate: float,
    periods: int,
    total_annuity_count: int,
) -> float:
    """Cette fonction permet de déterminer la somme totale qui aura été remboursée
    sur un crédit au terme de n périodes, donc d'isoler et de additionner la part
    des mensualités consacrée au remboursement de capital au terme de n périodes.

    Ref:
        Calcul du capital remboursé au terme de n périodes.

    Args:
        capital (float): le capital initial
        proportionnal_periodic_rate (int): le taux périodique proportionnel
        periods (int): le nombre de périodes
        total_annuity_count (int): le nombre total d'annuités (nombre d'années x remboursements par an)

    Returns:
        float: le capital remboursé
    """

    # Vérification des entrées
    ___(
        {
            periods <= 0: "Le nombre de périodes doit être strictement supérieur à 0.",
            total_annuity_count
            < 0: "Le nombre total d'annuités doit être strictement supérieur à 0.",
        }
    )

    # Opération de calcul
    return (
        capital
        * (pow(1 + proportionnal_periodic_rate, periods) - 1)
        / (pow(1 + proportionnal_periodic_rate, total_annuity_count) - 1)
    )

# %%
# Calcul du capital restant à rembourser au terme de n périodes.
def capital_remaining(
    annuity: float,
    proportionnal_periodic_rate: float,
    periods: int,
    total_annuity_count: int,
) -> float:
    """Cette fonction permet de calculer le capital restant à rembourser R sur
    un crédit au terme de n périodes.

    Ref:
        Calcul du capital restant à rembourser au terme de n périodes.

    Args:
        annuity (float): l'annuité
        proportionnal_periodic_rate (int): le taux périodique proportionnel
        periods (int): le nombre de périodes
        total_annuity_count (int): le nombre total d'annuités (nombre d'années x remboursements par an)

    Returns:
        float: le capital restant à payer
    """

    # Vérification des entrées
    ___(
        {
            periods <= 0: "Le nombre de périodes doit être strictement supérieur à 0.",
            total_annuity_count
            < 0: "Le nombre total d'annuités doit être strictement supérieur à 0.",
            proportionnal_periodic_rate
            == 0: "Le taux périodique proportionnel ne peut pas être égal à 0.",
        }
    )

    # Opération de calcul
    return (
        annuity
        * (1 - pow(1 + proportionnal_periodic_rate, -(total_annuity_count - periods)))
        / proportionnal_periodic_rate
    )

# %% [markdown]
# ### Durée du crédit

# %%
# Calcul de la durée d'un crédit en nombre de périodes à partir de montant, taux et mensualité.
def credit_duration(
    capital: float,
    mensuality: float,
    annual_nominal_interest_rate: float,
    payements_per_year: int,
) -> float:
    """Cette fonction permet de calculer durée d'un crédit lorsque le montant,
    le taux d'intérêt et de la mensualité sont connus.

    Ref:
        Calcul de la durée d'un crédit en nombre de périodes à partir de montant, taux et mensualité.

    Args:
        captial (float): le capital initial
        mensuality (float): la mensualité
        annual_nominal_interest_rate (int): le taux d'intérêt nominal annuel
        payements_per_year (int): le nombre de paiements par an

    Returns:
        float: la durée du crédit (en mois)
        
    """

    # Vérification des entrées
    ___(
        {
            payements_per_year
            <= 0: "Le nombre de paiements par an doit être strictement supérieur à 0.",
            annual_nominal_interest_rate
            == 0: "Le taux périodique proportionnel ne peut pas être égal à 0.",
        }
    )

    # Opération de calcul
    return math.log(
        -mensuality
        / (capital * annual_nominal_interest_rate / payements_per_year - mensuality)
    ) / math.log(1 + annual_nominal_interest_rate / payements_per_year)

# %% [markdown]
# ---

# %% [markdown]
# ## Démonstrations pratiques avec des exercices

# %% [markdown]
# ### Importation du module

# %%
import awaz

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

print(f"""Les ventes ont connu une augmentation de {augmentation_percent *100}% de la première à la 
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

print(f"""Les ventes ont connu une diminution de {diminution_percent * 100}% de la première à la deuxième 
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
# Cette fonction permet de calculer la durée d'un crédit lorsque le montant, le 
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
# ---

# %% [markdown]
# ## Exemples de cas d'utilisation

# %% [markdown]
# ### Interpolation linéaire
# L'interpolation linéaire peut être utilisée pour estimer des valeurs intermédiaires entre deux points de données connus. Dans le contexte du calcul des impôts sur le revenu, cette méthode pourrait être appliquée pour estimer le montant d'impôts à payer pour un revenu situé entre deux tranches d'imposition connues.
# #### Exemple
# Supposons qu'un contribuable a un revenu annuel de 45 000 €. Les tranches d'imposition connues sont les suivantes :
# - De 0 € à 30 000 € : Taux d'imposition de 15%
# - De 30 001 € à 50 000 € : Taux d'imposition de 25%
# Pour calculer les impôts à payer sur ce revenu, nous pouvons utiliser l'interpolation 
# linéaire pour estimer le montant d'impôts à payer pour la tranche de revenu située 
# entre 30 000 € et 45 000 €.

# %%
# Le revenu du contribuable
income: float = 45_000
# Calcul du tax d'imposition
tax: float = awaz.linear_interpolation(income, 30_000, 50_000, 15 / 100, 25 / 100)
# Arrondissement du taux
tax = round(tax, 2)
# Affichage du résultat
print(
f"""Le taux d'impôt estimé à payer pour le revenu de 45 000 € est de {tax * 100}% 
pour un total de montant d'imposition de {income * tax}€."""
)

# %% [markdown]
# ### Moyenne pondérée
# Pour calculer des impôts sur le salaire en utilisant la formule de la moyenne pondérée, nous pouvons appliquer cette formule pour estimer les impôts à payer en fonction des différents composants du salaire et de leurs poids respectifs.
# ### Exemple
# Supposons qu'un salarié ait les revenus suivants avec leurs coefficients respectifs :
# - Salaire de base : 440 500 FCFA (coefficient 3)
# - Prime annuelle : 120 300 FCFA (coefficient 2)
# - Avantages en nature : 59 850 FCFA (coefficient 1)
# En utilisant la fonction de calcul de la moyenne pondérée avec les valeurs et les coefficients donnés, nous pouvons calculer la moyenne pondérée du salaire et ensuite, en appliquant le taux d'imposition approprié à cette moyenne pondérée, nous pouvons estimer les impôts à payer sur ce salaire.
# Cela permettrait au salarié de planifier ses obligations fiscales en tenant compte des différents composants de son salaire et de leurs poids respectifs.

# %%
# Impôt sur salaire selon l'OTR
tax:float = 25 / 100 # 25%
# Calcul du salaire pondéré
ponderous_salary:float = awaz.ponderous_mean([440_500, 120_300, 59_850], [3, 2, 1])
# Affichage du résultat
print(f"""Le salaire pondéré du salarié, revient à {ponderous_salary}FCFA. 
Le montant de son impôt s'élève donc à {ponderous_salary * tax}FCFA.""")

# %% [markdown]
# ### Calcul d'un taux d'intérêt réel
# Pour calculer des impôts sur le patrimoine immobilier d'une société en utilisant la formule du taux d'intérêt réel, nous pouvons estimer les impôts à payer en fonction de l'évolution de la valeur de ce patrimoine due à l'inflation.
# #### Exemple
# Supposons qu'une société possède un patrimoine immobilier composé de biens d'une valeur totale de 2 000 000 FCFA au 1er janvier de l'année d'imposition. De plus, le société a des dettes déductibles d'un montant total de 300 000 FCFA.
# Le taux d'inflation pour cette année est de 2%. Le taux d'intérêt nominal applicable à ce patrimoine est de 3%.
# Pour calculer les impôts sur le patrimoine, nous devons d'abord déterminer le taux d'intérêt réel en tenant compte du taux d'inflation et du taux d'intérêt nominal. Ensuite, nous appliquerons le taux d'imposition approprié en fonction du patrimoine net taxable.

# %%
# Taux d'impôt selon OTR
tax: float = 7 / 100  # 7%
# Calcul du taux d'intérêt réel
interest: float = awaz.fisher_real_interest(2 / 100, 3 / 100)
# Arrondi du taux d'intérêt réel
interest = round(interest, 2)
# Calcul du patrimoine net taxable
# avec les effets de l'inflation
real_estate = (2_000_000 - 300_000) + ((2_000_000 - 300_000) * interest)
# Affichage des résultats
print(
    f"""Les impôts à payer sur ce patrimoine s'élève à {round(tax * 100, 2)}%, soit {round(real_estate * tax, 2)}FCFA."""
)

# %% [markdown]
# ## Conclusion
# Le module de fisaclité `awaz` n'en est qu'à ses débuts avec une cinquante de fonctions prêtes à l'usage. Dans les prochaines versions, il comprendra une plus large gamme de méthodes fiscales plus avancées.
# 
# 
# ``Team awaz``

# %% [markdown]
# ---


