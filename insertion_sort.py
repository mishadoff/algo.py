# Insertion Sort
# Time complexity: O(n^2)
# Space complexity: O(1)
# Loop invariant:
#   at the start of each iteration i
#   array[0, i - 1] contains sorted array of elements

array = [5, 2, 4, 6, 1, 3, 9, 8, 2, 7, 3]

print "Unsorted: %r" % array

# Go over all elements in array, starting from second
for i in xrange(1, len(array)):
    key = array[i]
    # Insert key into sorted sequence array[0, i - 1]
    j = i - 1
    while j >= 0 and array[j] > key: # Changing > to < switch sorting order
        array[j + 1] = array[j]
        j = j - 1
    array[j + 1] = key

print "Sorted: %r" % array
