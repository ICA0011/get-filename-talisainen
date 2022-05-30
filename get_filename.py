import requests
from bs4 import BeautifulSoup

url = "http://upload.itcollege.ee/~aleksei/random_files/"
content_list = []
page = requests.get(url).text

def get_filename(url):
    soup = BeautifulSoup(page, 'html.parser')
    result = [url + '/' + node.get('href') for node in soup.find_all('a')]
    return result
