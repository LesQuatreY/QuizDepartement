import streamlit as st
import plotly.express as px

st.title("Affichage des résultats du quizz")

histo = st.session_state["histo"]

#Affiche du score
if "results" not in st.session_state:
    st.session_state['results'] = [None]

if st.session_state['results'].count(None)==0:
    st.write(f"Votre score est de {st.session_state['results'].count(True)}/{st.session_state['nb_tour']}.")
    #Reprendre ses erreurs
    code = st.radio(
        label="Quel département voulez-vous revoir ?", options=[None]+st.session_state['random_list'],
        horizontal = True
        )
    if code:
        from Lancement_jeu import Jeu_Dpt
        jeu = Jeu_Dpt()
        jeu._graph(code)  
else:
    st.write("Veuillez finir le quizz pour afficher votre score et revoir vos erreurs.")
 