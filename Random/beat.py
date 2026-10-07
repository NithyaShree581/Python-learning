from bs4 import BeautifulSoup

html = """<html><head><title>Test</title></head><body><h1>SampleHeading</h1>
<a href="www.google.com"> Google Link</a>
<p>Hello, World!</p><p> Something very important note</p></body></html>"""
soup = BeautifulSoup(html, "html.parser")

print(soup.p.text)  
print(soup.h1.text)
for i in soup.find_all('p'):
    print(i.text)
print(soup.find('p').parent.text)
print(soup.find('a').get('href'))
