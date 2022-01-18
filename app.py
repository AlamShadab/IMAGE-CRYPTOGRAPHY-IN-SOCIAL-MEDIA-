from flask.app import Flask
from flask.templating import render_template
from start_process import start_process


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")





if __name__ == '__main__':
    app.run(debug=True)
    #start_process()
        
        