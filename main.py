import requests
from send_email import send_email

api_key = '<KEY>'

url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-08-02&sortBy=publishedAt&apiKey=c4fc8c8feb89426a965344983b263913'

# Make request
response = requests.get(url)

# get a dictionary with data
content = response.json()

# primt(content)
# access the article titles and description
body = "subject: today's news\n\n"
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = body + article["title"] + "\n"\
            + article["description"]\
            + article["description"] + 2*"\n"
        # print(f"title= {article['title']}")
        # print(f"description= {article['description']}")

body = body.encode('utf-8')
send_email(message=body)





