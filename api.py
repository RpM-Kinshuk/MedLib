import requests

url = "https://www.googleapis.com/books/v1/volumes"
search_query = input("Enter a search query (e.g., 'flowers inauthor:keyes'): ")

params = {
    "q": search_query, 
    "key": "AIzaSyD78D5ryj5xyGJkzlWsSiPNRAmQhboPhOA", 
}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    
    for item in data.get("items", []):
        volume_info = item.get("volumeInfo", {})
        title = volume_info.get("title", "Title not available")
        authors = volume_info.get("authors", ["Author not available"])
        
        print(f"Title: {title}")
        print(f"Authors: {', '.join(authors)}")
        print("=" * 50)
else:
    print(f"Error: {response.status_code} - {response.text}")
