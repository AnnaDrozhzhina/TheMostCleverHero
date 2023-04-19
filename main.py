import requests


def get_files_list():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    params = {'powerstats': 'intelligence'}
    resp = requests.get(url=url, params=params)
    return resp.json()


data = get_files_list()
heroes_list = ['Hulk', 'Captain America', 'Thanos']
res = {}
for element in data:
    if element['name'] in heroes_list:
        res[element['name']] = element['powerstats']['intelligence']
max_intel = max(res.values())
name = max(res, key=res.get)
print(f'Самый умный супергерой {name} с уровнем intelligens: {max_intel}')














