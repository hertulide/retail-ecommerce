import sqlite3
from pathlib import Path
from data_quality import load_data, transactions_name
from data_preparation import prepare_sales

ROOT = Path(__file__).resolve().parents[1]

db_path = ROOT / "data" / "processed" / "retailvision.db"

data_path = ROOT / "data" / "raw" / "Online Retail.xlsx"

db_path.parent.mkdir(parents=True, exist_ok=True)


def save_to_sqlite(df_ventes, connexion):
    lignes = df_ventes.to_sql(
    name="sales",
    con=connexion,
    if_exists="replace",
    index=False
    )
    return lignes

def get_total_revenue(connexion):
    curseur = connexion.cursor()

    curseur.execute("SELECT SUM(total_price) FROM sales")
    ca_total = curseur.fetchone()[0]
    return ca_total

def get_revenue_by_country(connexion):
    curseur = connexion.cursor()
    curseur.execute(""" SELECT Country, SUM(total_price)  AS CA
            FROM sales
            GROUP BY Country 
            ORDER BY CA DESC""")
    pays_ca = curseur.fetchall()
    return pays_ca 

def get_revenue_by_month(connexion):
    curseur = connexion.cursor()
    curseur.execute("""
            SELECT
                strftime('%Y-%m', InvoiceDate) AS month,
                SUM(total_price) AS CA
            FROM sales
            GROUP BY strftime('%Y-%m', InvoiceDate)
            ORDER BY month ASC
        """)
    
    mois = curseur.fetchall()
    return mois

if __name__ == "__main__":
    df = load_data(data_path)
    df_classified = transactions_name(df)
    df_ventes = prepare_sales(df_classified)

    connexion = sqlite3.connect(db_path)

    lignes = save_to_sqlite(df_ventes, connexion)

    print("Nombre de lignes enregistrées :", lignes)

    curseur = connexion.cursor()

    #nombre de lignes
    curseur.execute("SELECT COUNT(*) FROM sales")
    nombre_lignes = curseur.fetchone()[0]
    
    #nombre de commandes
    curseur.execute("SELECT COUNT(DISTINCT InvoiceNo) FROM sales")
    nombre_commandes = curseur.fetchone()[0]
    
    #chiffre d'affaires
    ca_total = get_total_revenue(connexion)

    #top 5 des pays avec le plus grand ca
    pays_ca = get_revenue_by_country(connexion)

    #ca par mois
    month_ca = get_revenue_by_month(connexion)


    print("Nombre de lignes vérifiées avec SQL :", nombre_lignes)
    print("Chiffre d'affaires :", ca_total)
    print("Nombre de commandes :", nombre_commandes)
    print("Top 5 des pays :", pays_ca[:5])
    print("Chiffre d'affaires mensuel :", month_ca)
    
    
    connexion.close()
