from bs4 import BeautifulSoup

# with open('home.html', 'r') as html_file:
#     content = html_file.read()
# print(content)

# soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())
# tags = soup.find('h1')  # It searches for the first element with the given tag.
# tags2 = soup.find_all('h1')  # It returns list of all given tag elements
# print(tags)
# print(tags2)
# for tag in tags2:
#     print(tag.text)

import requests
html_text = requests.get('https://www.coursera.org/completed').text

soup = BeautifulSoup(html_text, 'lxml')
print(html_text)
