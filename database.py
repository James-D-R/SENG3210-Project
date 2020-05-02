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

    def save_set(self,user_id,set_name,head,chest,arm,waist,leg,charm,weapon_size1,weapon_size2,weapon_size3,
    weapon_slot1,weapon_slot2,weapon_slot3,head_slot1,head_slot2,head_slot3,chest_slot1,chest_slot2,chest_slot3,
    arm_slot1, arm_slot2, arm_slot3, waist_slot1, waist_slot2, waist_slot3, leg_slot1, leg_slot2, leg_slot3):

        query = ("INSERT INTO saved_sets (user_id, set_name, head, chest, arm, waist, leg, charm, weapon_size1, weapon_size2,"
        +"weapon_size3, weapon_slot1, weapon_slot2, weapon_slot3, head_slot1, head_slot2, head_slot3, chest_slot1, chest_slot2,"
        +"chest_slot3, arm_slot1, arm_slot2, arm_slot3, waist_slot1, waist_slot2, waist_slot3, leg_slot1, leg_slot2, leg_slot3) "
        +"VALUES ("
        +"'"+str(user_id)+"', '"+set_name+"', '"+head+"', '"+chest+"', '"+arm+"', '"+waist+"', '"+leg+"', '"+charm
        +"', '"+weapon_size1+"', '"+weapon_size2+"', '"+weapon_size3+"', '"+weapon_slot1+"', '"+weapon_slot2+"', '"+weapon_slot3
        +"', '"+head_slot1+"', '"+head_slot2+"', '"+head_slot3+"', '"+chest_slot1+"', '"+chest_slot2+"', '"+chest_slot3
        +"', '"+arm_slot1+"', '"+arm_slot2+"', '"+arm_slot3+"', '"+waist_slot1+"', '"+waist_slot2+"', '"+waist_slot3
        +"', '"+leg_slot1+"', '"+leg_slot2+"', '"+leg_slot3+"')")

        self.cur.execute(query)
        self.con.commit()
        return

    def get_sets(self,user_id):
        self.cur.execute("SELECT set_id, set_name FROM saved_sets WHERE user_id = "+str(user_id))
        result = self.cur.fetchall()
        return result

    def load_set(self,set_id):
        self.cur.execute("SELECT * FROM saved_sets WHERE set_id = "+str(set_id))
        result = self.cur.fetchall()
        return result

'''
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
    '''
