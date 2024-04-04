import requests
from bs4 import BeautifulSoup
from .adapter import EventSourceAdapter

class TicketmasterAdapter(EventSourceAdapter):
    def fetch_events(self):
        response = requests.get("https://api.ticketmaster.com/")
        data = response.json()

        # TODO: Convert data to main format here

        return data

class EdmtrainAdapter(EventSourceAdapter):
    def fetch_events(self):
        response = requests.get("https://api.edmtrain.com/")
        data = response.json()

        # TODO: Convert data to main format here

        return data

class DiceFmAdapter(EventSourceAdapter):
    def fetch_events(self):
        response = requests.get("https://www.dice.fm/")
        soup = BeautifulSoup(response.text, 'html.parser')
        data = {}

        # TODO: Perform scraping logic and convert data to main format here

        return data
