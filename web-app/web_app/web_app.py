from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

#------

@app.route('/')
def test():
	return render_template("home.html")

@app.route("/home", methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		#recuperation variables
		text = request.values.get('texte_a_resumer')
		
		#enregistrement
		input_var = [['commentaire'],[texte_a_resumer]]
		with open ('/texte_a_resumer.csv','a',newline = '') as csvfile:
    			my_writer = csv.writer(csvfile, delimiter = ' ')
    			my_writer.writerows(input_var)
    			
		#renvoit
		return render_template('home.html')
	
	else:
		return render_template('home.html') 
	
@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/contact",  methods=['GET', 'POST'])
def contact():
	if request.method == 'POST':
		#on recupere les variables
		username = request.values.get('user_name')
		usermail = request.values.get('user_mail')
		usercomment = request.values.get('user_message')
		
		#on enregistre dans un fichier .csv
		input_var = [['name', 'mail', 'commentaire'],[username, usermail, usercomment]]
		with open ('contact.csv','a',newline = '') as csvfile:
    			my_writer = csv.writer(csvfile, delimiter = ' ')
    			my_writer.writerows(input_var)
    			
    		#renvoit
		return render_template('contact.html')
	else:
		return render_template('contact.html')	

@app.route("/model")
def form():
	return render_template('model.html')


#------

def main():
	print('main a été executé')
	app.run(debug=True, host='0.0.0.0')

if __name__ == "__main__":
	main()
