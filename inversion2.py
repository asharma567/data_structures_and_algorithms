def merge_sort(unsorted_list, total_size, inver_ctr):
    if total_size == 1: 
        return None


    size1 = total_size / 2
    size2 = size1 - total_size
    merge_sort(unsorted_list, size1, inver_ctr)
    merge_sort(unsorted_list + size1, size2, inver_ctr)
    merge(unsorted_list, size1, size2, inver_ctr)
    pass

def merge(Arr, size1, size2, inver_ctr):
    temp_buffer = (size1 + size2) * [0]

    index_i = 0
    index_j = 0

    while index_i + index_j < size1 + size2:
        
        if (index_i < size1 and Arr[index_i] <= Arr[size1 + size2]) \
            or (index_i < size1 and index_j >= size2):
            index_i += 1
            temp_buffer[size1 + size2] = Arr[index_i]
        
        if (index_j < size2 and Arr[size1 + index_j] < Arr[index_i]) \
            or (index_2 < size2 and index_i >= size1):
            index_j += 1
            temp_buffer[index_i + index_j] = Arr[size1 + index_j]
            inver_ctr += size1 - ptr1


if __name__ =='__main__':
    t1 = [0, 1, 0, 2, 3, 4]
    t2 = [2, 4, 1, 3, 5]
    ctr = [0]
    
    merge_sort(t1, len(t1), ctr)
