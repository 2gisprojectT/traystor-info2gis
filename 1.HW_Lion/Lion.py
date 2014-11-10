class Lion:
    def __init__(self, state):
        if(state == 'full' or state == 'hungry'):
            self. state = state
        else:
            print('Error in input parameters')

    def antilopa(self):
        if self. state == 'full':
            self. state = 'hungry'
            return 'Lion sleep'
        else:
            return 'Lion eat'

    def hunter(self):
        if self. state == 'full':
            self. state = 'hungry'
            return 'Run Lion, RUN!'
        else:
            return 'Run Lion, RUN!'

    def tree(self):
        if self. state == 'full':
            self. state = 'hungry'
            return 'Lion see on tree'
        else:
            return 'Lion sleep'

lionState = Lion('full')
print(lionState.hunter())
