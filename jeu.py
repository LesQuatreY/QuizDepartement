import folium
import pandas as pd
from utils import (clean_data, read_historique)

class Jeu_Dpt:
    def __init__(self):
        self.geo = pd.read_csv(
                    "data/correspondance-code-insee-code-postal.csv",
                    sep=";",
                    usecols = ['Statut',
                               'Code Département',
                               'Commune',
                               "Département",
                               'geo_point_2d']
                 ).pipe(clean_data).set_index("Code Département")
        if not read_historique():
            self.historique=self.geo.assign(Correct=0).assign(Erreur=0)[["Commune","Correct","Erreur"]]
        else:
            self.historique=pd.read_csv("data/historique.csv", index_col=0)
        self.code_list = self.geo.index.tolist()
        self.erreur = 0
    
    def get_with_code(self, code, col):
        return self.geo.loc[code, col]

    def get_with_commune(self, commune, col):
        if col=="Code Département":
            return self.geo.loc[self.geo["Commune"]==commune.upper()].index[0]
        return self.geo.loc[self.geo["Commune"]==commune.upper(), col].to_list()[0]

    def get_with_departement(self, dep, col):
        if col=="Code Département":
            return self.geo.loc[self.geo["Département"]==dep.upper()].index[0]
        return self.geo.loc[self.geo["Département"]==dep.upper(), col].to_list()[0]
        
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
            fill_color='white'
            ).add_to(self.carte)
    
    def _graph(self, Code):
        from streamlit_folium import folium_static
        self._fit() #Initilisation de la carte
        folium.Marker(
            [
                self.get_with_code(Code,"geo_point_2d").split(',')[0], 
                self.get_with_code(Code,"geo_point_2d").split(',')[1]
                ], 
            popup="{} : {}".format(Code,self.get_with_code(Code, "Commune"))
            ).add_to(self.carte)
        folium_static(self.carte)

    def verification(self, Code, Commune_joueur):
        self.Commune = self.get_with_code(Code, "Commune")
        if (Commune_joueur.lower() == self.Commune.lower()) | (Commune_joueur.lower() == self.Commune.lower().replace("-", " ")): 
            return True
        else: return False
    
    def _save_histo(self):
        if read_historique():
            self.historique.to_csv("data/historique.csv")

    def main(self, Code, Commune_joueur, graph = True):
        if (graph)&(~self.verification(Code, Commune_joueur)): self._graph(Code)
        if self.verification(Code, Commune_joueur): self.historique.loc[Code,'Correct']+=1
        else:  
            self.historique.loc[Code,'Erreur']+=1
            self.erreur +=1
        self._save_histo()