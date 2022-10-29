import random
import streamlit as st

from Lancement_jeu import Jeu_Dpt

st.title("Jeu des Départements")

if 'nb_tour' not in st.session_state:
    nb_tour = int(st.number_input('Nombre de tours :', value=0))
    if nb_tour != 0:
        st.session_state['nb_tour'] = nb_tour

if ('random_list' not in st.session_state) & ('nb_tour' in st.session_state):
    jeu = Jeu_Dpt()
    random_list = [random.choice(jeu.code_list) for i in range(st.session_state['nb_tour'])]
    st.session_state['random_list'] = random_list

if ('random_list' in st.session_state) & (
    'nb_tour' in st.session_state
    ) & (
        'commune_joueur' not in st.session_state
    ):
    for tour in range(st.session_state['nb_tour']):
        jeu = Jeu_Dpt()
        Code = st.session_state['random_list'][tour]
        commune_joueur=st.text_input(
            f"Quelle est la préfécture associé au numéro de département {Code} : "
            )
        if commune_joueur != "":
            st.session_state['commune_joueur'] = commune_joueur
            jeu.main(Code, st.session_state['commune_joueur'])

if 'commune_joueur' in st.session_state:
    del st.session_state['commune_joueur']

rerun = st.checkbox("Voulez vous relancer ?")
if rerun:
    for key in st.session_state.keys():
        del st.session_state[key]
    st.write(st.session_state)
    #raise RerunException

####################
st.stop()
st.title("Jeu des Départements")
nb_tour = int(st.number_input('Nombre de tours :', value = 0))
if nb_tour==0: st.stop()
st.write('...Démarrage du jeu...', value = 20, step =1)

tour = 0
while tour < nb_tour:
    jeu = Jeu_Dpt()
    Code = random.choice(jeu.code_list)
    commune_joueur=st.text_input(
        f"Quelle est la préfécture associé au numéro de département {Code} : "
        )
    if commune_joueur!="":
        tour = tour +1
        jeu.main(Code, commune_joueur)
    else:
        st.stop()
