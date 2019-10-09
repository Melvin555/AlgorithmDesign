def run(tup):
    gotcha = array = []
    point = 0
    for i in range(len(tup)):
        if i==0:
            array = tup[0]
            gotcha.append(array[0])
        elif i>0:
            array = tup[i]
            if array[point]<array[point+1]:
                gotcha.append(array[point])
            elif array[point+1]<array[point]:
                gotcha.append(array[point+1])
                point+=1
            elif array[point-1]<array[point]:
                gotcha.append(array[point-1])
                point-=1
    return gotcha

n = input("Please input the number of level: ")
array = tup = []
i=j=0
for i in range(int(n+1)):
    for k in range(j):
        val = input("The value of level "+str(i)+" : ")
        array.append(val)
    j+=1
    tup.append(array)
    array = []
del tup[0]

runresult = run(tup)
print
print "The track is: ",runresult
result = sum(runresult)
print
print "The result is: ",result