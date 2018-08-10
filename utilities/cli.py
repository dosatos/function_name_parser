from .mixins import ValidatorMixin


class CommandLineInterface(ValidatorMixin):

    def __init__(self, arguments):
        super().__init__()
        self.source_type = None
        self.part_of_speech = None
        self.words_count = None

        # validating all the attirbutes of the arguments passed in CLI
        source_type, part_of_speech, words_count = self.validate_cli(arguments)
        
        # setting the properties after verification of 
        # the sys.argv's length
        self.set_source_type(source_type)
        self.set_part_of_speech(part_of_speech)
        self.set_words_count(words_count)
        
    def get_words_count(self):
        return self.words_count

    def set_words_count(self, words_count):
        self.validate_words_count(words_count)
        self.words_count = words_count

    def get_part_of_speech(self):
        return self.part_of_speech

    def set_part_of_speech(self, part_of_speech):
        self.validate_part_of_speech(part_of_speech)
        self.part_of_speech = part_of_speech

    def get_source_type(self):
        return self.source_type

    def set_source_type(self, source_type):
        self.validate_source_type(source_type)
        self.source_type = source_type

    def validate_cli(self, arguments):
        if len(arguments) != 4:
            raise AttributeError(self.error_message)
        
        _, source_type, part_of_speech, words_count = arguments
        self.validate_source_type(source_type)
        self.validate_part_of_speech(part_of_speech)
        self.validate_words_count(words_count)

        return source_type, part_of_speech, words_count