'''pastebin_api.py - Posting to Pastebin, return a URL
COMP 593 Scripting Applications, Section L1 Winter 2025 Valerie McQueen

Usage:

Import as a module


'''
import my_credentials
import requests


def pastebin_post(title, body_text, expiration, unlisted=True):
    API_KEY = my_credentials.key
    URL = 'https://pastebin.com/api/api_post.php'
    
    data ={
        'api_dev_key':API_KEY,
        'api_option':'paste',
        'api_paste_code':body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private':unlisted
    }
    
    r = requests.post(URL, data )
    print(f"Posting {title}:{body_text} to URL: {URL} using PasteBin.")
    
    if r.status_code < 400:
        print("Success")
        paste_url = r.text
    else:
        paste_url = ""
        print("Unsucessful")
    
    return paste_url  
