import streamlit as st
from Lancement_jeu import Jeu_Dpt

st.title("Jeu des Départements")
nb_tour = int(st.number_input('Nombre de tours :'))
st.write('...Démarrage du jeu...', value = 20, step =1)
jeu = Jeu_Dpt()
jeu.play(nb_tour=nb_tour)