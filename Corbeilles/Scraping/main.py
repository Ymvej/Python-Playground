# Imports & Variable Inits

import requests as rq
from bs4 import BeautifulSoup as bs 

cible = 'EmmanuelMacron'
robots = rq.get('https://fr.wikipedia.org/robots.txt')
datagov = rq.get('https://www.data.gov')
lin = rq.get('https://www.linkedin.com/')
wikim = rq.get('https://en.wikipedia.org/wiki/Main_Page')
lisa2 = rq.get('https://fr.wikipedia.org/wiki/Élisabeth_II')
twit = rq.get('https://twitter.com/' + cible)
# # Ex 1 :
# print(robots.text)


# # Ex 2 :
# datagov = bs(datagov.text, 'html.parser')

# for source in datagov.find_all('a'):
#     if source.get('href') == '/metrics':
#         print(source.get_text())


# # Ex 3 :
# lin = bs(lin.text, 'html.parser')

# print(lin.h1)


# # Ex 4 :
# wikim = bs(wikim.text, 'html.parser')
# list_of_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']

# for header in wikim.find_all(list_of_tags):
#     print(header)


# # Ex 5 :
# lisa2 = bs(lisa2.text, 'html.parser')

# for img in lisa2.find_all('img'):
#     if img['src'][0] == '/' and img['src'][1] == '/':
#         print(img['src'][2:])
#     else:
#         print(img['src'][1:])


# # Ex 6 :
# twit = bs(twit.text, 'lxml')

# for a in twit.find_all('a'):
#     try:
#         if a['href'] == '/{}/followers'.format(cible):
#             print(a['title'])
#     except KeyError:
#         continue

# # Ex 7 :
# print(rq.get('http://api.openweathermap.org/data/2.5/weather?id=6454307&appid=f478ab762c72baf973578daf23567be0'))

