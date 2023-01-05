import requests
from bs4 import BeautifulSoup
import os

def loadData():
    acts = []
    obs = []
    print("loading data......")
    url = 'https://www.gymlibrary.dev/environments/atari/complete_list/#complete-list-atari'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    env_list = soup.find(name='div', attrs={'class': 'env-grid'}).find_all(name='a')
    for env in env_list:
        env_name = env.attrs['href'][3:]
        child_url = os.path.join('https://www.gymlibrary.dev/environments/atari/', env_name)
        response = requests.get(child_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        info = soup.find(name='table', attrs={'class': 'docutils align-default'}).find(name='tbody').find_all(name='p')
        acts.append(info[1].string)
        obs.append(info[3].string)
    return acts, obs

if __name__ == "__main__":
    acts, obs = loadData()