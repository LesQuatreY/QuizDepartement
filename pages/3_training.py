import streamlit as st

from Lancement_jeu import Jeu_Dpt

st.markdown(
    '<div align="center"> <h1 align="center">Entraînement</h1> </div>',
    unsafe_allow_html=True
    )

jeu = Jeu_Dpt()

options = st.selectbox(
    label="Comment souhaitez-vous définir le département ?",
    options=["Numéro de département", "Nom de la commune", "Nom du département"],
    index=0)
input = st.text_input("")
if not input: st.stop()
    
try:
    if options=="Numéro de département":
        Commune = jeu.geo.loc[jeu.geo["Code Département"]==input,"Commune"].to_list()[0]
        st.markdown(
            "<div style='text-align:center'> La commune est {}.</div>".format(Commune.title()),
            unsafe_allow_html=True
            )
        jeu._graph(input)
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