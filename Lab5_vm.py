'''
Lab5_vm.py - Requests a dad joke and pastes it to Pastebin
COMP 593 Scripting Applications Winter 2025 Lab 5 Section 1

Usage: 

python Lab5_vm.py <jokes_category> where jokes_category is the type of joke you would
like to paste



'''
#imports
from pastebin_api import pastebin_post # pastebin handling
from dad_jokes_api import search_dad_jokes #api handling for dad jokes
from sys import argv

def main():
  
    # get the category from the command line arguments
    joke_category = get_subject()
    
    # search the dad jokes API
    joke = search_dad_jokes(joke_category)
    print(joke)
    #post the joke using pastebin
    
    joke_post = pastebin_post(joke_category, joke, "1D", "1")
    print(joke_post)

def get_subject():
    '''
    Retrieves the command line argument 1 , converts it to a string, strips any 
    leading trailing whitespace and converts it to lower case.
    
    Returns: the argument (Jokes Category)
    '''
        
    if len(argv) > 1:
        joke_category = str(argv[1]).strip().lower()
        print(f"You have selected a joke category of:{joke_category}. \n")
        return joke_category
    else:
        print("Please include a joke category argument")
        exit(1)


if __name__ == '__main__':
    main()    