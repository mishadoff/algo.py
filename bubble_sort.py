# Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)

array = [6, 2, 3, 1, 7, 9, 4, 8, 5, 0]

print "Unsorted %r" % array

for i in xrange(len(array) - 1):
    for j in xrange(len(array) - 1 - i):
        if array[j] > array[j+1]:
            (array[j], array[j+1]) = (array[j+1], array[j])

print "Sorted %r" % array
