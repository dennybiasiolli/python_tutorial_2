from sys import argv

if len(argv) == 0:
    print 'len(argv) == 0'
elif len(argv) == 1:
    print 'len(argv) == 1'
elif len(argv) == 2:
    print 'len(argv) == 2'
else:
    print 'len(argv) > 2'
