from flask import Flask, render_template, url_for
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vahackathon'

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    form = SignUpForm()
    return render_template('home.html', title='Submit', form=form)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/menu')
def menu():
    return render_template("menu.html")

if __name__ == '__main__':
    app.run(debug=True)
