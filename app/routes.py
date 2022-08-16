from app import app
from flask import render_template

@app.route('/')
def index():
    fav_bands = [
        'System_of_a_down',
        'Bring_me_the_horizon',
        'Agatha_Kristy',
        'Obladaet',
        'Max_korzh'
    ]
    return render_template('index.html', bands = fav_bands)

@app.route('/songs')
def songs():
    fav_songs = ['Toxicity','Shadow mouses', 'Arials', 'Can you feel my heart']
    return render_template('songs.html', songs = fav_songs)