import re

phrase = "Dad, mom, Jasper, Alyce, Seymour. That's our fam!"

pphrase = re.split("[,.?!']", phrase)

print(pphrase)