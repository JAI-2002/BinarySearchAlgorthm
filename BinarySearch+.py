pool = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
        80,82,84,86,88,90,92,94,96,98,100]


def Binary_Search(arr, num):
    high = len(arr) -1
    low = 0

    while low <=high:
        midp = low + (high - low) //2
        midp_value= arr[midp]

        if midp_value == num:
            return True
        elif midp_value > num:
            high = midp - 1
        else: #midp_value < num:
            low = midp + 1
    return False

print(Binary_Search(pool, 54))