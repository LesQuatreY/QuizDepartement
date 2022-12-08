def clean_data(data):
    return data[
        (data['Statut'].isin(['Préfecture', 'Préfecture de région', 'Capitale d\'état']))
        &(data['Code Département'] != '97')
        ].assign(
            Commune = data['Commune'].str.replace( 
            "--1ER-ARRONDISSEMENT", ""
            ).str.replace(
                "-1ER-ARRONDISSEMENT", ""
            )
            )

def read_historique():
    import pandas as pd
    try: 
        pd.read_csv(
            "data/historique.csv", 
            index_col=0
            )
        return True
    except: return False
