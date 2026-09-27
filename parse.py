import re

phrase = "Dad, mom, Jasper, Alyce, Seymour. That's our fam!"

pphrase = re.split("[,.?!']", phrase)

print(pphrase)
print("\034[34mKIDDO\034[0m")   