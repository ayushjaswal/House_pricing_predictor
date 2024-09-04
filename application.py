import pickle
from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

#importing ridge and standard scaler
lasso = pickle.load(open("model/lasso.pkl", 'rb'))
linreg = pickle.load(open("model/linreg.pkl", 'rb'))
scaler = pickle.load(open("model/scaler.pkl", 'rb'))
application = Flask(__name__)
app = application


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        area = float(request.form.get("area"))
        bedrooms = float(request.form.get("bedrooms"))
        bathrooms = float(request.form.get("bathrooms"))
        stories = float(request.form.get("stories"))
        mainroad = 1 if request.form.get("mainroad").lower() == "yes" else 0
        guestroom = 1 if request.form.get("guestroom").lower() == "yes" else 0
        basement = 1 if request.form.get("basement").lower() == "yes" else 0
        hotwaterheating = 1 if request.form.get("hotwaterheating").lower() == "yes" else 0
        airconditioning = 1 if request.form.get("airconditioning").lower() == "yes" else 0
        parking = 1 if request.form.get("parking").lower() == "yes" else 0
        prefarea = 1 if request.form.get("prefarea").lower() == "yes" else 0
        furnishingstatus = request.form.get("furnishingstatus")
        furnished = 0
        semi_furnished = 0
        unfurnished = 0
        if furnishingstatus == "furnished":
            furnished = 1
        elif furnishingstatus == "semi-furnished":
            semi_furnished = 1
        elif furnishingstatus == "unfurnished":
            unfurnished = 1
        data = [[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnished, semi_furnished, unfurnished]]
        print(data)
        data = scaler.transform(data)
        result = linreg.predict(data)

        return render_template('predict.html', result=int(result[0]))
    else:
        return render_template("predict.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
