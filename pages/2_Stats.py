import config
import streamlit as st
import plotly.express as px

# Configuration de la page
st.set_page_config(
    page_title="Statistiques",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊",
    menu_items={
    'Get Help': 'mailto:tanguy.minot@laposte.net',
    'About': "Quizz by Tanguy Minot! 🧑‍💻"
    }
)

#Affichage d'un titre
st.title("📊 Statistiques")

# Configuration avec des styles CSS pour les différents background
st.markdown('<style>{}</style>'.format(config.secondary_pages_background), unsafe_allow_html=True)
st.markdown('<style>{}</style>'.format(config.sidebar_background), unsafe_allow_html=True)

histo = st.session_state["histo"]

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
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)", 
        paper_bgcolor="rgba(0, 0, 0, 0)",
        xaxis_title=dict(font=dict(color='black')),
        xaxis=dict(tickfont=dict(color='black'), title=dict(font=dict(color='black'))),
        yaxis=dict(tickfont=dict(color='black'), title=dict(font=dict(color='black')))
    ).update_traces(textposition='auto', textfont=dict(color='white')),
    use_container_width=True
)

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
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)", 
        paper_bgcolor="rgba(0, 0, 0, 0)",
        xaxis_title=dict(font=dict(color='black')),
        xaxis=dict(tickfont=dict(color='black'), title=dict(font=dict(color='black'))),
        yaxis=dict(tickfont=dict(color='black'), title=dict(font=dict(color='black')))
    ).update_traces(textposition='auto', textfont=dict(color='white')),
    use_container_width=True
)

#Affichage du nombre de communes considérées comme acquises
nb_acquis=((histo["Correct"]>histo["Erreur"])).sum() #&(histo["Correct"]>2) 
pct_acquis=nb_acquis/histo.shape[0]
st.markdown(
    "Nombre de communes acquises : {} ({:.0%})".format(nb_acquis, pct_acquis)
    )
