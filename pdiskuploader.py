import requests

PDISK_API_KEY = 'empty'
CONTENT_SRC = 'empty'
LINK_TYPE = 'empty'
FILE_NAME = 'empty'
Result = 'final result'


def user(header):
    header = header
    res = requests.post('http://linkapi.net/open/create_item', headers=header, params=header)
    if res.status_code == 200:
        print(res.text)
        global Result
        Result = str(res.text)



