
from flask import Flask, request, render_template
app = Flask(__name__)
app.debug = True 

@app.route('/begining')
def begining():
    return render_template('begining.html')


@app.route('/end/<artist>')
def end(artist):
	result = request.args
	chosen_artist= result.get('options')
	base_url = "https://itunes.apple.com/search?term=" 
	url = base_url + chosen_artist
	x = requests.get(url, params = {"entity": "musicArtist"}).text
	return render_template('end.html', data= json.loads(x)["results"][0]["primaryGenreName"])
if __name__ == '__main__':
    app.run()

   
