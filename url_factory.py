import urllib.parse as urlparse


def get_pdu_api_url(ip_addr, footer=''):
    """
    PDUのapi用URLを作成する
    Args:
        ip_addr(str): pduのアドレス

        footer(any): api urlの後に追加するpath
    
    Returns:
        api用のURL

    """
    return url_add_footer(f'https://{ip_addr}/api/', footer)

def url_add_footer(url, footer=''):
    """
    urlの後ろにpathを追加

    Args: 
        url(str): URL

        footer: 追加するpath

    Returns:
        加工されたURL
    
    """
    return urlparse.urljoin(url, footer)

