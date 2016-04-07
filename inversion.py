import numpy as np
import sys
from itertools import combinations

def inversion_ctr_truth(Arr):
    output = []
    for idx, item_1 in enumerate(Arr):
        for item_2 in Arr[idx + 1:]:
            if item_1 > item_2: 
                output.append((item_1, item_2))
            
    return len(output)


def merge(L_Arr, R_Arr):
    inversion_ctr = 0
    output_list = []
    
    i = 0
    j = 0
    
    
    while len(L_Arr) > i and len(R_Arr) > j:

        #ctr
        if L_Arr[i] < R_Arr[j]:
            output_list.append(L_Arr[i])
            i += 1
        else:
            output_list.append(R_Arr[j])
            inversion_ctr += len(L_Arr[i:])
            j += 1

    output_list.extend(L_Arr[i:])
    output_list.extend(R_Arr[j:])

    return output_list, inversion_ctr


def merge_sort(some_list):
    
    if len(some_list) < 2:
        return some_list, 0

    #divide
    mid_point = len(some_list) // 2
    R_Arr = some_list[:mid_point]
    L_Arr = some_list[mid_point:]

    #sort
    R_Arr, r_ctr = merge_sort(R_Arr)
    L_Arr, l_ctr = merge_sort(L_Arr)

    #merge
    lis, split_ctr = merge(R_Arr, L_Arr)
    
    return lis, r_ctr + l_ctr + split_ctr

if  __name__ == '__main__':
    
    #fix it to use arg_parse
    if len(sys.argv) > 1:
        file_name = sys.argv[1]

        with open(file_name) as f:
            
            # datatype to int
            index_list = [int(line.strip()) for line in f]
            
        print 'file read in..'
        # print inversion_ctr_truth(index_list)
        print merge_sort(index_list)

        
    else:
        #this effectively like saving it's like a global parameter 
        ctr = [0]
        t1 = [0, 1, 5, 2, 3, 4]
        t2 = [2, 4, 1, 3, 5]
        n = range(10)[::-1]
        
        print 'n:', len(n), 'total number of inversions: ', len(list(combinations(n, 2)))
        _, inversions = merge_sort(n)
        print inversions    

        print inversion_ctr_truth(n)

    
