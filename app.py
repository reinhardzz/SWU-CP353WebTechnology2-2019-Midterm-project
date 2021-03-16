import json
from flask import Flask, render_template,request
import json
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    url0 = 'https://api.jikan.moe/v3/top/anime/1/upcoming'
    data = requests.get(url0).json()['top']
    upcoming = [(i['title'],i['image_url'],i['mal_id']) for i in data]
    url1 = 'https://api.jikan.moe/v3/top/anime/1/bypopularity'
    data = requests.get(url1).json()['top']
    mostPop = [(i['title'],i['image_url'],i['mal_id'],i['type'],i['score'],i['episodes']) for i in data]
    return render_template('index.html', upcoming = upcoming, mostPop = mostPop)

@app.route('/info/<id>')
def info(id):
    url = 'https://api.jikan.moe/v3/anime/' + id
    return requests.get(url).json()
 
 
@app.route('/genre')
def news():
    tag = request.args.get('search_news')

    if not tag:
        tag = 'phone'

    news = searchNews(tag,NEWS_KEY)
    return render_template('genre.html', news=news)



@app.route('/aboutus')
def aboutme():
    return render_template('aboutus.html')

def searchNews(tag,API_KEY):
    query = quote(tag)
    url = NEWS_URL.format(query, API_KEY)
    print(url)
    data = urlopen(url).read()
    parsed = json.loads(data)
    news = parsed.get('articles')
    
    return news
    


if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)