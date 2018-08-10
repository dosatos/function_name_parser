## Code refactoring to a more readable and maintainable one
##### Original Source: https://gist.github.com/Melevir/5754a1b553eb11839238e43734d0eb79

##### To set up the environment (Python version: 3.6)
$ virtualenv --python=$(which python3) py
$ source py/bin/activate  
$ pip install -r requirements.txt

##### To run the program use the following format, please:
    
    >>> python3 get_words.py <source_type> <POS> <words_count>
        

        :source_type      str: source type. Available: [web, folder]
        :POS         str: (part of speech). Available: [verb, noun]
        :words_count  int: number of words
        

    For example:

    >>> python3 get_words.py folder verb 105

    OR

    >>> python3 get_words.py web noun 77