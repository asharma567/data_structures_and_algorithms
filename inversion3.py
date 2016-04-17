import sys
from itertools import combinations
def SortCount(A):
   l = len(A)
   if l > 1:
      n = l//2
      C = A[:n]
      D = A[n:]
      C, c = SortCount(A[:n])
      D, d = SortCount(A[n:])
      B, b = MergeCount(C,D)
      return B, b+c+d
   else:
      return A, 0


def MergeCount(A,B):
   count = 0
   M = []
   while A and B:
      if A[0] <= B[0]: 
         M.append(A.pop(0)) 
      else: 
         count += len(A)
         M.append(B.pop(0)) 
   M  += A + B     
   return M, count 

if  __name__ == '__main__':
    
    #fix it to use arg_parse
    if len(sys.argv) > 1:
        file_name = sys.argv[1]

        with open(file_name) as f:
            
            # datatype to int
            index_list = [int(line.strip()) for line in f]
            
        print 'file read in..'
        print inversion_ctr_truth(index_list)
        ctr = [0]
        merge_sort(t1, ctr)
        print ctr
        
    else:
        #this effectively like saving it's like a global parameter 
        
        t1 = [0, 1, 5, 2, 3, 4]
        t2 = [2, 4, 1, 3, 5]
        n = range(15)[::-1]
        
        print 'n:', len(n), 'total number of inversions: ', len(list(combinations(n, 2)))
        print SortCount(n)
        
    
