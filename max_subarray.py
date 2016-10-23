# Max Subarray Problem
# Given array a[0, N] find subarray a[p, q]
# where sum a[p q] is max

import sys, random, time

a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

def generate_array(n):
    arr = []
    for i in xrange(n):
        arr.append(random.randrange(-100, 100))
    return arr

# Solution 1: Bruteforce, O(n^3) :|
def max_subarray_bruteforce(array):
    (idx, jdx, max_so_far) = (None, None, -sys.maxint+1)
    for i in xrange(len(array)):
        for j in xrange(i, len(array)):
            # Debug string print "(i, j)=(%r, %r)" % (i, j)
            current_sum = 0
            for k in xrange(i, j + 1):
                current_sum += array[k]
            if current_sum > max_so_far:
                (idx, jdx, max_so_far) = (i, j, current_sum)
    return (idx, jdx, max_so_far)

## TODO Can be optimized to calculate bruteforce sum base on previous sum computation

# Solution 2: Bruteforce #2, optimize max calculations O(n^2) :)
def max_subarray_bruteforce_opt(array):
    (idx, jdx, max_so_far) = (None, None, -sys.maxint+1)
    for i in xrange(len(array)):
        current_sum = 0
        for j in xrange(i, len(array)):
            # Debug string print "(i, j)=(%r, %r)" % (i, j)
            current_sum += array[j]
            if current_sum > max_so_far:
                (idx, jdx, max_so_far) = (i, j, current_sum)
    return (idx, jdx, max_so_far)

def max_subarray_dnc(array):
    return max_subarray_dnc_internal(array, 0, len(array))

def max_subarray_dnc_internal(array, low, high):
    if high - low <= 1:
        return (low, high, array[low])
    else:
        midpoint = (low + high) / 2
        left_sum = max_subarray_dnc_internal(array, low, midpoint)
        right_sum = max_subarray_dnc_internal(array, midpoint, high)
        crossing_sum = max_crossing_subarray_dnc(array, low, midpoint, high)
        # Sort by max sum
        sums = [left_sum, right_sum, crossing_sum]
        sums.sort(key = lambda x: x[2], reverse = True)
        return sums[0]

def max_crossing_subarray_dnc(array, low, midpoint, high):
    # Calculate max left sum and then max right sum
    left_sum = -sys.maxint + 1
    sum = 0
    for i in reversed(xrange(low, midpoint)):
        sum += array[i]
        if sum > left_sum:
            left_sum = sum
            left_idx = i

    right_sum = -sys.maxint + 1
    sum = 0
    for i in xrange(midpoint, high):
        sum += array[i]
        if sum > right_sum:
            right_sum = sum
            right_idx = i
    return (left_idx, right_idx, left_sum + right_sum)

# Array must contain at least one element
def max_subarray_kadane(array):
    (idx, jdx, max_so_far) = (0, 1, array[0])
    (start, max_ending_here) = (0, array[0])
    for i in xrange(1, len(array)):
        if array[i] > max_ending_here + array[i]:
            start = i
            max_ending_here = array[i]
        else:
            max_ending_here = max_ending_here + array[i]
        if max_ending_here > max_so_far:
            (idx, jdx, max_so_far) = (start, i, max_ending_here)
    return (idx, jdx, max_so_far)

print "Max Subarray Bruteforce O(n^3) at [%d, %d] = %d" % max_subarray_bruteforce(a)
print "Max Subarray Bruteforce O(n^2) at [%d, %d] = %d" % max_subarray_bruteforce_opt(a)
print "Max Subarray Divide and Conquer O(n log n) at [%d, %d] = %d" % max_subarray_dnc(a)
print "Max Subarray Kadane Algorithm O(n) at [%d, %d] = %d" % max_subarray_kadane(a)

def test(n):
    array = generate_array(n)
    print "Max Subarray Problem Test"
    print "Problem Size = %d " % n
    algorithms = [
#        ("Bruteforce O(n^3)", lambda n : max_subarray_bruteforce(n)),
        ("Bruteforce O(n^2)", lambda n : max_subarray_bruteforce_opt(n)),
        ("Divide & Conquer O(n log n)", lambda n : max_subarray_dnc(n)),
        ("Kadane's Algorithm O(n)", lambda n : max_subarray_kadane(n))
    ]
    for e in algorithms:
        (title, fun) = e
        print "Running [%s]..." % title
        before = time.time()
        (i, j, result) = fun(array)
        after = time.time()
        print "Algorithm [%s] result is array [%d, %d] with sum %d took %0.2f seconds" % (
            title, i, j, result, after - before)
