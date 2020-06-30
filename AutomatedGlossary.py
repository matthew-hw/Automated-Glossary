import sys, os

glossaryLocation = '/'

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

# Check if word already appended
try :
    file = open(glossaryLocation + 'AutomatedGlossary.txt')
    for word in file:
        if sys.argv[1].lower() == word.rstrip():
            notify('Word already existed','😅')
            bypass = True
            sys.exit()
except OSError:
    notify('First time?😘','Creating a new Automated Glossary in ' + glossaryLocation)
    os.system('sleep 4')

# Append Word
file = open(glossaryLocation + 'AutomatedGlossary.txt','a')
file.write(sys.argv[1].lower()+'\n')
notify(sys.argv[1].capitalize() + '🥳','Successfully add to Automated Glossary')
