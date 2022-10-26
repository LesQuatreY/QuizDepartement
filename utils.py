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
