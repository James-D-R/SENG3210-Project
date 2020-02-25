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

    if (skill2 != None):
        y = skill2.split()
        points2 = y[-1]
        del y[-1]

    print(skill1)
    print(skill2)

    return


list1 = ['name','rare','skill1','skill2']
