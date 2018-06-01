import re
def main():
    file = open("code.txt" , 'r')
    lines = file.readlines()
    file.close()
    count =0
    mainPath =[]
    trueBranch=[]
    falseBranh[]
    for  line in lines:
        print(line)
         
def constructType(line):
       
    regexr = r'[^\S]?((def)|(if)|(elif)|(while)|(for))[\s]|(else[\s]*:)'

    match = re.search(regexr, line)
    if not match:
        return 0
    elif match.group(2):
        return 1
    elif match.group(3):
        return 2
    elif match.group(4):
        return 3
    elif match.group(7):
        return 4
    elif match.group(5):
        return 5
    elif match.group(6):
        return 6
    else:
        return None
def isStatement():
    count+=1
    mainPath.append(count)
    break;
def insideConditional(line):
    match = re.search(r'[^\S]?if[\s]', line)
        if match != None:
        #inside if true path
            count +=1 
            mainPath.append(count)
        type =constructType(line)
        checkType(type)
        else:
            return
        
def isStatement():
    count+=1
    ma
    
def checkType(type):
    if type == 0:
        isStatement()
        break
     elif type == 2:
        isIf()
        break
     elif type == 3:
        isElif()
        break
     elif type ==4:
        isElse()
        break
     elif type == 5:
        isWhile()
        break
     elif type == 6:
        isFor()
        break
main()            
