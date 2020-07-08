import vk
import getpass
import auth_vk

def auth_vk_password():
    session = vk.AuthSession(app_id=API_ID, user_login=input("VK user_login: "), user_password=getpass.getpass("VK user_password: "))
    file = open("auth_vk.ini", 'w')
    file.writelines(session.access_token)
    return session


def auth_vk_token():
    try:
        file = open("auth_vk.ini", 'r')
    except IOError as e:
        access_token = auth_vk_password().access_token
    else:
        access_token = file.readline()

    session = vk.Session(access_token=access_token)

    return session


def main():

    session = auth_vk.auth_vk_token()

    if session:
        print('Авторизация прошла успешно!')
    else:
        print('Авторизация не удалась!')


if __name__ == "__main__":
    main()
