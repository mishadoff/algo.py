# Merge Sort
# Time Complexity: O(n log n)
# Space Complexity: O(n)
import sys

array = [1, 8, 2, 3, 5, 4, 7, 0, 9, 6]

# Apply merge sort for the [p, q) part of array
def merge_sort(array, p, q):
    # split array into two parts
    if q - p == 1:
        # Array contains one elment, therefore it is sorted
        return array
    else:
        mid_point = (q + p) / 2
        merge_sort(array, p, mid_point)
        merge_sort(array, mid_point, q)
        merge(array, p, mid_point, q)
    

# Procedure to merge two arrays array [p, q) and array [q, r)
def merge(array, p, q, r):
    # Create left and right array for merging
    # Size greater by one for sentinel elements
    larray = [None] * (q - p + 1)
    rarray = [None] * (r - q + 1)

    # Copy elements from original into left and right arrays
    for i in xrange(len(larray) - 1):
        larray[i] = array[p + i]
    for i in xrange(len(rarray) - 1):
        rarray[i] = array[q + i]

    # Set sentinels
    larray[len(larray) - 1] = sys.maxint
    rarray[len(rarray) - 1] = sys.maxint

    # Merge them by modifying original array
    lidx = 0
    ridx = 0
    for i in xrange(p, r):
        if larray[lidx] <= rarray[ridx]:
            array[i] = larray[lidx]
            lidx = lidx + 1
        else:
            array[i] = rarray[ridx]
            ridx = ridx + 1
    return array

print "Unsorted: %r" % array
merge_sort(array, 0, len(array))
print "Sorted: %r" % array
    
        
    
    
    
