from urllib.request import urlopen
from bs4 import BeautifulSoup
from Word_Enitity import Word_Enitity

url = "https://www.ang.pl/gramatyka/czasowniki-verbs/czasowniki-nieregularne"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

tbody_index = html.find("<tbody>")
start_index = tbody_index + len("<tbody>")
end_index = html.find("</tbody>")
table = html[start_index:end_index]

words_preparse = soup.find_all("tr")

word_preparse = words_preparse[-1].find_all("td")

#print(word_preparse[0])

for i in  range(len(word_preparse)-1):
    #print(word_preparse[i].find('a').next_sibling) <- 1 form
    #print(word_preparse[i]['class'][1]) <- level
    #print(word_preparse[i].string) <- 2,3 form & polish trans