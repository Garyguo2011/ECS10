
from htmloutputfile import *
import random

MyHTMLOutputFile = HTMLOutputFile()
if MyHTMLOutputFile.SetTitle(random.randint(1,100)):
    print('Error: SetTitle accepted non-string')
    exit(0)
    
if not MyHTMLOutputFile.SetTitle('My Title'):
    print('Error: SetTitle did not accept string')
    exit(0)
    
if MyHTMLOutputFile.AddHeading1(random.randint(1,100)):
    print('Error: AddHeading1 accepted non-string')
    exit(0)
    
if not MyHTMLOutputFile.AddHeading1('Heading 1'):
    print('Error: AddHeading1 did not accept string')
    exit(0)

if MyHTMLOutputFile.AddBold(['str',1.0,100]):
    print('Error: AddBold accepted invalid type')
    exit(0)

if not MyHTMLOutputFile.AddBold(100):
    print('Error: AddBold did not accept integer')
    exit(0)
    
if not MyHTMLOutputFile.AddBold(' Bold String '):
    print('Error: AddBold did not accept string')
    exit(0)
    
if not MyHTMLOutputFile.AddBold(2.0):
    print('Error: AddBold did not accept float')
    exit(0)

if MyHTMLOutputFile.AddHeading2(random.randint(1,100)):
    print('Error: AddHeading2 accepted non-string')
    exit(0)
    
if not MyHTMLOutputFile.AddHeading2('Heading 2'):
    print('Error: AddHeading2 did not accept string')
    exit(0)
    
if MyHTMLOutputFile.AddItalic(['str']):
    print('Error: AddItalic accepted invalid type')
    exit(0)

if not MyHTMLOutputFile.AddItalic(200):
    print('Error: AddItalic did not accept integer')
    exit(0)
    
if not MyHTMLOutputFile.AddItalic(' Italic String '):
    print('Error: AddItalic did not accept string')
    exit(0)
    
if not MyHTMLOutputFile.AddItalic(3.0):
    print('Error: AddItalic did not accept float')
    exit(0)

if MyHTMLOutputFile.AddHeading3(random.randint(1,100)):
    print('Error: AddHeading3 accepted non-string')
    exit(0)
    
if not MyHTMLOutputFile.AddHeading3('Heading 3'):
    print('Error: AddHeading3 did not accept string')
    exit(0)

if MyHTMLOutputFile.AddText(['str','anotherstr']):
    print('Error: AddText accepted invalid type')
    exit(0)

if not MyHTMLOutputFile.AddText(250):
    print('Error: AddText did not accept integer')
    exit(0)
    
if not MyHTMLOutputFile.AddText(' Plain String '):
    print('Error: AddText did not accept string')
    exit(0)
    
if not MyHTMLOutputFile.AddText(4.0):
    print('Error: AddText did not accept float')
    exit(0)



if MyHTMLOutputFile.AddTable('test'):
    print('Error: AddTable accepted non-list')
    exit(0)

MyTable = ['Cell 1','Cell 2', 'Cell 3']
if not MyHTMLOutputFile.AddTable(MyTable):
    print('Error: AddTable did not accept list')
    exit(0)

MyTable.pop(0)
MyTable.pop(0)
MyTable.pop(0)
MyTable.append(['Cell 1,1','Cell 1,2', 'Cell 1,3'])
MyTable.append(['Cell 2,1','Cell 2,2', 'Cell 2,3'])
MyTable.append(['Cell 3,1','Cell 3,2', 'Cell 3,3'])
if not MyHTMLOutputFile.AddTable(MyTable):
    print('Error: AddTable did not accept list')
    exit(0)

if not MyHTMLOutputFile.SetTitle('My Title 2'):
    print('Error: SetTitle did not accept string')
    exit(0)

if MyHTMLOutputFile.SaveToFile(random.randint(1,100)):
    print('Error: SaveToFile accepted non-string')
    exit(0)
    
if not MyHTMLOutputFile.SaveToFile('MyOutput.html'):
    print('Error: SaveToFile did not accept string')
    exit(0)
    


