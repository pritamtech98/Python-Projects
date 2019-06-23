from urllib.parse import urlparse


def get_main_domain_name(url):
    try:
        result=get_full_domain_name(url).split('.')
        return result[-2]+'.'+result[-1]
    except:
        return ''

def get_full_domain_name(url):
    url_parse=urlparse(url)
    try:
        return url_parse.netloc
    except:
        return ''

