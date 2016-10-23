# Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

array = [1, 2, 3, 6, 7, 9, 11]
elem_to_find = 6

# Returns index if found or None
def binary_search(p, q):
    # print "Call p=%r q=%r" % (p, q)
    if q - p == 1:
        if array[p] == elem_to_find:
            return p
        else:
            return None
    else:
        mid_point = (p + q) / 2
        if elem_to_find < array[mid_point]:
            return binary_search(p, mid_point)
        else:
            return binary_search(mid_point, q)
        
idx = binary_search(0, len(array))

if idx == None:
    print "Element %r not found" % elem_to_find
else:
    print "Element %r found at index %r" % (elem_to_find, idx)

