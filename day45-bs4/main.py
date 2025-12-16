from bs4 import BeautifulSoup
import requests
# import lxml

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
movie_webpage = response.text
soup = BeautifulSoup(movie_webpage, 'html.parser')
movie_tags = soup.find_all(name='span', class_ = 'content_content__i0P3p')

movie_list = []

for movie in movie_tags:
    name_tag = movie.select_one(selector = 'h2 strong ')
    if name_tag != None:
        name = name_tag.getText()
        movie_list.append(name)
            
reverse_list = movie_list[::-1]
print(reverse_list)

with open("movie_list.txt", 'w') as file:
    for movie in reverse_list:
        file.write(f"{movie}\n")


# with open("website.html", 'r', encoding='utf-8') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)

# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)


# for tag in all_anchor_tags:
#     print(tag.get_text())
#     print(tag.get("href"))

# heading = soup.find(name='h1', id='name')
# print(heading)
# section_heading = soup.find(name='h3', class_="heading")

# company_url = soup.select_one(selector='p a')