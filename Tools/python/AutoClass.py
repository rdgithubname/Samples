''' class that stores all arguments as attributes
'''

class AutoClass:
    def __init__( self, samples):
        for s in samples:
            setattr( self, s.name, s )
