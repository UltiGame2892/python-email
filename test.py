from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='your_gmail@gmail.com',
    MAIL_PASSWORD='your_app_password'
)

mail = Mail(app)

@app.route('/send-email')
def send_email():
    msg = Message('Hello from Flask', sender='spoofed@whatever.com', recipients=['tec2themax@gmail.com'])
    msg.body = "This is a test email from Flask."
    mail.send(msg)
    return "Email sent!"

if __name__ == '__main__':
    app.run(debug=True)

