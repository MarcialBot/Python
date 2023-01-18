import os
from bs4 import BeautifulSoup
current_directory = os.path.dirname(os.path.abspath(__file__))

#Import language files
zh_import = os.path.join(current_directory, "html", "index_zh.html")
zh_file = BeautifulSoup(open(zh_import), "html.parser")
zh_nav = zh_file.find("div", {"class": "utility-nav"})

#Import utility nav file
utility_nav_import = os.path.join(current_directory, "html", "utility_nav.html")
utility_nav_file = BeautifulSoup(open(utility_nav_import), "html.parser")
utility_nav = utility_nav_file.find("div", {"class": "utility-nav"})

#Language text
lang_elements = zh_file.find_all("li", {"class": "gov-site"})

text1 = None
text2 = None
text3 = None

for index, li in enumerate(lang_elements):
    for span in li.find_all('span'):
        text1 = span.text.strip()
    if index == 0:
        text2 = li.text.replace(text1,"").strip()
    else:
        text3 = li.text.strip()

#Replace utility nav text with language text
util_nav_elements = utility_nav.find_all("li", {"class": "gov-site"})

text4 = None
text5 = None
text6 = None

for index, li in enumerate(util_nav_elements):
    if index == 0:
        text4 = li.text.strip()
    elif index == 1:
        text5 = li.text.strip()
    else:
        text6 = li.text.strip()

#Replace text in utility nav with translated text
