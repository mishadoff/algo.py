# N-bit digits adder
# Space complexity: O(n)
# Time Complexity:  O(n)

digit1 = [1, 0, 0, 1, 0, 1, 0, 0, 0, 1]
digit2 = [1, 1, 1, 0, 0, 0, 1, 0, 1, 1]
result_digits = [0] * (len(digit1) + 1)

carry = 0
for i in xrange(len(digit1) - 1, -1, -1):
    bit1 = digit1[i]
    bit2 = digit2[i]
    result = bit1 + bit2 + carry
    if result > 1:
        (result_bit, carry) = (0, 1)
    else:
        (result_bit, carry) = (result, 0)
    result_digits[i + 1] = result_bit

result_digits[0] = carry

print "Result %r" % result_digits
