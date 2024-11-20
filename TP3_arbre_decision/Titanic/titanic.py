# Importer les bibliothèques nécessaires
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
data_bank = pd.read_csv('bank.csv', delimiter=';')

# Préparer les données pour l'arbre de décision

# Sélectionner les caractéristiques
X = data_bank[['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']]

# Convertir les colonnes catégoriques en valeurs numériques
data_bank['y'] = data_bank['y'].map({'no': 0, 'yes': 1})  # Cible binaire
y = data_bank['y']

# Gérer les valeurs manquantes (s'il y en a)
X = X.fillna(X.median())

# Diviser les données en jeu d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer et entraîner l'arbre de décision
clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(X_train, y_train)

# Évaluer le modèle
accuracy = clf.score(X_test, y_test)
print(f"Précision du modèle sur les données de test : {accuracy:.2f}")

# Visualiser l'arbre de décision
plt.figure(figsize=(20, 14))
plot_tree(
    clf,
    feature_names=X.columns,
    class_names=['No', 'Yes'],
    filled=True,
    fontsize=10
)
plt.tight_layout()
plt.show()

# Exporter une version textuelle des règles de l'arbre de décision
tree_rules = export_text(clf, feature_names=list(X.columns))
print(tree_rules)
