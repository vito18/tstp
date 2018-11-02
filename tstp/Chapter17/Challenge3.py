import re

#abc = "[abcdefghijklmnopqrstuvwxyz]oo"
text = "The ghost that says boo haunts the loo"
m = re.findall(".oo", text, re.IGNORECASE)
print(m)

