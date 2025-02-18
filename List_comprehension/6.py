import pandas as pd
names = ["Alice, Bob,      Charlie"]
spplit = names[0].split(",")
spplit2 = [x.strip() for x in spplit]
print(spplit)
print(spplit2)

result = "_ ".join(names)
print(result)

result2 = " ".join(spplit2)
print(result2)

