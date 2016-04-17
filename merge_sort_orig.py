def merge(R_list, L_list):
    output = len(R_list + L_list) * [0]
    index_r, index_l = 0, 0
    i=0

    while index_r < len(R_list) and index_l < len(L_list):
        
        #assignment
        curr_l = L_list[index_l]
        curr_r = R_list[index_r]
        
        #comparison
        if curr_r > curr_l:
            output[i] = curr_l
            index_l += 1
        else:
            output[i] = curr_r
            index_r += 1
        i += 1

    while index_r < len(R_list):
        i += 1
        output[i] = R_list[index_r]
        index_r += 1

    while index_l < len(L_list):
        i += 1
        output[i] = L_list[index_l]
        index_l += 1

    return output

def merge_sort(unsorted_list):

    if len(unsorted_list) < 2:
        return unsorted_list

    #divide
    mid = len(unsorted_list) // 2

    R = unsorted_list[mid:]
    L = unsorted_list[:mid]

    #conquer
    R_sorted = merge_sort(R)
    L_sorted = merge_sort(L)

    return merge(R_sorted, L_sorted)

if __name__ == '__main__':
    print merge_sort(range(10)[::-1])