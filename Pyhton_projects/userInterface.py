


def createdict(name):
    dict1= {}
    file=open(name,"r")
    j=-1
    for i in file.readline():
        list1=i.split(".")
        for part in list1:
            max = 0
            maxc = 0
            letter1 = part[0:1]
            letter2 = ""
            j += 1
            for pos in range(0,len(part)):
                if letter1 is part[pos:pos+1]:
                    max += 1
                    print(max)
                elif  letter2 is part[pos:pos+1]:
                    maxc+=1
                    letter2= part[pos:pos+1]
                if max < maxc:
                    letter1=letter2
                    max=maxc
                    maxc=0
                    letter2=""
                if letter2 and letter1 is not part[pos:pos+1]:
                    maxc=0
                    letter2=part[pos:pos+1]
            dict1.update({i:max})
    return dict1



dict2=createdict("word11.txt")
print(dict2)
