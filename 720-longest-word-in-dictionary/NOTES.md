max_word = ""
for word in words:
boolean = True
for i in range(len(word)+1):
prefix = word[:i]
if prefix not in seen:
boolean = False
break
if boolean:
if len(max_word) < len(word):
max_word = word
return max_word