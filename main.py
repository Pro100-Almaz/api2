from fastapi import FastAPI
import requests
import webbrowser

app = FastAPI()

# some database data
db_data = {
    'China': {
        'population': "1439323776",
        'density': "153",
        'wr_share': "18.47"
    },
    'India': {
        'population': "1380004385",
        'density': "464",
        'wr_share': "17.7"
    },
    'US':{
        'population': "331002651",
        'density': "36",
        'wr_share': "4.25"
    },
    'Indonesia':{
        'population': "273523615",
        'density': "151",
        'wr_share': "2.51"
    },
    'Pakistan':{
        'population': "220892340",
        'density': "287",
        'wr_share': "2.83"
    }
}


class RequestAPI:
    url = 'https://animechan.vercel.app/api/random'

    def get_quote(self,num):
        result = requests.get(self.url).json()
        if num==2:
            return result['quote'] 
        elif num==0:
            return result['anime']
        else:
            return result['character']

    def get_text_with_quote_for_name(self, name):
        return 'My friend %s, %s once sad >%s<. (anime %s)' % (name, self.get_quote(4), self.get_quote(2), self.get_quote(0))


@app.get('/')
def index():
    f = open('index.html','w')

    message = """<html>
    <head></head>
    <body><center><i><h1>Hello there! This is the main page of my project!</h1></i></center>
    </body>
    </html>"""

    f.write(message)
    f.close()

    webbrowser.open('index.html')


@app.get('/countries')
def names():
    f = open('country.html','w')

    message = """<html>
    <head></head>
    <body><center><i><h1>I know that this weak project is not working well, but plz just add needed
    information to end of the url.</h1></i></center>
    <ul>
    <li>China</li>
    <li>India</li>
    <li>United States</li>
    <li>Indonesia</li>
    <li>Pakistan</li>
    </ul></body>
    </html>"""

    f.write(message)
    f.close()

    webbrowser.open_new_tab('country.html')


@app.get('/countries/{name}')
def names_one(name):
    if name in db_data:
        name.capitalize()
        data = db_data[name]
        return (f'In country {name}, number of population is ' + data['population']+', density (person/km^2) is ' + data['density']+' and world share is '+data['wr_share']+' %.')
    else:
        my_request = RequestAPI()

        return my_request.get_text_with_quote_for_name(name)