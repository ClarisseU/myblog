import urllib.request, json
from .models import Quote
from config import Config
import requests

# def configure_request(app):
#     global base_url
#     base_url = app.config['QUOTE_API_BASE_URL']

quotes_url = Config.QUOTE_API_BASE_URL
    
def getQuotes():
    '''
    function that gets the json response a.k.a quotes to our url request
    '''
    quote=requests.get(quotes_url)
    nu_quote = quote.json()
    author = nu_quote.get('author')
    quote = nu_quote.get('quote')
    quote_result = Quote(author, quote)
        
    return quote_result     