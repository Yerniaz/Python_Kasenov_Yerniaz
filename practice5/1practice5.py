import re
text = input()
list = re.findall("[e]\w+", text)
print(list)
