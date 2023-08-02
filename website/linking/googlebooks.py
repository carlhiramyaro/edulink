from flask import Flask, render_template, request, jsonify

import requests

# website = Flask('Edulink')

# @website.route('/')
# def index():
#     return render_template('index.html')

# @website.route('/search', methods=['GET'])
# def search_books():
#     key = 'AIzaSyAA1pU9qxfXrwkEnic6XwYZFCnXjvrrs44'
#     queries = {"api_key": key}
#     api_url = f'https://www.googleapis.com/books/v1/volumes'

#     try:
#         for i in range(1, 10):
#             response = requests.get(api_url, params=queries)
#             response_data = response.json()

#         # print(response.headers['content-type'])

#             if 'i' in response_data:
#                 books = response_data['i']
#                 print(jsonify(books))
#                 return jsonify(books)
#             else:
#                 return jsonify({'error': 'No results found.'}), 404

#     except requests.exceptions.RequestException as e:
#         return jsonify({'error': f'Error fetching data: {e}'}), 500

# if __name__ == '__main__':
#     website.run(debug=True)



key = 'AIzaSyCU_OM1RAoBGxG9gSLk_TzUPlsJIqozJvU'
queries = {"key": key, 'q':'math'}
api_url = f'https://www.googleapis.com/books/v1/volumes'


for i in range(1, 10):
    response = requests.get(api_url, params=queries)
    response_data = response.json()
    print(response_data)
# print(response.headers['content-type'])

    # if 'i' in response_data:
    #     books = response_data['i']
    #     print(jsonify(books))
    #     # return jsonify(books)
    # else:
    #     print(jsonify({'error': 'No results found.'}), 404)
