from flask import Flask, render_template, request, jsonify

import requests, json

website = Flask('Edulink')

key = 'AIzaSyCU_OM1RAoBGxG9gSLk_TzUPlsJIqozJvU'
queries = {"key": key, 'q':'math', 'categories':'Mathematics'}
api_url = f'https://www.googleapis.com/books/v1/volumes'



@website.route('/mathBooks', methods = ['GET'])
def ReturnJSON():
    response = requests.get(api_url, params=queries)
    # print(response.text)
    data = json.loads(response.text)
 
    return jsonify(data)
    
if __name__=='__main__':
    website.run(debug=True)