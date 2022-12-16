import sys

import pymysql as MySQLdb
import MySQLdb.cursors

def getGuiaPeso(guiaNo):
#===================================================================
# connect to mysql
#===================================================================
    try:
        #db = MySQLdb.connect(host='sanfona.myvnc.com', user='julio', passwd='j301052', db='agro', cursorclass=MySQLdb.cursors.DictCursor)
        db = MySQLdb.connect(host='192.168.1.6', user='julio', passwd='j301052', db='agro',
                             cursorclass=MySQLdb.cursors.DictCursor)
    except MySQLdb.Error as e:
        print ('Error %d: %s' % (e.args[0], e.args[1]))
        sys.exit(1)
    #===================================================================
    # query select from table
    #===================================================================
    cursor = db.cursor()
    #sql = "SELECT sum(ValorLiq) FROM facturas WHERE Date > %s and Item = '00' and Designacao like %s and Preco > 20"
    sql = "select Data, GuiaNo, Hora, Descricao, Peso, Parcela" \
          " from agro.guiaentrada where GuiaNo like %s order by Data, Hora, GuiaNo"
    cursor.execute(sql, (guiaNo,))
    all_rows = cursor.fetchall()
    #print (len(all_rows)) # How many rows are returned.
    peso = 0.0
    for row in all_rows: # While loops always make me shudder!
        peso += float(row['Peso'])
    cursor.close()
    db.close()
    return peso