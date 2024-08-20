import urllib.parse as urlparse


def get_pdu_api_url(ip_addr, footer=''):
    return url_add_footer(f'https://{ip_addr}/api/', footer)

def url_add_footer(url, footer=''):
    return urlparse.urljoin(url, footer)

