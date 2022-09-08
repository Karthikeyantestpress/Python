import re 

# Pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
# Output=re.search(Pattern,'XI')
# print(Output)

New_Pattern ='^T.'
Output2 =re.search(New_Pattern,'Test press')
print(Output2)