import requests
from requests.exceptions import Timeout, SSLError


def get(url, payload={}, timeout=5):

    print(f'GET requset url: {url}')

    try:
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

    print(f'POST request url: {url}\npayload: {payload}')

    try:
        # SSL認証を回避
        res = requests.post(url, json=payload, timeout=timeout, verify=False)
    except Timeout:
        raise "設定された制限時間を超えたので処理を終了しました。"
    except SSLError:
        raise "SSLエラー"
    except Exception as e:
        raise e

    if res.status_code != 200:
        print(f'URL: {url}へのリクエストに失敗しています。')
    
    return res


