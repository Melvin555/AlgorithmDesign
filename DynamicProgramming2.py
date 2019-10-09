n = input("Input the box N dimension: ")
dimension = int(n)**2
array = []
i=j=0
for i in range(int(n)):
    array.append([])
    for j in range(int(n)):
        m = input("Input value of "+str(i+1)+str(j+1)+" coordinate: ")
        array[i].append(int(m))

take = []
take.append(array[0][0])
px = py = 0
while (array[px][py]!=array[n-1][n-1]):
    if (px==n-1):
        take.append(array[px][py+1])
        py+=1
    elif (py==n-1):
        take.append(array[px+1][py])
        px+=1
    elif (array[px+1][py])<(array[px][py+1]):
        take.append((array[px+1][py]))
        px+=1
    elif (array[px][py+1])<(array[px+1][py]):
        take.append((array[px][py+1]))
        py+=1

print
print "The track is: ",take
result = sum(take)
print
print "The sum result of track is: ", result