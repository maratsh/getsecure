# -*- coding: utf-8 -*-

import hashlib
from base64 import b64encode
from datetime import datetime, timedelta
from urllib.parse import urlparse


def secure_link(baselink, secret, period=30):
    """

    :param baselink: base url for signing
    :param secret: secret string shared only with web server
    :param period: optional period in days
    :return: signed link as str
    """


    url = urlparse(baselink)

    expires = int((datetime.now() + timedelta(days=period)).timestamp())

    hashstring = '{e}{u} {s}'.format(e=expires, u=url.path, s=secret)

    m = hashlib.md5()
    m.update(bytes(hashstring, encoding='utf-8'))
    protection_string = b64encode(m.digest(), altchars=b'-_').replace(b'=', b'').decode("ascii")

    protected_link = '{b}?md5={p}&expires={e}'.format(b=baselink, p=protection_string, e=expires)

    return protected_link


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Utility for securing expiring links')
    parser.add_argument('baselink')
    parser.add_argument('secret', type=str)

    parser.add_argument('--period', default=30, type=int)

    options = parser.parse_args()
    link = secure_link(options.baselink, options.secret, options.period)

    print(link)
