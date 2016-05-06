io_sono_lista = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
io_sono_dictionary = {1: 1, 2: 23, 3: 32, }
io_sono_tupla = (1, 2, 3,)

print(io_sono_lista)
print(io_sono_dictionary)
print(io_sono_tupla)

print(len(io_sono_lista))
print(len(io_sono_dictionary))
print(len(io_sono_tupla))

print(io_sono_lista[3:5])
print(io_sono_lista[:4])
print(io_sono_lista[4:])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

print(range(0, 100, 9))
print(range(0, 100)[::-9])
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])

cubes = [i**3 for i in range(5)]
print(cubes)

sqs = [i**2 for i in range(1, 20)]
sqsArr = []
for index, num in enumerate(sqs):
    sqsArr.append((index + 1, num,))
print(sqsArr)

sqs2 = [(index + 1, n**2,) for index, n in enumerate(range(1, 20)) if n % 2 == 0]
print sqs2
