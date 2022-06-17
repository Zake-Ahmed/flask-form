from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateField,IntegerField,SelectField
import random

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    DoB = DateField('DOB')
    fNum = IntegerField('favourite number')
    fFood = SelectField('favourite food', choices=['pizza', 'spaghetti', 'chilli'])

    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        DoB = form.DoB.data
        fNum = form.fNum.data
        fFood= form.fFood.data

        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {fFood[random.randint(0,len(fFood)-2):-1]}{fFood[random.randint(0,len(fFood)-4):-1]}{fNum}{str(DoB.year)[random.randint(0,3)]}'

    return render_template('home.html', form=form, message=message)


if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')