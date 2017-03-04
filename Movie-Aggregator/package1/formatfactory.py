'''
Created on Mar 4, 2017
Base class for plugins.
@author: Arvind
'''
class formatfactory(object):
    '''
    This is the abstraction for dynamically assigning classes
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    def _write(self,somedict,savelocation):
        '''
        Write method for concrete classes
        '''
        raise NotImplementedError;
