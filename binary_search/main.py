
def binary_search(list, item):
    low = 0
    height = len(list)-1
    
    while low <= height:
        mid = (low + height)/2
        mid_v = list[mid]
        if item == mid_v:
            return mid
        
        if mid_v > item:
            height = mid-1
        else:
            low = mid + 1


    return None

test_list = [1, 3, 7, 8, 56, 78, 100]

print binary_search(test_list, 56)




