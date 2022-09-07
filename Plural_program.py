'''Regular Expression program 
   '''

import re
def Plurals(Noun):
    if re.search('[sxz]$',Noun):
        return re.sub('$','es',Noun)
    elif re.search('[^aeioudgpktr]h$',Noun):
        return re.sub('$','es',Noun)
    elif re.search('[^aeiou]y$',Noun):
        return re.sub('$','ies',Noun)
    else :
        return Noun + 'S'

print(Plurals("fax"))
print(Plurals('Coach'))
print(Plurals('vacancy'))