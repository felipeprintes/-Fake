import csv
import pymysql.cursors
from gravaLog import gravar_log

emp=[]
result=[]
x = 0
y = 0
def buscaOperacoes(empresa):
    ope = []
    with open("operacoes2018.csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            if row[0] in str(empresa):
                ope.append(row)
    with open("operacoes2018.csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            if row[0] in str(empresa):
                ope.append(row)
                
                
        x = 0
        while x < len(ope):
            gravar_log('',ope[x])
            x+=1


def buscaEmpresas(empresas):
    z = 0
    while z < len(empresas):
        busca = '%' + empresas[z] +'%'
        for i in busca:
            busca = busca.replace(" ", "")
        if "%%" not in busca:
            #print (busca)
            #break
            con = pymysql.connect(user='root', db='hackathon')
            cursor = con.cursor()
            
            sql = "SELECT nome FROM empresas WHERE nome LIKE (%s)"
            
            cursor.execute(sql,[busca])
            
            queryResult = cursor.fetchall()
            if queryResult is not None:
                print(busca)
            #print(queryResult)
            #gravar_log("erro:",queryResult)
            #break
            for x in queryResult:
                buscaOperacoes(x)
        z+=1

with open("arq (1).csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            emp.append(row[0:-1])

while x < len(emp):
    if 'BNDES' not in emp[x][0]:
        result.append(emp[x][0])
    if 'BNDES' not in emp[x][1]:
        result.append(emp[x][1])
    if 'BNDES' not in emp[x][2]:
        result.append(emp[x][2])
    if 'BNDES' not in emp[x][3]:
        result.append(emp[x][3])
    if 'BNDES' not in emp[x][4]:
        result.append(emp[x][4])
    if 'BNDES' not in emp[x][5]:
        result.append(emp[x][5])
    #print(result)
    buscaEmpresas(result)
    result = None
    result = []
    x+=1