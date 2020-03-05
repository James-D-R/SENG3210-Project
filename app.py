'''
app.py
Authors: James Remer, Brendan VandeVoorde
Creation Date: 2/10/20
Last Updated: 3/4/20
Description: 
    Main python file ran when starting the app. Contains routes and rendering instructions for html pages. 
    Sets up database connections.
'''
from flask import Flask, render_template, request
from calculate_skills import skillTotal
import pymysql
import re

app = Flask(__name__)

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

    #class method to query DB table
    #tables are: head, chest, arms, waist, legs
    def list_armor(self,table):
        self.cur.execute("SELECT * FROM "+table)
        result = self.cur.fetchall()
        return result
    
    def list_Weapons(self,table):
        self.cur.execute("SELECT * FROM "+table)
        result = self.cur.fetchall()
        return result

    def piece_detail(self,table,name):
        self.cur.execute("SELECT * FROM "+table+" WHERE name = '"+name+"'")
        result = self.cur.fetchall()
        return result


#Pages
#Homepage
@app.route('/')
def main():
    db = Database("armor")
    result1 = db.list_armor("head")
    result2 = db.list_armor("chest")
    result3 = db.list_armor("arms")
    result4 = db.list_armor("waist")
    result5 = db.list_armor("legs")
    result6 = db.list_armor("skills")
    return render_template("selectArmors.htm",head = result1,chest = result2,arm = result3,waist = result4,leg = result5,skill = result6)

@app.route('/',methods=['POST'])
def showTables():
    #Get current value of each dropdown box
    headName = request.form.get('headName')
    chestName = request.form.get('chestName')
    armName = request.form.get('armName')
    waistName = request.form.get('waistName')
    legName = request.form.get('legName')
    skillName = request.form.get('skillName')

    #Escape any single quotes
    headName = headName.replace("'","''")
    chestName = chestName.replace("'","''")
    armName = armName.replace("'","''")
    waistName = waistName.replace("'","''")
    legName = legName.replace("'","''")
    skillName = skillName.replace("'","''")

    #Specify db and query tables for dropdown boxes
    db = Database("armor")
    result1 = db.list_armor("head")
    result2 = db.list_armor("chest")
    result3 = db.list_armor("arms")
    result4 = db.list_armor("waist")
    result5 = db.list_armor("legs")
    result6 = db.list_armor("skills")
    #Select specified armor piece from each table
    details1 = db.piece_detail("head",headName)
    details2 = db.piece_detail("chest",chestName)
    details3 = db.piece_detail("arms",armName)
    details4 = db.piece_detail("waist",waistName)
    details5 = db.piece_detail("legs",legName)

    skillLevels = db.piece_detail("skills",skillName)

    #skillTotal(details1)
    #print(details1)


    return render_template("selectArmors.htm",head = result1,chest = result2,arm = result3,waist = result4,leg = result5,
    headpiece = details1,chestpiece = details2,armpiece = details3,waistpiece = details4,legpiece = details5,skill = result6,
    skillLv = skillLevels)

#Head pieces table
@app.route('/head-pieces')
def showHeadPieces():
    db = Database("armor")
    pieces = db.list_armor("head")
    return render_template('headArmor.htm',result = pieces)

#Chest pieces table
@app.route('/chest-pieces')
def showChestPieces():
    db = Database("armor")
    pieces = db.list_armor("chest")
    return render_template('chestArmor.htm',result = pieces)

#Arm pieces table
@app.route('/arm-pieces')
def showArmPieces():
    db = Database("armor")
    pieces = db.list_armor("arms")
    return render_template('armArmor.htm',result = pieces)

#Waist pieces table
@app.route('/waist-pieces')
def showWaistPieces():
    db = Database("armor")
    pieces = db.list_armor("waist")
    return render_template('waistArmor.htm',result = pieces)

#Leg pieces table
@app.route('/leg-pieces')
def showLegPieces():
    db = Database("armor")
    pieces = db.list_armor("legs")
    return render_template('legArmor.htm',result = pieces)

#Charms table
@app.route('/charms')
def showCharms():
    db = Database("armor")
    charms = db.list_armor("charms")
    return render_template('charms.htm',result = charms)

#Decorations table
@app.route('/decorations')
def showDecorations():
    db = Database("armor")
    decorations = db.list_armor("decorations")
    return render_template('decorations.htm',result = decorations)

#Great Sword table
@app.route('/Great-Swords')
def showGreatSwords():
    db = Database("Weapons")
    pieces = db.list_Weapons("Great_Swords")
    return render_template('Weapon-Great-Sword.htm',result = pieces)

#Sword & Shield table
@app.route('/Sword-Shields')
def showSwordShields():
    db = Database("Weapons")
    pieces = db.list_Weapons("Sword_Shields")
    return render_template('Weapon-Sword-Shield.htm',result = pieces)

#Dual Blades table
@app.route('/Dual-Blades')
def showDualBlades():
    db = Database("Weapons")
    pieces = db.list_Weapons("Dual_Blades")
    return render_template('Weapon-Dual-Blade.htm',result = pieces)

#Long Sword table
@app.route('/Long-Swords')
def showLongSwords():
    db = Database("Weapons")
    pieces = db.list_Weapons("Long_Swords")
    return render_template('Weapon-Long-Sword.htm',result = pieces)

#Hammer table
@app.route('/Hammers')
def showHammers():
    db = Database("Weapons")
    pieces = db.list_Weapons("Hammers")
    return render_template('Weapon-Hammer.htm',result = pieces)

#Hunting Horn table
@app.route('/Hunting-Horns')
def showHuntingHorns():
    db = Database("Weapons")
    pieces = db.list_Weapons("Hunting_Horns")
    return render_template('Weapon-Hunting-Horn.htm',result = pieces)

#Lance table
@app.route('/Lances')
def showLances():
    db = Database("Weapons")
    pieces = db.list_Weapons("Lances")
    return render_template('Weapon-Lance.htm',result = pieces)

#Gun Lance table
@app.route('/Gun-Lances')
def showGunLances():
    db = Database("Weapons")
    pieces = db.list_Weapons("Gun_Lances")
    return render_template('Weapon-Gun-Lance.htm',result = pieces)

#Switch Axe table
@app.route('/Switch-Axes')
def showSwitchAxes():
    db = Database("Weapons")
    pieces = db.list_Weapons("Switch_Axes")
    return render_template('Weapon-Switch-Axe.htm',result = pieces)

#Charge Blade table
@app.route('/Charge-Blades')
def showChargeBlades():
    db = Database("Weapons")
    pieces = db.list_Weapons("Charge_Blades")
    return render_template('Weapon-Charge-Blade.htm',result = pieces)

#Insect Glaive table
@app.route('/Insect-Glaives')
def showInsectGlaives():
    db = Database("Weapons")
    pieces = db.list_Weapons("Insect_Glaives")
    return render_template('Weapon-Insect-Glaive.htm',result = pieces)

if __name__ == "__main__":
    app.run()