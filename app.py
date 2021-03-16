import json
from flask import Flask, render_template,request
import json
import requests
app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    upcomingUrl = 'https://api.jikan.moe/v3/top/anime/1/upcoming'
    mostPopUrl = 'https://api.jikan.moe/v3/top/anime/1/bypopularity'
    upcoming = requests.get(upcomingUrl).json()['top']
    mostPop = requests.get(mostPopUrl).json()['top']
    return render_template('index.html', upcoming = upcoming, mostPop = mostPop, title = "Index")
@app.route('/Upcoming')
@app.route('/Upcoming/<page>')
def upcoming(page = 0):
    curPage = 1
    curPage += int(page)
    upcomingUrl = 'https://api.jikan.moe/v3/top/anime/{}/upcoming'.format(curPage)
    upcoming = requests.get(upcomingUrl).json()['top']
    return render_template('upcoming.html', data = upcoming,curPage = curPage, title = "Upcoming")
@app.route('/MostPopular')
@app.route('/MostPopular/<page>')
def mostPop(page = 0):
    curPage = 1
    curPage += int(page)
    mostPopUrl = 'https://api.jikan.moe/v3/top/anime/{}/bypopularity'.format(curPage)
    mostPop = requests.get(mostPopUrl).json()['top']
    return render_template('mostPop.html', data = mostPop, curPage = curPage, title = "MostPopular")


@app.route('/info/<id>')
def info(id):
    url = 'https://api.jikan.moe/v3/anime/' + id
    return requests.get(url).json()
 
 
@app.route('/search/')
def news():
    keyword = request.args.get('keyword', default = '')
    url = 'https://api.jikan.moe/v3/search/anime?q=' + keyword
    try:
        search = requests.get(url).json()['results']
        if search:
            return render_template('search.html', search = search, title = "Search : " + keyword)            
        else:
            raise Exception()
    except:
        return render_template('NoResult.html',title ='No Result')
    
@app.route('/genre/')
def genre():
    return render_template('genre.html', title = 'Genre')

@app.route('/aboutus')
def aboutme():
    return render_template('aboutus.html')


if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
