import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode, quote_plus, quote
from urllib.error import HTTPError, URLError
from random import randint
import requests
from bs4 import BeautifulSoup
import re
from time import sleep
import ssl
import csv
import datetime
import random
import time
# INFOS #

# Search API : https://asciimoo.github.io/searx/dev/search_api.html

# Infos
# The searX API direct call Google, Bing and Yahoo Search APIs without any limits / securities + it's anonymous

class Postcode():

    def __init__(self, q):
        self.q = q

        return

    def create_url(self):
        # rand_base = ['https://searx.site', 'https://searx.ch', 'https://searx.xyz', 'https://searx.cc', 'https://www.searx.de', 'https://searx.info']
        rand_base = ['https://searx.site']
        encoded_query = urlencode({'q' : self.q, 'categories' : 'map', 'format' : 'json'})
        url = random.choice(rand_base) + "/search?" + encoded_query

        print(url)

        return url

    def call_url(self):
        url = self.create_url()
        response = requests.get(url).json()
        # print(json.dumps(response, indent=4))

        return response

    def get_postcode(self):

      try:
        response = self.call_url()
        print('Finding postcode...')
        if response['results']:
          # print(response['results'])
          return {'city': response['results'][0]['address']['locality'],
                  'number': response['results'][0]['address']['house_number'],
                  'street': response['results'][0]['address']['road'],
                  'postcode': response['results'][0]['address']['postcode'],
                  'country': response['results'][0]['address']['country'],
                  'map': response['results'][0]['pretty_url']}
        else:
          return None
      except Exception as e:
        print(e)
        return None

    def run(self):
      return self.get_postcode()

if __name__ == "__main__":

    scrap = Postcode("island poke london")
    print(scrap.run())
    # phone = scrap.get_phone()
    # print(phone)
