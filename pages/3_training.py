import streamlit as st

from Lancement_jeu import Jeu_Dpt

st.title("Entraînement :")
jeu = Jeu_Dpt()

options = st.selectbox(
    label="Comment souhaitez-vous définir le département ?",
    options=["Numéro de département", "Nom de la commune", "Nom du département"],
    index=0)
input = st.text_input("")
if not input: st.stop()
    
try:
    if options=="Numéro de département":
        jeu._graph(input)
        st.write(f"La commune est {jeu.Commune.title()}.")
except:
    st.write("La valeur entrée ne correspond à aucun numéro de département !!")

try:
    if options=="Nom de la commune":
        code_input=jeu.geo.loc[jeu.geo["Commune"]==input.upper(), "Code Département"].to_list()[0]
        jeu._graph(code_input)
except:
    st.write("La valeur entrée ne correspond à aucune préfecture !!")

try:
    if options=="Nom du département":
        code_input=jeu.geo.loc[jeu.geo["Département"]==input.upper(), "Code Département"].to_list()[0]
        jeu._graph(code_input)
except:
    st.write("La valeur entrée ne correspond à aucun nom de département !!")