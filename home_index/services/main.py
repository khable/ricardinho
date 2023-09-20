from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

def enviar_email(sender_email, sender_password, destinatario_email, assunto, corpo):
    # Configurar o servidor SMTP do Google
    servidor_smtp = "smtp.gmail.com"
    porta_smtp = 587

    # Criar objeto MIMEMultipart para construir o e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = sender_email
    mensagem['To'] = destinatario_email
    mensagem['Subject'] = assunto

    # Adicionar o corpo do e-mail
    mensagem.attach(MIMEText(corpo, 'plain'))

    try:
        # Iniciar uma conexão SMTP segura com o servidor
        servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
        servidor.starttls()

        # Efetuar login com as credenciais do remetente
        servidor.login(sender_email, sender_password)

        # Enviar o e-mail
        servidor.sendmail(sender_email, destinatario_email, mensagem.as_string())

        # Fechar a conexão SMTP
        servidor.quit()

        return "E-mail enviado com sucesso!"

    except Exception as e:
        return f"Erro ao enviar o e-mail: {str(e)}"

@app.route('/enviar_email', methods=['POST'])
def enviar_email_api():
    data = request.get_json()

    sender_email = data['sender_email']
    sender_password = data['sender_password']
    destinatario_email = data['destinatario_email']
    assunto = data['assunto']
    corpo = data['corpo']

    resultado = enviar_email(sender_email, sender_password, destinatario_email, assunto, corpo)

    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)
