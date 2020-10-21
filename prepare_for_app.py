import json
from WordEntity import WordEntity

with open('all-words.json') as json_file:
    data = json.load(json_file)

all_words = []
    
for category in range(len(data)):
    for word in data[category]:
        first_form = word['first_form']
        second_form = word['second_form']
        third_form = word['third_form']
        polish_translation = word['polish_translation']
        level = word['level']
        all_words.append(WordEntity(first_form, second_form, third_form, polish_translation, level))

with open('words.json', 'w') as outfile:
    json.dump([ob.__dict__ for ob in all_words], indent=3, fp=outfile)

with open('words.min.json', 'w') as outfile:
    json.dump([ob.__dict__ for ob in all_words], fp=outfile)