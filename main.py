# in the json file CRTL + R
# ^([A-Za-z]*)$
# Replaced by "$1",
# At the top and the end, you gotta place [ and ] respectively to make it a list

import json
import os
import string


names = json.loads(open('names.json').read())
for name in names:
    tmp = name + " Lewis"
    print(tmp)
