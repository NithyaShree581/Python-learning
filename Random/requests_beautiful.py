import requests
from bs4 import BeautifulSoup
import sys

print(sys.argv[1])

link=sys.argv[1]

html_text=requests.get(link).text

normal_text_with_html=BeautifulSoup(html_text,"html.parser")

for i in normal_text_with_html.find_all('p'):
    print(i.text)
    
print("we are extracting all the text from the html page including the html tags\n\n")  
  
print(normal_text_with_html.get_text())  

print("\n\n")

print("we are extracting the text from the html page excluding the html tags\n\n")

print(normal_text_with_html.find('p').parent.text)
