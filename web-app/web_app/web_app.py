from flask import Flask, render_template, url_for, request, redirect
from model_utils import predict
from db_utils import *
import csv

app = Flask(__name__)

#------
text_resume = ''
@app.route('/')
def test():
	return render_template("home.html")

@app.route("/home", methods=['GET', 'POST'])
def home():
	#global text_resume
	#if request.method == 'POST':
		#recuperation variables
	#	text = request.values.get('texte_a_resumer')
	#	text_resume = predict(text)
	#	print(text_resume)

		#enregistrement
		#input_var = [['commentaire'],['texte_a_resumer']]
		#with open ('/texte_a_resumer.csv','a',newline = '') as csvfile:
    	#		my_writer = csv.writer(csvfile, delimiter = ' ')
    	#		my_writer.writerows(input_var)
    			
		#renvoit
		return render_template('home.html')
	
	#else:
	#	return render_template('home.html') 
	
@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/contact",  methods=['GET', 'POST'])
def contact():
		#on enregistre dans un fichier .csv
		#input_var = [['name', 'mail', 'commentaire'],[username, usermail, usercomment]]
		#with open ('contact.csv','a',newline = '') as csvfile:
    	#		my_writer = csv.writer(csvfile, delimiter = ' ')
    	#		my_writer.writerows(input_var)
    			
    		#renvoit
		return render_template('contact.html')

@app.route("/model")
def form():
	return render_template('model.html')

@app.route("/summary", methods=['GET', 'POST'])
def summary(summary = None):
	if request.method == 'POST':
		#recuperation variables
		text = request.values.get('texte_a_resumer')
		text_resume = predict(text)
		db = DB(port='5432', log='wym_admin', password='admin', nom_DB='wym_admin')
		db.create_connection()
		db.init_bdd()
		db_func = dbs_utils()
		nb_mot_E = db_func.nb_mot(text)
		nb_mot_S = db_func.nb_mot(text_resume)
		#frq_mot_E = db_func.frq_mot(text)
		#frq_mot_S = db_func.frq_mot(text_resume)
		nb_carac_E = db_func.nb_carac(text)
		nb_carac_S = db_func.nb_carac(text_resume)
		diff_mot = db_func.dif_mot(text, text_resume)[0]
		diff_carac = db_func.dif_carac(text, text_resume)[0]
		db.recup_stats(text, text_resume, nb_mot_E, 1, nb_carac_E, nb_mot_S, 1, nb_carac_S, diff_mot, diff_carac)

		#enregistrement
		#input_var = [['commentaire'],['texte_a_resumer']]
		#with open ('/texte_a_resumer.csv','a',newline = '') as csvfile:
    	#		my_writer = csv.writer(csvfile, delimiter = ' ')
    	#		my_writer.writerows(input_var)
    			
		#renvoit
		return render_template('summary.html', text_resume = text_resume)
	
	else:
		return render_template('summary.html', text_resume = '') 
	
@app.route("/contacted", methods=['GET', 'POST'])
def contacted():
	if request.method == 'POST':
		#on recupere les variables
		username = request.values.get('user_name')
		usermail = request.values.get('user_mail')
		usercomment = request.values.get('user_message')
		
		db = DB(port='5432', log='wym_admin', password='admin', nom_DB='wym_admin')
		db.create_connection()
		db.init_bdd()
		db.recup_user(usercomment, usermail, usercomment)
		return render_template('contacted.html')
	else:
		return render_template('contacted.html')	
#------

def main():
	print('main a été executé')
	app.run(debug=True, host='0.0.0.0')

if __name__ == "__main__":
	main()
