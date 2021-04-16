import smtplib
import base64
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from datetime import datetime as dt
from email import encoders
    
    #faz a estrutura do email
def PrepararEmail(self, assunto, destino, conteudo, arquivo):
    username = 'datacenteracompanhamento@gmail.com'
    conteudo = conteudo+"\n\n\nSend by: SENDEX"
    message = MIMEMultipart()
    message['subject'] = assunto
    message['from'] = username
    message['to'] = destino
    message.attach(MIMEText(conteudo))
    qtd = arquivo.split(" ")
    if len(qtd)>1:
        for i in range(1, len(qtd)):
            nome = qtd[i].split("/")
            arq = open(qtd[i], "rb")
            anexo = mimetypes.guess_type(qtd[i])[0].split("/")
            part = MIMEBase(anexo[0], anexo[1])
            part.set_payload(arq.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", "attachment; filename= %s" % nome[len(nome)-1])
            message.attach(part)
    else:
        nome = arquivo.split("/")
        arq = open(arquivo, "rb")
        anexo = mimetypes.guess_type(arquivo)[0].split("/")
        part = MIMEBase(anexo[0], anexo[1])
        part.set_payload(arq.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename= %s" % nome[len(nome)-1])
        message.attach(part)

    if assunto=="" or destino=="" or conteudo=="":
        return "Vazio"
    else:
        envio = EnviarEmail(None, username, destino, message)
        if envio:
            return True
        else:
            return envio
    
    #envia a estrura do email para o gmail
def EnviarEmail(self, from_addr, to_addrs, message):
    smtp_ssl_host = 'smtp.gmail.com'
    password = 'vidagolplano21'
    smtp_ssl_port = 465
    servidor = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    servidor.login(from_addr, password)
    servidor.sendmail(from_addr, to_addrs, message.as_string())
    servidor.quit()

def Logs(self, metodo):
    hora = dt.now()
    with open("logs/logs.txt", "a") as log:
        if metodo==0:
            l = "-> Programa iniciado - [{}]".format(hora)
            log.write("%s\n" % base64.b85encode(l.encode("utf-8")))
            log.close()
        if metodo==10:
            l = "-> Tentativa falida de envio de e-mail. - [{}]".format(hora)
            log.write("%s\n" % base64.b85encode(l.encode("utf-8")))
            log.close()
        if metodo==11:
            l = "-> E-mail enviado com sucesso. - [{}]".format(hora)
            log.write("%s\n" % base64.b85encode(l.encode("utf-8")))
            log.close()
        if metodo==2:
            l = "-> Solicitado/Envio de log para e-mail registrado. - [{}]".format(hora)
            log.write("%s\n" % base64.b85encode(l.encode("utf-8")))
            log.close()

#parei aqui
def LogsEmail(self):
    para = 'datacenteracompanhamento@gmail.com'
    assunto = 'Atenção: Solicitação de logs'
    mensagem = "O conteúdo do arquivo de logs foi solicitado. Segue abaixo o conteúdo:\n\n\n"
    logs = open("logs/logs.txt").readlines()
    for i in range(len(logs)):
        x = logs[i][2:len(logs[i])-2].encode("utf-8")
        x = base64.b85decode(x)
        mensagem = mensagem+"{}\n".format(x)
    PrepararEmail(self, assunto, para, mensagem)
