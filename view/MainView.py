from tkinter import *

class MainView(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("350x450")
        self.title("LearningLanguage")
        self.iconbitmap("image\icon\langues.ico")

        ##var
        bigFont = 30
        normalFont = 20
        smalFont = 10

        #top (menu)
        menu = Frame(self)
        buttondico = Button(menu,text="Dicsionaire",font=("Courier", smalFont))
        buttonhistorique = Button(menu,text="Historique",font=("Courier", smalFont))

        buttondico.pack(side="left")
        buttonhistorique.pack(side="left")

        menu.pack(side="top",fill='x')

        #midel (mots)
        question = Frame(self)

        self.mots = Label(question,text="MOTS",font=("Courier", bigFont))
        self.reponce = Label(question,text="Réponce",fg="green",font=("Courier", smalFont))

        self.mots.pack()
        self.reponce.pack()

        question.pack(expand=1)


        #bottom (réponce)

        reponce = Frame(self)

        entreyReponce = Entry(reponce)
        buttonValider = Button(reponce,text="Valider",bg="green",font=("Courier", smalFont))
        buttonPasser = Button(reponce,text="Passer",bg="grey",font=("Courier", smalFont))

        reponce.columnconfigure(0, weight=1)

        entreyReponce.grid(row=0,column=0, sticky="WE")
        buttonValider.grid(row=1,column=0, sticky="WE")
        buttonPasser.grid(row=2,column=0, sticky="WE")

        reponce.pack(side="bottom",expand=0,padx=5,pady=5)
    