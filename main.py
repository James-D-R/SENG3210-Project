'''
Authors: James Remer, Brendan Vandevoorde
Last Updated: 4/27/20
Description: 
    Contains routes for non-authentication related pages. Sets up needed database connections for 
    *Utilizes the example from https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
'''

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .database import Database
from .calculate_skills import skillTotal, addSkills, setTotal
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    dbPy = Database("armor")
    result1 = dbPy.list_armor("head")
    result2 = dbPy.list_armor("chest")
    result3 = dbPy.list_armor("arms")
    result4 = dbPy.list_armor("waist")
    result5 = dbPy.list_armor("legs")
    result6 = dbPy.list_armor("skills")
    result7 = dbPy.list_armor("charms")

    #check if a user is logged in using flask login method
    x = current_user.is_authenticated
    #print(x)
    if x == True:
        message = "Welcome, " + current_user.name
        return render_template("selectArmors.htm",head = result1,chest = result2,arm = result3,waist = result4,leg = result5,skill = result6,
        charm = result7, confirmation = message)

    return render_template("selectArmors.htm",head = result1,chest = result2,arm = result3,waist = result4,leg = result5,skill = result6,
    charm = result7)

@main.route('/',methods=['POST'])
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

    #Specify dbPy and query tables for dropdown boxes
    dbPy = Database("armor")
    result1 = dbPy.list_armor("head")
    result2 = dbPy.list_armor("chest")
    result3 = dbPy.list_armor("arms")
    result4 = dbPy.list_armor("waist")
    result5 = dbPy.list_armor("legs")
    result6 = dbPy.list_armor("skills")
    result7 = dbPy.list_armor("charms")
    #Select specified armor piece from each table
    details1 = dbPy.piece_detail("head",headName)
    details2 = dbPy.piece_detail("chest",chestName)
    details3 = dbPy.piece_detail("arms",armName)
    details4 = dbPy.piece_detail("waist",waistName)
    details5 = dbPy.piece_detail("legs",legName)
    details6 = dbPy.piece_detail("charms",charmName)
    skillLevels = dbPy.piece_detail("skills",skillName)

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
        head1skills = dbPy.piece_detail("decorations",headslot1)
        head2skills = dbPy.piece_detail("decorations",headslot2)
        head3skills = dbPy.piece_detail("decorations",headslot3)
    if chestslot1 != 'None':
        chest1skills = dbPy.piece_detail("decorations",chestslot1)
        chest2skills = dbPy.piece_detail("decorations",chestslot2)
        chest3skills = dbPy.piece_detail("decorations",chestslot3)
    if armslot1 != 'None':
        arm1skills = dbPy.piece_detail("decorations",armslot1)
        arm2skills = dbPy.piece_detail("decorations",armslot2)
        arm3skills = dbPy.piece_detail("decorations",armslot3)
    if waistslot1 != 'None':
        waist1skills = dbPy.piece_detail("decorations",waistslot1)
        waist2skills = dbPy.piece_detail("decorations",waistslot2)
        waist3skills = dbPy.piece_detail("decorations",waistslot3)
    if legslot1 != 'None':
        leg1skills = dbPy.piece_detail("decorations",legslot1)
        leg2skills = dbPy.piece_detail("decorations",legslot2)
        leg3skills = dbPy.piece_detail("decorations",legslot3)
    if weaponslot1 != 'None':
        wep1skills = dbPy.piece_detail("decorations",weaponslot1)
    if weaponslot2 != 'None':
        wep2skills = dbPy.piece_detail("decorations",weaponslot2)
    if weaponslot3 != 'None':
        wep3skills = dbPy.piece_detail("decorations",weaponslot3)

    #Put the queried decoration information in a list, so setTotal() can loop through them easier
    slotinfo = [head1skills,head2skills,head3skills,chest1skills,chest2skills,chest3skills,arm1skills,arm2skills,arm3skills,waist1skills,waist2skills,waist3skills,leg1skills,leg2skills,leg3skills,wep1skills,wep2skills,wep3skills]

    #Calculate skill totals
    skillnames,skillnumbers = setTotal(details1,details2,details3,details4,details5,details6,slotinfo)

    #Get all possible decorations
    size1, size2, size3, size4 = dbPy.decoration_list()

    #Check if the user is still logged in
    message = "Please Login or Signup"
    x = current_user.is_authenticated
    if x == True:
        message = "Welcome, " + current_user.name
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
        wepslot1skills = wep1skills, wepslot2skills = wep2skills, wepslot3skills = wep3skills,
        confirmation = message)

    #Render template without welcome message if user is not logged in
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


#Individual pages for specific types of armor and weapons
#Head pieces table
@main.route('/head-pieces')
def showHeadPieces():
    dbPy = Database("armor")
    pieces = dbPy.list_armor("head")
    return render_template('headArmor.htm',result = pieces)

#Chest pieces table
@main.route('/chest-pieces')
def showChestPieces():
    dbPy = Database("armor")
    pieces = dbPy.list_armor("chest")
    return render_template('chestArmor.htm',result = pieces)

#Arm pieces table
@main.route('/arm-pieces')
def showArmPieces():
    dbPy = Database("armor")
    pieces = dbPy.list_armor("arms")
    return render_template('armArmor.htm',result = pieces)

#Waist pieces table
@main.route('/waist-pieces')
def showWaistPieces():
    dbPy = Database("armor")
    pieces = dbPy.list_armor("waist")
    return render_template('waistArmor.htm',result = pieces)

#Leg pieces table
@main.route('/leg-pieces')
def showLegPieces():
    dbPy = Database("armor")
    pieces = dbPy.list_armor("legs")
    return render_template('legArmor.htm',result = pieces)

#Charms table
@main.route('/charms')
def showCharms():
    dbPy = Database("armor")
    charms = dbPy.list_armor("charms")
    return render_template('charms.htm',result = charms)

#Decorations table
@main.route('/decorations')
def showDecorations():
    dbPy = Database("armor")
    decorations = dbPy.list_armor("decorations")
    return render_template('decorations.htm',result = decorations)

#Great Sword table
@main.route('/Great-Swords')
def showGreatSwords():
    dbPy = Database("Weapons")
    pieces = dbPy.list_Weapons("Great_Swords")
    return render_template('Weapon-Great-Sword.htm',result = pieces)

@main.route('/Great-Swords',methods=['POST'])
def GSDamage():

    TrueDamage = request.form.get('TD')

    #print("True Damage is: " + TrueDamage)

    Sharpness = request.form.get('Sharp')

    #print("Sharpness Color is: " + Sharpness)

    AttackValue = request.form.get('AV')

    #print("Attack Value is: " + AttackValue)

    MonsterArmor = request.form.get('MA')

    #print("Monster Armor is: " + MonsterArmor)

    if Sharpness == "Red":

        Sharpness = 0.5

    elif Sharpness == "Orange":

        Sharpness = 0.75

    elif Sharpness == "Yellow":

        Sharpness = 1

    elif Sharpness == "Green":

        Sharpness = 1.05

    elif Sharpness == "Blue":

        Sharpness = 1.2

    elif Sharpness == "White":

        Sharpness = 1.32

    elif Sharpness == "Purple":

        Sharpness = 1.39

    CalculatedDamage = round(int(TrueDamage)*Sharpness*(int(AttackValue)/100)*(int(MonsterArmor)/100))

    print("Calculated Damage: ", CalculatedDamage)

    dbPy = Database("Weapons")

    pieces = dbPy.list_Weapons("Great_Swords")

    return render_template('Weapon-Great-Sword.htm',result = pieces,DR = CalculatedDamage)

#Sword & Shield table
@main.route('/Sword-Shields')
def showSwordShields():
    dbPy = Database("Weapons")
    pieces = dbPy.list_Weapons("Sword_Shields")
    return render_template('Weapon-Sword-Shield.htm',result = pieces)

#Dual Blades table
@main.route('/Dual-Blades')
def showDualBlades():
    dbPy = Database("Weapons")
    pieces = dbPy.list_Weapons("Dual_Blades")
    return render_template('Weapon-Dual-Blade.htm',result = pieces)

#Long Sword table
@main.route('/Long-Swords')
def showLongSwords():
    dbPy = Database("Weapons")
    pieces = dbPy.list_Weapons("Long_Swords")
    return render_template('Weapon-Long-Sword.htm',result = pieces)

#Hammer table
@main.route('/Hammers')
def showHammers():
    dbPy = Database("Weapons")
    pieces = dbPy.list_Weapons("Hammers")
    return render_template('Weapon-Hammer.htm',result = pieces)

#Hunting Horn table
@main.route('/Hunting-Horns')
def showHuntingHorns():
    dbPy = Database("Weapons")
    pieces = dbPy.list_Weapons("Hunting_Horns")
    return render_template('Weapon-Hunting-Horn.htm',result = pieces)

#Lance table
@main.route('/Lances')
def showLances():
    dbPy = Database("Weapons")
    pieces = dbPy.list_Weapons("Lances")
    return render_template('Weapon-Lance.htm',result = pieces)

#Gun Lance table
@main.route('/Gun-Lances')
def showGunLances():
    dbPy = Database("Weapons")
    pieces = dbPy.list_Weapons("Gun_Lances")
    return render_template('Weapon-Gun-Lance.htm',result = pieces)

#Switch Axe table
@main.route('/Switch-Axes')
def showSwitchAxes():
    dbPy = Database("Weapons")
    pieces = dbPy.list_Weapons("Switch_Axes")
    return render_template('Weapon-Switch-Axe.htm',result = pieces)

#Charge Blade table
@main.route('/Charge-Blades')
def showChargeBlades():
    dbPy = Database("Weapons")
    pieces = dbPy.list_Weapons("Charge_Blades")
    return render_template('Weapon-Charge-Blade.htm',result = pieces)

#Insect Glaive table
@main.route('/Insect-Glaives')
def showInsectGlaives():
    dbPy = Database("Weapons")
    pieces = dbPy.list_Weapons("Insect_Glaives")
    return render_template('Weapon-Insect-Glaive.htm',result = pieces)