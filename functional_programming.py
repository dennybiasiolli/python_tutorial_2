from itertools import product, permutations

def my_func(f, arg):
    return f(arg)

print(my_func(lambda x: 2 * x * x, 5))


# named function
def polynomial(x):
    return x**2 + 5 * x + 4
print(polynomial(-4))

# lambda
print((lambda x: x**2 + 5 * x + 4)(-4))

double = lambda x: x * 2
print(double(7))


def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
print(list(map(add_five, nums)))
print(list(map(lambda x: x + 5, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))
print(list(map(lambda x: x / 2, filter(lambda x: x % 2 == 0, nums))))


# generators
def countdown():
    i = 50
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i),
print('')
print(list(countdown()))


# decorators
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap


@decor
def print_text():
    print("Hello world!")

print_text()


# recursion
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))


# sets
nums = {9, 1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.add(-8)
nums.add(-8)
nums.add(-5)
nums.add(0)
nums.remove(3)
print(nums)


first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
# The union operator | combines two sets to form a new one containing
# items in either.
print(first | second)
# The intersection operator & gets items only in both.
print(first & second)
# The difference operator - gets items in the first set but not in the second.
print(first - second)
print(second - first)
# The symmetric difference operator ^ gets items in either set, but not both.
print(first ^ second)


# itertools
blood_groups = ['0', 'A', 'B', 'AB']
rh = ['+', '-']
print(list(product(blood_groups, rh)))
print(len(list(permutations("123456"))))


def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
		
print(power(2, 3))
