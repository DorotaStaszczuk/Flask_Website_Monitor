import requests
from bs4 import BeautifulSoup
from datetime import datetime
from flask import Flask
import json


def read_file(url):
    """reading from a configuration file"""
    with open('config.json') as json_file:
        data = json.load(json_file)
        for d in data['websites']:
            print('url: ' + d['url'])
            print('look_for: ' + d['lookFor'])
            print('period: ' + d['period'])
            print('')
    return("File opened")

def check_url(url):
    """ checking websites and returning status code """
    try:
        status_code = requests.get(url, timeout=30).status_code
        return status_code
    except requests.ConnectionError:
        return site_down

def check_time():
    """ checking response time """
    time = str(r.elapsed.total_seconds())
    return time

def check_content():
    """ parsing using BeautifulSoup and checking if page content matches the
    content requirements """
    soup = BeautifulSoup(r.text, 'html.parser')
    result = soup.find_all(string=look_for)
    return result
