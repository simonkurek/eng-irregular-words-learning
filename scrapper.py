from urllib.request import urlopen
from bs4 import BeautifulSoup
from Word_Enitity import Word_Enitity

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

for i in range(len(words)):
    if len(words[i]) > 0:
        level = words[i][0]
        first_form = words[i][1]
        second_form = words[i][2]
        third_form = words[i][3]
        pol_trans = words[i][4]
        words_obj.append(Word_Enitity(first_form, second_form, third_form, pol_trans, level))

for word in words_obj:
    print(word.__dict__)

#for word in words:
#    print(word.display())


    # level = word_preparse[0]['class'][1]
    # first_form = word_preparse[0].find('a').next_sibling.split(', ')
    # second_form = word_preparse[1].string.split(', ')
    # third_form = word_preparse[2].string.split(', ')
    # pol_trans = word_preparse[3].string.split(', ')
    # word = Word_Enitity(first_form, second_form, third_form, pol_trans, level)
    # words.append(word)