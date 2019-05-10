def binarySearch(list, item):
    '''二分查找.

    运用二分法查找给定有序数组中某元素的位置(如果它存在的话)

    Args:
        list: 给定有序数组.
        item: 给定元素.

    Returns:
        如果该元素存在则返回索引,不存在则返回-1.
        Forexample:

        print(binarySearch(test_list,6)) 
        #3
        print(binarySearch(test_list,10)) 
        #-1

    Raises:
        IOError: .
    '''
    low = 0
    high = len(list)-1

    while low <= high:
        mid = int((low+high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid + 1
    return -1


test_list = [1, 3, 5, 6, 7, 8, 9]

print(binarySearch(test_list, 6))

print(binarySearch(test_list, 10))
