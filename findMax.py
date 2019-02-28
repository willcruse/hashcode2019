import multiprocessing
fileName = r'./outputs/horizontalsA.txt'
f = open(fileName)
for qwer in f:
    if int(qwer.rstrip()) <= totalTags:
        newWrite = True
    break
print(totalTags)