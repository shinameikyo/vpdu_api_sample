import urllib.parse as urlparse


ipv4 = ''
ipv6 = ''

addr = ipv4 if ipv4 else ipv6


def create_url(addr, footer='', stuffings=[]):g
    
    url = urlparse.urljoin('https://' + addr, footer)

    return url