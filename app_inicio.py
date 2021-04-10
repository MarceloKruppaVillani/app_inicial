from flask import Flask, render_template
appl = Flask(__name__)

@appl.route("/")
def inicio():
    return render_template("home.html", titulo = "Home")
    
if __name__ == '__main__':
	appl.run(host='0.0.0.0', port=8080, debug=True)
