# pool = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
#         80,82,84,86,88,90,92,94,96,98,100]


# def Binary_Search(arr, num):
#     high = len(arr) -1
#     low = 0

#     while low <=high:
#         midp = low + (high - low) //2
#         midp_value= arr[midp]

#         if midp_value == num:
#             return True
#         elif midp_value > num:
#             high = midp - 1
#         else: #midp_value < num:
#             low = midp + 1
#     return False

# print(Binary_Search(pool, 54))





#the code mentioned above is good too. but the one below is better i guess
from sys import stdin
def binarySearch(arr, n, x) :
    #Your code goes here
    start = 0
    end = n-1
    mid = start      #---> initially
    while start <= end:
        mid = (start+end)//2
        if arr[mid] > x:
            end = mid-1
        elif arr[mid] < x:
            start = mid+1
        elif arr[mid] == x:
            return mid
    return -1

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

#main
arr, n = takeInput()
t = int(stdin.readline().strip())
while t > 0 :  
    x = int(input().strip())    
    print(binarySearch(arr, n, x))
    t -= 1
