import os
from bs4 import BeautifulSoup
current_directory = os.path.dirname(os.path.abspath(__file__))
utility_nav_translated = "utility_nav_translated.html" 

utility_nav = '''<div class="utility-nav">
    <div class="grid-container bg-ghost-gray">
        <div class="top-bar bg-ghost-gray" id="responsive-menu">
            <div class="top-bar-left valign-mu">
                <ul class="menu">
                    <li class="gov-site show-for-medium">
                        An official website of the City of Philadelphia government
                    </li>
                    <li class="gov-site show-for-medium"><a href="#" class="trusted-site-toggle">Here's how you
                            know <i class="fas fa-solid fa-caret-down"></i></a></li>
                    <li class="gov-site show-for-small-only">
                        <a href="" class="trusted-site-toggle">An official website <i
                                class="fas fa-info-circle"></i></a>
                    </li>
                </ul>
            </div>
            <!-- Translations Navigation -->
            <div class="top-bar-right translations-nav">
                <ul id="translations-menu" class="dropdown menu" data-dropdown-menu>
                    <li class="show-for-medium"><a
                            href="https://staging-phila-gov-elb-942614641.us-east-1.elb.amazonaws.com/">English</a>
                    </li>
                    <li class="show-for-medium"><a
                            href="https://staging-phila-gov-elb-942614641.us-east-1.elb.amazonaws.com/es/">Español</a>
                    </li>
                    <li class="show-for-medium"><a
                            href="https://staging-phila-gov-elb-942614641.us-east-1.elb.amazonaws.com/zh/">中文</a>
                    </li>
                    <li>
                        <a href="#" class="dropdown-selector">
                            <i class="fa-solid fa-earth-americas"></i> <span
                                class="show-for-small-only">Translate</span><i
                                class="fas fa-solid fa-caret-down"></i>
                        </a>
                        <ul class="translations-dropdown menu" data-dropdown-content>
                            <li class="show-for-small-only"><a
                                    href="https://staging-phila-gov-elb-942614641.us-east-1.elb.amazonaws.com/">English</a>
                            </li>
                            <li class="show-for-small-only"><a
                                    href="https://staging-phila-gov-elb-942614641.us-east-1.elb.amazonaws.com/es/">Español</a>
                            </li>
                            <li class="show-for-small-only"><a
                                    href="https://staging-phila-gov-elb-942614641.us-east-1.elb.amazonaws.com/zh/">中文</a>
                            </li>
                            <li id="google_translate_element"></li>
                            <li class="translations-support"><a href="#"><i class="fa fa-messages"></i>Feedback
                                    and Support</a></li>
                            <li class="translations-support"><a href="#"><i
                                        class="fa fa-file-lines"></i>Translated Publications</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</div>
'''

# 1. Create translated utility nav
# 2. Find all html files in current directory
# 3. Replace utility nav in all html files

def create_translated_util_nav():
#Function to create translated utility nav
    text1 = None
    text2 = None
    text3 = None
    text4 = None
    text5 = None
    text6 = None

    utility_nav_file = BeautifulSoup(utility_nav, "html.parser")
    utility_nav_element = utility_nav_file.find("div", {"class": "utility-nav"}) 
    utility_nav_li_elements = utility_nav_element.find_all("li", {"class": "gov-site"})

    zh_import = os.path.join(current_directory, "html", "index_zh.html")
    zh_file = BeautifulSoup(open(zh_import), "html.parser")
    zh_nav_element = zh_file.find("div", {"class": "utility-nav"})
    lang_li_elements = zh_nav_element.find_all("li", {"class": "gov-site"})
    
    #Find language elements and replace text in utility nav
    for index, li in enumerate(lang_li_elements):
        for span in li.find_all('span'):
            text1 = span.text.strip()
        if index == 0:
            text2 = li.text.replace(text1,"").strip()
        else:
            text3 = li.text.strip()
    
    for index, li in enumerate(utility_nav_li_elements):
        if index == 0:
            text4 = li
            text4.string = text1
        elif index == 1 and text2 != None:
            text5 = li.a
            text5.string = text2
        else:
            text6 = li
            text6.string = text3
    
    with open(utility_nav_translated, "w") as file:
        file.write(str(utility_nav_file.prettify()))

    replace_util_nav()

create_translated_util_nav()

def get_html_files():
# Function to get all html files in current directory
# Output: List of html files in current directory
    current_dir = os.getcwd()
    html_files = []
    for root, dirs, files in os.walk(current_dir): #Get files from test_html directory  and subdirectories
        for file in files:
            if file.endswith(".html"):
                html_files.append(file)
                html_files.append(os.path.join(root, file))

    return html_files


def replace_util_nav():
    html_files = get_html_files()
    utility_nav_translated_import = os.path.join(current_directory, utility_nav_translated)
    utility_nav_translated_file = BeautifulSoup(open(utility_nav_translated_import), "html.parser")
    utility_nav_translated_element = utility_nav_translated_file.find("div", {"class": "utility-nav"})
    
    #Replace the utility nav in all html files
    if html_files != [] and utility_nav_translated_element != None:
        for file in html_files:
            if file != utility_nav_translated_import:
                html_file = BeautifulSoup(open(file), "html.parser")
                old_utility_nav = html_file.find("div", {"class": "utility-nav"})
                old_utility_nav.replace_with(utility_nav_translated_element)

