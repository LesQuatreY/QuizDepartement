import config
import streamlit as st

from jeu import Jeu_Dpt

# Configuration de la page
st.set_page_config(
    page_title="Entraînement",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🧠",
    menu_items={
    'Get Help': 'mailto:tanguy.minot@laposte.net',
    'About': "Quizz by Tanguy Minot! 🧑‍💻"
    }
)

#Affichage d'un titre
st.title("🧠 Entraînement")

# Configuration avec des styles CSS pour les différents background
st.markdown('<style>{}</style>'.format(config.secondary_pages_background), unsafe_allow_html=True)
st.markdown('<style>{}</style>'.format(config.sidebar_background), unsafe_allow_html=True)

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
            "<div style='text-align:center'> La préfecture est {}.</div>".format(Commune.title()),
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
