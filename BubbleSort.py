# The task is to complete bubble function which is used to implement Bubble Sort!

# Input Format:
# First line of the input denotes the number of test cases 'T'. 
# First line of the test case is the size of array and second line consists of array elements.

# Output Format:
# For each testcase, in a new line, print the sorted array.

# Your Task:
# This is a function problem. You only need to complete the function bubble that sorts the array. Printing is done automatically by the driver code.

# Constraints:
# 1 <=T<= 100
# 1 <=N<= 103
# 1 <=arr[i]<= 103

T = int(input("Please insert the nummber of test case: "))
book = []
for test in range(T):
    n = int(input("Please input the size of array: "))
    arr =  input("Please insert the array: ")
    l = list(map(int,arr.split(' ')))
    book.append(l)

def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j+1]<l[j]:
                temp = l[j+1]
                l[j+1] = l[j]
                l[j] = temp
    return

print()
print("The sorted version of the arrays are: ")
for test in range(len(book)):
    bubble_sort(book[test])
    print(book[test])

