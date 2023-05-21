from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
import cred

app = Flask(__name__)
app.secret_key = cred.SECRET_KEY

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = cred.EMAIL
app.config['MAIL_PASSWORD'] = cred.PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = cred.EMAIL
mail = Mail(app)

@app.route('/')
def index():
    flash('send message')
    return render_template('index.html')

@app.route('/send', methods=['GET','POST'])
def send():
    try:
        email = request.form['email']
        message = request.form['message']
        msg = Message('Happy Halloween',
                    sender=cred.EMAIL,
                    recipients=[email])
        msg.body = message
        mail.send(msg)
        flash('message sent!')
    except Exception as e:
        print('ERROR\n', e)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)