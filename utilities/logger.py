class Logger:
    def message_log(self, debug_message):
        logging.basicConfig(filename='message.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w')
        logging.debug(debug_message)


    def error_log(self, debug_message):
        logging.basicConfig(filename='errors.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w')
        logging.debug(debug_message)