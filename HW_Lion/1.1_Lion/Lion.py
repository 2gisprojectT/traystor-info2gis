class Lion:
    def __init__(self, state):
        if(state == 'full' or state == 'hungry'):
            self. state = state
        else:
            print('Error in input parameters')

    def antilopa(self, antilopa):
        if antilopa == 'antilopa':
            if self. state == 'full':
                print('Lion sleep')
                self. state = 'hungry'
            else:
                print('Lion eat')

    def hunter(self, hunter):
        if hunter == 'hunter':
            if self. state == 'full':
                print('Run Lion, RUN!')
                self. state = 'hungry'
            else:
                print('Run Lion, RUN!')

    def tree(self, tree):
        if tree == 'tree':
            if self. state == 'full':
                print('Lion see on tree')
                self. state = 'hungry'
            else:
                print('Lion sleep')

lion = Lion('hungry')
lion .antilopa('antilopa')