from post_test import *


def vpdu_user_registration(addr, user='admin', pswd='magic5580', role='', permission=''):

    url = create_url(addr, footer='api/auth')

    payload = {'cmd': 'add', 'data': {'username': user, 'password': pswd, 'admin': True, 'control': True}}

    print(f"url: {url}, payload: {payload}")

    successFlg, msg = post_request(url, payload)

    return successFlg, msg



successFlg, msg = vpdu_user_registration(addr)

print(msg)
