class CommandLineInterfaceParser:

    def __init__(self, arguments):
        self.parts_of_speach = ['VB', 'NN']
        self.source_types = ['folder', 'web']
        
        self.source_type = None
        self.part_of_speach = None
        self.word_count = None

        self.error_message = """ 

========================================================================
    To run the program use the following format, please:
    
    >>> python3 get_words.py <source_type> <POS> <word_count>
        

        :source_type      str: source type. Available: [web, folder]
        :POS         str: (part of speach). Available: [VB, NN] (Verb or noun)
        :word_count  int: number of words
        

    
    For example:

    >>> python3 get_words.py folder VB 105

    OR

    >>> python3 get_words.py web NN 77
        
========================================================================

    """
        # verifying all the attirbutes of the arguments passed in CLI
        source_type, part_of_speach, word_count = self.verify_cli(arguments)
        
        # setting the properties after verification of 
        # the sys.argv's length
        self.set_source_type(source_type)
        self.set_part_of_speach(part_of_speach)
        self.set_word_count(word_count)
        
    def get_word_count(self):
        return self.word_count

    def set_word_count(self, word_count):
        self.verify_word_count(word_count)
        self.word_count = word_count

    def get_part_of_speach(self):
        return self.pos

    def set_part_of_speach(self, part_of_speach):
        self.verify_part_of_speach(part_of_speach)
        self.part_of_speach = part_of_speach

    def get_source_type(self):
        return self.source_type

    def set_source_type(self, source_type):
        self.verify_source_type(source_type)
        self.source_type = source_type

    def verify_cli(self, arguments):
        if len(arguments) != 4:
            raise AttributeError(self.error_message)
        
        _, source_type, part_of_speach, word_count = arguments
        self.verify_source_type(source_type)
        self.verify_part_of_speach(part_of_speach)
        self.verify_word_count(word_count)

        return source_type, part_of_speach, word_count

    def verify_source_type(self, source_type):
        if source_type not in self.source_types:
            raise TypeError("Wrong source type.\n", self.error_message)

    def verify_part_of_speach(self, part_of_speach):
        if part_of_speach not in self.parts_of_speach:
            raise TypeError("Wrong part of speach type.\n", self.error_message)
    
    def verify_word_count(self, word_count):
        try:
            return int(word_count)
        except TypeError as e:
            raise TypeError("Wrong word count.\n", self.error_message)

    


