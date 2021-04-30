from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "12")
        
        self.menuContainer = Frame(master)
        self.menuContainer.pack()
        
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
        
        self.segundoContainer = Frame(master)
        self.primeiroContainer["pady"] = 20
        self.segundoContainer.pack()
        
        self.terceiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 20
        self.terceiroContainer.pack()
        
        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.Email = Label(self.primeiroContainer, text="E-mail: ")
        self.Email.pack(side=LEFT)

        self.valorEmail = Entry(self.primeiroContainer)
        self.valorEmail["width"] = 30
        self.valorEmail.pack(side=RIGHT)

        self.Senha = Label(self.segundoContainer, text="Senha: ")
        self.Senha.pack(side=LEFT)

        self.valorSenha = Entry(self.segundoContainer)
        self.valorSenha["width"] = 30
        self.valorSenha["show"] = "*"
        self.valorSenha.pack(side=RIGHT)

        self.Verificar = Button(self.terceiroContainer, text="Entrar", command=self.VerificarUsuario)
        self.Verificar.pack()
    
    def VerificarUsuario(self):
        print(self.valorSenha.get())

root = Tk()
root.title("Autenticação")
Application(root.geometry('550x300'))
root.resizable(0, 0)
root.mainloop()