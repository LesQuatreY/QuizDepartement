import streamlit as st
import plotly.express as px

st.title("Affichage des résultats du quizz")

#Affiche du score
if "results" not in st.session_state:
    st.session_state['results'] = [None]

if st.session_state['results'].count(None)==0:
    st.write(f"Votre score est de {st.session_state['results'].count(True)}/{st.session_state['nb_tour']}.")
else:
    st.write("Veuillez finir le quizz pour afficher votre score.")

#Reprendre ses erreurs
# st.write(
#     st.session_state['random_list'][st.session_state['results']==True]
#     )#[st.session_state['results']])
# st.radio(
#     label="Choisir les départements que vous souhaitez revoir",
#     options=[st.session_state['random_list'][st.session_state['results']==True]]
#     )

st.title("Affichage des statistiques")

histo = st.session_state["histo"]

#Affichage des tops d'erreurs
st.plotly_chart(
    px.bar(
        histo.assign(Commune=lambda x: x.Commune+" ("+x.index+")").sort_values(
            ["Erreur", "Correct"], ascending=[False, True]
            ).iloc[:5,:],
        x="Commune", 
        y="Erreur",
        color_discrete_sequence=['#FF8181']*histo.shape[1],
        labels={"Erreur":"Nombre d'erreurs"},
        title="Top du nombre d'erreurs"
    )
)

#Affichage des tops bonnes réponses
st.plotly_chart(
    px.bar(
        histo.assign(Commune=lambda x: x.Commune+" ("+x.index+")").sort_values(
            ["Correct", "Erreur"], ascending=[False, True]
            ).iloc[:5,:],
        x="Commune", 
        y="Correct",
        color_discrete_sequence=['#81FFA7']*histo.shape[1],
        labels={"Correct":"Nombre de bonnes réponses"},
        title="Top du nombre de bonnes réponses"
    )
)
