# Custiom glossary saving location, default save to same folder
glossaryLocation = ''
    
import sys, os

if not glossaryLocation:
    glossaryLocation = os.path.realpath(__file__)[:20]

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
    
# Check if word already appended, if then Check if need to remove
try :
    file = open(glossaryLocation + 'AutomatedGlossary.txt','r+')
    for n,word in enumerate(file):
        if sys.argv[1].lower() == word.rstrip():
            try:
                sys.argv[2]
                word = '\n'
                notify('Removing ' + sys.argv[1].capitalize(),'😅')
                sys.exit()
            except:
                pass
            notify('Word already existed','😅')
            bypass = True
            sys.exit()
except OSError:
    notify('First time?😘','Creating a new Automated Glossary in ' + glossaryLocation)
    os.system('sleep 4')

# Append Word to file
file = open(glossaryLocation + 'AutomatedGlossary.txt','a')
file.write(sys.argv[1].lower()+'\n')
notify(sys.argv[1].capitalize() + '🥳','Successfully add to Automated Glossary')
