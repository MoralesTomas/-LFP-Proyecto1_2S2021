import re
a = "#FFF"
if re.search("^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$",a):
    print("Lo encontro")