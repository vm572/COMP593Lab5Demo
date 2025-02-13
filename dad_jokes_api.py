'''dad_jokes_api.py -Searchs for a dad joke on https://icanhazdadjoke.com/search
COMP 593 Scripting Applications Winter 2025 Lab 5 Sec 1
Valerie McQueen <Valerie.McQueen@FlemingCollege.ca>

Usage:
Import as a module.
'''
import requests

def search_dad_jokes(term, limit ='1',page='1'):
    '''
    Seearches for a dad joke
    
    parameters: The term to search for, limit: the number of jokes, page: which page
    '''
    JOKE_URL = 'https://icanhazdadjoke.com/search' #https://icanhazdadjoke.com/api
    #header parameters
    headers = {
        'Accept':'text/plain'
    }
    params = {
        'term':term,  #jokes_category
        'page': page, #defaults to '1'
        'limit':limit #defaults to '1'
        
    }
    joke = requests.get(JOKE_URL,headers=headers,params=params) #new get request https://pypi.org/project/requests/
    print(f"Getting you a joke about {term}....")
    if joke.status_code > 400:
        print(f"You have encoutered an error {joke.status_code}")
        return ""
    else:
        print(f"Status Code: {joke.status_code}")
        return joke.text
    
if __name__ == "__main__":
    print("Please import this module.")