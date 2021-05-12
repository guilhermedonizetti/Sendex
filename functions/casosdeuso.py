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

def enviarAlteracao(self, email, senha, registro):
    print("{} | {} | {}".format(email, senha, registro))
    dados = CifrarDados(email, senha, registro)
    base = open("dados.txt","w")
    base.write("{} {} {}".format(dados[0], dados[1], dados[2]))
    base.close()

def CifrarDados(email, senha, registro):
    dados = [email, senha, registro]
    cript_dados = []
    caracter = [
            'A','B','&','D','E','Ô','F','G','H','I','J','K','L',
            'N','f','g','h','í','O','P','Q','W','X','Y','Z','6',
            ' ','a','b','c','d','e','+','i','j','k','l','8','9',
            'm','n','o','p','q','r','s','t','u','v','w','x','y',
            'z','1','2','Ç','3','4','5','R','S','T','U','V','\n',
            '?','!',':','$','-','/','*','%','(',')','Ã','Â','À',
            'Á','É','Ê','Í','M','Ó','Õ','Ú','á','â','à','ã','é',
            'ê','ó','õ','ô','0','.','ç',',','ú','@','7','#','C'
        ]
    for i in range(3):
        texto = dados[i]
        if len(texto)<10:
            chave = 16
        if len(texto)>=10 and len(texto)<=29:
            chave = 24
        else:
            chave = 42
        nvtexto = "" 
        for i in range(len(texto)):
            # x recebe o indice da lista de caracteres onde esta o elemento atual + o tamanho da chave
            x = caracter.index(texto[i])+chave
            y = len(caracter)-x
            if y>0:
                nvtexto = nvtexto + caracter[x]
            else:
                nvtexto = nvtexto + caracter[-(y)]
        cript_dados.append(nvtexto)
            
    return cript_dados