import plotly
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import plotly.express as px



#Wordcloud
def plot_wordcloud(text:str, max_words:int, list_exception:list()):
	wordcloud = WordCloud(background_color = 'white', stopwords = list_exception, max_words = max_words).generate(text)
	fig, ax = plt.subplots(figsize = (12, 8))
	ax.imshow(wordcloud, interpolation = 'bilinear')
	plt.axis('off')
	st.pyplot(fig)

def deux_wordcloud(text_1:str, text_2:str, label_1:str, label_2:str, max_words:int, list_exception:list()):
	wordcloud1 = WordCloud(background_color = 'white', stopwords = list_exception, max_words = max_words).generate(text_1)
	wordcloud2 = WordCloud(background_color = 'white', stopwords = list_exception, max_words = max_words).generate(text_1)
	fig1, ax1 = plt.subplots(figsize = (12, 8))
	fig2, ax2 = plt.subplots(figsize = (12, 8))
	ax1.imshow(wordcloud1, interpolation = 'bilinear')
	ax2.imshow(wordcloud2, interpolation = 'bilinear')
	plt.axis('off')
	fig = make_subplots(rows=rows, cols=cols, subplot_titles=(label_1, label_2))
	fig.add_trace(ax1, rows=1, cols=1)
	fig.add_trace(ax2, rows=2, cols=2)
	st.plotly_chart(fig)




# Scatter plot :
def plot_scatter(df:pd.DataFrame(), X_label:str, Y_label:str):
	fig = px.scatter(df, x = X_label, y = Y_label,)
	st.header(f"Scatter Plot {Y_label} function of {X_label}")
	st.plotly_chart(fig)

def deux_subplots_horizontal(title_1:str, title_2:str, x_1, y_1, x_2, y_2):
	fig = make_subplots(rows=rows, cols=cols, subplot_titles=(title_1, title_2))
	fig.add_trace(
			go.Scatter(
			 x=x_1, 
				 y=y_1),
			row=1, col=1
			)
	fig.add_trace(
			go.Scatter(
			 x=x_2, 
				 y=y_2),
			row=1, col=2
			)
	st.plotly_chart(fig)	
    	    			
def deux_subplots_vertical(title_1:str, title_2:str, x_1, y_1, x_2, y_2):
	fig = make_subplots(rows=rows, cols=cols, subplot_titles=(title_1, title_2))
	fig.add_trace(
			go.Scatter(
			 x=x_1, 
				 y=y_1),
			row=1, col=1
			)
	fig.add_trace(
			go.Scatter(
			 x=x_2, 
				 y=y_2),
			row=2, col=1
			)    
	st.plotly_chart(fig)

# Bar plot : 	
def plot_bar(df:pd.DataFrame(), X_label:str, Y_label:str):
	fig = px.bar(DataFrame, x=X_label, y=Y_label)		
	st.header(f"Bar Plot {Y_label} function of {X_label}")
	st.plotly_chart(fig)

