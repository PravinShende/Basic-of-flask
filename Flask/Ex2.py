

from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hello():
	return '<h1>Knowlege Shelf!!!! </h1>'

@app.route('/info')

def info():

	return '<h1>Pravin Shende</h1>'


if __name__ =='__main__':
	app.run()


