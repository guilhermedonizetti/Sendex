from tkinter.filedialog import askopenfiles

#FUNCAO PARA SELECIONAR ARQUIVOS PARA ANEXO EM E-MAIL
def SelecionarArquivo(self):
    x = []
    conteudo = []
    arq = askopenfiles()
    if arq:
        print("%s\n" % str(arq))
        qtd = str(arq).split(",")
        print("{}\n".format(qtd))
        if len(qtd)==1:
            nome = str(arq).split("'")
            conteudo.append(nome[1])
            nome = nome[1].split("/")
            nome = nome[len(nome)-1]
            conteudo.append(nome)
            print(conteudo)
            return conteudo
        else:
            cont = ""
            path = ""
            for i in range(len(qtd)):
                nome = qtd[i].split("'")
                path = path+" %s" % nome[1]
                nome = nome[1].split("/")
                nome = nome[len(nome)-1]
                cont = cont+" %s" % nome
            conteudo.append(path)
            conteudo.append(cont)
            print(conteudo)

            return conteudo