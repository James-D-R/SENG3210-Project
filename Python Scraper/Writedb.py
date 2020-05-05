import pymysql

def insert_armor(db,table,filename):

    #Set up DB connection
    host = "192.168.56.117"
    user = "remjamd"
    password = "password1"
    database = db

    connection = pymysql.connect(host=host, user=user, password=password, db=database, cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    #Read lines from csv
    csv = open(filename,'r')
    lines = csv.readlines()

    #Insert each line to DB table
    for line in lines:
        column = line.split(",")
        query = ("INSERT INTO " + table + " (name,rarity,skill1,skill2,defense,slot1,slot2,slot3,firedef,waterdef,thunderdef,icedef,dragondef)" 
        + " VALUES('"
        + column[0] + "'," + (column[1]) + ",'" + (column[2]) + "','" + column[3] + "'," + column[4] + ",'" + column[5] + "','" 
        + column[6] + "','"+ column[7] + "','"+ column[8] + "',"+ column[9] + ","+ column[10] + ","+ column[11] + ","+ column[12] 
        + ")")
    
        cur.execute(query)

    connection.commit()
    connection.close()

    csv.close()


def insert_charms(db,table,filename):

    #Set up DB connection
    host = "192.168.56.117"
    user = "remjamd"
    password = "password1"
    database = db

    connection = pymysql.connect(host=host, user=user, password=password, db=database, cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    #Read lines from csv
    csv = open(filename,'r')
    lines = csv.readlines()

    #Insert each line to DB table
    for line in lines:
        column = line.split(",")
        query = ("INSERT INTO " + table + " (name,rarity,skill1,skill2)" 
        + " VALUES('"
        + column[0] + "'," + (column[1]) + ",'" + (column[2]) + "','" + column[3] + "')")
    
        cur.execute(query)

    connection.commit()
    connection.close()

    csv.close()

def insert_decorations(db,table,filename):

    #Set up DB connection
    host = "192.168.56.117"
    user = "remjamd"
    password = "password1"
    database = db

    connection = pymysql.connect(host=host, user=user, password=password, db=database, cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    #Read lines from csv
    csv = open(filename,'r')
    lines = csv.readlines()

    #Insert each line to DB table
    for line in lines:
        column = line.split(",")
        query = ("INSERT INTO " + table + " (name,size,skill1,skill2)" 
        + " VALUES('"
        + column[0] + "'," + (column[1]) + ",'" + (column[2]) + "','" + column[3] +  "')")
    
        cur.execute(query)

    connection.commit()
    connection.close()

    csv.close()


def insert_skills(db,table,filename):

    #Set up DB connection
    host = "192.168.56.117"
    user = "remjamd"
    password = "password1"
    database = db

    connection = pymysql.connect(host=host, user=user, password=password, db=database, cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    #Read lines from csv
    csv = open(filename,'r')
    lines = csv.readlines()

    #Insert each line to DB table
    for line in lines:
        column = line.split(",")
        query = ("INSERT INTO " + table + " (name,tier1,tier2,tier3,tier4,tier5,tier6,tier7)" 
        + " VALUES('"
        + column[0] + "','" + (column[1]) + "','" + (column[2]) + "','" + column[3] + "','" + column[4] + "','" + column[5] + "','" 
        + column[6] + "','"+ column[7] + "')")
    
        cur.execute(query)

    connection.commit()
    connection.close()

    csv.close()

def insert_attacks(db, table, filename):

    #Set up DB connection
    host = "192.168.56.117"
    user = "remjamd"
    password = "password1"
    database = db

    connection = pymysql.connect(host=host, user=user, password=password, db=database, cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    #Read lines from csv
    csv = open(filename,'r')
    lines = csv.readlines()

    for line in lines:
        column = line.split(",")
        query = ("INSERT INTO " + table + " (ID,Move,Power,Stun,Exhaust,Mount,Element_Multiplier,Ailment_Multiplier,Part_Break_Multiplier,Tenderize)" 
        + " VALUES('"
        + column[0] + "','" + (column[1]) + "','" + (column[2]) + "','" + column[3] + "','" + column[4] + "','" + column[5] + "','" 
        + column[6] + "','"+ column[7] + "','"+ column[8] + "','"+column[9] + "')")

        cur.execute(query)

    connection.commit()
    connection.close()

    csv.close()


#Run
#db = "armor"
#table = "head"
#filename = "Head_Pieces.csv"

#insert_armor(db,table,filename)
'''
table = "chest"
filename = "Chest_Pieces.csv"
#insert_armor(db,table,filename)

table = "arms"
filename = "Arm_Pieces.csv"
#insert_armor(db,table,filename)

table = "waist"
filename = "Waist_Pieces.csv"
#insert_armor(db,table,filename)

table = "legs"
filename = "Leg_Pieces.csv"
#insert_armor(db,table,filename)

table = "charms"
filename = "Charms.csv"
#insert_charms(db,table,filename)

table = "decorations"
filename = "Decorations.csv"
#insert_decorations(db,table,filename)


table = "skills"
filename = "Skills.csv"
insert_skills(db,table,filename)



table = "GS_Attacks"
filename = "MHWData_GSAttack.csv"
insert_attacks(db,table,filename)
'''

db = "Weapons"
insert_attacks(db,"SH_Attacks","MHWData_SHAttack.csv")

insert_attacks(db,"DB_Attacks","MHWData_DBAttack.csv")

insert_attacks(db,"LS_Attacks","MHWData_LSAttack.csv")

insert_attacks(db,"H_Attacks","MHWData_HAttack.csv")

insert_attacks(db,"HH_Attacks","MHWData_HHAttack.csv")

insert_attacks(db,"L_Attacks","MHWData_LAttack.csv")

insert_attacks(db,"GL_Attacks","MHWData_GLAttack.csv")

insert_attacks(db,"SA_Attacks","MHWData_SAAttack.csv")

insert_attacks(db,"CB_Attacks","MHWData_CBAttack.csv")

insert_attacks(db,"IG_Attacks","MHWData_IGAttack.csv")