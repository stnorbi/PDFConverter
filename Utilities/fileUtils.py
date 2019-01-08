import os

iconpath=os.path.dirname(__file__).replace("Utilities","icons")+"/"

def getIcon():
    icons={"barIcon":iconpath + "smallIcon.png",
           }
    return icons