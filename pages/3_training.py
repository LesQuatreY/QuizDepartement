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
        Commune = jeu.get_with_code(input, "Commune")
        st.markdown(
            "<div style='text-align:center'> La commune est {}.</div>".format(Commune.title()),
            unsafe_allow_html=True
            )
        jeu._graph(input)
except:
    st.markdown(":x: La valeur entrée ne correspond à aucun numéro de département !! :x:")

try:
    if options=="Nom de la commune":
        code_input=jeu.get_with_commune(input.upper(), "Code Département")
        jeu._graph(code_input)
except:
    st.markdown(":x: La valeur entrée ne correspond à aucune préfecture !! :x:")

try:
    if options=="Nom du département":
        code_input=jeu.get_with_departement(input.upper(), "Code Département")
        jeu._graph(code_input)
except:
    st.markdown(":x: La valeur entrée ne correspond à aucun nom de département !! :x:")
