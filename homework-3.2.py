import requests

APP_ID = 6773586
AUTH_URL = 'https://oauth.vk.com/authorize?'
URL_API = 'https://api.vk.com/method/'

url_get_token = 'https://oauth.vk.com/authorize?client_id=6773586&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.52'

TOKEN = 'ebd19367b930c8adc72dcb642a4545810d4fd7b40d830a5644ee8308a8413f044f7fe46481694f9dbb0cc'

def find_total(first, second):
    return list(set(first) & set(second))

class User():

    def __init__(self, user_id):
        self.user_id = user_id

    def search_matual_friends(self, user_id=None):
        params = {
            'access_token': TOKEN,
            'v': '5.92',
            'user_id': user_id if user_id else self.user_id,
        }
        resp = requests.get(URL_API + 'friends.get', params=params)
        friends = resp.json()
        return friends['response']['items']

    def __and__(self, other):
        user_1 = self.search_matual_friends()
        user_2 = other.search_matual_friends()
        mutual_friends = find_total(user_1, user_2)
        return mutual_friends

    def __str__(self):
        return f'https://vk.com/id{self.user_id}'


user_1 = User(97333658)
user_2 = User(3781426)
print(user_1 & user_2)
print(user_2)
