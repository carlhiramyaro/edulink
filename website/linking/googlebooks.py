from flask import Flask, render_template, request, jsonify

import requests

website = Flask('Edulink')

@website.route('/')
def index():
    return render_template('index.html')

@website.route('/search', methods=['POST'])
def search_books():
    search_query = request.form.get('Math, Science, English')
    api_key = 'AIzaSyAA1pU9qxfXrwkEnic6XwYZFCnXjvrrs44'
    api_url = f'https://www.googleapis.com/books/v1/volumes?q=flowers&orderBy=newest&key=AIzaSyAA1pU9qxfXrwkEnic6XwYZFCnXjvrrs44'

    try:
        response = requests.get(api_url)
        response_data = response.json()

        if 'i' in response_data:
            books = response_data['i']
            return jsonify(books)
        else:
            return jsonify({'error': 'No results found.'}), 404

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error fetching data: {e}'}), 500

if __name__ == '__main__':
    website.run(debug=True)



