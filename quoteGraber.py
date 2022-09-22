from random import randint
import requests
from bs4 import BeautifulSoup

def to_dict(quote_list):
    """ 
        A simple function that will return a dictionnry from a quote html page
    """

    quote = dict()
    quote['author'] = quote_list.find('span').text.strip()
    quote['text'] = quote_list.text.strip().split('\n')[0]

    return quote

def grab_quote(term, number_of_quotes=1):
    url = "https://www.goodreads.com/quotes/search?commit=Search&page="+ str(randint(1, 100)) + "&q=" + str(term) + "&utf8=%E2%9C%93"
    page = requests.get(url).text
    bs = BeautifulSoup(page, "lxml")

    quotes = bs.findAll('div', {'class':'quoteText'})
    quote = [to_dict(quote) for quote in quotes] 

    return quote[:number_of_quotes]

if __name__ == "__main__":
    print(grab_quote('motivation', 5))



