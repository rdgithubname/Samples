'''
Very much stripped down sample class. Nothing more than a dictionary, but why not. Can be extended if needed.
'''

class Sample:
    def __init__(self, name, DASname=None):
        self.name       = name
        self.DASname    = DASname
