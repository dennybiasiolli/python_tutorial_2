print 'something'
# comment
string1 = 'string'
int1 = 12
float1 = 12.0
print 'string1 = %s' % string1
print 'int1 = %d' % int1
print 'float1 = %d' % float1
print 'string1 = %s, int1 = %d, float1 = %d' % (string1, int1, float1)
print 'string = %s' % 'ciao\tciao, ', 'raw = %r' % 'ciao\tciao'
print """Elenco numeri
- %02d
- %02d
- %02d
- %02d
""" % (10, 18, 5, 9)

# # inputs
# print "How old are you?",
# age = raw_input()
# # oppure
# age = raw_input("How old are you? ")

# argomenti da linea di comando
from sys import argv
print "%r" % argv

# files
txt = open('test.txt')
print txt.read()
txt.close()
txt = open('test.txt', 'w') # 'w'->'write', 'a'->'append'
txt.write('This is line 1\n')
txt.write('This is line 2\n')
txt.write('This is line 3\n')
txt.close()

#functions
# this one is like your scripts with argv
def args_array(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    return True
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    return True
# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1
    return True
# this one takes no arguments
def print_none():
    print "I got nothin'."
    return True
