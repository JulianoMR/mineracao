ref_arquivo = open('/Users/Juliano/Documents/Python/Araraquara5atrib.data', 'r')
linha = ref_arquivo.readline()
linha = ref_arquivo.readline()#Desconsidera a primeira linha do arquivo (cabeçalho).

print("ID\tPrec\t\tTemp\t\tNDVI\t\tWRSI")

#Variáveis que irão armazenar os dados discretizados (Prec e Temp)de cada linha do arquivo. E também os não discretizados (NDVI e WRSI).
id = []
prec = []
temp = []
ndvi = []
wrsi = []

while linha:
    valores = linha.split()
    
    id.append(valores[0])
    
    #Precipitação:
    if float(valores[1]) >= 0 and float(valores[1]) < 0.5 :
        prec.append("Sem chuva")
    elif float(valores[1]) >= 0.5 and float(valores[1]) < 1 :
        prec.append("Vestigio")
    elif float(valores[1]) >= 1 and float(valores[1]) < 49 :
        prec.append("Leve")
    elif float(valores[1]) >= 49 and float(valores[1]) < 250 :
        prec.append("Moderada")
    elif float(valores[1]) >= 250 and float(valores[1]) < 1000 :
        prec.append("Pesada")
    
    #Temperatura média:
    if (float(valores[2]) + float(valores[3]))/2 >= 0 and (float(valores[2]) + float(valores[3]))/2 < 10 :
        temp.append("Muito Frio")
    elif (float(valores[2]) + float(valores[3]))/2 >= 10 and (float(valores[2]) + float(valores[3]))/2 < 16 :
        temp.append("Frio")
    elif (float(valores[2]) + float(valores[3]))/2 >= 16 and (float(valores[2]) + float(valores[3]))/2 < 22 :
        temp.append("Suave")
    elif (float(valores[2]) + float(valores[3]))/2 >= 22 and (float(valores[2]) + float(valores[3]))/2 < 28 :
        temp.append("Caloroso")
    elif (float(valores[2]) + float(valores[3]))/2 >= 28 and (float(valores[2]) + float(valores[3]))/2 < 50 :
        temp.append("Quente")

    #NDVI e WRSI:
    ndvi.append(valores[4])
    wrsi.append(valores[5])

    linha = ref_arquivo.readline()

ref_arquivo.close()

novo_Arquivo = open('/Users/Juliano/Documents/Python/novo.data', 'w')
novo_Arquivo.write("ID\tPrec\t\tTemp\t\tNDVI\t\tWRSI\n")

#Apenas para mostrar corretamente ao usuário em um novo arquivo:
for a in id:
    txt = ""
       
    if prec[int(a)-1] == "Moderada" or prec[int(a)-1] == "Sem chuva" :
        txt=(id[int(a)-1] + "\t" + prec[int(a)-1] + "\t" )
    else:
        txt=(id[int(a)-1] + "\t" + prec[int(a)-1] + "\t\t")
        
    if temp[int(a)-1] == "Caloroso":
        txt = txt + temp[int(a)-1] + "\t" + ndvi[int(a)-1] + "\t" + wrsi[int(a)-1]
    else:
        txt = txt + temp[int(a)-1] + "\t\t" + ndvi[int(a)-1] + "\t" + wrsi[int(a)-1]
    
    print(txt)
    novo_Arquivo.write(txt + "\n")

novo_Arquivo.close();

nCB = int(len(prec)/7)

#Cada variável representa uma discretização da temperatura, e cada posição do vetor corresponde 1 dia (Domingo a Sábado).
#Em cada posição, é incrementada sua ocorrência nos nCB ciclos, que é calculado acima.
s=[0,0,0,0,0,0,0]
v=[0,0,0,0,0,0,0]
l=[0,0,0,0,0,0,0]
m=[0,0,0,0,0,0,0]
p=[0,0,0,0,0,0,0]

aux=0
for j in range(7):
    print ("Dia: " + str(j))#teste (Dia 0 = Domingo, Dia 1 = Segunda...)
    for i in range(nCB):
        if prec[j] == "Sem chuva":
            s[aux]+=1
            print(j)
        j+=7
    aux+=1
print(s)

aux=0
for j in range(7):
    print ("Dia: " + str(j))#teste (Dia 0 = Domingo, Dia 1 = Segunda...)
    for i in range(nCB):
        if prec[j] == "Verstigio":
            v[aux]+=1
            print(j)
        j+=7
    aux+=1
print(v)

aux=0
for j in range(7):
    print ("Dia: " + str(j))#teste (Dia 0 = Domingo, Dia 1 = Segunda...)
    for i in range(nCB):
        if prec[j] == "Leve":
            l[aux]+= 1
            print(j)
        j+=7
    aux+=1
print(l)

aux=0
for j in range(7):
    print ("Dia: " + str(j))#teste (Dia 0 = Domingo, Dia 1 = Segunda...)
    for i in range(nCB):
        if prec[j] == "Moderada":
            m[aux]+= 1
            print(j)
        j+=7
    aux+=1
print(m)

aux=0
for j in range(7):
    print ("Dia: " + str(j))#teste (Dia 0 = Domingo, Dia 1 = Segunda...)
    for i in range(nCB):
        if prec[j] == "Pesada":
            p[aux]+= 1
            print(j)
        j+=7
    aux+=1
print(p)
