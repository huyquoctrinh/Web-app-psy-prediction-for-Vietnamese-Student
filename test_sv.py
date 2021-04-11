from flask import Flask 
app = Flask(__name__)   
@app.route('/', methods=['POST'])
def main():
	return "<h1>hello world<h1>"
app.run(host="0.0.0.0", port=5000, debug=True)
