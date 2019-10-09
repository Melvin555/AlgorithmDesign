c = input("Input the number of capacity: ")
n = input("Input the number of items: ")
weight = []
value = []
for i in range(int(n)):
    wi = input("input the item "+str(i+1)+" weight to be put into sack: ")
    weight.append(int(wi))
    vi = input("input the value respectively: ")
    value.append(int(vi))

K = [[0 for x in range(c+1)] for x in range(n+1)]

for i in range(n+1):
    for j in range(c+1):
        if i==0 or j==0:
            K[i][j] = 0
            print("slash 1 "+str(i)+str(j))
        elif weight[i-1] <= j:
            K[i][j] = max(value[i-1] + K[i-1][j-weight[i-1]],  K[i-1][j])
            print("slash 2 "+str(i)+str(j))
            print i-1,i-1,j-weight[i-1]
        else:
            K[i][j] = K[i-1][j]
            print("slash 3 "+str(i)+str(j))

print
print("The max value to be put inside: "+str(K[n][c]))

# val = [5.0, 4.0, 1.0]
# wt = [4, 3, 2]
# W = 6
# n = len(val)