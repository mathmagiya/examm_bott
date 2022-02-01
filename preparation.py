import csv
from pyexpat import version_info
from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from datetime import datetime
import sqlite3




#from locale import strcoll
count=0
string=""

def open_new_file(file_name) -> list:
    total_list=[]
    rowsSamsung, colsSamsung = (5, 3)
    arrSamsung = [[0 for i in range(colsSamsung)] for j in range(rowsSamsung)]
    rowsHerox, colsHerox = (3, 3)
    arrHerox=[[0 for i in range(rowsHerox)] for j in range(colsHerox)]
    rowsHP, colsHP = (2, 3)
    arrHP=[[0 for i in range(colsHP)] for j in range(rowsHP)]
    rowsCanon, colsCanon = (4, 3)
    arrCanon=[[0 for i in range(colsCanon)] for j in range(rowsCanon)]

    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        countForDB=-1
        for row in spamreader:
            countForDB=countForDB+1    
            if (countForDB<rowsSamsung):
                for j in range(0,colsSamsung):
                    #print("countForDB ][j==",countForDB,j)
                    arrSamsung[countForDB][j]=row[j+2]
                    #print(row[j+2])

            if (countForDB>=rowsSamsung and countForDB<rowsSamsung+rowsHerox):
                for j in range(0,colsHerox):
                    #print("countForDB ][j==",countForDB,j)
                    arrHerox[countForDB-rowsSamsung][j]=row[j+2]
                    #print(row[j+2])

            if (countForDB>=rowsSamsung+rowsHerox and countForDB<rowsSamsung+rowsHerox+rowsHP):
                for j in range(0,colsHP):
                    #print("countForDB ][j==",countForDB,j)
                    arrHP[countForDB-rowsSamsung-rowsHerox][j]=row[j+2]
                    #print(row[j+2])

            if (countForDB>=rowsSamsung+rowsHerox+rowsHP and countForDB<rowsSamsung+rowsHerox+rowsHP+rowsCanon):
                for j in range(0,colsCanon):
                    #print("countForDB ][j==",countForDB,j)
                    arrCanon[countForDB-rowsSamsung-rowsHerox-rowsHP][j]=row[j+2]
                    #print(row[j+2])

                    
    #print("arrsams",arrSamsung)


    total_list.append(arrSamsung)
    total_list.append(arrHerox)
    total_list.append(arrHP)
    total_list.append(arrCanon)
    csvfile.close
    return total_list

fout = open("db_query_log.txt","a")
out="file was written successevely: at "+str(datetime.now())+"\n"
fout.write(out)
fout.close()

total_list1=open_new_file("printers1.csv")

def orm_apply_add(total_list):
    db_uri = "sqlite:///db.sqlite"
    engine = create_engine(db_uri)

    engine.execute('DROP TABLE IF EXISTS samsung;')
    #oh gosh there is no analogues for DROP TABLE IF EXISTS. 
    #Only just DROP table.drop(engine) which is not absolutely fit
    
    metadata = MetaData(bind=None)
    meta = MetaData()
    
    samsung = Table(
        'samsung', meta, 
        Column('id', Integer, primary_key = True), 
        Column('model', String), 
        Column('service_1', Integer), 
        Column('service_2', Integer), 
        Column('service_3', Integer)
        )
    
    meta.create_all(engine)
    
    with engine.connect() as connection:
        with connection.begin():
            r1 = connection.execute(samsung.select())
            for i in range(0,len(total_list[0])):
                connection.execute(samsung.insert(), {"model": "model#"+str(i+1), "service_1": total_list[0][i][0], 
                "service_2": total_list[0][i][1], "service_3": total_list[0][i][2]})

#Herox
    engine.execute('DROP TABLE IF EXISTS herox;')

    herox = Table(
        'herox', meta, 
        Column('id', Integer, primary_key = True), 
        Column('model', String), 
        Column('service_1', Integer), 
        Column('service_2', Integer), 
        Column('service_3', Integer)
        )
    
    meta.create_all(engine)
    
    with engine.connect() as connection:
        with connection.begin():
            r1 = connection.execute(herox.select())
            for i in range(0,len(total_list[1])):
                connection.execute(herox.insert(), {"model": "model#"+str(i+1), "service_1": total_list[1][i][0], 
                "service_2": total_list[1][i][1], "service_3": total_list[1][i][2]})


    #HP
    engine.execute('DROP TABLE IF EXISTS hp;')

    hp = Table(
        'hp', meta, 
        Column('id', Integer, primary_key = True), 
        Column('model', String), 
        Column('service_1', Integer), 
        Column('service_2', Integer), 
        Column('service_3', Integer)
        )
    
    meta.create_all(engine)
    
    with engine.connect() as connection:
        with connection.begin():
            r1 = connection.execute(hp.select())
            for i in range(0,len(total_list[2])):
                connection.execute(hp.insert(), {"model": "model#"+str(i+1), "service_1": total_list[2][i][0], 
                "service_2": total_list[2][i][1], "service_3": total_list[2][i][2]})


#Canon
    engine.execute('DROP TABLE IF EXISTS canon;')

    canon = Table(
        'canon', meta, 
        Column('id', Integer, primary_key = True), 
        Column('model', String), 
        Column('service_1', Integer), 
        Column('service_2', Integer), 
        Column('service_3', Integer)
        )
    
    meta.create_all(engine)
    
    with engine.connect() as connection:
        with connection.begin():
            r1 = connection.execute(canon.select())
            for i in range(0,len(total_list[3])):
                connection.execute(canon.insert(), {"model": "model#"+str(i+1), "service_1": total_list[3][i][0], 
                "service_2": total_list[3][i][1], "service_3": total_list[3][i][2]})


    engine.dispose()
    fout = open("db_query_log.txt","a")
    fout.write("\nDB was loaded at "+str(datetime.now())+"\n")
    fout.close()
#orm_apply_add(total_list1)


def select_brand(tabName) -> tuple:

    db_uri = "sqlite:///db.sqlite"

    engine = create_engine(db_uri)
    metadata = MetaData(bind=None)
    table = Table(
        tabName, 
        metadata, 
        autoload=True, 
        autoload_with=engine
    )

    query = table.select()

    connection = engine.connect()
    results = connection.execute(query).fetchall()

    fout = open("db_query_log.txt","a")
    fout.write("The table "+tabName+"was selectesd: at "+str(datetime.now())+". The result is:"+str(results))
    fout.close()
    
    #for row in results:
    #    print (row)

    engine.dispose()
    return results


#print("Проверка функции select")
#print(type(select_brand("HP")))
#select_brand("samsung")
fout.close()