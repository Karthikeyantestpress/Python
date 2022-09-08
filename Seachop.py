import re

Detail = "My name is KARTHIK and my age is 20"
result = re.search(r"(\b[A-Z]+\b).+(\b\d+)", Detail)
print(result.groups())