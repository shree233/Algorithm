def searchSmallest(array):
    smallest = array[0]
    smallestIndex = 0
    for i in range(1, len(array)):
        if smallest > array[i]:
            smallest = array[i]
            smallestIndex = i
    return smallestIndex

def selectionSort(array):
    '''选择排序.

    每一次从待排序的数据元素中选出最小,放到新序列里

    Args:
        array: 给定待排序的数据元素.

    Returns:
        Forexample:
        print(selectionSort(test_list))
        #[-7, 1, 3.4, 5, 9, 12, 36]

    Raises:
        IOError: .
    '''
    newArray = []
    for i in range(len(array)):
        smallest = searchSmallest(array)
        newArray.append(array.pop(smallest))
    return newArray


test_list = [1, 36, 5, 12, -7, 3.4, 9]

print(selectionSort(test_list))
