'''

'''
import requests

def search_dad_jokes(term, limit,page):
    '''
    
    '''
    JOKE_URL = 'https://icanhazdadjoke.com/search'
    #header parameters
    headers = {
        'Accept':'text/plain'
    }
    params = {
        'term':term,
        'page': page,
        'limit':limit
        
    }
    joke = requests.get(JOKE_URL,headers=headers,params=params)
    
    if joke.status_code > 400:
        print(f"you have encoutered an error {joke.status_code}")
        return ""
    else:
        print(f"Status Code: {joke.status_code}")
        return joke.text
    
if __name__ == "__main__":
    print("Please import this module.")