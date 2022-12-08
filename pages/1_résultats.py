import streamlit as st

st.markdown(
    '<div align="center"> <h1 align="center">Affichage du résultat du quizz</h1> </div>',
    unsafe_allow_html=True
    )

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
        from Lancement_jeu import Jeu_Dpt
        jeu = Jeu_Dpt()
        Commune = jeu.get_with_code(code,"Commune")
        dep_name = jeu.get_with_code(code, "Département")
        st.markdown(
            "<div style='text-align:center'> La préfécture du {} est {} ({}).</div>".format(code, Commune.title(), dep_name.title()),
            unsafe_allow_html=True
            )
        jeu._graph(code)  
else:
    st.markdown(
        "<span style='font-size:25px;color:red;'> Veuillez finir le quizz pour afficher votre score et revoir vos erreurs.</span>",
        unsafe_allow_html=True)
