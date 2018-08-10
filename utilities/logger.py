import logging


class Logger:
    def message(self, debug_message):
        logging.basicConfig(filename='message.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='a')
        logging.debug(debug_message)


    def error(self, debug_message):
        logging.basicConfig(filename='errors.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='a')
        logging.debug(debug_message)