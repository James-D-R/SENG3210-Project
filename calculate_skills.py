'''
    calculate_skills.py
    Authors: James Remer
    Last Updated: 4/12/20
    Description: Functions which take armor pieces as input, then returns formatted skill totals 
'''

#Function to return skill name and number as seperate values
def skillTotal(piece):

    #Get skill name and number from dictionary
    skill1 = (piece[0])["skill1"]
    skill2 = (piece[0])["skill2"]

    #Split the string and get the point values
    x = skill1.split()
    points1 = x[-1]
    del x[-1]
    name1 = ""
    for word in x:
        name1 = name1 + word + " "
    name1 = name1.strip()

    name2 = ""
    points2 = ""
    if (skill2 == "None"):
        name2 = ""
        points2 = ""       
    elif (skill2 != ""):
        y = skill2.split()
        points2 = y[-1]
        del y[-1]
        for word in y:
            name2 = name2 + word + " "
        name2 = name2.strip()

    #print("name 1 =",name1,"/ points 1 =",points1)
    #print("name 2 =",name2,"/ points 2 =",points2)

    return name1, points1, name2, points2


#Updates lists with skill totals
def addSkills(skillnames,skillnumbers,name1,points1,name2,points2):
   
    checkskill1 = False
    checkskill2 = False
    for name in skillnames:
        if name1 == name:
            #if name is a match, then get the current position in the list
            index = skillnames.index(name)
            #get the corresponding number value in skillnumbers list
            number = skillnumbers[index]
            #update the list with the new value
            number = int(number) + int(points1)
            skillnumbers[index] = number

            #boolean value so that the skill name won't get added agian
            checkskill1 = True

        if name2 == name:
            #if name is a match, then get the current position in the list
            index = skillnames.index(name)
            #get the corresponding number value in skillnumbers list
            number = skillnumbers[index]
            #update the list with the new value
            number = int(number) + int(points2)
            skillnumbers[index] = number

            checkskill2 = True


    #Add the new skill if it isn't already in the list
    if checkskill1 == False:
        skillnames = skillnames + [name1]
        skillnumbers = skillnumbers + [int(points1)]

    if checkskill2 == False and name2 != "":
        skillnames = skillnames + [name2]
        skillnumbers = skillnumbers + [int(points2)]
    
    return skillnames, skillnumbers


#Take values returned from 'skillTotal' function and add up totals 
def setTotal(head,chest,arm,waist,leg,charm,slotinfo):

    skillnames = []
    skillnumbers = []
    name1,points1,name2,points2 = skillTotal(head)

    #HeadPiece
    skillnames = skillnames + [name1]
    skillnumbers = skillnumbers + [int(points1)]
    if name2 != "":
        skillnames = skillnames + [name2]
        skillnumbers = skillnumbers + [int(points2)]

    #ChestPiece
    name1,points1,name2,points2 = skillTotal(chest)
    skillnames,skillnumbers = addSkills(skillnames,skillnumbers,name1,points1,name2,points2)

    #ArmPiece
    name1,points1,name2,points2 = skillTotal(arm)
    skillnames,skillnumbers = addSkills(skillnames,skillnumbers,name1,points1,name2,points2)

    #WaistPiece
    name1,points1,name2,points2 = skillTotal(waist)
    skillnames,skillnumbers = addSkills(skillnames,skillnumbers,name1,points1,name2,points2)

    #LegPiece
    name1,points1,name2,points2 = skillTotal(leg)
    skillnames,skillnumbers = addSkills(skillnames,skillnumbers,name1,points1,name2,points2) 

    #Charm
    name1,points1,name2,points2 = skillTotal(charm)
    skillnames,skillnumbers = addSkills(skillnames,skillnumbers,name1,points1,name2,points2) 

    #Decorations
    #SQL will return an empty tuple if a query yeilds no results. Check each variable to ensure it isn't empty
    for query in slotinfo:
        if len(query) > 0:
            name1,points1,name2,points2 = skillTotal(query)
            skillnames,skillnumbers = addSkills(skillnames,skillnumbers,name1,points1,name2,points2) 
    
    return skillnames,skillnumbers


