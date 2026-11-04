import pandas as pd 
from pathlib import Path
import json


def load_data(path):
    try:
        df = pd.read_excel(path)
        print(f'Données chargées avec succès depuis {path}.')
        return df
    except FileNotFoundError:
        print(f'Erreur : Le fichier {path} est introuvable. Attention: cela doit etre un fichier excel.')
        return None 


def check_data(df):
    report = {
        "Nombre total de lignes": len(df),
        "Nombre de ligne sans CustomerID": int(df["CustomerID"].isna().sum()),
        "Nombre de doublons exacts": int(df.duplicated(keep=False).sum()),
        "Nombre de lignes avec quantité négative": int((df["Quantity"] < 0).sum())
    }
    return report


def transactions_name(df):
    df_clean = df.copy()

    # 1. Initialiser toutes les lignes
    df_clean["transaction_type"] = "a_classifier"

    # 2. Construire le masque des ventes positives
    mask_vente = (
        (df_clean["Quantity"] > 0)
        & (df_clean["UnitPrice"] > 0)
        & ~(df_clean["InvoiceNo"].astype(str).str.startswith("C"))
    )

    mask_annulation = df_clean["InvoiceNo"].astype(str).str.startswith("C")
    

    # 3. Affecter la catégorie aux lignes concernées
    df_clean.loc[mask_vente, "transaction_type"] = "vente_positive"
    df_clean.loc[mask_annulation, "transaction_type"] = "annulation"

    return df_clean

def fichier_report(report, output_path):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, mode="w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=4)
    
    print(f"✅ Le rapport JSON a été généré ici : {output_path}")
    
    


if __name__ == "__main__":
    ROOT = Path(__file__).resolve().parents[1]
    path = ROOT / "data" / "raw" / "Online Retail.xlsx"

    output_path = ROOT / "reports" / "data_quality.json"
    df = load_data(path)
    df_classified = transactions_name(df)
    quality_report = check_data(df)
    data_quality_report = fichier_report(quality_report, output_path)

    print(df_classified["transaction_type"].value_counts())
    print(df_classified.shape)

df_autres = df_classified[
    df_classified["transaction_type"] == "a_classifier"
]

print(f'Nombre de ligne a classifier avec un prix inferieur a zéros {(df_autres["UnitPrice"] < 0).sum()}.')
print(f'Nombre de ligne a classifier avec un prix égale à zéros {(df_autres["UnitPrice"] == 0).sum()}.')
print(f'Nombre de ligne a classifier avec une quantité négative {(df_autres["Quantity"] < 0).sum()}.')

