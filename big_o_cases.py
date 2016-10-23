import math, re

print "How much time is needed to run different algorithms depending on the problem size"
print "    (assuming 1 operation takes 1 microsecond)"

# f(n) runs in microseconds

# Functions we trying to test 
functions = [
    ["O(log n)",   lambda n: math.log(n, 2)],
    ["O(sqrt n)",  lambda n: math.sqrt(n)],
    ["O(n)",       lambda n: n],
    ["O(n log n)", lambda n: math.log(n, 2) * n],
    ["O(n^2)",     lambda n: n * n],
    ["O(n^3)",     lambda n: n * n * n],
    ["O(2^n)",     lambda n: math.pow(2, n)],
    ["O(n!)",      lambda n: reduce(lambda x, y : x * y, range(1, n + 1))]
]

# Only integers allowed as a base and power
problem_sizes = ["1", "10", "10^2", "10^3", "10^6", "10^9", "10^12"]

fmt_string = "Algorithm {0} with problem size {1} takes {2}"

def parse_square(s):
    nums = map(lambda x: int(x), re.split("\\^", s))
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] ** nums[1]

def calculate_time(fn, size):
    micros_time = fn(size)
    return "{0} microseconds".format(micros_time)
    
for fn in functions:
    fn_title = fn[0]
    fn_impl  = fn[1]
    for ps in problem_sizes:
        real_size = parse_square(ps)
        print fmt_string.format(fn_title, ps, calculate_time(fn_impl, real_size))
    
print map(lambda x: int(x), re.split("\\^", "10^2"))
