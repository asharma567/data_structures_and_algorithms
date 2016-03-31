import numpy as np
import sys

def merge(L_Arr, R_Arr, inversion_ctr):
    output_list = []
    
    i = 0
    j = 0
    
    while len(L_Arr) > i and len(R_Arr) > j:

        if L_Arr[i] < R_Arr[j]:
            output_list.append(L_Arr[i])
            i += 1
            inversion_ctr[0] += 1
        else:
            output_list.append(R_Arr[j])
            j += 1

        
    # change these to while loops
    output_list.extend(L_Arr[i:])
    output_list.extend(R_Arr[j:])

    return output_list


def merge_sort(some_list, inversion_ctr):
    
    if len(some_list) < 2:
        return some_list

    #divide
    mid_point = len(some_list) // 2
    R_Arr = some_list[:mid_point]
    L_Arr = some_list[mid_point:]

    #sort
    R_Arr = merge_sort(R_Arr, inversion_ctr)
    L_Arr = merge_sort(L_Arr, inversion_ctr)

    #merge
    lis = merge(R_Arr, L_Arr, inversion_ctr)
    
    return lis

if  __name__ == '__main__':
    
    #this effectively like saving it's like a global parameter 
    ctr = [0]
    
    #fix it to use arg_parse
    if len(sys.argv) > 1:
        file_name = sys.argv[1]

        with open(file_name) as f:
            index_list = [int(line.strip()) for line in f]
            
        print 'file read in..'

    merge_sort(index_list, ctr)
    print ctr
