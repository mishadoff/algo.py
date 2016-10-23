# Selection Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)

array = [1, 8, 2, 3, 5, 4, 7, 0, 9, 6]

print "Unsorted: %r" % array

for i in xrange(len(array) - 1):
    (idx, min_so_far) = (i, array[i])
    for j in xrange(i, len(array)):
        if array[j] < min_so_far:
            (idx, min_so_far) = (j, array[j])
    (array[i], array[idx]) = (array[idx], array[i]) # Swap

print "Sorted: %r" % array
