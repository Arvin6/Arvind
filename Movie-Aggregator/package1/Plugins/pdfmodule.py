'''
Created on Mar 4, 2017
PDF Module
@author: Arvind
'''
from reportlab.pdfgen import canvas
from package1.formatfactory import formatfactory
from reportlab.lib.pagesizes import letter

class pdfwrite(formatfactory):
    '''
    Save as pdf.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def _write(self,details,saveloc):
            can=canvas.Canvas(saveloc+"/Movie.pdf",pagesize=letter)                                 
            can.drawString(100,750,"Name: "+details['name'])
            can.drawString(100,700,"Lead actor: "+details['act'])
            can.drawString(100,650,"Language: "+details['language'])
            can.drawString(100,600,"Run time: "+details['time'])
            can.drawString(100,550,"Genre: "+details['genre'])
            can.save()
                
                
if __name__ == '__main__':
    '''For testing'''
    d= pdfwrite()
    det={'genre': 'Action', 'act': 'Hugh Jackman', 'name': 'Logan', 'language': 'Eng', 'time': '128 min'}
    save='G://Eclipse workspace/Movie-Aggregator/package1/Result'
    d._write(det,save)        