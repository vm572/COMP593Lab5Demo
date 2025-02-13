'''pastebin_api.py - Posting to Pastebin, return a URL
COMP 593 Scripting Applications Winter 2025 Lab 5 Sec 1
Valerie McQueen <Valerie.McQueen@FlemingCollege.ca>

Usage:
Import as a module.
'''
import my_credentials
import requests


def pastebin_post(title= " ", body_text=" ", expiration="1M", unlisted="1"):
    API_KEY = my_credentials.key #Private file with individual API key
    URL = 'https://pastebin.com/api/api_post.php' #URL you can post to.  See https://pastebin.com/doc_api  
    
    data ={   
        'api_dev_key':API_KEY, #required see https://pastebin.com/doc_api#3
        'api_option':'paste',  #required, here we want to paste
        'api_paste_code':body_text, #required, this is the content we want to paste to the board
        'api_paste_name': title, #optional, but it adds a nice title
        'api_paste_expire_date': expiration, # 1D, 1M etc https://pastebin.com/doc_api#6
        'api_paste_private':unlisted #'0' public, '1', Unlisted, '2' Private
    }
    
    r = requests.post(URL, data ) #new post request https://pypi.org/project/requests/
    
    if r.status_code < 400:
        print(f"Posting Title:{title} Text:{body_text} to URL: {URL} using PasteBin. Status Code: {r.status_code}")
        paste_url = r.text
        return paste_url  
        
    else:
        paste_url = ""
        print(f"Unable to post Title:{title} Text:{body_text} to URL: {URL} using PasteBin. Status Code: {r.status_code}")
        return paste_url  


if __name__ == "__main__":
    print("Please import this module.")