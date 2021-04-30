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
		main.Logs(self, 0)

		self.arq = False

		self.fontePadrao = ("Arial", "12")

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
		self.logs["width"] = 60
		self.logs.pack(side=LEFT)

		self.projeto = Button(self.menuContainer, text="Tutorial", command=self.abrirProjeto)
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
		else:
			main.Logs(self, 11)
			messagebox.showinfo("","Enviado!")
			self.conteudo.delete(0.0, END)
	
	def logsEmail(self):
		main.Logs(self, 2)
		e = main.LogsEmail(self)
		if e==True:
			messagebox.showerror("","Erro!")
		else:
			messagebox.showinfo("","Enviado!")
	
	def abrirProjeto(self):
		webbrowser.open("tutorial/tutorial.html")

root = Tk()
root.title("Sendex - 2021")
Sendex(root.geometry('1000x900'))
root.resizable(0, 0)
root.mainloop()