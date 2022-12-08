import random
import streamlit as st

from Lancement_jeu import Jeu_Dpt

st.markdown(
    '<div align="center"> <h1 align="center">Jeu des Départements</h1> </div>',
    unsafe_allow_html=True
    )

jeu = Jeu_Dpt()

if jeu.init_historique() is None: 
    st.markdown(":x: Erreur, vous n'avez pas de fichier historique !! :x:")
    st.stop()
st.session_state["histo"] = jeu.historique

if 'nb_tour' not in st.session_state:
    nb_tour = int(st.number_input('Nombre de tours :', value=0))
    if nb_tour != 0:
        st.session_state['nb_tour'] = nb_tour
        st.session_state['results'] = [None]*nb_tour
        st.session_state['commune_joueur'] = [None]*nb_tour
    else:
        st.stop()

st.session_state['graph']=not st.checkbox("Retirer l'affichage des graphs")

if ('random_list' not in st.session_state) & ('nb_tour' in st.session_state):
    random_list = random.sample(jeu.code_list, st.session_state['nb_tour'])
    st.session_state['random_list'] = random_list

if ('random_list' in st.session_state) & (
    'nb_tour' in st.session_state
    ) & (
        st.session_state['results'].count(None)!=0
    ):
    for tour in range(st.session_state['nb_tour']):
        if st.session_state['results'][tour] is None:
            Code = st.session_state['random_list'][tour]
            dep_name = jeu.get_with_code(Code, "Département")
            st.session_state['commune_joueur'][tour] = st.text_input(
                f"Quelle est la préfécture associée au numéro de département {Code} ({dep_name.title()}) :",
                key = tour
                )
            if st.session_state['commune_joueur'][tour] != "":
                st.session_state['results'][tour] = jeu.verification(Code, st.session_state['commune_joueur'][tour])
                if not st.session_state['results'][tour]:
                    st.markdown(f":x: ERROR : La préfécture est {jeu.Commune.title()}")
                else:
                    st.markdown(":white_check_mark: Bravo, c'est la bonne réponse.")
                if (st.session_state['results'][tour])&(st.session_state['graph']):
                    with st.spinner("Chargement de la map :"):
                        jeu.main(Code, st.session_state['commune_joueur'][tour], graph=st.session_state['graph'])
                else:
                    jeu.main(Code, st.session_state['commune_joueur'][tour], graph=st.session_state['graph'])
    st.session_state["histo"] = jeu.historique  

rerun = st.button("Relancer")
if rerun:
    for key in st.session_state.keys():
        del st.session_state[key]
    st.experimental_rerun()
