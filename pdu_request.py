import requests
from requests.exceptions import Timeout, SSLError


def get(url, payload={}, timeout=5):
    """
    GETリクエストを送信する関数。

    Args:
        url (str): リクエスト先のURL。
        payload (dict): リクエストのペイロード。デフォルトは空の辞書。
        timeout (int): タイムアウト時間（秒）。デフォルトは5秒。

    Returns:
        (json | str): レスポンス
    """

    print(f'GET requset url: {url}')

    try:
        # SSL認証を回避しているので、認証を行うように修正の必要あり
        res = requests.get(url, timeout=timeout, verify=False)
        
    except Timeout:
        raise "設定された制限時間を超えたので処理を終了しました。"
    
    except SSLError:
        raise "SSLエラー"
    
    except Exception as e:
        raise e
    
    if res.status_code != 200:
        print(f'URL: {url}へのリクエストに失敗しています。')

    return res.text



def post(url, payload={}, timeout=5):
    """
    POSTリクエストを送信する関数。

    Args:
        url (str): リクエスト先のURL。
        payload (dict): リクエストのペイロード。デフォルトは空の辞書。
        timeout (int): タイムアウト時間（秒）。デフォルトは5秒。

    Returns:
        (json | str): レスポンス
    """

    print(f'POST request url: {url}\npayload: {payload}')

    try:
        # SSL認証を回避しているので、認証を行うように修正の必要あり
        res = requests.post(url, json=payload, timeout=timeout, verify=False)
        
    except Timeout:
        raise "設定された制限時間を超えたので処理を終了しました。"
    
    except SSLError:
        raise "SSLエラー"
    
    except Exception as e:
        raise e

    if res.status_code != 200:
        print(f'URL: {url}へのリクエストに失敗しています。')
    
    return res.text


