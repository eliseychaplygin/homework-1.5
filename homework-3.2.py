import requests

APP_ID = 6773586
AUTH_URL = 'https://oauth.vk.com/authorize?'
URL_API = 'https://api.vk.com/method/'

url_get_token = 'https://oauth.vk.com/authorize?client_id=6773586&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.52'

TOKEN = 'ed75f48dd8de0ddeb8f5875a7ecb970b101f80bd689130e67b313e29b97d53be91b7b0f5b185511704414'

class User():

    def __init__(self, user_id):
        self.user_id = user_id

    def get_friends_list(self, user_id=None):
        params = {
            'access_token': TOKEN,
            'v': '5.92',
            'user_id': user_id if user_id else self.user_id,
        }
        resp = requests.get(URL_API + 'friends.get', params=params)
        friends = resp.json()
        return friends['response']['items']

    def find_total(self, first, second):
        return list(set(first) & set(second))

    def __and__(self, other):
        user_1 = self.get_friends_list()
        user_2 = other.get_friends_list()
        mutual_friends = self.find_total(user_1, user_2)
        return mutual_friends

    def __str__(self):
        return f'https://vk.com/id{self.user_id}'




user_1 = User(97333658)
user_2 = User(3781426)
print(user_1 & user_2)
print(user_2)
