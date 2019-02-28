import re


def strip_url(line):
    ozon_url = re.search("(?P<url>https?://[^\s]+)", line).group("url")
    return ozon_url


source = open('all.txt')
url_list = open('stripped_ozon.txt', 'w')
for line in source.readlines():
    surl = strip_url(line)
    url_list.write(surl + '\n')

source.close()
url_list.close()