''' class that stores all arguments as attributes
'''

class AutoClass:
    def __init__( self, samples):
        for s in samples:
            setattr( self, s.name, s )

        names = [ s.name for s in samples ]
        for name in names:
            if names.count( name )>1:
                raise RuntimeError( "Sample name is not unique: %s", name )
