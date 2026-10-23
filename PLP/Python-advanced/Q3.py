"""Topic: JSON & API Interaction 
Write a script interacting with https://jsonplaceholder.typicode.com/posts: 
(a) Fetch all 100 posts. Handle ConnectionError and JSONDecodeError. 
(b) Parse and print title + body of posts 1, 25, 50, 100. 
(c) Filter posts where body contains more than 5 words. Print the count. 
(d) Build {userId: [list of post titles]} and save as posts_by_user.json with indent=2. Add timeout=5. 
(e) Predict the output: import json data = '[{"id":1,"title":"Hello"},{"id":2,"title":"World"}]' posts = json.loads(data) titles = {p['id']: p['title'].upper() for p in posts} print(titles) print(json.dumps(titles)) 
"""
#a
import requests
import json
url = "https://jsonplaceholder.typicode.com/posts"
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    posts = response.json()
    print("Total posts are ", len(posts))
except requests.exceptions.ConnectionError:
    print("Connection error")
except json.JSONDecodeError:
    print("Invalid json ")
#b Parse and print title + body of posts 1, 25, 50, 100.
something=[1,25,50,100]
for i in something:
    if(i<len(posts)):
        print("title:",posts[i]['title'])
        print("body:",posts[i]['body'])
    else:
        print("Not found")
#c Filter posts where body contains more than 5 words. Print the count.
count=0
for i in range(len(posts)):
    if (len(posts[i]['body'].split())>5):
        count=count+1
print("posts that contain more than 5 words are ", count)
#d Build {userId: [list of post titles]} and save as posts_by_user.json with indent=2. Add timeout=5. 
dictionary = {}
for post in posts:
    user_id = post["userId"]
    title = post["title"]
    if user_id not in dictionary:
        dictionary[user_id] = []
    dictionary[user_id].append(title)

with open("posts_by_user.json", "w") as file:
    json.dump(dictionary, file, indent=2)
print("Data saved to posts_by_user.json")

print("the content inside the posts_by_user.json")
with open("posts_by_user.json","r") as so:
    data=json.load(so)
print(data)
    





