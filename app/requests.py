import urllib.request, json
from .models import Quote

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']
    
def getQuotes():
    '''
    function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format(quote,QUOTE_API_BASE_URL)
    quote_object = None
    
    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        new_quotes = json.loads(get_quotes_data)
        id = new_quotes.get("id")      
        author = new_quotes.get("author")
        quote = new_quotes.get("quote")
        quote_object = Quote(id, author, quote)
        
    return quote_object      