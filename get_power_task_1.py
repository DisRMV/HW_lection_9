import requests


class Superhero:

    def __init__(self, token, name):
        self.token = token
        self.name = name
        self.id = self.get_id()

    def get_id(self):
        url = f'https://superheroapi.com/api/{self.token}/search/{self.name}'
        response = requests.get(url=url).json()
        if response['response'] == 'error':
            return response['error']
        return response['results'][0]['id']

    def get_power_stats(self, stat):
        url = f'https://superheroapi.com/api/{self.token}/{self.id}/powerstats'
        response = requests.get(url=url).json()
        return response[stat]

    def whos_better(self, stat, *heroes):
        heroes_dict = dict()
        heroes_dict[self.name] = int(self.get_power_stats(stat))
        heroes_ = list(heroes)
        for hero in heroes_:
            if isinstance(hero, Superhero):
                heroes_dict[hero.name] = int(hero.get_power_stats(stat))
        res = {k: v for k,v in heroes_dict.items() if v == max(heroes_dict.values())}
        return f"{', '.join(list(res.keys()))} is the best with {stat} {max(heroes_dict.values())}"


if __name__ == '__main__':
    hulk = Superhero('2619421814940190', 'Hulk')
    c_america = Superhero('2619421814940190', 'Captain America')
    thanos = Superhero('2619421814940190', 'Thanos')

    print(hulk.whos_better('intelligence', c_america, thanos))

