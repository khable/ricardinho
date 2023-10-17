from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

USERNAME = "af7f3358846937e3dc1690da6d2258a1"
PASSWORD = "1d14b7522cee9a57410cc2985a5cc035"
SMTP_HOST = "in-v3.mailjet.com"
SMTP_PORT = 587
SENDER = "nunopinto1519966@gmail.com"

def send_email(subject, body):
    # Configure the Google SMTP server

    # Create a MIMEMultipart object to construct the email
    message = MIMEMultipart()
    message['To'] = SENDER
    message['Subject'] = subject

    # Add the email body
    message.attach(MIMEText(body, 'plain'))

    try:
        # Start a secure SMTP connection with the server
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()
        # Log in with the sender's credentials
        server.login(USERNAME, PASSWORD)
        # Send the email
        server.sendmail(SENDER, SENDER, message.as_string())
        # Close the SMTP connection
        server.quit()

        return "Email sent successfully!"

    except Exception as e:
        return f"Error sending email: {str(e)}"

@app.route('/send_mail', methods=['POST'])
def send_email_api():
    data = request.get_json()
    subject = data['subject']
    body = data['body']

    result = send_email(subject, body)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
