# use boolean
a = 97
b = 55
# test expression
if a < b:
    # statement to be run
    print(b)

test_expression = 2
if test_expression:
    # statement(s) to be run
    print("hello")


a = 93
b = 27
if a >= b:
    print(a)

# with conditional
a = 24
b = 44
if a <= 0:
    print(a)
print(b)


# What are else

a = 93
b = 27
if a >= b:
    print(a)
else:
    print(b)

# Work with elif
a = 93
b = 27
if a >= b:
    print("a is greater than or equal to b")
elif a == b:
    print("a is equal to b")

# Combine if, elif, and else

a = 93
b = 27
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# Work with nested conditional logic
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print("a is greater than b and b is greater than c")
    else:
        print("a is greater than b and less than c")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

# EXERCISE - WRITE 'if' statements *************************

object_size = 10
if object_size > 5:
    print('We need to keep an eye on this object')
else:
    print('Object poses no threat.')


# What are 'and' and 'or' operators
a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

#The and operator

a = 23
b = 34
if a == 34 and b == 34:
    print(a + b)

# EXERCISE - USE AND AND OR OPERATORS
object_size = 10
proximity = 9000
if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')
