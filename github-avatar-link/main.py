import requests
from bs4 import BeautifulSoup as bs

def retrieve_avatar_link():
    github_username = input('Input Github username: ')
    url = f'https://github.com/{github_username}'
    request = requests.get(url)
    if not request.status_code == 200:
        print('Avatar link could not be retrieved for username provided')
        exit()
    soup = bs(request.content, 'html.parser')
    profile_image = soup.find('img', {'alt': 'Avatar'})['src']
    print(profile_image)
    
retrieve_avatar_link()
