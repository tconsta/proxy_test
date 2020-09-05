# This is a sample Python script.
import requests
from bs4 import BeautifulSoup
from random import choice, uniform
from time import sleep

url = 'http://sitespy.ru/my-ip'


def get_html(url, user_agent=None, proxy=None):
    """Request and return HTML (string)"""
    print('Proxy: ', proxy)
    print('Request to ', url, 'is in progress...')
    r = requests.get(url, headers=user_agent, proxies=proxy)
    return r.text


def get_ip(html):
    """For example, get IP address and User-Agent from http://sitespy.ru/my-ip"""
    print('New identity:')
    soup = BeautifulSoup(html, 'lxml')
    ip = soup.find('span', class_='ip').text.strip()
    ua = soup.find('span', class_='ip').find_next_sibling('span').text.strip()
    print(ip)
    print(ua)


def main():

    with open('user_agents_list.txt') as ua:
        user_agents = ua.read().split('\n')
    with open('proxy_list.txt') as pr:
        proxies = pr.read().split('\n')

    for i in range(10):
        sleep(uniform(0, 1))
        proxy = {'http': 'http://' + choice(proxies)}
        user_agent = {'User-Agent': choice(user_agents)}
        try:
            html = get_html(url, user_agent, proxy)
        except:
            print('Dead proxy: ', proxy)
            continue
        get_ip(html)


if __name__ == '__main__':
    main()
