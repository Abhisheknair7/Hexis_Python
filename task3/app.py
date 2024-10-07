from flask import Flask , render_template , request , redirect , url_for
import requests 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dog")
def dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    dog = response.json()["message"]
    
    return render_template("dog.html" , dog = dog)

@app.route("/cat")
def cat():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    cat = response.json()[0]["url"]
    return render_template("dog.html", dog = cat)

@app.route("/pincode" , methods = ["GET","POST"] )
def pincode():
    if request.method == "POST":
        pincode = request.form.get("pin")
        return redirect(url_for("results" ,pincode =pincode))
    return render_template("pin.html")
    
@app.route("/results")
def results():
    pincode = request.args.get("pincode")
    response = requests.get(f"https://api.postalpincode.in/pincode/{pincode}")
    address = response.json()
    address = address[0]["PostOffice"][0]["Name"]
    return render_template("results.html" , address = address)

if __name__ == '__main__':
    app.run(debug=True)