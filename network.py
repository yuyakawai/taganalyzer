# -*- coding: utf-8 -*-

import requests

def reauest_html(url):
    try:
        target_html = requests.get(url, timeout = 3)
    except:
        return ""

    target_html.encoding = target_html.apparent_encoding # 日本語の文字化け防止
    return target_html.text

