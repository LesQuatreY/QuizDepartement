import streamlit as st
st.title("Affichage des résultats")

if st.session_state['results'].count(None)==0:
    print_results = st.checkbox('Afficher les résultats ?')
    if print_results:
        st.write(f"Votre score est de {st.session_state['results'].count(True)}/{st.session_state['nb_tour']}")
else:
    st.write("Veuillez finir le quizz.")