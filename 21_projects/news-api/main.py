import requests # pip install requests

query = input("What type of news are you interested in today? ")
api = "122f52b9-5c44-47e8-9f39-2f8fd53450b8"

# url = f"https://newsapi.org/v2/everything?q={query}&from=2025-02-08&sortBy=publishedAt&apiKey={api}"
url = f"https://eventregistry.org/api/v1/article/getArticles?query={query}&articlesSortBy=date&apiKey={api}&callback=JSON_CALLBACK"

print(url)
r =  requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
