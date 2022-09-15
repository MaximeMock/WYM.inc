import streamlit as st
import pandas as pd
import numpy as np
from dbStats_utils import *
from utils import *

st.title('WYM.inc app')

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Quels données voulez vous visualiser?',
    ('Etat des données', 'Nombre de mots en entrée', 'Fréquence des mots en entrée', 'Nombre de caractères en entrée', 'Nombre de mots en sortie', 'Fréquence des mots en sortie', 'Nombre de caractères en sortie', 'Différence de mots entre entée et sortie', 'Différence de caractères entre entrée et sortie')
)

db = DB_stats(port='5430', log='wym_admin', password='admin', nom_DB='wym_admin')
engine = db.create_connection()
session = db.init_bdd()


# Import data:
data = engine.execute("SELECT * from statistics").fetchall()
#Creation dataFrame
df_data = pd.read_sql("SELECT * from statistics", engine)
# Afficher le DF : 




#SelectBox:
if (add_selectbox == 'Etat des données'):
	st.dataframe(df_data)
elif (add_selectbox == 'Nombre de mots en entrée'):
	df2 = df_data.loc[:,['id_stat','nb_mot_E']]
	plot_scatter(df2, 'nb_mot_E', 'id_stat')

	
elif (add_selectbox == 'Fréquence des mots en entrée'):
	length = len(df_data)-1
	text = df_data.loc[length, 'text_input']
	plot_wordcloud(text, max_words=20, list_exception=[])
elif (add_selectbox == 'Nombre de caractères en entrée'):
	df2 = df_data.loc[:,['id_stat','nb_carac_E']]
	plot_scatter(df2, 'nb_carac_E', 'id_stat')
elif (add_selectbox == 'Nombre de mots en sortie'):
	df2 = df_data.loc[:,['id_stat','nb_mot_S']]
	plot_scatter(df2, 'nb_mot_S', 'id_stat')
elif (add_selectbox == 'Fréquence des mots en sortie'):
	length = len(df_data)-1
	text = df_data.loc[length, 'text_output']
	plot_wordcloud(text, max_words=20, list_exception=[])
	
elif (add_selectbox == 'Nombre de caractères en sortie'):
	df2 = df_data.loc[:,['id_stat','nb_carac_S']]
	plot_scatter(df2, 'nb_carac_S', 'id_stat')
elif (add_selectbox == 'Différence de mots entre entée et sortie'):
	st.subheader(add_selectbox)
else:
	st.subheader(add_selectbox)
