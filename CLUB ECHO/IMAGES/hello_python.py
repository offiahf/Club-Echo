# This program prints off a sequence of "pseudorandom" numbers.  If you pick
# a different starting value, then you will get a different sequence of numbers.

number = 3

number_max = 101
a = 29
b = 47

for i in range(0, 10):
    print(number)
    number = (number * a + b) % number_max
    
print(number)
