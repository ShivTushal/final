
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

NEWS_API_KEY = "2df0522c46654a7a81047c9ce38744cd"

@app.route('/')
def home():
    query = request.args.get('query') or 'technology'
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return render_template('index.html', articles=articles, query=query)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
