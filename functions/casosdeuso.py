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

#Metodo para alterar os dados de acesso ao programa
def enviarAlteracao(self, email, senha, registro, emailnv, senhanv, registronv):
    dados = DecifrarDados(email, senha, registro)
    if dados=="Diferente":
        return dados
    else:
        dadosnv = CifrarDados(emailnv, senhanv, registronv)
        base = open("functions/dados.txt","w")
        base.write("{} {} {}".format(dadosnv[0], dadosnv[1], dadosnv[2]))
        base.close()
        return True

#metodo para cifrar dados com a cifra de Cesar
def CifrarDados(emailnv, senhanv, registronv):
    dados = [emailnv, senhanv, registronv]
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
    chave = 32
    for i in range(3):
        texto = dados[i]
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

#metodo para decifrar dados com a cifra de Cesar
def DecifrarDados(email, senha, registro):
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
    dados = [email, senha, registro] # dados informado pelo user para comparar c/ o atual
    conteudo = open("functions/dados.txt").read()
    dados_at = conteudo.split(" ") #recebe os dados atuais
    dados_dec = [] #recebe os dados
    dados_iguais = 0 #status da comparacao entre os dados informados e registrados
    nvtexto = ""
    chave = 32
    for i in range(3):
        texto = dados_at[i]
        for g in range(len(texto)):
            # x recebe o indice da lista de caracteres onde esta o elemento atual + o tamanho da chave
            x = caracter.index(texto[g])-chave
            if x>=0:
                nvtexto = nvtexto + caracter[x]
            else:
                nvtexto = nvtexto + caracter[len(caracter)+x]
        dados_dec.append(nvtexto)
        if nvtexto==dados[i]:
            dados_iguais = dados_iguais+1
        nvtexto=""
    if dados_iguais==3:
        return dados_dec
    else:
        return "Diferente"

#Buscar dados para servidor SMTP
def DadosServidor():
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
    conteudo = open("functions/dados.txt").read()
    dados_at = conteudo.split(" ") #recebe os dados atuais
    dados_dec = [] #recebe os dados
    nvtexto = ""
    chave = 32
    for i in range(3):
        texto = dados_at[i]
        for g in range(len(texto)):
            # x recebe o indice da lista de caracteres onde esta o elemento atual + o tamanho da chave
            x = caracter.index(texto[g])-chave
            if x>=0:
                nvtexto = nvtexto + caracter[x]
            else:
                nvtexto = nvtexto + caracter[len(caracter)+x]
        dados_dec.append(nvtexto)
        nvtexto=""
    return dados_dec #retorna os dados decifrados para tentar login