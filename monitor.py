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
