import smtplib
from modules.pwr import givepw, givesender
from modules.genmail import generate_mail
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# from flask import Flask
# from flask_mail import Mail, Message


def rnf_mail(email, OTP):
    message = EmailMessage()
    message['from'] = givesender()
    message['to'] = email
    message['subject'] = "MedLib OTP"
    message.set_content(
        "Hello, this is an automated message from MedLib!\n\n\t\tThe OTP is: {}.\n\nRegards,\nKin and Bells :3".format(OTP))
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(givesender(), givepw())
    s.send_message(message)
    s.quit()


def rnf_mail_alt(email, OTP):
    message = EmailMessage()
    message['from'] = givesender()
    message['to'] = email
    message['subject'] = "MedLib OTP"
    # text_part = "\n\n\
    #     Hello, this is an automated message from the Rainfall Prediction Page!\n\n\t\tThe Predicted Rainfall is: {0:.2f} mm.\n\nRegards,\nKin and Bells :3\
    #         ".format(rainfall)
    html_part = generate_mail(OTP)
    message.set_content(f'''{html_part}''',subtype='html')
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(givesender(), givepw())
    s.sendmail(givesender(), email, message.as_string())
    s.quit()


# def flask_send(email, rainfall):
#     app = Flask(__name__)
#     app.run(debug=True)
#     mail = Mail(app)
#     app.config["MAIL_DEFAULT_SENDER"] = givesender()
#     app.config["MAIL_PASSWORD"] = givepw()
#     app.config["MAIL_PORT"] = 587
#     app.config["MAIL_SERVER"] = "smtp.gmail.com"
#     app.config["MAIL_USE_TLS"] = True
#     app.config["MAIL_USERNAME"] = "Kinshuk"
#     mail = Mail(app)
#     msg = Message(
#         sender=givesender(),
#         recipients=email,
#         subject='Rainfall Prediction Result'
#     )
#     msg.body = 'Hello, this is an automated message from the Rainfall Prediction Page!\n\n\t\tThe Predicted Rainfall is: {0:.2f} mm.\n\nRegards,\nKin and Bells :3'.format(rainfall)
#     mail.send(msg)
