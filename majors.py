def mathMajorsSet():
    mathList = []
    with open('math.txt', 'r') as f:
        for line in f:
            if "_" not in line:
                mathList.append(line.strip())
    mathSet = set(mathList)
    return mathSet
mathSet = mathMajorsSet()

def csMajorsSet():
    csList = []
    with open('cs.txt', 'r') as f:
        for line in f:
            if "_" not in line:
                csList.append(line.strip())
    csSet = set(csList)
    return csSet
csSet = csMajorsSet()
print("CS and Math Double Majors: ", csSet.intersection(mathSet))
print("CS or Math Majors: ", csSet.union(mathSet))
print("CS Majors: ", csSet)

def grades():
    freshman = set()
    sophomore = set()
    junior = set()
    senior = set()
    with open('studentYear.txt', 'r') as f:
        for line in f:
            if "1" in line:
                freshman.add(line.strip()[2:])
            elif "2" in line:
                sophomore.add(line.strip()[2:])
            elif "3" in line:
                junior.add(line.strip()[2:])
            elif "4" in line:
                senior.add(line.strip()[2:])
    return freshman, sophomore, junior, senior
freshman, sophomore, junior, senior = grades()
print("Sophmore CS Majors: ", sophomore.intersection(csSet))
print("Freshman not in CS or Math: ", freshman.difference(csSet).difference(mathSet))
print("Senior Math and CS Majors: ", senior.intersection(csSet).intersection(mathSet))