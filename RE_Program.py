import re

Strings = '''Madhesh   kumar'''


# 86-731-3797
# 2344-765-5323
# 678453.345.9878

# Karthikeyan
# Karthik@gmail.com
# Karthik@testpress.com
# Kart@yahoo.in
# Testpressofficial@tp.com

# Mr.tpress
# Mr tp
# Mrs.thg

# Karthik Testpress
# Madeesh Testpress
# Newempl Testpress
# '''

Pattern=re.compile(r'^M.*h$')
Printing =Pattern.finditer(Strings)

for Match in Printing:
    print (Match)