import pandas as pd
import folium

class Jeu_Dpt:
    def __init__(self):
        self.geo = pd.read_csv(
                    "data/correspondance-code-insee-code-postal.csv",
                    sep=";",
                    usecols = ['Statut',
                               'Code Département',
                               'Commune',
                               'geo_point_2d']
                 ).query(
                    'Statut in ["Préfecture", "Préfecture de région"]'
                 ).query('`Code Département` != 97')
        self.historique = pd.read_csv(
            "data/historique.csv", 
            index_col=0
            )

    def _fit(self):
        fond = r'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'
        self.carte = folium.Map(
            location=[46.5, 2.3], 
            zoom_start=6, 
            tiles=fond, 
            attr='© OpenStreetMap © CartoDB'
            )
        self.carte.save("data/image.html")
        folium.Choropleth(
            "data/contour-des-departements.geojson",
            fill_color='yellow'
            ).add_to(self.carte)
    
    def _graph(self, Code):
        self._fit() #Initilisation de la carte
        loc = self.geo.loc[self.geo['Code Département']==Code, 'geo_point_2d'].to_list()[0]
        Commune = self.geo.loc[self.geo['Code Département']==Code, 'Commune'].tolist()[0]
        folium.Marker(
            [loc.split(',')[0], loc.split(',')[1]], popup=f"{Code} : {Commune}"
            ).add_to(self.carte)
        display(self.carte)

    def play(self, graph = True, nb_tour=20):
        import random
        erreur = 0
        code_list = self.geo['Code Département'].unique().tolist()
        for i in range(nb_tour):
            Code = random.choice(code_list)
            code_list.remove(Code)
            Commune = self.geo.loc[self.geo['Code Département']==Code, 'Commune'].tolist()[0]
            Commune_joueur = input(f"Quelle est la préfécture associé au numéro de département {Code} : ")
            if Commune_joueur.lower() != Commune.lower():
                print(f"ERROR : La préfécture est {Commune.lower()}")
                erreur +=1
                self.historique.loc[Code,'Erreur'] = self.historique.loc[Code,'Erreur'] + 1
                if graph:
                    _graph()
            else:
                self.historique.loc[Code,'Correct'] = self.historique.loc[Code,'Correct'] + 1
        self.historique.to_csv("data/historique.csv")
        print(f"Votre score est de {nb_tour-erreur}/{nb_tour}")
