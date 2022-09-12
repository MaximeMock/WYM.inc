from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)



@app.route('/')
def test():
	return "<p>Bienvenue chez moi</p>"





#print('hey') 
app.run(debug=True, host='0.0.0.0')

def main():
	print('main a été executé')
	app.run(debug=True, host='0.0.0.0')
		
if __name__ == "__main__":
	main()
