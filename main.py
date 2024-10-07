import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilename


Tk().withdraw()


caminho_arquivo = askopenfilename(title="Selecione o arquivo PDF", 
                                  filetypes=[("Arquivos PDF", "*.pdf")])
#Substituir por caminho do pdf

if caminho_arquivo:
    with open(caminho_arquivo, 'rb') as pdf_file:
       
        reader = PyPDF2.PdfReader(pdf_file)
        
        texto_completo = ""
        
        for page in reader.pages:
            texto_completo += page.extract_text()     
        print(texto_completo)
else:
    print("Nenhum arquivo foi selecionado.")



