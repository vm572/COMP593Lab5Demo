'''
Lab5_vm.py - Requests a dad joke and pastes it to Pastebin

Usage: 

python Lab5_vm.py <jokes_category> where jokes_category is the type of joke you would
like to paste



'''
#imports
from pastebin_api import pastebin_post # pastebin handling
from dad_jokes_api import search_dad_jokes #api handling for dad jokes
from sys import argv

def main():
  
    joke_category = get_subject()
    joke = search_dad_jokes(joke_category, '1','1')
    print(joke)
    
    joke_post = pastebin_post(joke_category, joke, "1M", "1")
    print(joke_post)

  #p = pastebin_post("test title", "test text", "1D","1")  

  #print(p)  


def get_subject():
    '''
    Retrieves the command line argument 1 , converts it to a string, strips any 
    leading trailing whitespace and converts it to lower case.
    
    Returns: the argument (Jokes Category)
    '''
        
    if len(argv) > 1:
        joke_category = str(argv[1]).strip().lower()
        print(f"You have selected a joke category of:{joke_category}")
        return joke_category
    else:
        print("Please include a joke category argument")
        exit(1)


if __name__ == '__main__':
    main()    