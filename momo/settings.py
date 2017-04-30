# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from os import environ
from six.moves.urllib.parse import urlparse

# from .error_codes import error_codes


class Config(object):

    DEBUG = True
    TESTING = False

    SECRET_KEY = '53a01e6bd34caef997eed24f5ee9d3e0'

    STATIC_FOLDER = 'static'

    APP_TRANSPORT = environ.get('APP_TRANSPORT', 'http')
    APP_DOMAIN = environ.get('APP_DOMAIN', 'http://gusibi.com')
    API_DOMAIN = environ.get('API_DOMAIN', 'http://gusibi.com')
    DOMAIN = '%s://%s' % (APP_TRANSPORT, urlparse(APP_DOMAIN).netloc)

    # 微信 公众账号信息
    WEIXINMP_APPID = environ.get('WEIXINMP_APPID', 'appid')
    WEIXINMP_APP_SECRET = environ.get('WEIXINMP_APP_SECRET', '')
    WEIXINMP_TOKEN = environ.get('WEIXINMP_TOKEN', 'token')
    WEIXINMP_ENCODINGAESKEY = environ.get(
        'WEIXINMP_ENCODINGAESKEY', '')

    # 微信获取用户信息接口
    WX_USER_INFO_URL = 'https://api.weixin.qq.com/cgi-bin/user/info'

    QINIU_ACCESS_TOKEN = ''
    QINIU_SECRET_TOKEN = ''
    QINIU_UPLOAD_URL = 'http://up.qiniu.com/'
    QINIU_DOMAIN = environ.get('QINIU_DOMAIN', 'medias.gusibi.com')
    QINIU_DOMAINS = [QINIU_DOMAIN, 'oddfrn1vt.qnssl.com']
    QINIU_HOST = "https://%s" % QINIU_DOMAIN
    QINIU_NOTIFY_URL = '%s/qiniu/pfop/notify' % DOMAIN
    QINIU_PUBLIC_BUCKET = 'gusibi'

    QINIU_AUDIOS_TIME_KEY = environ.get('QINIU_AUDIOS_TIME_KEY', '')
    QINIU_AUDIOS_HOST = environ.get('QINIU_AUDIOS_HOST',
                                    'https://audios.gusibi.com')

    QINIU_AUDIOS_CONFIG = {
        'access_key': QINIU_ACCESS_TOKEN,
        'secret_key': QINIU_SECRET_TOKEN,
        'time_key': QINIU_AUDIOS_TIME_KEY,
        'host': QINIU_AUDIOS_HOST
    }
