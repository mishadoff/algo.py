# Fibonacci Sequence

fibs = [1, 1]
n = 10 # How many fibonacci numbers we need
for i in xrange(len(fibs), n):
    fibs.append(fibs[i - 1] + fibs[i - 2])

print "Fibonacci: %r" % fibs
