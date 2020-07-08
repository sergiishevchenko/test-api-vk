import sys
import vk_api
from config import API_ID, TOKEN, EXPIRES_IN

vk_session = vk_api.VkApi(input("Введите логин"), input("Введите пароль"))
vk_session.auth()

vk = vk_session.get_api()

def get_friends(API_ID):
    return vk.friends.get(user_id=API_ID)['items']


# link = "https://oauth.vk.com/authorize?client_id=API_ID&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=TOKEN&v=5.120"

# link_friends = "https://api.vk.com/method/friends.getOnline?v=5.120&access_token=TOKEN"

def main():
    friends = get_friends(API_ID)

    print('user_id')
    for friend in friends:
        print(friend)
    pass

if __name__ == "__main__":
    main()
