from tkinter.filedialog import askopenfiles

#FUNCAO PARA SELECIONAR ARQUIVOS PARA ANEXO EM E-MAIL
def SelecionarArquivo(self):
    x = []
    conteudo = []
    arq = askopenfiles()
    if arq:
        qtd = str(arq).split(",")
        if len(qtd)==1:
            nome = str(arq).split("'")
            conteudo.append(nome[1])
            nome = nome[1].split("/")
            nome = nome[len(nome)-1]
            conteudo.append(nome)
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

            return conteudo

#Alterar os dados de acesso ao programa
def enviarAlteracao(self, email, senha, registro, emailnv, senhanv, registronv):
    dados = DecifrarDados(email, senha, registro)
    if dados=="Diferente":
        return dados
    else:
        dadosnv = CifrarDados(emailnv, senhanv, registronv)
        #Atualizar
        base = open("functions/dados.txt","w")
        base.write("{} {} {}".format(dadosnv[0], dadosnv[1], dadosnv[2]))
        base.close()
        return True

#Cifrar dados com a cifra de Cesar
def CifrarDados(emailnv, senhanv, registronv):
    dados = [emailnv, senhanv, registronv]
    chave = [2, 0, 3, 1, 4]
    cript_dados = []
    caracter = [
        'A','B','C','D','E','Ô','F','G','H','I','J','K','L',
        'N','f','g','h','í','O','P','Q','W','X','Y','Z','6',
        'a','b','c','d','e','+','i','j','k','l','8','9','@',
        'm','n','o','p','q','r','s','t','u','v','w','x','y',
        'z','1','2','Ç','3','4','5','R','S','T','U','V','7',
        '?','!',':','$','-','/','*','%','(',')','Ã','Â','À',
        'Á','É','Ê','Í','M','Ó','Õ','Ú','á','â','à','ã','é',
        'ê','ó','õ','ô','0','.','ç',',','ú'
    ]
    #separa em fragmentos de até 4 carcteres (exc: o primeiro sera 5)
    for texto in dados:
        fragmentos = []
        permuta = []
        n_texto = ""
        x = []
        for i in range(len(texto)):
            if i%4!=0.0 or i==0:
                x.append(texto[i])
            else:
                x.append(texto[i])
                fragmentos.append(x)
                x = []
        fragmentos.append(x)
        #faz a permuta
        for i in fragmentos:
            if len(i)<4:
                for c in i:
                    permuta.append(c)
            else:
                for g in range(len(i)):
                    try:
                        permuta.append(i[chave[g]])
                    except:
                        permuta.append(i[g])
        #embaralha os carcateres
        for i in permuta:
            # x recebe o indice da lista de caracteres onde esta o elemento atual + o tamanho da chave
            x = caracter.index(i)+len(permuta)
            y = len(caracter)-x
            if y>0:
                n_texto = n_texto + caracter[x]
            else:
                n_texto = n_texto + caracter[-(y)]
        cript_dados.append(n_texto)
    return cript_dados

#Decifrar dados com a cifra de Cesar
def DecifrarDados(email, senha, registro):
    chave = [2, 0, 3, 1, 4]
    dados = [email, senha, registro] # dados informado pelo user para comparar c/ o atual
    conteudo = open("functions/dados.txt").read()
    dados_at = conteudo.split(" ") #recebe os dados atuais
    dados_dec = [] #recebe os dados
    dados_iguais = 0 #status da comparacao entre os dados informados e registrados
    caracter = [
        'A','B','C','D','E','Ô','F','G','H','I','J','K','L',
        'N','f','g','h','í','O','P','Q','W','X','Y','Z','6',
        'a','b','c','d','e','+','i','j','k','l','8','9','@',
        'm','n','o','p','q','r','s','t','u','v','w','x','y',
        'z','1','2','Ç','3','4','5','R','S','T','U','V','7',
        '?','!',':','$','-','/','*','%','(',')','Ã','Â','À',
        'Á','É','Ê','Í','M','Ó','Õ','Ú','á','â','à','ã','é',
        'ê','ó','õ','ô','0','.','ç',',','ú'
    ]
    for texto in dados_at:
        reverter = n_texto = ""
        x = []
        revert = []
        letras = []
        permuta = []
        fragmentos = []
        for i in range(len(texto)):
            # x recebe o indice da lista de caracteres onde esta o elemento atual + o tamanho da chave
            x = caracter.index(texto[i])-len(texto)
            if x>=0:
                n_texto = n_texto + caracter[x]
            else:
                n_texto = n_texto + caracter[len(caracter)+x]

        #separa em fragmentos de ate 4 caracteres (exc: o primeiro sera 5)
        for i in range(len(n_texto)):
            if i%4!=0.0 or i==0:
                letras.append(n_texto[i])
            else:
                letras.append(n_texto[i])
                fragmentos.append(letras)
                letras = []
        fragmentos.append(letras)
        #desfazer a permutacao
        for i in fragmentos:
            if len(i)<4:
                for c in i:
                    reverter = reverter+c
            else:
                for g in range(len(i)):
                    try:
                        reverter = reverter+i[chave.index(g)]
                    except:
                        reverter = reverter+i[g]
            permuta.append(reverter)
            reverter = ""
        for i in permuta:
            reverter = reverter+i
        dados_dec.append(reverter)
    if dados==dados_dec:
        return dados_dec
    else:
        return "Diferente"

#Buscar dados para servidor SMTP
def DadosServidor():
    chave = [2, 0, 3, 1, 4]
    conteudo = open("functions/dados.txt").read()
    dados_at = conteudo.split(" ") #recebe os dados atuais
    dados_dec = [] #recebe os dados
    dados_iguais = 0 #status da comparacao entre os dados informados e registrados
    caracter = [
        'A','B','C','D','E','Ô','F','G','H','I','J','K','L',
        'N','f','g','h','í','O','P','Q','W','X','Y','Z','6',
        'a','b','c','d','e','+','i','j','k','l','8','9','@',
        'm','n','o','p','q','r','s','t','u','v','w','x','y',
        'z','1','2','Ç','3','4','5','R','S','T','U','V','7',
        '?','!',':','$','-','/','*','%','(',')','Ã','Â','À',
        'Á','É','Ê','Í','M','Ó','Õ','Ú','á','â','à','ã','é',
        'ê','ó','õ','ô','0','.','ç',',','ú'
    ]
    for texto in dados_at:
        reverter = ""
        n_texto = ""
        x = []
        revert = []
        letras = []
        permuta = []
        fragmentos = []
        #decifrar para reverter a permuta
        for i in range(len(texto)):
            # x recebe o indice da lista de caracteres onde esta o elemento atual + o tamanho da chave
            x = caracter.index(texto[i])-len(texto)
            if x>=0:
                n_texto = n_texto + caracter[x]
            else:
                n_texto = n_texto + caracter[len(caracter)+x]

        #separa em fragmentos de ate 4 caracteres (exc: o primeiro sera 5)
        for i in range(len(n_texto)):
            if i%4!=0.0 or i==0:
                letras.append(n_texto[i])
            else:
                letras.append(n_texto[i])
                fragmentos.append(letras)
                letras = []
        fragmentos.append(letras)
        #desfazer a permutacao
        for i in fragmentos:
            if len(i)<4:
                for c in i:
                    reverter = reverter+c
            else:
                for g in range(len(i)):
                    try:
                        reverter = reverter+i[chave.index(g)]
                    except:
                        reverter = reverter+i[g]
            permuta.append(reverter)
            reverter = ""
        for i in permuta:
            reverter = reverter+i
        dados_dec.append(reverter)
    return dados_dec