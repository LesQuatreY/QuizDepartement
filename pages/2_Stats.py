import streamlit as st
import plotly.express as px

st.markdown(
    '<div align="center"> <h1 align="center">Affichage des statistiques</h1> </div>',
    unsafe_allow_html=True
    )

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

#Affichage du nombre de communes considérées comme acquises
nb_acquis=((histo["Correct"]>histo["Erreur"])).sum() #&(histo["Correct"]>2) 
pct_acquis=nb_acquis/histo.shape[0]
st.markdown(
    "Nombre de communes acquises : {} ({:.0%})".format(nb_acquis, pct_acquis)
    )
