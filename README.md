\# RetailVision — Intelligence commerciale e-commerce



\*\*Data Analysis | Python | Pandas | SQL | Streamlit | Machine Learning | Power BI\*\*



\*\*Statut :\*\* Projet en développement — Phase 1 : exploration et qualité des données.



\## 1 / Présentation du projet



RetailVision est un projet d'analyse et de valorisation des données commerciales d'une entreprise e-commerce.



À partir du dataset Online Retail, nous cherchons à construire une solution permettant de comprendre les performances commerciales, d'analyser les comportements d'achat et d'anticiper l'évolution du chiffre d'affaires.



L'objectif est de transformer des données transactionnelles brutes en informations exploitables afin de faciliter la prise de décision commerciale.



\## 2 / Objectifs



Le projet s'articule autour de trois axes principaux.



\### Analyse commerciale



Nous souhaitons mesurer le chiffre d'affaires, étudier son évolution dans le temps et identifier les produits ainsi que les marchés qui contribuent le plus aux ventes.



\### Segmentation client



Nous prévoyons d'utiliser la méthode RFM (Récence, Fréquence, Montant) pour identifier différents profils de clients et mieux comprendre leur contribution aux performances commerciales.



\### Prévision



Nous souhaitons développer un modèle permettant d'estimer le chiffre d'affaires hebdomadaire. Nous comparerons une méthode de prévision naïve à un modèle supervisé.



\## 3 / Présentation des données



Nous utilisons le dataset \[Online Retail — UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail).



Il contient 541 909 lignes de transactions, réparties sur huit variables, entre décembre 2010 et décembre 2011.



Les données concernent 38 pays et les prix sont exprimés en livres sterling (£).



Les variables disponibles sont `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID` et `Country`.



\## 4 / Première exploitation des données



Avant de construire les indicateurs commerciaux, nous avons commencé par une exploration du dataset afin d'en comprendre la structure et d'identifier les principales anomalies.



Cette première analyse a mis en évidence :



\- 135 080 lignes sans identifiant client.

\- 1 454 lignes sans description de produit.

\- 10 624 lignes présentant une quantité négative.

\- 2 515 lignes avec un prix nul.

\- 2 lignes avec un prix négatif.



Nous avons également identifié des doublons et plusieurs types d'opérations particulières.



Ces résultats montrent l'importance de définir des règles de gestion avant de calculer le chiffre d'affaires.



Nous avons donc choisi de conserver les données brutes et de distinguer les ventes positives, les annulations et les autres opérations.



\## 5 / Présentation du code



Le premier script développé, `src/data\_quality.py`, permet de charger les données, de mesurer leur qualité, de classifier les transactions et de générer un rapport JSON.



\### `load\_data()`



Cette fonction charge le fichier Excel dans un DataFrame Pandas.



\### `check\_data()`



Elle calcule les premiers indicateurs de qualité : nombre de lignes, identifiants clients manquants, doublons et quantités négatives.



\### `transactions\_name()`



Cette fonction ajoute une colonne `transaction\_type` afin de distinguer les transactions.



La première classification a permis d'identifier :



\- \*\*530 104 lignes\*\* de ventes positives.

\- \*\*9 288 lignes\*\* d'annulations.

\- \*\*2 517 lignes\*\* nécessitant une classification complémentaire.



\### `fichier\_report()`



Cette fonction exporte les indicateurs de qualité dans le fichier `reports/data\_quality.json`.



\## 6 / Structure du projet



Les différents fichiers sont organisés selon leur fonction :



\- `data/raw/` : données brutes.

\- `data/processed/` : données préparées.

\- `notebooks/` : analyses exploratoires.

\- `src/` : scripts Python.

\- `reports/` : rapports générés.

\- `app.py` : future application Streamlit.

\- `requirements.txt` : dépendances du projet.



Les données brutes et le notebook personnel ne sont pas publiés dans le dépôt GitHub.



\## 7 / Installation et exécution



Le dataset doit être téléchargé depuis l'UCI Machine Learning Repository et placé dans `data/raw/` sous le nom `Online Retail.xlsx`.



Sous Windows, nous pouvons préparer l'environnement Python avec :



```powershell

py -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

python -m pip install -r requirements.txt

```



Puis exécuter le script :



```powershell

python src/data\_quality.py

```



Le rapport de qualité est alors généré dans `reports/data\_quality.json`.



\## 8 / Méthodologie



Notre démarche repose sur la conservation des données originales et sur la définition de règles explicites pour les différentes analyses.



Les ventes positives sont provisoirement définies comme les transactions présentant une quantité et un prix positifs, avec un numéro de facture ne commençant pas par `C`.



Les factures commençant par `C` sont classées parmi les annulations.



Les transactions sans identifiant client peuvent être conservées pour le calcul des ventes positives, mais seront exclues de la segmentation RFM individuelle.



Les doublons et les opérations particulières nécessitent encore une validation de leur traitement.



\## 9 / Limites de l'analyse



Cette première version se concentre sur l'exploration et les contrôles qualité.



Certaines écritures restent à interpréter et les règles de calcul du chiffre d'affaires net ne sont pas encore finalisées.



Les motifs des retours ne sont pas disponibles, et les données ne permettent pas de mesurer directement la satisfaction client.



L'application web, la segmentation RFM et les modèles de prévision restent à développer.



\## 10 / Perspectives d'évolution



Les prochaines étapes du projet sont :



\- Finaliser le pipeline de nettoyage et ses tests.

\- Construire la base SQLite et les requêtes SQL.

\- Développer les KPI commerciaux et les visualisations.

\- Créer l'application Streamlit avec filtres et exports CSV.

\- Réaliser la segmentation RFM.

\- Comparer les modèles de prévision.

\- Créer le dashboard Power BI.

\- Déployer une version fonctionnelle de RetailVision.



L'objectif final est de proposer une solution d'analyse commerciale accessible depuis une application web, avec des traitements reproductibles et une méthodologie documentée.

