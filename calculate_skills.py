'''
    calculate_skills.py
    Authors: James Remer
    Last Updated: 3/5/20
    Description: (NOT COMPLETE) Function to take selected armor pieces and total up skills
'''
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
    if (skill2 != ""):
        y = skill2.split()
        points2 = y[-1]
        del y[-1]
        for word in y:
            name2 = name2 + word + " "
        name2 = name2.strip()

    print("name 1 =",name1,"/ points 1 =",points1)
    print("name 2 =",name2,"/ points 2 =",points2)

    return name1, points1, name2, points2


dict1 = [{"name":"head","skill1":"Weakness Exploit 2","skill2": "Attack Boost 3"}]
dict2 = [{"name":"chest","skill1":"Weakness Exploit 2","skill2": "Critical Eye 2"}]
dict3 = [{"name":"arms","skill1":"Critical Boost 1","skill2": ""}]
dict4 = [{"name":"waist","skill1":"Attack Boost 2","skill2": "Critical Eye 4"}]
dict5 = [{"name":"legs","skill1":"Handicraft 2","skill2": ""}]
dict6 = [{"name":"charm","skill1":"Defense Boost 3","skill2":""}]
#skillTotal(dict1)
