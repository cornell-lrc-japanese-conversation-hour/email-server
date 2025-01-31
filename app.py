import os, json

from flask import Flask, request, render_template, redirect, make_response
from flask_mail import Mail, Message

from dotenv import load_dotenv


load_dotenv('.env')

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ['EMAIL']
app.config['MAIL_PASSWORD'] = os.environ['EMAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route("/send", methods=["POST"])
def send_emails_for_date():
    number = request.form.get('number')
    custom_title = request.form.get('title')
    testing = request.form.get('testing')
    
    title = f'Newsletter #{number}: {custom_title}'

    try:
        recipients_file = ''
        if testing == 'True':
            recipients_file = open('jpch_data/recipients/beta.txt', 'r')
        else:
            recipients_file = open('jpch_data/recipients/all.txt', 'r')
        
        recipients = recipients_file.read().split('\n')
        recipients_file.close()
        
        msg = Message(
            title,
            sender=('和会話教室', 'pyontajch@gmail.com'),
            recipients=['pyontajch@gmail.com'],
            bcc=recipients
        )
        
        email_file = request.files['email']
        msg.html = email_file.read()
        
        mail.send(msg)
        
        print('Sent (connection can be closed)')
    except Exception as e:
        print(e)
        return make_response('File not found or unable to send', 400)
    
    return 'Success'


if __name__ == "__main__":
    app.debug = True
    app.run(port=8000)
