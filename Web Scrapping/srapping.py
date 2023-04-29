from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
articles = soup.find_all(name='a', class_='titlelink')

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

highest_score = max(article_upvotes)

index = article_upvotes.index(highest_score)

print(article_texts[index + 1])
print(article_links[index + 1])
print(article_upvotes[index])
