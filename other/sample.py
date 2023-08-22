import re

pattern = r'^(?=.*foo)(?=.*bar)'
text1 = "This is foo and that is bar."
text2 = "This is bar and that is foo."

if re.search(pattern, text1):
    print("text1 matches!")
if re.search(pattern, text1):
    print("text1 matches!")
