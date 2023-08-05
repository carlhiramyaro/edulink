import requests

def fetch_youtube_data(subject_query):
    key = 'AIzaSyAZfv9BMAP2KSrlk4LPK8XePqz3hHo0mHA'
    api_url = 'https://www.googleapis.com/youtube/v3/search'
    #https://www.googleapis.com/youtube/v3/search?q=math&part=snippet&key=AIzaSyAZfv9BMAP2KSrlk4LPK8XePqz3hHo0mHA

    
    # Modify the query to target youtube suitable for kids aged 10 to 25
    age_range_query = "10-25"
    query = f'{subject_query} educational videos'
    # query = f'subject:{subject_query} AND {age_range_query}'

    #Parameters of the Youtube API requests
    params = {
        'q': query,
        'key': key,
        'part': 'snippet',
        'type': 'video',
        'maxResults': 5  # You can adjust this based on your preference
    }
    
    response = requests.get(api_url, params=params)
    response_data = response.json()
    
    youtube = []
#Loop through the items in the API response
    for item in response_data.get("items", []):
        video_info = item.get("snippet", {})
        #dictionary to store video information
        video = {
            "title": video_info.get("title", "Unknown Title"),
            "author": video_info.get("channelTitle", "Unknown Author"),
            "image_link": video_info.get("thumbnails", {}).get("default", {}).get("url", ""),
            "video_link": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
        }
        #add the video dictionary
        youtube.append(video)

#return the list of the youtube videos
    return youtube

# Example usage for the 'math' subject
math_youtube_data = fetch_youtube_data("mathematics")
print(math_youtube_data)


