# LearningLanguage

Application d'apprentissage des langues pour apprendre de nouveaux mots en anglais/français avec un système d'entraînement interactif.

## 📋 Table des Matières
- [Informations Générales](#informations-générales)
- [Installation](#installation)
- [Lancement](#lancement)
- [Architecture](#architecture)
- [Fonctionnalités](#fonctionnalités)
- [Utilisation](#utilisation)
- [Structure du Projet](#structure-du-projet)
- [Développement](#développement)
- [Licence](#licence)

## 📊 Informations Générales

- **Nom du projet** : LearningLanguage
- **Type** : Application d'apprentissage des langues
- **Langage** : Python avec interface Tkinter
- **Architecture** : MVC (Model-View-Controller)
- **Date de début** : 10/08/2024

## 🚀 Installation

### Prérequis
- Python 3.x installé
- Environnement de développement configuré

### Commandes
```bash
# Cloner le projet
git clone <repository-url>

# Se placer dans le répertoire
cd LearningLanguage

# Lancer l'application
python main.py
```

## 🎯 Lancement

### Démarrer l'application
```bash
python main.py
```

### Options
- L'application se lance en mode fenêtre (350x450 pixels)
- Interface graphique Tkinter avec icône personnalisée

## 🏗️ Architecture

### Architecture MVC
L'application suit le pattern Modèle-Vue-Contrôleur :

```mermaid
graph TD
    A[Vue (MainView.py)] --> B[Contrôleur (controler/)]
    B --> C[Modèle (model/)]
    C --> D[Données (data.json)]
```

### Classes Principales

#### Modèle (`model/`)
- **`Mot`** : Représente un mot avec sa traduction et son statut de connexion
- **`Boite`** : Conteneur de mots avec date
- **`MainModel`** : Gestionnaire principal des mots

#### Vue (`view/`)
- **`MainView`** : Interface graphique Tkinter avec système de quiz

## 🔧 Fonctionnalités

### Interface Graphique
- Fenêtre principale de 350x450 pixels
- Menu avec boutons "Dictionnaire" et "Historique"
- Zone d'affichage des mots à traduire
- Zone de saisie pour les réponses
- Boutons "Valider" et "Passer"

### Système de Mots
- Liste prédéfinie de mots anglais/français
- Classe `Mot` avec attributs : mot, traduction, connet
- Système de boîtes pour organiser les mots

### Système d'Entraînement
- Quiz interactif pour apprendre les traductions
- Système de validation des réponses
- Possibilité de passer les mots difficiles

## 👤 Utilisation

### Démarrage
1. Lancez l'application avec `python main.py`
2. L'interface principale s'affiche avec un mot à traduire

### Fonctionnement
1. Un mot anglais s'affiche dans la zone principale
2. Saisissez la traduction française dans le champ de saisie
3. Cliquez sur "Valider" pour vérifier votre réponse
4. Utilisez "Passer" pour passer au mot suivant

### Navigation
- **Dictionnaire** : Accès au dictionnaire complet (fonctionnalité à implémenter)
- **Historique** : Consultation de l'historique des réponses (fonctionnalité à implémenter)

## 📁 Structure du Projet

```
LearningLanguage/
├── main.py                 # Point d'entrée principal
├── README.md               # Documentation
├── LICENSE                 # Licence du projet
├── .gitignore              # Fichiers ignorés par Git
├── controler/              # Contrôleurs (vides pour l'instant)
├── image/                  # Ressources visuelles
│   ├── icon/               # Icônes
│   └── shema/              # Schémas (vides pour l'instant)
├── model/                  # Modèle de données
│   ├── __init__.py
│   ├── Boite.py            # Classe pour les boîtes de mots
│   ├── data.json           # Données (vide)
│   ├── entrainement.py     # Algorithmes d'entraînement
│   ├── MainModel.py        # Modèle principal
│   ├── Mot.py              # Classe pour les mots
│   └── __init__.py
└── view/                   # Interface graphique
    ├── __init__.py
    └── MainView.py          # Vue principale
```

## 🐛 Développement

### Comment Contribuer
1. Fork du projet
2. Création d'une branche (`git checkout -b feature/nouvelle-fonctionnalité`)
3. Commit des changements (`git commit -am 'Ajout de la fonctionnalité X'`)
4. Push vers la branche (`git push origin feature/nouvelle-fonctionnalité`)
5. Ouverture d'une Pull Request

### Tests
- Tests unitaires à implémenter
- Tests d'interface graphique à implémenter

### Dépannage
- Problèmes courants
- Solutions
- Contact

## 📝 Licence

Ce projet est sous licence [MIT](LICENSE).

## 🔗 Ressources

- [Liste de mots anglais les plus utilisés](https://bilingueanglais.com/blog/54212/mots-plus-utilises-anglais/)
- [500 mots fréquents en anglais](https://www.ispeakspokespoken.com/500-mots-frequents-anglais/)
- [Documentation Tkinter](https://docs.python.org/fr/3/library/tkinter.html)

## 🔄 Évolution Future

### Fonctionnalités Prévues
- [ ] Dictionnaire complet avec recherche
- [ ] Historique des réponses et statistiques
- [ ] Système de niveaux et progression
- [ ] Mode multijoueur
- [ ] Export des données d'apprentissage
- [ ] Support de plusieurs langues

### Améliorations
- [ ] Interface plus moderne
- [ ] Animations et effets visuels
- [ ] Système de notifications
- [ ] Mode hors-ligne

---

*Ce projet a été développé dans le cadre d'un apprentissage personnel du Python et de la programmation d'interfaces graphiques.*