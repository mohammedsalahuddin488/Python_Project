import requests
query = input("Enter the topic you want to search for: ")
api_key = "8dbc8e03114a4221ba471cb39abff91a"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-08-17&sortBy=publishedAt&apiKey={api_key}"

print(url)

r = requests.get(url)

data = r.json()
articles = data['articles']

for index ,article in enumerate(articles):
    print(f"Article {index + 1}")
    print(article["title"], article["description"], article["url"])
    print("\n*******************************************\n")