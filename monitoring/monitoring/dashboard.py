import streamlit as st
import pandas as pd
import numpy as np
from dbStats_utils import *

st.title('WYM.inc app')

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Quels données voulez vous visualiser?',
    ('Nombre de mots en entrée', 'Fréquence des mots en entrée', 'Nombre de caractères en entrée', 'Nombre de mots en sortie', 'Fréquence des mots en sortie', 'Nombre de caractères en sortie', 'Différence de mots entre entée et sortie', 'Différence de caractères entre entrée et sortie')
)

db = DB_stats(port='5431', log='wym_admin', password='admin', nom_DB='wym_admin')
db.create_connection()
session = db.init_bdd()

if (add_selectbox == 'Nombre de mots en entrée'):
	st.subheader(session.query(Stats.id_stat).count()+1)
elif (add_selectbox == 'Fréquence des mots en entrée'):
	st.subheader(add_selectbox)
elif (add_selectbox == 'Nombre de caractères en entrée'):
	st.subheader(add_selectbox)
elif (add_selectbox == 'Nombre de mots en sortie'):
	st.subheader(add_selectbox)
elif (add_selectbox == 'Fréquence des mots en sortie'):
	st.subheader(add_selectbox)
elif (add_selectbox == 'Nombre de caractères en sortie'):
	st.subheader(add_selectbox)
elif (add_selectbox == 'Différence de mots entre entée et sortie'):
	st.subheader(add_selectbox)
else:
	st.subheader(add_selectbox)
