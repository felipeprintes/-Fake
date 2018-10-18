#este programa busca o nome de uma empresa em um texto
import MySQLdb # para o MySQL


def buscaEmpresa(busca):
    resultSet = []
    empresas = []
    #busca = "%JBS%"
    x = 0
    con = MySQLdb.connect(user='root', db='hackathon')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM empresas where nome LIKE (%s)", [busca])
    resultSet = cursor.fetchall()
    #print (resultSet[1])
    while x < len(resultSet):
        empresas.append(resultSet[x])
        
        x +=1 
    
    con.close()

