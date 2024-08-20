import urllib.parse as urlparse
import requests
from requests.exceptions import Timeout, SSLError


ipv4 = ''
ipv6 = '[fe80::202:99ff:fe2e:1e3c]'

addr = ipv4 if ipv4 else ipv6


def create_url(addr, footer=''):
    
    url = urlparse.urljoin('https://' + addr, footer)

    return url


def post_request(url, payload={}, timeout=5):
    successFlg = False
    try:
        # SSL認証を回避
        res = requests.post(url, json=payload, timeout=timeout, verify=False)
    except Timeout:
        raise "設定された制限時間を超えたので処理を終了しました。"
    except SSLError:
        raise "SSLエラー"
    except Exception as e:
        raise e

    if res.status_code == 200:
        successFlg = True
        msg = f'Success: {res.text}'
    else:
        msg = f'Failed to post: {res.text}'
    
    return successFlg, msg

