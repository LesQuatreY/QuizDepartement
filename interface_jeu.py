import random
import streamlit as st

from Lancement_jeu import Jeu_Dpt

st.title("Jeu des Départements")
jeu = Jeu_Dpt()

if 'nb_tour' not in st.session_state:
    nb_tour = int(st.number_input('Nombre de tours :', value=0))
    if nb_tour != 0:
        st.session_state['nb_tour'] = nb_tour
        st.session_state['results'] = [None]*nb_tour

if ('random_list' not in st.session_state) & ('nb_tour' in st.session_state):
    random_list = random.sample(jeu.code_list, st.session_state['nb_tour'])
    st.session_state['random_list'] = random_list

if ('random_list' in st.session_state) & (
    'nb_tour' in st.session_state
    ) & (
        'commune_joueur' not in st.session_state
    ):
    for tour in range(st.session_state['nb_tour']):
        Code = st.session_state['random_list'][tour]
        commune_joueur=st.text_input(
            f"Quelle est la préfécture associé au numéro de département {Code} : ",
            key = tour
            )
        if commune_joueur != "":
            st.session_state['commune_joueur'] = commune_joueur
            st.session_state['results'][tour] = jeu.verification(Code, st.session_state['commune_joueur'])
            jeu.main(Code, st.session_state['commune_joueur'])
            if not st.session_state['results'][tour]:
                st.write(f"ERROR : La préfécture est {jeu.Commune.lower()}")
            else:
                st.write("Bravo, c'est la bonne réponse.")


if 'commune_joueur' in st.session_state:
    del st.session_state['commune_joueur']

print_results = st.checkbox('Afficher les résultats ?')
if print_results:
    st.write(f"Votre score est de {st.session_state['results'].count(True)}/{st.session_state['nb_tour']}")

rerun = st.checkbox("Voulez vous relancer ?")
if rerun:
    for key in st.session_state.keys():
        del st.session_state[key]
