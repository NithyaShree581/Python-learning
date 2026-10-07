import requests
#something=requests.get("https://www.york.ac.uk/teaching/cws/wws/webpage1.html")
try:
    something=requests.get("https://www.york.ac.uk/teaching/cws/wws/page1.html",timeout=5)
    print(something.status_code)
except requests.RequestException as error:
    print("API failed")
    print(error)
