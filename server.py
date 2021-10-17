from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return '<h1>Hello world</h1>'

@app.route('/hello')
def hello_you():
	return '<h2> This is the Second Page </h2>'
if __name__ == '__main__':	
	app.run(host="0.0.0.0", debug=True)
