lista=["teste","teste1","teste2","teste3","teste4","teste5"]

teste ='teste'
teste3 ='teste3'
teste5='teste5'

def intervalo(ini,fim):
    indice_inicio = lista.index(ini)
    indice_fim = lista.index(fim)


    intervalo_palavras = lista[indice_inicio:indice_fim]

    print(intervalo_palavras)

intervalo(teste,teste3)

intervalo(teste3,teste5)