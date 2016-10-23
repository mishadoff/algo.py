# List all inversions in array
#  if i < j and A[i] > A[j], pair (i, j) called inversion
# Time Complexity: O(n^2)
# Space Complexity: O(1)

#array = [2, 3, 8, 6, 1]
array = [7, 6, 5, 4, 3, 2, 1]

inversions_list = []
for i in xrange(len(array)):
    for j in xrange(i + 1, len(array)):
        if array[i] > array[j]:
            inversions_list.append((i, j))

for inv in inversions_list:
    (i, j) = inv
    print "Inversion: array[%d]=%d > array[%d]=%d" % (i, array[i], j, array[j])

print "Total number of inversions: %d" % len(inversions_list)    
