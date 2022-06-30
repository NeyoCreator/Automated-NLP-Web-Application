from flask import Flask, render_template,flash
from wtforms import StringField, PasswordField,BooleanField,IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length 
import os
from flask_bootstrap import Bootstrap


from flask import Flask
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY']=SECRET_KEY
bootstrap = Bootstrap(app)

class InputForm(FlaskForm):
    username = StringField('username',validators = [InputRequired(), Length(min=4, max=15 )])


@app.route("/")
def home():
    form = InputForm()
    flash(f" ZA tokens has been sent to")
    return render_template('index.html',form = form)

if __name__ == '__main__':
    app.run(debug=True)