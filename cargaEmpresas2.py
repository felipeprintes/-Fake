import csv
import sys
import MySQLdb # para o MySQL
from gravaLog import gravar_log

con = MySQLdb.connect(user='root', db='hackathon')
cursor = con.cursor()
numCarga = 0
emp = []
x=0
while numCarga < 11:
    csvx = "empresas"+str(numCarga)+".csv"
    with open(csvx, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                if row[0][1:-1] not in emp:
                    emp.append(row[0][1:-1])
                    x+=1
                    
                    
            numCarga +=1
            print(x,numCarga)
            
    """        
    x = 0
    while x < len(emp):
        empresa = emp[x]
                #print (x,empresa)
        try:
            cursor.execute('INSERT INTO Empresas (nome) VALUES (%s)',[empresa])
            con.commit()
        except Exception as e:
            # Em caso de erro de referência, gravo no log
            gravar_log("type error: ", e)
        x +=1
    """                      