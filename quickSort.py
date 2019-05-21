def quickSort(array):
    '''快速排序.

    运用分而治之思想,每趟将待排序的数据元素分割成两个部分,其中一部分的所有数据都比
    基准值小,另外一部分的所有数据都比基准值大

    Args:
        array: 给定待排序的数据元素.

    Returns:
        Forexample:
        print(selectionSort(test_list))
        #[-7, 1, 3.4, 5, 9, 12, 36]

    Raises:
        IOError: .
    '''    
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        lessNumber = [i for i in array[1:] if i <= pivot]
        moreNumber = [i for i in array[1:] if i > pivot]
        return quickSort(lessNumber)+[pivot]+quickSort(moreNumber)

test_list = [1, 36, 5, 12, -7, 3.4, 9]

print(quickSort(test_list))
