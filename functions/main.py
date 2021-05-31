import functions.casosdeuso as cs #metodos internos
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
    if assunto=="" or destino=="":
        return "Vazio"
    else:
        srv_email = cs.DadosServidor()
        username = srv_email[0] #email registrado no servidor SMTP
        conteudo = conteudo+"\n\n\nSend by: SENDEX"
        message = MIMEMultipart()
        message['subject'] = assunto
        message['from'] = username
        message['to'] = destino
        message.attach(MIMEText(conteudo))
        if arquivo == False:
            #se existir nenhum arquivo para anexar
            mensagem = message
        else:
            qtd = arquivo.split(" ")
            #se a quantidade de arquivos for maior que 1
            if len(qtd)>1:
                try:
                    mensagem = MuitosArquivos(qtd, message)
                except:
                    return False
            #se a quantidade de arquivo for igual a 1
            else:
                try:
                    mensagem = UmArquivo(arquivo, message)
                except:
                    return False
            
        try:
            envio = EnviarEmail(None, username, destino, mensagem)
            if envio:
                return False
            else:
                return True
        except:
            return False

#Prepara envio de email com 1 arquivo em anexo
def UmArquivo(arquivo, message):
    nome = arquivo.split("/")
    arq = open(arquivo, "rb")
    anexo = mimetypes.guess_type(arquivo)[0].split("/")
    part = MIMEBase(anexo[0], anexo[1])
    part.set_payload(arq.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename= %s" % nome[len(nome)-1])
    message.attach(part)
    return message

#Prepara envio de email com muitos arquivos em anexo
def MuitosArquivos(qtd, message):
    for i in range(1, len(qtd)):
        nome = qtd[i].split("/")
        arq = open(qtd[i], "rb")
        anexo = mimetypes.guess_type(qtd[i])[0].split("/")
        part = MIMEBase(anexo[0], anexo[1])
        part.set_payload(arq.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename= %s" % nome[len(nome)-1])
        message.attach(part)
    return message

#envia a estrura do email para o gmail
def EnviarEmail(self, from_addr, to_addrs, message):
    srv_senha = cs.DadosServidor()
    smtp_ssl_host = 'smtp.gmail.com'
    password = srv_senha[1] #senha do email registrado no servidor SMTP
    smtp_ssl_port = 465
    servidor = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    servidor.login(from_addr, password)
    servidor.sendmail(from_addr, to_addrs, message.as_string())
    servidor.quit()

#Registrar logs de atividades dentro do programas
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

#Enviar logs para email registrado
def LogsEmail(self):
    srv_email = cs.DadosServidor()
    para = srv_email[0]
    assunto = 'Atenção: Solicitação de logs'
    mensagem = "O conteúdo do arquivo de logs foi solicitado. Segue abaixo o conteúdo:\n\n\n"
    logs = open("logs/logs.txt").readlines()
    for i in range(len(logs)):
        x = logs[i][2:len(logs[i])-2].encode("utf-8")
        x = base64.b85decode(x)
        mensagem = mensagem+"{}\n".format(x)
    a = False
    PrepararEmail(None, assunto, para, mensagem, a)
    return True
