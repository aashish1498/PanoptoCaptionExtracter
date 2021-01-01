import urllib
import os
from bs4 import BeautifulSoup
myModule = "ME40054" # Folder which contains the html files
Week= "W11" # Name of the html file
mydir = "C:/Users/aashi/Documents/Uni/Final year/Transcripts/" + myModule + "/" # Directory which contains your module folders

# If there are multiple lectures in a week, you can save them as W1_1, W1_2, etc., and the script will put them all into one file

filename = mydir + Week + ".txt" # Transcript is saved here
with open(filename, "a") as myfile:
    myfile.truncate(0)

for file in os.listdir(mydir):
    if (file.startswith(Week + ".")  or file.startswith(Week + "_")) and file.endswith('.html'):
        Lecture = os.path.splitext(file)[0]
    else:
        continue

    url = "file:///" + mydir + Lecture + ".html"
    
    html = urllib.urlopen(url)
    page = html.read()

    soup = BeautifulSoup(page, "html.parser")

    with open(filename, "a") as myfile:
        mytitle = soup.find("meta",  property="og:title")["content"]
        myurl = soup.find('meta', {"property":"og:url"})["content"]
        myfile.write(myModule + " " + Week + '\n\n' + mytitle + '\n\n' + myurl + '\n\n')

    texts = soup.body.find_all('div', attrs={'class': 'event-text'})


    for text in texts:
        mytext = text.contents[3].get_text()
        with open(filename, "a") as myfile:
            myfile.write(mytext.encode('utf-8').strip() + " ")

os.startfile(filename)
print("Completed")