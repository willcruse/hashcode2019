import random

fileName = r'inputs/c.txt'

first = True
verticals = []
allPics = []
i = 0

for line in open(fileName):
    if first:
        first = False
    else:
        line = line.rstrip().split()
        if line[0] == 'V':
            verticals.append((i, {line[i] for i in range(2, len(line))}))
        else:
            allPics.append((i, {line[i] for i in range(2, len(line))}))
        i += 1


for uiop in range(50):
    random.seed(uiop)
    vertUse = [False] * len(verticals)
    horiComb = []
    totalTags = 0
    for abc in range(2):
        if abc == 0:
            startRand = random.randint(0, len(verticals)-1)
            end = len(verticals)
        else:
            end = startRand
            startRand = 0
        for i in range(startRand, end):
            if not vertUse[i]:
                vertUse[i] = True
                maxJoined = 0
                maxJoinedDict = {}
                maxIndex = 0
                index1 = verticals[i][0]
                for i2 in range(len(verticals)):
                    if i != i2:
                        if not vertUse[i2]:
                            theDict = verticals[i][1].union(verticals[i2][1])
                            if len(theDict) > maxJoined:
                                maxJoined = len(theDict)
                                maxJoinedDict = theDict
                                maxIndex = i2
                                index2 = verticals[i2][0]
                vertUse[maxIndex] = True
                horiComb.append((index1, index2, maxJoinedDict))
                totalTags += maxJoined
        newWrite = False
        fileName = r'./outputs/horizontalsC.txt'
        f = open(fileName)
        for qwer in f:
            if int(qwer.rstrip()) <= totalTags:
                newWrite = True
            break
        print(totalTags)
        if newWrite:
            writeFile = open(r'./outputs/horizontalsC.txt', "w+")
            writeFile.write(str(totalTags) + '\n')
            for x in horiComb:
                for i in range(len(x)):
                    if i != 2:
                        writeFile.write(str(x[i]) + " ")
                    else:
                        for a in x[2]:
                            writeFile.write(a + " ")
                writeFile.write('\n')
            writeFile.close()
        f.close()