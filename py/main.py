from bs4 import BeautifulSoup as bs4

with open("index.html") as file:
    src = file.read()

soup = bs4(src, "lxml")

#page_h = soup.find("h1")
#print(page_h)

page_h_all = soup.find_all("div")

for i in page_h_all:
    print(i.text)