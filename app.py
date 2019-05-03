from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:

            url = 'https://pokeapi.co/api/v2/pokemon/{}/'
            cari = request.form['cari']

            req_pokemon = requests.get(url.format(cari)).json()

            poke_stats = {
                'nama' : req_pokemon['name'],
                'gambar' : req_pokemon['sprites']['front_default'],
                'id' : req_pokemon['id'],
                'tinggi' : req_pokemon['height'],
                'berat' : req_pokemon['weight']
            }
            
            return render_template ('result.html', poke_stats=poke_stats)
        except:
            return redirect ('error.html')
    else:
        return render_template ('home.html')


@app.route('/result')
def result():
    return render_template ('result.html')


@app.errorhandler(404)
def notFound404(error):
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)