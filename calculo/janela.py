from tkinter import * 


janela = Tk()

class Application():
    def __init__(self):
        self.janela = janela
        self.screen()
        janela.mainloop()
    def screen(self):
        self.janela.title("Primeira tela Tkinter")
        self.janela.configure(background="#69b2ce")
        self.janela.geometry("600x350")
        self.janela.resizable(False, False)




Application()