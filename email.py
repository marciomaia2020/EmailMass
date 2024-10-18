import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_emails_em_massa(remetente, senha, lista_destinatarios, assunto, mensagem):
    # Conexão com o servidor SMTP
    servidor = smtplib.SMTP('smtp.gmail.com', 587)  # Para Gmail
    servidor.starttls()
    
    try:
        servidor.login(remetente, senha)
        print("Login realizado com sucesso!")

        for destinatario in lista_destinatarios:
            msg = MIMEMultipart()
            msg['From'] = remetente
            msg['To'] = destinatario
            msg['Subject'] = assunto

            # Corpo do e-mail
            msg.attach(MIMEText(mensagem, 'plain'))

            # Enviando o e-mail
            servidor.sendmail(remetente, destinatario, msg.as_string())
            print(f"E-mail enviado para {destinatario}")

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        servidor.quit()

# Exemplo de uso
remetente = "seu_email@gmail.com"
senha = "sua_senha"
lista_destinatarios = ["email1@exemplo.com", "email2@exemplo.com"]
assunto = "Promoção Especial"
mensagem = "Olá! Não perca nossa promoção válida até o final do mês."

enviar_emails_em_massa(remetente, senha, lista_destinatarios, assunto, mensagem)
