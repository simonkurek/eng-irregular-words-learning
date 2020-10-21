from urllib.request import urlopen
from bs4 import BeautifulSoup
from Word_Enitity import Word_Enitity
import json

#html parsing
url = "https://www.ang.pl/gramatyka/czasowniki-verbs/czasowniki-nieregularne"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

#get table
tbody_index = html.find("<tbody>")
start_index = tbody_index + len("<tbody>")
end_index = html.find("</tbody>")
table = html[start_index:end_index]
words_preparse = soup.find_all("tr")

#lists
words_obj = []
words = []

#get needed data
for word_preparse in words_preparse:
    entries = word_preparse.find_all("td")
    word_enery = []
    for entry in entries:
        text = entry.string
        if text == None:
            try:
                text_sample = entry.find('a').next_sibling.string
                word_enery.append(entry['class'][1])
                if text_sample != None:
                    text = text_sample
            except:
                pass
        if text != None:
            text = text.split(', ')
            word_enery.append(text)
    words.append(word_enery)

#create objects from data
for i in range(len(words)):
    if len(words[i]) > 0:
        level = words[i][0]
        first_form = words[i][1]
        second_form = words[i][2]
        third_form = words[i][3]
        pol_trans = words[i][4]
        words_obj.append(Word_Enitity(first_form, second_form, third_form, pol_trans, level))

#group by level
a2 = []
b1 = []
b2 = []
c1 = []
c2 = []

for word in words_obj:
    if word.level == 'a2':
        a2.append(word)
    if word.level == 'b1':
        b1.append(word)
    if word.level == 'b2':
        b2.append(word)
    if word.level == 'c1':
        c1.append(word)
    if word.level == 'c2':
        c2.append(word)

#dumps lists to files
with open('a2-words.json', 'w') as outfile:
    json.dump([ob.__dict__ for ob in a2], indent=3, fp=outfile)

with open('a2-words.min.json', 'w') as outfile:
    json.dump([ob.__dict__ for ob in a2], fp=outfile)

with open('b1-words.json', 'w') as outfile:
    json.dump([ob.__dict__ for ob in b1], indent=3, fp=outfile)

with open('b1-words.min.json', 'w') as outfile:
    json.dump([ob.__dict__ for ob in b1], fp=outfile)

with open('b2-words.json', 'w') as outfile:
    json.dump([ob.__dict__ for ob in b2], indent=3, fp=outfile)

with open('b2-words.min.json', 'w') as outfile:
    json.dump([ob.__dict__ for ob in b2], fp=outfile)

with open('c1-words.json', 'w') as outfile:
    json.dump([ob.__dict__ for ob in c1], indent=3, fp=outfile)

with open('c1-words.min.json', 'w') as outfile:
    json.dump([ob.__dict__ for ob in c1], fp=outfile)

with open('c2-words.json', 'w') as outfile:
    json.dump([ob.__dict__ for ob in c2], indent=3, fp=outfile)

with open('c2-words.min.json', 'w') as outfile:
    json.dump([ob.__dict__ for ob in c2], fp=outfile)