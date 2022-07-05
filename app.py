from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/search', methods = ["POST", "GET"])
def search():
    if request.method == "POST":
        pincode = request.form["pincode"]
        date = request.form["date"]

        url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}";
        response = requests.get(url).json();

        if response["sessions"] == []:
            error = "Sorry we have no current Covid Center near in your selected area. Please use another nearby place and try again."
            return render_template("result.html", output = error)

        else:
            return render_template("result.html", output=response, date = date)

@app.route('/guidelines')
def guidelines():
    return render_template('guideline.html');

app.route('./feedback')
def feedback():
    return render_template('feedback.html');

if __name__ == "__main__":
    app.run(debug=True, port=3000);