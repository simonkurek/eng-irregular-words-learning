import json

with open('a2-words.min.json') as json_file:
    a2 = json.load(json_file)

with open('b1-words.min.json') as json_file:
    b1 = json.load(json_file)

with open('b2-words.min.json') as json_file:
    b2 = json.load(json_file)

with open('c1-words.min.json') as json_file:
    c1 = json.load(json_file)

with open('c2-words.min.json') as json_file:
    c2 = json.load(json_file)

final = []
final.append(a2)
final.append(b1)
final.append(b2)
final.append(c1)
final.append(c2)

with open('all-words.json', 'w') as outfile:
    json.dump(final, indent=3, fp=outfile)

with open('all-words.min.json', 'w') as outfile:
    json.dump(final, fp=outfile)