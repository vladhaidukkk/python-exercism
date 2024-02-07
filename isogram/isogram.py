import re

def is_isogram(string):
    scrubbed = re.sub("[^a-zA-Z]", "", string).lower()
    return len(set(scrubbed)) == len(scrubbed)
