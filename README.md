<<<<<<< HEAD
# Data-Science---Arbre-de-d-cision

=======
# Data-Science Arbre-de-decision

Explication détaillée du travail effectué dans le code
Étapes principales du code :
Chargement des données :
Le fichier bank.csv est chargé en utilisant pandas. Le séparateur est spécifié comme ; pour s'assurer que les données sont correctement lues.
Les colonnes disponibles dans le fichier sont explorées pour comprendre leur structure et leur utilité.

Préparation des données :
Sélection des caractéristiques (features) : Certaines colonnes numériques comme age, balance, day, duration, campaign, pdays, et previous sont utilisées comme variables explicatives.
Conversion des données catégoriques : La colonne cible y est transformée en valeurs numériques, où no devient 0 et yes devient 1. Cela est nécessaire pour que le modèle puisse interpréter les données.
Gestion des valeurs manquantes : Si des valeurs manquantes existent, elles sont remplacées par la médiane de chaque colonne.

Division des données :
Les données sont divisées en deux ensembles : un ensemble d'entraînement (80 % des données) et un ensemble de test (20 % des données). Cette division permet d'entraîner le modèle et de tester sa performance sur des données non vues.

Création et entraînement de l'arbre de décision :
Un arbre de décision est créé avec une profondeur maximale de 5. Cela limite le sur-apprentissage en empêchant l'arbre de devenir trop complexe.
L'arbre est entraîné sur l'ensemble d'entraînement.

Évaluation du modèle :
La précision du modèle est calculée sur l'ensemble de test. Elle mesure le pourcentage de prédictions correctes.

Visualisation de l'arbre de décision :
Un graphique de l'arbre est généré, montrant les règles utilisées pour classer les observations.

Exportation des règles :
Les règles de décision sont exportées sous forme textuelle pour mieux comprendre les décisions prises par l'arbre.

![Figure_1](https://github.com/user-attachments/assets/cd9cdc6a-ca5e-4d93-977f-739b7947107f)
>>>>>>> 88ce8e794972710838bb5444e8c5dcf57ae36bde
