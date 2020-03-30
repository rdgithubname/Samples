''' class that stores all arguments as attributes
'''
        
import os
import subprocess
from multiprocessing import Pool

def copy( job ):
    source, target = job
    cmd = ["/usr/bin/rfcp",  source, target]
    dir = os.path.dirname( target )
    if not os.path.exists(dir):
        #try:
            os.makedirs(dir)
        #except:
        #    pass
            
    if not os.path.exists(target):
        print ( " ".join( cmd ) )
        subprocess.call(cmd)
    else:
        print( "Found %s. Skip.", target)

def echo( job ):
    source, target = job
    cmd = ["/usr/bin/xrdcp", source, target ]
    print (" ".join( cmd ))

## Logger
#import logging
#logger = logging.getLogger(__name__)

class AutoClass:
    def __init__( self, samples):
        for s in samples:
            setattr( self, s.name, s )

        self.__samples = samples

        names = [ s.name for s in samples ]
        for name in names:
            if names.count( name )>1:
                raise RuntimeError( "Sample name is not unique: %s", name )

    def __add__( self, other ):
        self.__samples += other.__samples
        self.__samples = list(set(self.__samples))
        return self

    def __iadd__( self, other ):
        self.__add__( other )

    def get_all( self ):
        return self.__samples

    def get_jobs( self, path = "/data/dpm/"):
        import os
        if not path.endswith('/'): path+='/'
        jobs = []
        for sample in self.__samples:
            for source in sample.files:
                _source = os.path.join( "/dpm/oeaw.ac.at/home/cms", ("".join( source.split('//')[2:])).lstrip('/') )
                _target = os.path.join( path, ("".join( source.split('//')[2:])).lstrip('/') )
                jobs.append( [_source, _target] )
        return jobs

    def copy_to_local( self, path = "/data/dpm/", n_processes = 4, do_it = False):
        jobs = self.get_jobs(path = path)
        self.copy_jobs( jobs, n_processes = n_processes, do_it = do_it)

    def copy_jobs( self, jobs, n_processes = 4, do_it = False):
        pool = Pool(processes = n_processes)
        if do_it:
            results = pool.map(copy, jobs)
        else:
            results = pool.map(echo, jobs)
        pool.close()
        pool.join()

