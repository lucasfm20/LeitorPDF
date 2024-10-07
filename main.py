import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilename


Tk().withdraw()

contato ='Contato'
competencia ='Principais'

def intervalo(ini,fim):
    indice_inicio = palavras.index(ini)
    indice_fim = palavras.index(fim)


    intervalo_palavras = palavras[indice_inicio:indice_fim]

    print(intervalo_palavras)

caminho_arquivo = askopenfilename(title="Selecione o arquivo PDF", 
                                  filetypes=[("Arquivos PDF", "*.pdf")])
#Substituir por caminho do pdf

if caminho_arquivo:
    with open(caminho_arquivo, 'rb') as pdf_file:
       
        reader = PyPDF2.PdfReader(pdf_file)
        
        texto_completo = ""
        
        for page in reader.pages:
            texto_completo += page.extract_text()     
        #print(texto_completo)
        palavras = texto_completo.split()
        #print(palavras)

        intervalo(contato,competencia)
else:
    print("Nenhum arquivo foi selecionado.")



