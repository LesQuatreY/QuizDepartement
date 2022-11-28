import folium
import pandas as pd
import streamlit as st
from utils import clean_data

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
                 ).pipe(clean_data)
        self.historique = pd.read_csv(
            "data/historique.csv", 
            index_col=0
            )
        self.code_list = self.geo['Code Département'].unique().tolist()
        self.erreur = 0

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
        from streamlit_folium import folium_static
        self._fit() #Initilisation de la carte
        loc = self.geo.loc[self.geo['Code Département']==Code, 'geo_point_2d'].to_list()[0]
        folium.Marker(
            [loc.split(',')[0], loc.split(',')[1]], popup=f"{Code} : {self.geo.loc[self.geo['Code Département']==Code, 'Commune'].tolist()[0]}"
            ).add_to(self.carte)
        folium_static(self.carte)
    def verification(self, Code, Commune_joueur):
        self.Commune = self.geo.loc[self.geo['Code Département']==Code, 'Commune'].tolist()[0]
        if Commune_joueur.lower() != self.Commune.lower():
            self.erreur +=1
            return False
        else:
            return True

    def main(self, Code, Commune_joueur, graph = True):
        if (graph)&(~self.verification(Code, Commune_joueur)): self._graph(Code)
        if self.verification(Code, Commune_joueur): self.historique.loc[Code,'Correct']+=1
        else:  self.historique.loc[Code,'Erreur']+=1
        self.historique.to_csv("data/historique.csv")