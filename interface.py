#imports for project
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfiles
from time import sleep, time
from PIL import ImageTk, Image
import webbrowser
import functions.main as main
import functions.casosdeuso as csu
#my class
class Sendex:

	def __init__(self, master=None):
		self.tela = 1
		self.fontePadrao = ("Arial", "12")

		self.campoRegistrologo = Frame(master)
		self.campoRegistrologo["pady"] = 200
		self.campoRegistrologo.pack()

		self.campoRegistro = Frame(master)
		self.campoRegistro["pady"] = 10
		self.campoRegistro["padx"] = 10
		self.campoRegistro.pack()

		imgLogo = Image.open("images/logoSendex.png")
		imgLogo = ImageTk.PhotoImage(imgLogo)
		self.logo = Label(self.campoRegistrologo, image=imgLogo)
		self.logo.image = imgLogo
		self.logo.pack()

		self.textRegistro = Label(self.campoRegistro, text="Registro:")
		self.textRegistro.pack(side=LEFT)

		self.registro = Entry(self.campoRegistro)
		self.registro["width"] = 40
		self.registro["show"] = "*"
		self.registro.pack(side=LEFT)

		self.botao = Button(self.campoRegistro, text="Entrar", command=self.Entrar, bg="#98FB98")
		self.botao.pack(side=RIGHT)
	
	def Entrar(self):
		registro_sendex = csu.DadosServidor()
		x = registro_sendex[2]
		if self.registro.get()==x:
			self.Elementos()
		else:
			messagebox.showerror("", "Errado!")

	def Autenticacao(self, master=None):
		self.segundoContainer.pack_forget()
		self.terceiroContainer.pack_forget()
		self.quartoContainer.pack_forget()
		self.quintoContainer.pack_forget()
		self.sextoContainer.pack_forget()
		self.setimoContainer.pack_forget()
		self.oitavoContainer.pack_forget()
		self.nonoContainer.pack_forget()
		self.decimoContainer.pack_forget()

		self.emailContainer = Frame(master)
		self.emailContainer["pady"] = 10
		self.emailContainer.pack()

		self.senhaContainer = Frame(master)
		self.senhaContainer["pady"] = 10
		self.senhaContainer.pack()

		self.registroContainer = Frame(master)
		self.registroContainer["pady"] = 10
		self.registroContainer.pack()

		self.emailContainernovo = Frame(master)
		self.emailContainernovo["pady"] = 10
		self.emailContainernovo.pack()

		self.novoContainer = Frame(master)
		self.novoContainer["pady"] = 10
		self.novoContainer.pack()

		self.alterarContainer = Frame(master)
		self.alterarContainer["pady"] = 10
		self.alterarContainer.pack()

		self.typeEmailatual = Label(self.emailContainer, text="Conta do atual G-mail: ", font=self.fontePadrao)
		self.typeEmailatual.pack(side=LEFT)

		self.campoEmailatual = Entry(self.emailContainer)
		self.campoEmailatual["width"] = 45
		self.campoEmailatual.pack(side=RIGHT)

		self.typeSenhaatual = Label(self.senhaContainer, text="Senha do atual e-mail: ", font=self.fontePadrao)
		self.typeSenhaatual.pack(side=LEFT)

		self.campoSenhaatual = Entry(self.senhaContainer)
		self.campoSenhaatual["show"] = "*"
		self.campoSenhaatual["width"] = 16
		self.campoSenhaatual.pack(side=LEFT)

		self.typeRegistroatual = Label(self.senhaContainer, text="Registro atual: ", font=self.fontePadrao)
		self.typeRegistroatual.pack(side=LEFT)
		
		self.Registroatual = Entry(self.senhaContainer)
		self.Registroatual["show"] = "*"
		self.Registroatual["width"] = 16
		self.Registroatual.pack(side=RIGHT)

		linha = "___________________________"
		self.separa = Label(self.registroContainer, text="{} Alterar para {}".format(linha, linha), font=self.fontePadrao)
		self.separa.pack()

		self.typeEmailnovo = Label(self.emailContainernovo, text="Conta do novo G-mail: ", font=self.fontePadrao)
		self.typeEmailnovo.pack(side=LEFT)

		self.campoEmailnovo = Entry(self.emailContainernovo)
		self.campoEmailnovo["width"] = 45
		self.campoEmailnovo.pack(side=RIGHT)

		self.typeSenhanovo = Label(self.novoContainer, text="Senha do novo e-mail: ", font=self.fontePadrao)
		self.typeSenhanovo.pack(side=LEFT)

		self.campoSenhanovo = Entry(self.novoContainer)
		self.campoSenhanovo["show"] = "*"
		self.campoSenhanovo["width"] = 16
		self.campoSenhanovo.pack(side=LEFT)

		self.typeRegistronovo = Label(self.novoContainer, text="Novo registro: ", font=self.fontePadrao)
		self.typeRegistronovo.pack(side=LEFT)
		
		self.Registronovo = Entry(self.novoContainer)
		self.Registronovo["show"] = "*"
		self.Registronovo["width"] = 16
		self.Registronovo.pack(side=RIGHT)

		self.botaoAlterar = Button(self.alterarContainer, text="Alterar", command=self.AlterarRegistro)
		self.botaoAlterar.pack()

		self.tela = 3
		self.autent.pack_forget()
		self.autent = Button(self.menuContainer, text="Voltar", command=self.Elementos, bg="#98FB98")
		self.autent.pack(side=RIGHT)

	def Elementos(self, master=None):
		main.Logs(self, 0)

		if self.tela==1:
			self.campoRegistrologo.pack_forget()
			self.campoRegistro.pack_forget()
		if self.tela==3:
			self.menuContainer.pack_forget()
			self.primeiroContainer.pack_forget()
			self.emailContainer.pack_forget()
			self.senhaContainer.pack_forget()
			self.registroContainer.pack_forget()
			self.emailContainernovo.pack_forget()
			self.novoContainer.pack_forget()
			self.alterarContainer.pack_forget()

		self.arq = False

		self.menuContainer = Frame(master)
		self.menuContainer.pack()

		self.primeiroContainer = Frame(master)
		self.primeiroContainer["pady"] = 10
		self.primeiroContainer.pack()

		self.segundoContainer = Frame(master)
		self.segundoContainer["padx"] = 20
		self.segundoContainer.pack()

		self.terceiroContainer = Frame(master)
		self.terceiroContainer["padx"] = 20
		self.terceiroContainer.pack()

		self.quartoContainer = Frame(master)
		self.quartoContainer["padx"] = 20
		self.quartoContainer.pack()

		self.quintoContainer = Frame(master)
		self.quintoContainer["padx"] = 20
		self.quintoContainer.pack()

		self.sextoContainer = Frame(master)
		self.sextoContainer["padx"] = 20
		self.sextoContainer.pack()
		
		self.setimoContainer = Frame(master)
		self.setimoContainer["padx"] = 20
		self.setimoContainer.pack()

		self.oitavoContainer = Frame(master)
		self.oitavoContainer["padx"] = 20
		self.oitavoContainer.pack()

		self.nonoContainer = Frame(master)
		self.nonoContainer["padx"] = 20
		self.nonoContainer["pady"] = 5
		self.nonoContainer.pack()

		self.decimoContainer = Frame(master)
		self.decimoContainer["padx"] = 20
		self.decimoContainer.pack()

		self.logs = Button(self.menuContainer, text="Logs no e-mail", command=self.logsEmail)
		self.logs["width"] = 50
		self.logs.pack(side=LEFT)

		self.autent = Button(self.menuContainer, text="Autenticação", command=self.Autenticacao)
		self.autent["width"] = 10
		self.autent.pack(side=LEFT)

		self.projeto = Button(self.menuContainer, text="Tutorial", command=self.abrirTutorial)
		self.projeto["width"] = 10
		self.projeto.pack(side=RIGHT)

		imgLogo = Image.open("images/logoSendex.png")
		imgLogo = ImageTk.PhotoImage(imgLogo)
		self.logo = Label(self.primeiroContainer, image=imgLogo)
		self.logo.image = imgLogo
		self.logo.pack()

		self.labelemail = Label(self.segundoContainer, text='Para: ', font=self.fontePadrao)
		self.labelemail.pack(side=LEFT)

		self.email = Entry(self.segundoContainer)
		self.email["width"] = 30
		self.email["font"] = self.fontePadrao
		self.email.pack(side=LEFT)

		self.labelassunto = Label(self.segundoContainer, text='Assunto: ', font=self.fontePadrao)
		self.labelassunto.pack(side=LEFT)

		self.assunto = Entry(self.segundoContainer)
		self.assunto["width"] = 30
		self.assunto["font"] = self.fontePadrao
		self.assunto.pack(side=RIGHT)

		self.labelconteudo = Label(self.sextoContainer, text='Conteúdo: ', font=self.fontePadrao)
		self.labelconteudo.pack(side=LEFT)

		self.conteudo = Text(self.setimoContainer, height=12, width=90)
		self.conteudo["font"] = self.fontePadrao
		self.conteudo.pack(side=RIGHT)

		self.arquivo = Button(self.nonoContainer, text="Selecionar arquivo", command=self.SelecionarArq)
		self.arquivo["width"] = 50
		self.arquivo.pack(side=LEFT)

		self.removeArq = Button(self.nonoContainer, command=self.RemoverArquivo)
		self.removeArq["width"] = 20

		self.enviar = Button(self.decimoContainer, text="Enviar", command=self.enviarEmail, bg="#98FB98")
		self.enviar["width"] = 20
		self.enviar.pack(side=LEFT)
	
	def SelecionarArq(self):
		conteudo = csu.SelecionarArquivo(self)
		if conteudo:
			self.arq = conteudo[0]
			self.arquivo["text"] = conteudo[1]
			self.arquivo["bg"] = "#98FB98"
			self.removeArq["text"] = "Remover arquivo"
			self.removeArq["bg"] = "#DCDCDC"
			self.removeArq.pack(side=RIGHT)
	
	def RemoverArquivo(self):
		self.arq = False
		self.arquivo["text"] = "Selecionar arquivo"
		self.arquivo["bg"] = "#DCDCDC"
		self.removeArq["text"] = "Removido"
		self.removeArq["bg"] = "#FA8072"

	def enviarEmail(self):
		x = time()
		if self.arq != False:
			enviar = main.PrepararEmail(None, self.assunto.get(), self.email.get(), self.conteudo.get(0.0,END), self.arq)
		else:
			self.arq = False
			enviar = main.PrepararEmail(None, self.assunto.get(), self.email.get(), self.conteudo.get(0.0,END), self.arq)
		y = time()
		print("Init: {}, Finish: {}, Result: {}".format(x, y, y-x))
		if enviar=="Vazio":
			main.Logs(self, 10)
			messagebox.showerror("","Preencha todos os campos.")
		if enviar==False:
			messagebox.showerror("","Erro: não enviado.")
			self.conteudo.delete(0.0, END)
		if enviar==True:
			main.Logs(self, 11)
			messagebox.showinfo("","Enviado!")
			self.conteudo.delete(0.0, END)
	
	def AlterarRegistro(self):
		email = self.campoEmailatual.get()
		senha = self.campoSenhaatual.get()
		registro = self.Registroatual.get()
		emailnovo = self.campoEmailnovo.get()
		senhanovo = self.campoSenhanovo.get()
		registronovo = self.Registronovo.get()
		alt = csu.enviarAlteracao(None, email, senha, registro, emailnovo, senhanovo, registronovo)
		if alt=="Diferente":
			messagebox.showerror("Dados incorretos.","Dados atuais incorretos.")
		else:
			messagebox.showinfo("Alterado!", "Alterado com sucesso.")
			self.Elementos()
	
	def logsEmail(self):
		main.Logs(self, 2)
		e = main.LogsEmail(self)
		if e==True:
			messagebox.showinfo("","Enviado!")
		else:
			messagebox.showerror("","Erro!")
	
	def abrirTutorial(self):
		try:
			webbrowser.open("tutorial/tutorial.html")
		except:
			webbrowser.open("github.com/guilhermedonizetti/Sendex")

root = Tk()
root.title("Sendex - 2021")
Sendex(root.geometry('1000x900'))
root.resizable(0, 0)
root.mainloop()