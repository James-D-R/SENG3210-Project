import pymysql

#Database class to open a new DB connection
class Database:
    def __init__(self,data_base):
        #Credentials
        self.db = data_base
        host = "192.168.56.117" #DO NOT USE THIS HOST IN PROD
        user = "remjamd"
        password = "password1"
        #Connect
        self.con = pymysql.connect(host=host, user=user, password=password, db=self.db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
        #print("connected to database")

    #class methods to query DB table
    #tables for Armor are: head, chest, arms, waist, legs
    def list_armor(self,table):
        self.cur.execute("SELECT * FROM "+table)
        result = self.cur.fetchall()
        return result
    #tables for Weapons are: Great_Swords, Long_Swords, Sword_Shields, Dual_Blades, Lances, Gun_Lances, Hammers, Hunting_Horns, Switch_Axes, Charge_Blades, Insect_Glaives                      
    def list_Weapons(self,table):
        self.cur.execute("SELECT * FROM "+table)
        result = self.cur.fetchall()
        return result

    def piece_detail(self,table,name):
        self.cur.execute("SELECT * FROM "+table+" WHERE name = '"+name+"'")
        result = self.cur.fetchall()
        return result

    #fields for the users table are: user_id, username, password, email
    def users_query(self,field,data):
        self.cur.execute("SELECT "+field+" FROM users WHERE "+field+" = '"+data+"'")
        result = self.cur.fetchall()
        return result

    def add_user(self,username,password,email):
        self.cur.execute("INSERT INTO users (username, password, email) VALUES ('"+username+"', '"+password+"', '"+email+"')")
        self.con.commit()
        return
    
    def validate_user(self, email):
        self.cur.execute("SELECT * FROM users WHERE email = '"+email+"'")
        result = self.cur.fetchall()
        return result
    
    #query to create multple different lists of decorations, which will be sent to the webpage
    def decoration_list(self):
        self.cur.execute("SELECT * FROM decorations WHERE size = 1")
        size1 = self.cur.fetchall()
        self.cur.execute("SELECT * FROM decorations WHERE size = 1 OR size = 2 ORDER BY size")
        size2 = self.cur.fetchall()
        self.cur.execute("SELECT * FROM decorations WHERE size = 1 OR size = 2 OR size = 3 ORDER BY size")
        size3 = self.cur.fetchall()
        self.cur.execute("SELECT * FROM decorations ORDER BY size")
        size4 = self.cur.fetchall()
        return size1, size2, size3, size4