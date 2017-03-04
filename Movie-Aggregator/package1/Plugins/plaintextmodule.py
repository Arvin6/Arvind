'''
Created on Mar 4, 2017
Plaintext module.
@author: Arvind
'''
from package1.formatfactory import formatfactory

class plaintextwrite(formatfactory):
    '''
    Save as txt file
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def _write(self,details,saveloc):
        file_mov= open(saveloc+"/Movie.txt","w")
        file_mov.write("Name of the movie: "+details['name'])
        file_mov.write("\nRun time:\t "+details['time'])
        file_mov.write("\nLead actor:\t "+details['act'])
        file_mov.write("\nLanguage:\t "+details['language'])
        file_mov.write("\nGenre:\t\t "+details['genre'])
        file_mov.close()
        

if __name__ == '__main__':
    det={'genre': 'Action', 'act': 'Hugh Jackman', 'name': 'Logan', 'language': 'English', 'time': '128 min'}
    d = plaintextwrite()
    save='G://Eclipse workspace/Movie-Aggregator/package1/Result'
    d._write(det,save)