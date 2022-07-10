import random
import string


def get_domain(uri):
    print(uri.split('//')[0] + '//' + uri.split('//')[1].split('/')[0])
    return uri.split('//')[0] + '//' + uri.split('//')[1].split('/')[0]


def shorneter(url):
    generated = ''.join(random.choice(string.ascii_letters) for i in range(10))
    shortened_url = get_domain(url) + '/' + generated
    return shortened_url
