import re

def isValidURL(url):
    pattern = ("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

       
    if(re.search(pattern,url)):
        return True
    else:
        return False