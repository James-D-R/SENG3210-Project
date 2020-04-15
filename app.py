'''
app.py
Authors: James Remer, Brendan VandeVoorde
Creation Date: 2/10/20
Last Updated: 4/12/20
Description: 
    Main python file ran when starting the app. Contains routes and rendering instructions for html pages. 
    Sets up database connections.
'''
from flask import Flask, render_template, request
from calculate_skills import skillTotal, addSkills, setTotal
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
    result7 = db.list_armor("charms")
    return render_template("selectArmors.htm",head = result1,chest = result2,arm = result3,waist = result4,leg = result5,skill = result6,
    charm = result7)

@app.route('/',methods=['POST'])
def calculateSkills():
    #Get current value of each armor dropdown box
    headName = request.form.get('headName')
    chestName = request.form.get('chestName')
    armName = request.form.get('armName')
    waistName = request.form.get('waistName')
    legName = request.form.get('legName')
    skillName = request.form.get('skillName')
    charmName = request.form.get('charmName')

    #Get current value of each decoration dropdown box
    headslot1 = request.form.get('headslot1')
    headslot2 = request.form.get('headslot2')
    headslot3 = request.form.get('headslot3')

    chestslot1 = request.form.get('chestslot1')
    chestslot2 = request.form.get('chestslot2')
    chestslot3 = request.form.get('chestslot3')

    armslot1 = request.form.get('armslot1')
    armslot2 = request.form.get('armslot2')
    armslot3 = request.form.get('armslot3')

    waistslot1 = request.form.get('waistslot1')
    waistslot2 = request.form.get('waistslot2')
    waistslot3 = request.form.get('waistslot3')

    legslot1 = request.form.get('legslot1')
    legslot2 = request.form.get('legslot2')
    legslot3 = request.form.get('legslot3')

    weaponsize1 = request.form.get('weaponslotsize1')
    weaponsize2 = request.form.get('weaponslotsize2')
    weaponsize3 = request.form.get('weaponslotsize3')

    weaponslot1 = request.form.get('weaponslot1')
    weaponslot2 = request.form.get('weaponslot2')
    weaponslot3 = request.form.get('weaponslot3')

    #Escape any single quotes
    headName = headName.replace("'","''")
    chestName = chestName.replace("'","''")
    armName = armName.replace("'","''")
    waistName = waistName.replace("'","''")
    legName = legName.replace("'","''")
    skillName = skillName.replace("'","''")
    charmName = charmName.replace("'","''")
    headslot1 = str(headslot1).replace("'","''")
    headslot2 = str(headslot2).replace("'","''")
    headslot3 = str(headslot3).replace("'","''")
    chestslot1 = str(chestslot1).replace("'","''")
    chestslot2 = str(chestslot2).replace("'","''")
    chestslot3 = str(chestslot3).replace("'","''")
    armslot1 = str(armslot1).replace("'","''")
    armslot2 = str(armslot2).replace("'","''")
    armslot3 = str(armslot3).replace("'","''")
    waistslot1 = str(waistslot1).replace("'","''")
    waistslot2 = str(waistslot2).replace("'","''")
    waistslot3 = str(waistslot3).replace("'","''")
    legslot1 = str(legslot1).replace("'","''")
    legslot2 = str(legslot2).replace("'","''")
    legslot3 = str(legslot3).replace("'","''")
    weaponslot1 = str(weaponslot1).replace("'","''")
    weaponslot2 = str(weaponslot2).replace("'","''")
    weaponslot3 = str(weaponslot3).replace("'","''")

    #Specify db and query tables for dropdown boxes
    db = Database("armor")
    result1 = db.list_armor("head")
    result2 = db.list_armor("chest")
    result3 = db.list_armor("arms")
    result4 = db.list_armor("waist")
    result5 = db.list_armor("legs")
    result6 = db.list_armor("skills")
    result7 = db.list_armor("charms")
    #Select specified armor piece from each table
    details1 = db.piece_detail("head",headName)
    details2 = db.piece_detail("chest",chestName)
    details3 = db.piece_detail("arms",armName)
    details4 = db.piece_detail("waist",waistName)
    details5 = db.piece_detail("legs",legName)
    details6 = db.piece_detail("charms",charmName)
    skillLevels = db.piece_detail("skills",skillName)

    #Placeholder
    head1skills = ''
    head2skills = ''
    head3skills = ''
    chest1skills = ''
    chest2skills = ''
    chest3skills = ''
    arm1skills = ''
    arm2skills = ''
    arm3skills = ''
    waist1skills = ''
    waist2skills = ''
    waist3skills = ''
    leg1skills = ''
    leg2skills = ''
    leg3skills = ''
    wep1skills = ''
    wep2skills = ''
    wep3skills = ''

    #Get decoration data
    if headslot1 != 'None':
        head1skills = db.piece_detail("decorations",headslot1)
        head2skills = db.piece_detail("decorations",headslot2)
        head3skills = db.piece_detail("decorations",headslot3)
    if chestslot1 != 'None':
        chest1skills = db.piece_detail("decorations",chestslot1)
        chest2skills = db.piece_detail("decorations",chestslot2)
        chest3skills = db.piece_detail("decorations",chestslot3)
    if armslot1 != 'None':
        arm1skills = db.piece_detail("decorations",armslot1)
        arm2skills = db.piece_detail("decorations",armslot2)
        arm3skills = db.piece_detail("decorations",armslot3)
    if waistslot1 != 'None':
        waist1skills = db.piece_detail("decorations",waistslot1)
        waist2skills = db.piece_detail("decorations",waistslot2)
        waist3skills = db.piece_detail("decorations",waistslot3)
    if legslot1 != 'None':
        leg1skills = db.piece_detail("decorations",legslot1)
        leg2skills = db.piece_detail("decorations",legslot2)
        leg3skills = db.piece_detail("decorations",legslot3)
    if weaponslot1 != 'None':
        wep1skills = db.piece_detail("decorations",weaponslot1)
    if weaponslot2 != 'None':
        wep2skills = db.piece_detail("decorations",weaponslot2)
    if weaponslot3 != 'None':
        wep3skills = db.piece_detail("decorations",weaponslot3)

    #Put the queried decoration information in a list, so setTotal() can loop through them easier
    slotinfo = [head1skills,head2skills,head3skills,chest1skills,chest2skills,chest3skills,arm1skills,arm2skills,arm3skills,waist1skills,waist2skills,waist3skills,leg1skills,leg2skills,leg3skills,wep1skills,wep2skills,wep3skills]

    #Calculate skill totals
    skillnames,skillnumbers = setTotal(details1,details2,details3,details4,details5,details6,slotinfo)

    #Get all possible decorations
    size1, size2, size3, size4 = db.decoration_list()

    return render_template("selectArmors.htm",head = result1,chest = result2,arm = result3,waist = result4,leg = result5,charm = result7,
    headpiece = details1,chestpiece = details2,armpiece = details3,waistpiece = details4,legpiece = details5,charmpiece = details6,
    skill = result6,skillLv = skillLevels,skillnames = skillnames, skilltotals = skillnumbers,
    level4deco = size4, level3deco = size3, level2deco = size2, level1deco = size1,
    headslot1skills = head1skills, headslot2skills = head2skills, headslot3skills = head3skills,
    chestslot1skills = chest1skills, chestslot2skills = chest2skills, chestslot3skills = chest3skills,
    armslot1skills = arm1skills, armslot2skills = arm2skills, armslot3skills = arm3skills,
    waistslot1skills = waist1skills, waistslot2skills = waist2skills, waistslot3skills = waist3skills,
    legslot1skills = leg1skills, legslot2skills = leg2skills, legslot3skills = leg3skills,
    wepslotsize1 = weaponsize1, wepslotsize2 = weaponsize2, wepslotsize3 = weaponsize3,
    wepslot1skills = wep1skills, wepslot2skills = wep2skills, wepslot3skills = wep3skills)

#
@app.route('/showSignUp')
def showSignUpPage():
    return render_template("signup.htm")

@app.route('/signUp')
def signUp():
    return

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