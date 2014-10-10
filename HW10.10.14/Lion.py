class Lion:
    def __init__(self, state):
        self. state = state

    def antilopa(self, antilopa):
        if antilopa == 'antilopa':
            if self. state == 'full':
                print('Lion sleep')
                self. state = 'hungry'
            else:
                print('Lion eat')
                self. state = 'full'
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

Lion = Lion('hungry')
Lion .hunter('hunter')

