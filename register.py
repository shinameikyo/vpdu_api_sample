from pdu_request import *
from url_factory import *


def initial_registration(addr, user='admin', pswd='magic5580', role='', permission=''):
    """
    初期登録を行う関数。

    Args:
        addr (str): 登録先のアドレス。
        user (str): ユーザー名。デフォルトは'admin'。
        pswd (str): パスワード。デフォルトは'magic5580'。
        !(未実装) role (str): ユーザーの役割。デフォルトは空文字。
        !(未実装) permission (str): ユーザーの権限。デフォルトは空文字。

    Returns:
        res: レスポンス。
    """

    url = url_add_footer(addr, footer='auth')

    payload = {'cmd': 'add', 'data': {'username': user, 'password': pswd, 'admin': True, 'control': True}}

    print(f"url: {url}, payload: {payload}")

    res = post(url, payload)

    return res


if __name__ == 'main':

    ip_addr = '192.168.7.195'

    url = get_pdu_api_url(ip_addr)

    res = initial_registration(url)

    print(res)
