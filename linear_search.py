# Linear Search
# Time Complexity: O(n) 
# Space Complexity: O(1)

array = [1, 5, 4, 2, 7, 2, 6, 3, 9, 8, 6]

elem_to_find = 6
elem_found = None
for i in xrange(len(array)):
    if array[i] == elem_to_find:
        print "Element %s found at index %s" % (elem_to_find, i)
        elem_found = elem_to_find
        break

if elem_found == None:
    print "Element %s not found" % elem_to_find
