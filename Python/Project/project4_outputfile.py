
class OutputFile:
    def __init__(self):
        self.FileIsOpen = False
    
    def Open(self,filename):
        if self.FileIsOpen:
            print('File %s is already open!\nMust close file before reopening it!'%self.FileName)
            return False
        else:
            self.FileName = filename
            self.FileIsOpen = True
            print('Opening file "%s"!'%filename)
            return True
            
            
    def Close(self):
        if not self.FileIsOpen:
            print('File is not open!\nMust open file before closing it!')
            return
        else:
            self.FileIsOpen = False
            print('Closing file "%s"!'%self.FileName)
        
        
    def Write(self,outstring):
        print(outstring,end='')
        
