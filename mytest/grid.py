import os
from random import randint

class Grid(object):
    def __init__(self):
        self.grid_size = 10
        self.position = {
            'x': 0,
            'y': 0,
        }
        self.treasure_position = {
            'x': randint(0, self.grid_size - 1),
            'y': randint(0, self.grid_size - 1),
        }

    def print_grid(self):
        self.grid = [["-" for i in range(self.grid_size)] for i in range(self.grid_size)]
        self.grid[self.treasure_position['y']][self.treasure_position['x']] = 'X'
        self.grid[self.position['y']][self.position['x']] = 'o'
        for row in self.grid:
            for e in row:
                print e,
            print

    def print_position(self, message):
        os.system('clear')
        treasure_found = self.position['x'] == self.treasure_position['x'] and self.position['y'] == self.treasure_position['y']
        print '[%d, %d] %s' % (self.position['x'], self.position['y'], message),
        if not treasure_found:
            print 'no treasure here...'
        else:
            print
        self.print_grid()
        return treasure_found

    def move_up(self):
        str_pos = 'moved up'
        if(self.position['y'] == 0):
            str_pos = 'already at the top!'
        else:
            self.position['y'] -= 1
        return self.print_position(str_pos)

    def move_down(self):
        str_pos = 'moved down'
        if(self.position['y'] == self.grid_size -1):
            str_pos = 'already at the bottom!'
        else:
            self.position['y'] += 1
        return self.print_position(str_pos)

    def move_right(self):
        str_pos = 'moved right'
        if(self.position['x'] == self.grid_size -1):
            str_pos = 'already at the right!'
        else:
            self.position['x'] += 1
        return self.print_position(str_pos)

    def move_left(self):
        str_pos = 'moved left'
        if(self.position['x'] == 0):
            str_pos = 'already at the left!'
        else:
            self.position['x'] -= 1
        return self.print_position(str_pos)

    def move(self, direction):
        if direction == 'w':
            return self.move_up()
        elif direction == 'a':
            return self.move_left()
        elif direction == 's':
            return self.move_down()
        elif direction == 'd':
            return self.move_right()
        else:
            return False
