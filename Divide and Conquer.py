##Melvin H. 17129122

def maxi(a,b):
    if a>b:
        return a
    else:
        return b
        
def mini(a,b):
    if a<b:
        return a
    else:
        return b

c = []
def divAndConq(array):
    if len(array)>1:
        
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        
        divAndConq(left)            
        divAndConq(right)
        #print left,'|', right
  
        a = left+right
        b = sum(a)
        leftsum = sum(left)
        d = mini(leftsum,b)
        c.append(d)
        #print c
        return c
        
array = []
n = input("Please input the number of values: ")
for l in range(int(n)):
    m = input("The value is: ")
    array.append(int(m))

r = divAndConq(array)
h = max(r)

print()
print("The result is :", h + 1)