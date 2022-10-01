import requests
from bs4 import BeautifulSoup


response = requests.get(url="https://news.ycombinator.com/news")
y_combinator = response.text


soup = BeautifulSoup(y_combinator, 'html.parser')

# article_text = soup.select_one(selector=".titleline a")
articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.find(name="a").get("href")
    article_links.append(link)

article_upvote = [int(upvote.getText().split()[0]) for upvote in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvote)

#   challenge
max_vote = max(article_upvote)
pos = article_upvote.index(max_vote)

a_article = article_texts[pos + 1]
b_link = article_links[pos + 1]

print(f"Article : {a_article}")
print(f"Link : {b_link}")
print(f"Upvote : {max_vote}")


















