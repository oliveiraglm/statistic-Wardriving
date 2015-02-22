####### authors ############
# Eric V L Monte-Alto
# Guilherme Brandão da Silva
# Guilherme Lucas Oliveira
############################

from pylab import *

def lerArquivo(caminho):
    arquivo = open(caminho)
    conteudo = arquivo.read()
    return conteudo

array_coleta = lerArquivo("loginternet.txt").split("Network ") # array contendo as networks
lista_ssid = lerArquivo("listassid.txt") # Lista de SSIDS Padrões
#array_fabricantes = lerArquivo("listafabricantes.txt").split("\n\n") # Array de fabricantes

manufactures = {} # Dictionary contendo a quantidade de cada Manufacturer

def processaConteudo(array):

     #Contadores
    cloakedSsid = 0
    encryptionNone = 0
    encryptionWep = 0
    encryptionWpa = 0
    ssidsDefault = 0

     #Contadores Canais
    canal1 = 0
    canal2 = 0
    canal3 = 0
    canal4 = 0
    canal5 = 0
    canal6 = 0
    canal7 = 0
    canal8 = 0
    canal9 = 0
    canal10 = 0
    canal11 = 0
    canal12 = 0
    canal13 = 0

    #Varredura das Networks

    for i in range(0, len(array)):
        #verifica se SSID é oculto
        #if "<no ssid>" in array[i]:
        #   clockedSsid+=1

        if "Type       : infrastructure" in array[i]: # Se a Network for do tipo Infrastucture realiza a verificação
            #Verifica se o SSID é padrão de fábrica;
            ssid = (array[i].split('\n'))[8].split('"')
            if (ssid[1]+" ") in lista_ssid:
                ssidsDefault+=1
            #
            ##### Codigo versão antiga do Kismet ###############################
            # verifica fabricante
            #for j in range(0,len(array_fabricantes)):
            #   quebraEspacosFabricantes = (array_fabricantes[j].split("\n")[0]).split("   ")
            #   if quebraEspacosFabricantes[0].replace("-",":") ==  (quebra_espacos[1])[:8]:
            #       nomeFabricante = quebraEspacosFabricantes[1].split("		")[1]
            #       if nomeFabricante in manufactures:
            #           manufactures[nomeFabricante] +=1
            #       else:
            #           manufactures[nomeFabricante] = 1
            ##############################################################

            #verifica fabricante
            fabricante = (array[i].split('\n')[1].split(":"))
            if fabricante[1]=="<cloaked>":
                cloakedSsid+=1
                
            if fabricante[1] in manufactures:
                manufactures[fabricante[1]] +=1
            else:
                manufactures[fabricante[1]]=1
            #

            # tipo de criptografia
            if "Encryption : None" in array[i]:
                encryptionNone+=1
            elif "Encryption : WEP" in array[i]:
                encryptionWep+=1
            else:
                encryptionWpa+=1
                

            # verifica o canal utilizado pela rede
            if "Channel    : 1\n" in array[i]:
                canal1+=1
            elif "Channel    :2\n" in array[i]:
                canal2+=1
            elif "Channel    : 3\n" in array[i]:
                canal3+=1
            elif "Channel    : 4\n" in array[i]:
                canal4+=1
            elif "Channel    : 5\n" in array[i]:
                canal5+=1
            elif "Channel    : 6\n" in array[i]:
                canal6+=1
            elif "Channel    : 7\n" in array[i]:
                canal7+=1
            elif "Channel    : 8\n" in array[i]:
                canal8+=1
            elif "Channel    : 9\n" in array[i]:
                canal9+=1
            elif "Channel    : 10\n" in array[i]:
                canal10+=1
            elif "Channel    : 11\n" in array[i]:
                canal11+=1
            elif "Channel    : 12\n" in array[i]:
                canal12+=1
            elif "Channel    : 13\" in array[i]":
                canal13+=1

    
    print "SSID's Ocultos: %d\nSSIDs Default: %d\n" % (cloakedSsid, ssidsDefault)
    print "Canal 01: %d\nCanal 02: %d\nCanal 03: %d\nCanal 04: %d\nCanal 05: %d\nCanal 06: %d\nCanal 07: %d\nCanal 08: %d\nCanal 09: %d\nCanal 10: %d\nCanal 11: %d\nCanal 12: %d\nCanal 13: %d" %(canal1,canal2,canal3,canal4,canal5,canal6,canal7,canal8,canal9,canal10,canal11,canal12,canal13)
    print "WPA:%d\nWEP:%d\nNone:%d\n\n" %(encryptionWpa,encryptionWep,encryptionNone)
def geraGraficos(manufactures):
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels =() # Tupla de Manufactures.   
    fracs=[] # Quantidade de cada Fabricante.
    explode=() # Separador de cada 'fatia'
    
    for i in range(0, len(manufactures)):
                   labels+=(manufactures.keys()[i],) #Adiciona à tupla o nome do fabricante
                   fracs.append(manufactures[manufactures.keys()[i]]) # Quantidade Fabricantes
                   explode+=0,
    
    pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
    title('Fabricantes mais utilizados', bbox={'facecolor':'0.8', 'pad':5})
    show()

# Chama Funções                   
processaConteudo(array_coleta)
geraGraficos(manufactures)





    
