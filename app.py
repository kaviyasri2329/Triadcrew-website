from flask import Flask, render_template 
app = Flask(__name__) 
@app.route("/") 
def home():
        return render_template("home.html")

@app.route("/About")
def about():
    return render_template("Aboutus.html")

@app.route("/Contact")
def contact():
    return render_template("Contactus.html")

if __name__ == "__main__":
        app.run(debug=True)
