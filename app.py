# app.py

from flask import Flask, render_template, jsonify, request
import logging
from data_processor import get_random_anime, genres

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/genres')
def get_genres():
    return jsonify(list(genres))

@app.route('/random_anime')
def random_anime():
    genre = request.args.get('genre', 'all')
    anime_data = get_random_anime(genre)
    if anime_data is None:
        return jsonify({'error': 'No anime found in this genre'}), 404
    return jsonify(anime_data)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
