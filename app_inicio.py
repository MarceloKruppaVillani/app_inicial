from flask import Flask
appl = Flask(__name__)

@appl.route("/")
def inicio():
    return ("<h1>Hello!</h1>")
    
if __name__ == '__main__':
	appl.run(host='0.0.0.0', port=8080, debug=True)
