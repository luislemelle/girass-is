from tkinter.filedialog import askopenfilename
import pandas as pd
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image

root = tk.Tk()

HEIGHT = 400
WIDTH = 400

C = tk.Canvas(root, bg="blue", height=HEIGHT, width=WIDTH)
arquivo = ImageTk.PhotoImage(file = "C:\\girassois\\girassol.jpeg")
background_label = tk.Label(root, image=arquivo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()


def clickbutton():
    filename = askopenfilename()
    dataframe = pd.read_excel(filename)
    pegaValor = dataframe['Valor']
    CalculaPorcentagem10 = pegaValor * .10
    CalculaPorcentagem20 = pegaValor * .20
    CalculaPorcentagem30 = pegaValor * .30
    resposta = ' 10% de do total é: R$'+ str(sum(CalculaPorcentagem10)) + '\n 20% de do total é: R$'+ str(sum(CalculaPorcentagem20)) + '\n 30% de do total é: R$'+ str(sum(CalculaPorcentagem30))
    popupmsg(resposta)

def popupmsg(resposta):
    popup = tk.Tk()
    popup.wm_title("Resultado")
    label = ttk.Label(popup, text=resposta)
    label.pack(side="top", fill="x", pady=50 , padx =150)
    B1 = ttk.Button(popup, text="Entendido", command = popup.destroy)
    B1.pack()
    canvas2 = tk.Canvas(popup, height=150 , width=150)
    canvas2.pack()

    
    popup.mainloop()    

button = tk.Button(root, text = 'Pesquisa Planilha', bg= 'Orange' , fg = 'Black', command = clickbutton).place(x=150, y=50)


root.mainloop()


