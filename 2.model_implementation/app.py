from flask import Flask, render_template,flash,request
from numpy import dtype
from wtforms import StringField, PasswordField,BooleanField,IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length 
import os
from flask_bootstrap import Bootstrap
import pickle


from flask import Flask
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY']=SECRET_KEY
bootstrap = Bootstrap(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    pkl_file = "model.pkl"  
    if request.method == "POST":
       # getting input with name = fname in HTML form
       language = [request.form.get("fname")]

       with open(pkl_file, 'rb') as file:  
        pickle_model = pickle.load(file)
        predictions = pickle_model.predict(language)

        result = str(predictions[0])

        if result == 'afr':
            result = 'Afrikaans'

        if result =="eng":
            result = 'English'

        if result == 'zul':
            result = 'Zulu'

        if result == "tsn":
            result = 'Tsonga'  

        if result == "sot":
            result = 'Sotho'

        if result == "ven":
            result = 'Venda'

        if result == "nso":
            result = 'Sotho'
        
        flash(f'Identified language is {result}')
       #return "Your name is " + result
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)