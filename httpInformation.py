import requests
from bs4 import BeautifulSoup as bs


def scanWeb():
    main_url = 'https://0ac200a20338613fc3678efa002a00df.web-security-academy.net/'
    r = requests.get(main_url)
    print(main_url)
    s = bs(r.text, 'lxml')
    print(f'\n HTTP status code: {r.status_code}')
    print('\n')
    print(r.headers)
    print('\n')
    print(s.text)


if __name__ == '__main__':
    scanWeb()