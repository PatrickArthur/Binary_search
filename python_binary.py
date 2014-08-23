def search(array,val):
    low = 0
    high = len(array) - 1
    while(low <= high):
        mid = (low + high)/2
        midval = array[mid]

        if midval < val:
            low = mid + 1
        elif midval > val:
            high = mid - 1
        else:
            print mid
            return mid
    print -1
    return -1

search([1,2,3],3)
