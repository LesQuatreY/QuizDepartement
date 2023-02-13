import config
import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Résultats",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📝",
    menu_items={
    'Get Help': 'mailto:tanguy.minot@laposte.net',
    'About': "Quizz by Tanguy Minot! 🧑‍💻"
    }
)

#Affichage d'un titre
st.title("📝 Résultats du Quizz")

# Configuration avec des styles CSS pour les différents background
st.markdown('<style>{}</style>'.format(config.secondary_pages_background), unsafe_allow_html=True)
st.markdown('<style>{}</style>'.format(config.sidebar_background), unsafe_allow_html=True)

histo = st.session_state["histo"]

#Affiche du score
if "results" not in st.session_state:
    st.session_state['results'] = [None]

if st.session_state['results'].count(None)==0:
    color = "green" if st.session_state['results'].count(True)/st.session_state['nb_tour']>.5 else "red"
    smiley = "&#128079" if st.session_state['results'].count(True)/st.session_state['nb_tour']==1 else ""
    st.markdown(
        f"<div style='text-align:center';> <span style='font-size:50px;color:{color};'> {smiley} {st.session_state['results'].count(True)}/{st.session_state['nb_tour']} {smiley}</span></div>",
        unsafe_allow_html=True
        )
    #Reprendre ses erreurs
    code = st.radio(
        label="Quel département souhaitez-vous revoir ?", options=[None]+st.session_state['random_list'],
        horizontal=True
        )
    if code:
        from jeu import Jeu_Dpt
        jeu = Jeu_Dpt()
        Commune = jeu.get_with_code(code,"Commune")
        dep_name = jeu.get_with_code(code, "Département")
        st.markdown(
            "<div style='text-align:center'> La préfécture du {} est {} ({}).</div>".format(code, Commune.title(), dep_name.title()),
            unsafe_allow_html=True
            )
        jeu._graph(code)  
else:
    st.info("Veuillez finir le quizz pour afficher votre score et revoir vos erreurs.")
