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
       first_name = [request.form.get("fname")]

       with open(pkl_file, 'rb') as file:  
        pickle_model = pickle.load(file)
        predictions = pickle_model.predict(first_name)

       return "Your name is " + str(predictions)
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)