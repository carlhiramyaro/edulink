import requests

def fetch_books_data(subject_query):
    key = 'AIzaSyCU_OM1RAoBGxG9gSLk_TzUPlsJIqozJvU'
    api_url = 'https://www.googleapis.com/books/v1/volumes'
    
    # Modify the query to target books suitable for kids aged 10 to 25
    age_range_query = "10-25"
    query = f'subject:{subject_query} AND {age_range_query}'

    
    params = {
        'q': query,
        'key': key,
        'maxResults': 5  # You can adjust this based on your preference
    }
    
    response = requests.get(api_url, params=params)
    response_data = response.json()
    
    books = []

    for item in response_data.get("items", []):
        volume_info = item.get("volumeInfo", {})
        book = {
            "title": volume_info.get("title", "Unknown Title"),
            "author": ", ".join(volume_info.get("authors", ["Unknown Author"])),
            "image_link": volume_info.get("imageLinks", {}).get("thumbnail", ""),
            "read_link": volume_info.get("webReaderLink", ""),
        }
        books.append(book)

    return books

# Example usage for the 'math' subject
math_books_data = fetch_books_data("Mathematics")
print(math_books_data)

