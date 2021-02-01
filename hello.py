from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
	return "<html><body><h1>Hello World</h1></body></html>" + name 

if __name__ == "__main__":
	app.run()
