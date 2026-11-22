from pathlib import Path
from data_quality import load_data, transactions_name

ROOT = Path(__file__).resolve().parents[1]
data_path = ROOT / "data" / "raw" / "Online Retail.xlsx"



df = load_data(data_path)
df_classified = transactions_name(df)

def prepare_sales(df_classified):
# Sélectionner les ventes positives
    df_ventes = df_classified[
        df_classified["transaction_type"] == "vente_positive"].copy()
    
# Calculer le montant de chaque ligne
    df_ventes["total_price"] = (
        df_ventes["Quantity"] * df_ventes["UnitPrice"])

    return df_ventes


def sales_by_country(df_ventes):
    ca_par_pays = (df_ventes.groupby("Country")["total_price"].sum().sort_values(ascending=False))

    return ca_par_pays


if __name__ == "__main__":
    df_ventes = prepare_sales(df_classified)

    montant_max = df_ventes["total_price"].max()

    transaction_max = df_ventes[
        df_ventes["total_price"] == montant_max
    ]

    print(
        transaction_max[
            ["InvoiceNo", "Description", "Quantity", "UnitPrice", "total_price"]
        ].to_string(index=False)
    )

    ca_total = df_ventes["total_price"].sum()

    print(f"Chiffre d'affaires des ventes positives : {ca_total:.2f} £")
    print("Nombre de lignes de ventes :", len(df_ventes))
    print("Montant minimum :", df_ventes["total_price"].min())
    print("Montant maximum :", df_ventes["total_price"].max())
    print(ca_par_pays)
    print(ca_par_pays.sum())

    nombre_commandes = df_ventes["InvoiceNo"].nunique()
    print("Nombre de commandes :", nombre_commandes)

    panier_moyen = ca_total/nombre_commandes
    print("Panier moyens :", panier_moyen)

    nombre_commandes_pays = df_ventes.groupby("Country")["InvoiceNo"].nunique()
    print("Nombre de commandes par pays :", nombre_commandes_pays)

    ca_par_pays = sales_by_country(df_ventes)
    panier_moyen_par_pays = ca_par_pays/nombre_commandes_pays
    print("Panier moyen par pays :", panier_moyen_par_pays)

    





